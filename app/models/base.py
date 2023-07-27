from database.engine import  engine
from sqlalchemy.ext.declarative import declarative_base


# Base Entity Model Schema
EntityMeta = declarative_base()

def init():
    EntityMeta.metadata.create_all(bind=engine)