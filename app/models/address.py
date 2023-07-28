from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.base import EntityMeta as Base


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    address_1 = Column(String(250), nullable=False)
    address_2 = Column(String(250), nullable=False)
    city = Column(String(250), nullable=False)
    state = Column(String(250), nullable=False)
    zip = Column(String(250), nullable=False)
    country = Column(String(250), nullable=False)
    user_id_fk = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", foreign_keys=[user_id_fk], back_populates="addresses")

    def __repr__(self) -> str:
        return f"id: {self.id}, address_1:{self.address_1}, address_2:{self.address_2}, city:{self.city}"
