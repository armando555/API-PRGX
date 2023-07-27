from sqlalchemy.orm import Session
from models.bicycle import Bicycle
from schema.bicycle_schema import BicycleSchema, ShowBicycleSchema
from fastapi import status, HTTPException
from typing import List


def get_all(db: Session):
    bicycles = db.query(Bicycle).all()
    return bicycles


def create(request:BicycleSchema, db: Session):
    new_blog = Bicycle(name=request.name, latitude=request.latitude, longitude=request.longitude)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get(db: Session, id: int):
    bicycle = db.query(Bicycle).filter(Bicycle.id == id).first()
    if not bicycle:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Bicycle with the id {id} is not available')
    return bicycle

def delete(db: Session, id: int):
    bicycle = db.query(Bicycle).filter(Bicycle.id == id)
    if not bicycle.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Bicycle with the id {id} is not available')
    bicycle.delete(synchronize_session=False)
    db.commit()
    return "Bicycle deleted"

def update(db: Session, request: BicycleSchema, id: int):
    bicycle = db.query(Bicycle).filter(Bicycle.id == id)
    if not bicycle.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Bicycle with the id {id} is not available')
    bicycle.update(request.dict())
    db.commit()
    return "Updated"

def bulk(db: Session, request: List[BicycleSchema]):
    for bicycle in request:
        new_bicycle= Bicycle(name=bicycle.name, latitude=bicycle.latitude, longitude=bicycle.longitude)
        db.add(new_bicycle)
    db.commit()
    return "Bicycles created"