from pydantic import BaseModel

class DataModel(BaseModel):
    id: str
    type: str
    relativePath: str
    text: str
    sorting: str