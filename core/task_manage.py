from civitai_api.v1 import CiviClient
from gospeed_api.index import GospeedAPI as GopeedAPI
from civitai_api.v1.models.base.modelVersion import Base_ModelVersion
from gospeed_api.models.create_a_task import CreateTask_DownloadOpt
from db.civitai_table import CivitAI_Model
from sqlalchemy.engine import Engine
from sqlmodel import Session

# https://testdriven.io/blog/fastapi-sqlmodel/

def create_download_task(engine: Engine, civitai_client: CiviClient, gopeed_api: GopeedAPI, path: str, modelVersion_response: Base_ModelVersion):
    with Session(engine) as session:
        task_id = gopeed_api.create_a_task_from_url(
        url=modelVersion_response.downloadUrl, 
        opt=CreateTask_DownloadOpt(
            name=modelVersion_response.name,
            path=path,
            )
        )
        session.commit()
        return task_id

