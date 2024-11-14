from typing import List

from pydantic import RootModel

from entities.response_Item import ResponseItem


class ResponseModel(RootModel[List[ResponseItem]]):
    pass