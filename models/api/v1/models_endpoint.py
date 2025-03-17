from models.api.v1.modelId_endpoint import ModelId_Response
from pydantic import BaseModel
from typing import List

class Models_Response(BaseModel):
    items: List[ModelId_Response]
