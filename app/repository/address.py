from sqlalchemy.orm import Session
from models.address import Address
from schema.address import AddressSchema, ShowAddressSchema
from fastapi import status, HTTPException
from typing import List


def get_all(db: Session):
    addreses = db.query(Address).all()
    return addreses


def create(request:AddressSchema, db: Session):
    new_address = Address(address_1=request.address_1, address_2=request.address_2, city=request.city, state=request.state, country=request.country, zip=request.zip)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

def get(db: Session, id: int):
    address = db.query(Address).filter(Address.id == id).first()
    if not address:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Address with the id {id} is not available')
    return address

def delete(db: Session, id: int):
    address = db.query(Address).filter(Address.id == id)
    if not address.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Address with the id {id} is not available')
    address.delete(synchronize_session=False)
    db.commit()
    return f"Address {id} deleted"

def update(db: Session, request: AddressSchema, id: int):
    address = db.query(Address).filter(Address.id == id)
    if not address.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Address with the id {id} is not available')
    address.update(request.model_dump())
    db.commit()
    return f"Address {id} Updated"

def bulk(db: Session, request: List[AddressSchema]):
    for user in request:
        new_user= Address(first_name=request.first_name, last_name=request.last_name, email=request.email, password=request.password)
        db.add(new_user)
    db.commit()
    return "Bicycles created"