from fastapi import APIRouter, Depends, status
from typing import List
from schema.address import ShowAddressSchema,AddressSchema
from sqlalchemy.orm import Session
from database.engine import get_db_connection
from repository import address as address_repository


router = APIRouter(
    prefix="/address",
    tags=["Address API"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create(request: AddressSchema, db: Session = Depends(get_db_connection)):
    return address_repository.create(request, db)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ShowAddressSchema])
async def all(db: Session = Depends(get_db_connection)):
    return address_repository.get_all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowAddressSchema)
async def get(id, db: Session = Depends(get_db_connection)):
    return address_repository.get(db, id)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete(id,db: Session = Depends(get_db_connection)):
    return address_repository.delete(db, id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: AddressSchema, db: Session = Depends(get_db_connection)):
    return address_repository.update(db, request, id)

@router.post("/bulk", status_code=status.HTTP_200_OK)
async def bulk(request: List[AddressSchema], db: Session = Depends(get_db_connection)):
    return address_repository.bulk(db=db, request=request)