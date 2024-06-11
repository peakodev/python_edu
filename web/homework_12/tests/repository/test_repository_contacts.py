import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime

from sqlalchemy.orm import Session

from src.database.models import User, Contact
from src.schemas.contact import (
    ContactUpdate as ContactUpdateSchema,
    Contact as ContactSchema
)
from src.repository.contacts import (
    get_contacts,
    get_contact,
    create_contact,
    update_contact,
    delete_contact,
    get_birthdays_contacts,
    search_contacts
)


class TestContactsRepository(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.db = MagicMock(spec=Session)
        self.user = User(id=1)
        self.contact1 = dict(
            id=1,
            first_name='Nazar',
            last_name='Kod',
            email='t1@example.com',
            phone='+380987456123',
            birth_date='1990-02-10',
            user_id=self.user.id)
        self.contact2 = dict(
            id=2,
            first_name='Den',
            last_name='Kod',
            email='t2@example.com',
            phone='+380987456124',
            birth_date='1990-05-10',
            user_id=self.user.id)
        self.contacts = [Contact(**self.contact1), Contact(**self.contact2)]

    async def test_get_contacts(self):
        self.db.query().filter().offset().limit().all.return_value = self.contacts

        result = await get_contacts(self.db, self.user)

        self.assertEqual(result, self.contacts)
        self.db.query(Contact).filter.assert_called()

    async def test_get_contact_found(self):
        contact = Contact(id=1)
        self.db.query().filter().first.return_value = contact

        result = await get_contact(self.db, self.user, 1)

        self.assertEqual(result, contact)

    async def test_get_contact_not_found(self):
        self.db.query().filter().first.return_value = None

        result = await get_contact(self.db, self.user, 1)

        self.assertIsNone(result)

    async def test_create_contact(self):
        contact = ContactUpdateSchema(**self.contact1)

        result = await create_contact(self.db, self.user, contact)

        self.assertEqual(result.first_name, contact.first_name)
        self.assertEqual(result.last_name, contact.last_name)
        self.assertEqual(result.email, contact.email)
        self.assertEqual(result.phone, contact.phone)
        self.assertEqual(result.birth_date, contact.birth_date)
        self.assertTrue(hasattr(result, "id"))
        self.assertEqual(result.user_id, self.user.id)
        self.db.commit.assert_called_once()

    async def test_delete_contact_found(self):
        contact = Contact(**self.contact1)
        self.db.query().filter().first.return_value = contact

        result = await delete_contact(self.db, self.user, contact.id)

        self.assertEqual(result, contact)
        self.db.delete.assert_called_once()
        self.db.commit.assert_called_once()

    async def test_delete_contact_not_found(self):
        self.db.query().filter().first.return_value = None

        result = await delete_contact(self.db, self.user, 1)

        self.assertIsNone(result)
        self.db.delete.assert_not_called()
        self.db.commit.assert_not_called()

    async def test_update_contact_found(self):
        contact = Contact(**self.contact1)
        body = ContactSchema(**self.contact1)

        self.db.query().filter().first.return_value = contact

        result = await update_contact(self.db, self.user, contact.id, body)

        self.assertEqual(result, contact)
        self.db.commit.assert_called_once()

    async def test_update_contact_not_found(self):
        self.db.query().filter().first.return_value = None

        result = await update_contact(self.db, self.user, 1, ContactSchema(**self.contact1))

        self.assertIsNone(result)
        self.db.commit.assert_not_called()

    @patch('src.repository.contacts.datetime')
    async def test_birthdays_within_next_seven_days(self, mock_datetime):
        # Setup
        today = datetime(2024, 6, 10)
        mock_datetime.today.return_value = today
        mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

        user = User(id=1)
        contacts = [
            Contact(id=1, user_id=1, birth_date=datetime(1990, 6, 11)),
            Contact(id=2, user_id=1, birth_date=datetime(1992, 6, 15)),
            Contact(id=3, user_id=1, birth_date=datetime(1988, 6, 17)),
        ]

        query_mock = self.db.query.return_value
        filter_mock = query_mock.filter.return_value
        order_by_mock = filter_mock.order_by.return_value
        order_by_mock.all.return_value = contacts

        result = await get_birthdays_contacts(self.db, user, 7)

        self.assertEqual(len(result), 3)
        self.assertEqual(result, contacts)
        self.db.query.assert_called_once_with(Contact)
        query_mock.filter.assert_called_once()
        filter_mock.order_by.assert_called_once()

    @patch('src.repository.contacts.datetime')
    async def test_birthdays_spanning_year_end(self, mock_datetime):
        # Setup
        today = datetime(2023, 12, 28)
        mock_datetime.today.return_value = today
        mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

        user = User(id=1)
        contacts = [
            Contact(id=1, user_id=1, birth_date=datetime(1990, 12, 29)),
            Contact(id=2, user_id=1, birth_date=datetime(1992, 12, 31)),
            Contact(id=3, user_id=1, birth_date=datetime(1988, 1, 1)),
        ]

        query_mock = self.db.query.return_value
        filter_mock = query_mock.filter.return_value
        order_by_mock = filter_mock.order_by.return_value
        order_by_mock.all.return_value = contacts

        result = await get_birthdays_contacts(self.db, user, 7)

        self.assertEqual(len(result), 3)
        self.assertEqual(result, contacts)
        self.db.query.assert_called_once_with(Contact)
        query_mock.filter.assert_called_once()
        filter_mock.order_by.assert_called_once()

    async def test_search_contacts(self):
        search_query = "Kod"

        query_mock = self.db.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.all.return_value = self.contacts

        result = await search_contacts(self.db, self.user, search_query)

        self.assertEqual(len(result), 2)
        self.assertEqual(result, self.contacts)
        self.db.query.assert_called_once_with(Contact)
        query_mock.filter.assert_called_once()

    async def test_search_contacts_not_found(self):
        search_query = "NonExistentName"
        
        query_mock = self.db.query.return_value
        filter_mock = query_mock.filter.return_value
        filter_mock.all.return_value = []

        result = await search_contacts(self.db, self.user, search_query)

        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])
        self.db.query.assert_called_once_with(Contact)
        query_mock.filter.assert_called_once()


if __name__ == "__main__":
    unittest.main()
