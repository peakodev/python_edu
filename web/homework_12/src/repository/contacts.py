from typing import List
from datetime import datetime, timedelta

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session
from sqlalchemy.sql import extract

from src.database.models import Contact, User
from src.schemas.contact import ContactUpdate as ContactUpdateSchema


async def get_contacts(
        db: Session,
        user: User,
        skip: int = 0,
        limit: int = 10
) -> List[Contact]:
    """
    Receive a list of contacts for a specific user
    with specified pagination parameters.

    Args:
        db (Session): The database session.
        user (User): The user to retrieve contacts for.
        skip (int, optional): The number of contacts to skip. Defaults to 0.
        limit (int, optional): The maximum number of contacts to return. Defaults to 10.

    Returns:
        List[Contact]: A list of contacts
    """
    return db.query(Contact).filter(
        Contact.user_id == user.id
    ).offset(skip).limit(limit).all()


async def get_contact(
        db: Session,
        user: User,
        contact_id: int
) -> Contact | None:
    """
    Get a specific contact for a specific user.

    Args:
        db (Session): The database session.
        user (User): The user to get contact for.
        contact_id (int): The ID of the contact to get.

    Returns:
        Contact | None: The contact, or None if the contact does not exist.
    """
    return db.query(Contact).filter(
        and_(Contact.id == contact_id, Contact.user_id == user.id)
    ).first()


async def create_contact(
        db: Session,
        user: User,
        contact: ContactUpdateSchema
) -> Contact:
    """
    Create a new contact for a specific user.

    Args:
        db (Session):  The database session
        user (User): The user to create contact for.
        contact (ContactUpdateSchema): The for the contact to create.

    Raises:
        e: Any exception that occurs during the database operation.

    Returns:
        Contact: The created contact.
    """
    try:
        new_contact = Contact(**contact.dict())
        new_contact.user_id = user.id
        db.add(new_contact)
        db.commit()
        db.refresh(new_contact)

        return new_contact
    except Exception as e:
        db.rollback()
        raise e


async def update_contact(
        db: Session,
        user: User,
        contact_id: int,
        contact: ContactUpdateSchema
) -> Contact | None:
    """
    Update a contact for a specific user.

    Args:
        db (Session): The database session.
        user (User): The user to update contact for.
        contact_id (int): The ID of the contact to update.
        contact (ContactUpdateSchema): The updated data for the contact.

    Returns:
        Contact | None: The updated contact, or None if the contact does not exist.
    """
    origin = await get_contact(db, user, contact_id)
    if origin is None:
        return None
    for key, value in contact.dict().items():
        setattr(origin, key, value)
    db.commit()

    return origin


async def delete_contact(
        db: Session,
        user: User,
        contact_id: int
) -> Contact | None:
    """
    Delete a contact for a specific user.

    Args:
        db (Session): The database session.
        user (User): The user to delete contact for.
        contact_id (int): The ID of the contact to delete.

    Returns:
        Contact | None: The deleted contact, or None if the contact does not exist.
    """
    contact = await get_contact(db, user, contact_id)
    if contact is None:
        return None
    db.delete(contact)
    db.commit()

    return contact


async def search_contacts(
        db: Session,
        user: User,
        search_query: str
) -> List[Contact]:
    """
    Search for contacts for a specific user

    Args:
        db (Session): The database session.
        user (User): The user to search contacts for.
        search_query (str): The search query to use. Will search in first_name, last_name, email, and phone.

    Returns:
        List[Contact]: A list of contacts that match the search query.
    """
    return db.query(Contact).filter(
        and_(
            Contact.user_id == user.id,
            or_(
                Contact.first_name.ilike(f"%{search_query}%"),
                Contact.last_name.ilike(f"%{search_query}%"),
                Contact.email.ilike(f"%{search_query}%"),
                Contact.phone.ilike(f"%{search_query}%")
            )
        )
    ).all()


async def get_birthdays_contacts(
        db: Session,
        user: User,
        days: int = 7
) -> List[Contact]:
    """
    Get a list of contacts that have birthdays within the next `days` days.

    Args:
        db (Session): The database session.
        user (User): The user to get contacts for.
        days (int, optional): The number of days to look ahead for birthdays. Defaults to 7.

    Returns:
        List[Contact]: A list of contacts that have birthdays within the next `days` days.
    """
    today = datetime.today()
    seven_days_later = today + timedelta(days=days)

    # Common filters
    user_filter = Contact.user_id == user.id
    current_month_day_filter = and_(
        extract('month', Contact.birth_date) == today.month,
        extract('day', Contact.birth_date) >= today.day
    )

    if today.year == seven_days_later.year:
        # If within the same year
        next_month_day_filter = and_(
            extract('month', Contact.birth_date) == seven_days_later.month,
            extract('day', Contact.birth_date) <= seven_days_later.day
        )
    else:
        # If spanning the end of one year to the start of the next year
        next_month_day_filter = and_(
            extract('month', Contact.birth_date) == 1,
            extract('day', Contact.birth_date) <= seven_days_later.day
        )

    return db.query(Contact).filter(
        and_(
            user_filter,
            or_(
                current_month_day_filter,
                next_month_day_filter
            )
        )
    ).order_by(
        extract('month', Contact.birth_date),
        extract('day', Contact.birth_date)
    ).all()
