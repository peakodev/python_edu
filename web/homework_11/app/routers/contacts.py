from fastapi import APIRouter, Depends, HTTPException, Query, Path, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..schemas import contact_schema
from ..database.models import Contact as ContactModel
from ..database.db import get_db
from ..repository import contacts as repo


router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/birthdays", response_model=list[contact_schema.Contact])
async def get_7_days_birthday_contacts(db: Session = Depends(get_db)) -> list[contact_schema.Contact]:
    return await repo.get_7_days_birthday_contacts(db)


@router.get("/search", response_model=list[contact_schema.Contact])
async def search_contacts(
    query: str = Query(..., min_length=2),
    db: Session = Depends(get_db)
) -> list[contact_schema.Contact]:
    return await repo.search_contacts(db, query)


@router.get("/", response_model=list[contact_schema.Contact])
async def get_contacts(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=10, le=100),
    db: Session = Depends(get_db)
) -> list[contact_schema.Contact]:

    return await repo.get_contacts(db, skip, limit)


@router.get("/{contact_id}", response_model=contact_schema.Contact)
async def get_contact(
    contact_id: int = Path(description="The ID of the contact to get", ge=1),
    db: Session = Depends(get_db)
) -> contact_schema.Contact:
    contact = await repo.get_contact(db, contact_id)

    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    return contact


@router.post("/", response_model=contact_schema.Contact)
async def create_contact(
    body: contact_schema.ContactCreate,
    db: Session = Depends(get_db)
) -> ContactModel:
    try:
        return await repo.create_contact(db, body)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email or phone number already exists")


@router.put("/{contact_id}", response_model=contact_schema.Contact)
async def update_contact(
    body: contact_schema.ContactCreate,
    contact_id: int = Path(description="The ID of the contact to update", ge=1),
    db: Session = Depends(get_db)
) -> contact_schema.Contact:
    updated_contact = await repo.update_contact(db, contact_id, body)

    if updated_contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    return updated_contact


@router.delete("/{contact_id}", response_model=contact_schema.Contact)
async def delete_contact(
    contact_id: int = Path(description="The ID of the contact to delete", ge=1),
    db: Session = Depends(get_db)
) -> contact_schema.Contact:
    contact = await repo.delete_contact(db, contact_id)

    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")

    return contact

