from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, EmailStr

PHONE_REGEX = r'^\+380\d{9}$'


class ContactUpdate(BaseModel):
    first_name: str = Field(description="Ім'я", min_length=2, max_length=50)
    last_name: str = Field(description="Прізвище", min_length=2, max_length=50)
    email: EmailStr = Field(description="Електронна пошта")
    phone: str = Field(pattern=PHONE_REGEX, description="Український номер телефону")
    birth_date: date = Field(description="Дата народження")
    additional_info: Optional[str] = Field(None, description="Додаткова інформація")


class Contact(ContactUpdate):
    id: int = Field(description="Ідентифікатор", ge=1)

    class Config:
        from_attributes = True
