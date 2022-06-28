from typing import List
from pydantic import BaseModel


class OperationsDictionary(BaseModel):
    Average: List[int] = None
    Standard_deviation: List[int] = None
    Exponential_average: List[int] = None
