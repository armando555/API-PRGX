from fastapi import APIRouter, Depends, status
from typing import List
from schema.user import ShowUserSchema,UserSchema
from sqlalchemy.orm import Session
from database.engine import get_db_connection
from repository import  user as user_repository


router = APIRouter(
    prefix="/user",
    tags=["Users API"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create(request: UserSchema, db: Session = Depends(get_db_connection)):
    return user_repository.create(request, db)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ShowUserSchema])
async def all(db: Session = Depends(get_db_connection)):
    return user_repository.get_all(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ShowUserSchema)
async def get(id, db: Session = Depends(get_db_connection)):
    return user_repository.get(db, id)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete(id,db: Session = Depends(get_db_connection)):
    return user_repository.delete(db, id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: UserSchema, db: Session = Depends(get_db_connection)):
    return user_repository.update(db, request, id)

@router.post("/bicycles", status_code=status.HTTP_200_OK)
async def bulk(request: List[UserSchema], db: Session = Depends(get_db_connection)):
    return user_repository.bulk(db=db, request=request)