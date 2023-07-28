from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import EntityMeta as Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(256), nullable=False)
    addresses = relationship("Address", back_populates="user")

    def __repr__(self) -> str:
        return f"id: {self.id}, first_name:{self.first_name}, last_name:{self.last_name}, email:{self.email}"
