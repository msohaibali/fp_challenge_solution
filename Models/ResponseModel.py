from typing import List
from pydantic import BaseModel


class ResponseModel(BaseModel):
    Loading_Time: str = None
    Processing_Time: str = None
    Final_Features_List: List[str] = None
