from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    
    
class UserCreate(UserBase):
    password: str


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str


class UserOut(UserBase):
    id: int


