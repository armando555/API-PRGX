from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    "root", "root", "localhost", "33061", "test"
)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # , connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)


def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
