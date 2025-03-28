from sqlmodel import SQLModel, Field, Relationship
# from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy import Column, JSON, BLOB
from civitai_api.v1.models.base.misc import Model_Types
from civitai_api.v1.models.modelId_endpoint import ModelId_Response
from pydantic import StrictInt

class CivitAI_ModelTagLink(SQLModel, table=True):
    model_id: StrictInt | None = Field(default=None, foreign_key="civitai_model.id", primary_key=True)
    tag_id: StrictInt | None = Field(default=None, foreign_key="civitai_tag.id", primary_key=True)

class CivitAI_Model(SQLModel, table=True):
    id: StrictInt = Field(primary_key=True)
    name: str = Field(index=True)
    type: Model_Types = Field(index=True)
    nsfw: bool
    json_data: dict = Field(sa_column=Column(JSON), default_factory=dict)
    model_versions: list["CivitAI_ModelVersion"] = Relationship(back_populates="model")
    
    tags: list["CivitAI_Tag"] = Relationship(back_populates="models", link_model=CivitAI_ModelTagLink)

class CivitAI_Tag(SQLModel, table=True):
    id: StrictInt | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    models: list[CivitAI_Model] = Relationship(back_populates="tags", link_model=CivitAI_ModelTagLink)

class CivitAI_ModelVersion(SQLModel, table=True):
    id: StrictInt = Field(primary_key=True)
    model_id: StrictInt = Field(foreign_key="civitai_model.id")
    # json_data: dict = Field(sa_column=Column(JSON), default_factory=dict)
    model: CivitAI_Model = Relationship(back_populates="model_versions")
    images: list["CivitAI_ModelVersionImage"] = Relationship(back_populates="model_version")

class CivitAI_ModelVersionImage(SQLModel, table=True):
    id: StrictInt = Field(primary_key=True)
    mime: str
    data: bytes = Field(sa_column=Column(BLOB), default_factory=bytes)
    model_version_id: StrictInt = Field(foreign_key="civitai_modelversion.id")
    # json_data: dict = Field(sa_column=Column(JSON), default_factory=dict)
    model_version: CivitAI_ModelVersion = Relationship(back_populates="images")