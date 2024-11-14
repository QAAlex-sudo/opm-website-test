from pydantic import BaseModel

from entities.data_model import DataModel


class ResponseItem(BaseModel):
    data: DataModel
    score: float