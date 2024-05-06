from enum import Enum
from pydantic import BaseModel

OperationType = Enum('OperationType', ['REVENUE', 'SPENDING'])


class Operation(BaseModel):
    type: OperationType
    description: str
    count: int
    date: str
