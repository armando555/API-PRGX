from typing import Optional, List
from pydantic import BaseModel
from .address import ShowAddressSchema

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    addresses: List[int]
    
class UserSchema(UserBase):
    class Config():
        orm_mode = True
        
class ShowUserSchema(UserSchema):
    id: int
    addresses: List[ShowAddressSchema]