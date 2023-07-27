from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    address_1: str
    address_2: str
    city: str
    state: str
    zip: str
    country: str
    
class AddressSchema(AddressBase):
    class Config():
        orm_mode = True
        
class ShowAddressSchema(AddressSchema):
    id: int