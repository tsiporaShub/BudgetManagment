from pydantic import BaseModel
from enum import IntEnum


class OperationType(IntEnum):
    REVENUE = 1
    SPENDING = 2


class Operation(BaseModel):
    id: int
    userId: int
    type: OperationType
    description: str
    count: int
    date: str
