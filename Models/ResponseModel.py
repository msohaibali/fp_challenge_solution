from typing import List
from pydantic import BaseModel


class ResponseModel(BaseModel):
    """
    Pydantic Model to Serialize Response Parameters
    """

    Loading_Time: str = None
    Processing_Time: str = None
    Final_Features_List: List[str] = None
