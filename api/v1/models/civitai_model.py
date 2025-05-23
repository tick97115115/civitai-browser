from enum import StrEnum
from pydantic import BaseModel, StrictInt, HttpUrl
from datetime import datetime

class Image(BaseModel):
    id: StrictInt
    url: HttpUrl
    nsfwLevel: StrictInt
    width: StrictInt
    height: StrictInt
    hash: str
    type: str

class File_Metadata(BaseModel):
    format: str

class File(BaseModel):
    id: StrictInt
    sizeKB: float
    name: str
    type: str
    scannedAt: None | datetime
    metadata: File_Metadata
    downloadUrl: HttpUrl

class ModelVersion_Availability(StrEnum):
    EarlyAccess = 'EarlyAccess'
    Public = 'Public'

class ModelVersion(BaseModel):
    id: StrictInt
    index: StrictInt
    name: str
    baseModel: str
    baseModelType: None | str
    publishedAt: None | datetime # "2024-01-30T00:24:15.582Z",
    availability: ModelVersion_Availability
    nsfwLevel: StrictInt
    description: None | str # HTML string
    trainedWords: list[str]
    stats: dict
    files: list[File]
    images: list[Image]
    downloadUrl: HttpUrl

class CivitAI_ModelId(BaseModel):
    id: int
    name: str
    description: None | str
    type: str
    poi: bool
    nsfw: bool
    nsfwLevel: int
    # cosmetic: None
    stats: dict
    tags: list[str]
    modelVersions: list[ModelVersion]