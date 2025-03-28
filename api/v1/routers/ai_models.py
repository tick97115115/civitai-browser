from fastapi import APIRouter, Depends, HTTPException
from civitai_api.v1.models.modelId_endpoint import ModelId_Response
from ..db.civitai_table import CivitAI_Model
from ..db.gopeed_table import ModelVersionGopeedTask, ModelVersionImageGopeedTask
from .util import find_modelVersion_in_modelId_response
from ...app import gospeed_api

router = APIRouter()

@router.post('/api/v1/models/download/{versionId}')
def download_model(modelId: ModelId_Response, versionId: int):
    model_version = find_modelVersion_in_modelId_response(modelId, versionId)
    task_id = gospeed_api.create_a_task_from_url(model_version.downloadUrl)
    gopeed_modelVersion_task = ModelVersionGopeedTask(
        version_id=model_version.id,
        task_id=model_version.taskId,
        file_name=model_version.fileName,
        path=model_version.path
    )
    image_tasks = []
    for image in model_version.images:
        image_task_id = gospeed_api.create_a_task_from_url(image.url)
        image_task = ModelVersionImageGopeedTask(
            version_id=model_version.id,
            task_id=image_task_id,
            file_name=image.,
            path=image.path
        )
    # try:
    #     modelVersion = find_modelVersion_in_modelId_response(modelId, versionId)
    # except Exception as e:
    #     raise HTTPException(status_code=404, detail=str(e))
