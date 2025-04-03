from fastapi import APIRouter, Depends, HTTPException
from civitai_api.v1.models.modelId_endpoint import ModelId_Response
from gospeed_api.models.create_a_task import CreateTask_DownloadOpt
from ..db.civitai_table import CivitAI_Model
from ..db.gopeed_table import ModelVersionGopeedTask, ModelVersionImageGopeedTask
from .util import find_modelVersion_in_modelId_response, get_model_version_path
from init import gospeed_api

router = APIRouter()

@router.post('/api/v1/models/download/{versionId}')
def download_model(modelId: ModelId_Response, versionId: int):
    model_version = find_modelVersion_in_modelId_response(modelId, versionId)
    model_version_path = get_model_version_path(modelId=modelId.id, versionId=versionId, modelType=modelId.type)
    # model_file_name = 
    file_tasks = []

    # if len(model)

    # 1. Download files
    for file in model_version.files:
        file_tasks.append(
            gospeed_api.create_a_task_from_url(
                file.downloadUrl,
                opt=CreateTask_DownloadOpt(
                    name=f"{file.id}_{file.name}",
                    path=model_version_path
                )
            )
        )
    # 2. Download Images
    img_tasks = []
    if len(model_version.images) > 0:
        if len(model_version.files) == 1 :
            img_tasks.append(
                gospeed_api.create_a_task_from_url(
                    url=model_version.images[0].url,
                    opt=CreateTask_DownloadOpt(
                        # name=
                        path=model_version_path
                    )
                )
            )
        
    for img in model_version.images:
        img_tasks.append(
            gospeed_api.create_a_task_from_url(
                url=img.url,
                opt=CreateTask_DownloadOpt(
                    path=model_version_path
                )
            )
        )
    
    # create task record
