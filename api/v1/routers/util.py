from .settings import load_settings
from civitai_api.v1.models.modelId_endpoint import ModelId_Response
from civitai_api.v1.models.base.modelVersion import Base_ModelVersion
from civitai_api.v1.models.base.misc import Model_Types
from fastapi import APIRouter
from pydantic import StrictInt
import pathlib
import anyio

civitai_browser_folder_name = 'civitai_browser'
civitai_model_id_info_file_name = 'civitai_model_id_info.json'
civitai_model_version_info_file_name = 'civitai_model_version_info.json'

router = APIRouter()

@router.get('/api/v1/util/get_model_id_path')
def get_model_id_path(modelId: int, modelType: Model_Types) -> str:
    if modelType == Model_Types.Checkpoint:
        dist = pathlib.Path(load_settings().checkpoint_folder) / civitai_browser_folder_name / str(modelId)
        return str(dist.absolute())
    elif modelType == Model_Types.LORA or \
        modelType == Model_Types.LoCon or \
        modelType == Model_Types.DoRA:
        dist = pathlib.Path(load_settings().lora_folder) / civitai_browser_folder_name / str(modelId)
        return str(dist.absolute())
    else:
        raise Exception("Model type not supported")
    
@router.get('/api/v1/util/get_model_version_path')
def get_model_version_path(modelId: int, versionId: int, modelType: Model_Types) -> str:
    dist = pathlib.Path(get_model_id_path(modelId, modelType)) / str(versionId)
    return str(dist.absolute())

def get_model_version_img_path(modelId: int, versionId: int, modelType: Model_Types) -> str:
    dist = pathlib.Path(get_model_version_path(modelId=modelId,versionId=versionId,modelType=modelType)) / "img"
    return str(dist.absolute())

@router.post('/api/v1/util/save_civitai_model_version_info')
def save_civitai_model_version_info(modelId: int, versionId: int, modelType: Model_Types, modelVersion_model: Base_ModelVersion):
    model_path_str = get_model_version_path(modelId=modelId, versionId=versionId, modelType=modelType)
    model_path = pathlib.Path(model_path_str)
    model_path.mkdir(parents=True, exist_ok=True)
    with open(model_path / civitai_model_version_info_file_name, 'w') as f:
        f.write(modelVersion_model.model_dump_json())

@router.post('/api/v1/util/save_civitai_model_id_info')
def save_model_civitai_id_info(modelId_model: ModelId_Response):
    model_id_path_str = get_model_id_path(modelId=modelId_model.id, modelType=modelId_model.type)
    model_id_path = pathlib.Path(model_id_path_str)
    model_id_path.mkdir(parents=True, exist_ok=True)
    with open(model_id_path / civitai_model_id_info_file_name, 'w') as f:
        f.write(modelId_model.model_dump_json())

def find_modelVersion_in_modelId_response(modelId_model: ModelId_Response, versionId: int) -> Base_ModelVersion:
    for modelVersion in modelId_model.modelVersions:
        if modelVersion.id == versionId:
            return modelVersion
    raise Exception("Model version not found")

@router.get('/api/v1/util/get_model_version_file_download_path')
def get_model_version_file_download_path(modelId_model: ModelId_Response, versionId: int, modelType: Model_Types) -> str:
    model_version = find_modelVersion_in_modelId_response(modelId_model, versionId)
    model_path = pathlib.Path(get_model_version_path(modelId_model.id, versionId, modelType)) / (modelId_model.name + model_version.name)
    return str(model_path.absolute())