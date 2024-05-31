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
    return db.query(Contact).filter(
        Contact.user_id == user.id
    ).offset(skip).limit(limit).all()


async def get_contact(
        db: Session,
        user: User,
        contact_id: int
) -> Contact | None:
    return db.query(Contact).filter(
        and_(Contact.id == contact_id, Contact.user_id == user.id)
    ).first()


async def create_contact(
        db: Session,
        user: User,
        contact: ContactUpdateSchema
) -> Contact:
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
    db.query(Contact).filter(
        and_(Contact.id == contact_id, Contact.user_id == user.id)
    ).update(contact.dict())
    db.commit()

    return await get_contact(db, user, contact_id)


async def delete_contact(
        db: Session,
        user: User,
        contact_id: int
) -> Contact:
    contact = await get_contact(db, user, contact_id)
    db.delete(contact)
    db.commit()

    return contact


async def search_contacts(
        db: Session,
        user: User,
        search_query: str
) -> List[Contact]:
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


async def get_7_days_birthday_contacts(
        db: Session,
        user: User
) -> List[Contact]:
    today = datetime.today()
    seven_days_later = today + timedelta(days=7)

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
