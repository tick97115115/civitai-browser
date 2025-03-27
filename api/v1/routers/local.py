from fastapi import APIRouter, Depends, HTTPException
from civitai_api.v1.models.modelId_endpoint import ModelId_Response
from ..db.civitai_table import CivitAI_Model
from ..db.gopeed_table import ModelVersionGopeedTask
from .util import find_modelVersion_in_modelId_response
router = APIRouter()

# @router.post('/download')
# async def download_model(modelId:):

@router.post('/api/v1/download/{versionId}')
async def download_model(modelId: ModelId_Response, versionId: int):
    try:
        modelVersion = find_modelVersion_in_modelId_response(modelId, versionId)

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
