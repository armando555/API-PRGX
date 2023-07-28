from models.base import EntityMeta
from database import SessionLocal, engine
import pytest
import os


def pytest_sessionstart(session):
    if not os.getenv("TESTING") == "True":
        return pytest.exit(
            "Test environment not set correctly, set the 'TESTING' environment variable to 'True'"
        )


@pytest.fixture(scope="module")
def db():
    EntityMeta.metadata.create_all(engine)
    
    session = SessionLocal()

    yield session

    session.close()
    EntityMeta.metadata.drop_all(engine)