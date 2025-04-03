from typing import Sequence
from ..db.gopeed_table import ModelVersionGopeedTask, ModelVersionImageGopeedTask
from fastapi import APIRouter
from sqlmodel import select
from ..dependencies import get_db_session
from civitai_api.v1 import CiviClient, creators

router = APIRouter()

@router.get('/api/v1/gopeed_tasks', response_model=Sequence[ModelVersionGopeedTask])
def get_tasks():
    with get_db_session() as session:
        statement = select(ModelVersionGopeedTask)
        result = session.exec(statement)
        return result.all()

@router.get('/api/v1/gopeed_tasks/images/{version_id}', response_model=Sequence[ModelVersionImageGopeedTask])
def get_imgs(version_id):
    with get_db_session() as session:
        statement = select(ModelVersionImageGopeedTask).where(ModelVersionImageGopeedTask.version_id == version_id)
        result = session.exec(statement)
        return result.all()

# @router.post('/api/v1/gopeed_tasks/add_one/{version_id}', response_model=ModelVersionGopeedTask)
# def add_task():
