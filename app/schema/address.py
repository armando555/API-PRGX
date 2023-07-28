from typing import Optional
from pydantic import BaseModel, Field

class AddressBase(BaseModel):
    address_1: str = Field(...,max_length=250)
    address_2: str = Field(...,max_length=250)
    city: str = Field(...,max_length=250)
    state: str = Field(...,max_length=250)
    zip: str = Field(...,max_length=250)
    country: str = Field(...,max_length=250)
    user_id_fk: Optional[int]
    
class AddressSchema(AddressBase):
    class Config():
        orm_mode = True
        
class ShowAddressSchema(AddressSchema):
    id: int