from typing import List
from pydantic import BaseModel


class OperationsDictionary(BaseModel):
    """
    Pydantic Model to Serialize and Validate Incoming Parameters
    """

    Average: List[int] = None
    Standard_deviation: List[int] = None
    Exponential_average: List[int] = None
