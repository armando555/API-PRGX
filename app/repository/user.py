from sqlalchemy.orm import Session
from models.user import User
from models.address import Address
from schema.user import UserSchema, ShowUserSchema
from fastapi import status, HTTPException
from typing import List
from utils import password_hash
from .address import get_by_id


def get_all(db: Session):
    users = db.query(User).all()
    return users


def create(request:UserSchema, db: Session):
    addresses = []
    for address_id in request.addresses:
        addresses.append(get_by_id(db=db, id=address_id))
    new_user = User(first_name=request.first_name, last_name=request.last_name, email=request.email, password=password_hash.hash_password(request.password), addresses=addresses)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_by_id(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not available')
    return user

def delete(db: Session, id: int):
    user = db.query(User).filter(User.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not available')
    user.delete(synchronize_session=False)
    db.commit()
    return f"User {id} deleted"

def update(db: Session, request: UserSchema, id: int):
    user = db.query(User).filter(User.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not available')
    user.update(request.model_dump())
    db.commit()
    return f"User {id} Updated"

def bulk(db: Session, request: List[UserSchema]):
    for user in request:
        addresses = []
        for address_id in request.addresses:
            addresses.append(get_by_id(db=db, id=address_id))
        new_user = User(first_name=user.first_name, last_name=user.last_name, email=user.email, password=password_hash.hash_password(user.password), addresses=addresses)
        db.add(new_user)
    db.commit()
    return "Users created"