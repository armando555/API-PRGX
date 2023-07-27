from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    
class UserSchema(UserBase):
    class Config():
        orm_mode = True
        
class ShowUserSchema(UserSchema):
    id: int