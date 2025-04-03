from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel
from init import settings
from contextlib import contextmanager
from typing import Annotated

import api.v1.db.civitai_table
import api.v1.db.gopeed_table
engine = create_engine(settings.db_uri)
SQLModel.metadata.create_all(engine)

@contextmanager
def get_db_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

DbSessionDep = Annotated[dict, Depends(get_db_session)]

