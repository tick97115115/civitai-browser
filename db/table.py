from sqlmodel import SQLModel, Field, Relationship
# from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy import Column, JSON
from models.api.v1.base.misc import Model_Types
from models.api.v1.modelId_endpoint import ModelId_Response
from pydantic import StrictInt

class CivitAI_Model(SQLModel, table=True):
    id: StrictInt = Field(primary_key=True)
    name: str = Field(index=True)
    type: Model_Types = Field(index=True)
    nsfw: bool
    json_data: dict = Field(sa_column=Column(JSON), default_factory=dict)
    model_versions: list["CivitAI_ModelVersion"] = Relationship(back_populates="model")

# class CivitAI_Model_Tag(SQLModel, table=True):
#     model_id: StrictInt = Field(index=True)
#     tag_id: StrictInt = Field(index=True)

# class CivitAI_Tag(SQLModel, table=True):
#     id: StrictInt | None = Field(default=None, primary_key=True)
#     name: str = Field(unique=True, index=True)

class CivitAI_ModelVersion(SQLModel, table=True):
    id: StrictInt = Field(primary_key=True)
    model_id: StrictInt = Field(foreign_key="civitai_model.id")
    # json_data: dict = Field(sa_column=Column(JSON), default_factory=dict)
    model: CivitAI_Model = Relationship(back_populates="model_versions")
