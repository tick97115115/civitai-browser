from sqlmodel import SQLModel, Field, Relationship
from pydantic import StrictInt

class ModelVersionGopeedTask(SQLModel, table=True):
    version_id: StrictInt = Field(primary_key=True)
    task_id: str
    file_name: str
    path: str
    image_tasks: list["ModelVersionImageGopeedTask"] = Relationship(back_populates="model_version_task")

class ModelVersionImageGopeedTask(SQLModel, table=True):
    version_id: StrictInt = Field(foreign_key=f"{ModelVersionGopeedTask.__tablename__}.version_id", index=True)
    task_id: str = Field(primary_key=True)
    file_name: str
    path: str
    model_version_task: ModelVersionGopeedTask = Relationship(back_populates="image_tasks")
