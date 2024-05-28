from typing import List

from sqlalchemy import func, text
from sqlalchemy.orm import Session

from ..database.models import Contact
from ..schemas.contact_schema import Contact as ContactSchema, ContactCreate as ContactCreateSchema


async def get_contacts(db: Session, skip: int = 0, limit: int = 10) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(db: Session, contact_id: int) -> Contact | None:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(db: Session, contact: ContactCreateSchema) -> Contact:
    try:
        new_contact = Contact(**contact.dict())
        db.add(new_contact)
        db.commit()
        db.refresh(new_contact)

        return new_contact
    except Exception as e:
        db.rollback()
        raise e


async def update_contact(db: Session, contact_id: int, contact: ContactCreateSchema) -> Contact | None:
    db.query(Contact).filter(Contact.id == contact_id).update(contact.dict())
    db.commit()

    return await get_contact(db, contact_id)


async def delete_contact(db: Session, contact_id: int) -> Contact:
    contact = await get_contact(db, contact_id)
    db.delete(contact)
    db.commit()

    return contact


async def search_contacts(db: Session, search_query: str) -> List[Contact]:
    return db.query(Contact).filter(
        Contact.first_name.ilike(f"%{search_query}%") |
        Contact.last_name.ilike(f"%{search_query}%") |
        Contact.email.ilike(f"%{search_query}%") |
        Contact.phone.ilike(f"%{search_query}%")
    ).all()


async def get_7_days_birthday_contacts(db: Session) -> List[Contact]:
    return db.query(Contact).filter(
        Contact.birth_date.between(
            func.current_date(),
            func.current_date() + text("'7 days'::interval")
        )
    ).order_by(Contact.birth_date.asc()).all()
