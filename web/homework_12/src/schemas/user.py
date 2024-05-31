from datetime import datetime
from pydantic import BaseModel, Field


class UserModel(BaseModel):
    email: str
    password: str = Field(min_length=6, max_length=25)


class UserDb(BaseModel):
    id: int
    email: str
    created_at: datetime
    avatar: str

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
