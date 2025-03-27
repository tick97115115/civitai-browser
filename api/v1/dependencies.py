from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel
from .routers.settings import load_settings
from contextlib import contextmanager

settings = load_settings()
engine = create_engine(settings.db_uri)
SQLModel.metadata.create_all(engine)

@contextmanager
def get_db_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
        