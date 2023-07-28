from typing import Optional, List
from pydantic import BaseModel, Field
from .address import ShowAddressSchema


class UserBase(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: str = Field(..., max_length=250)
    password: str = Field(..., max_length=256)
    addresses: List[int] = []


class UserSchema(UserBase):
    class Config:
        orm_mode = True


class ShowUserSchema(UserSchema):
    id: int
    addresses: Optional[List[ShowAddressSchema]]
