from pydantic import BaseModel, conint
from enum import IntEnum


class OperationType(IntEnum):
    REVENUE = 1
    SPENDING = 2


class Operation(BaseModel):
    id: int
    user_id: int
    type: OperationType
    description: str
    amount: conint(gt=0)
    date: str
