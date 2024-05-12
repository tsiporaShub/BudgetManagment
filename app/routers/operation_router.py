from fastapi import APIRouter
from app.models.operation_model import Operation
import app.services.operation_service as operation_service

operation_router = APIRouter()


@operation_router.get("/getBalance/{userId}")
async def getBalance(userId):
    return await operation_service.get_balance(userId)


@operation_router.get("/getAllRevenues/{userId}")
async def getAllRevenues(userId):
    return await operation_service.get_all_user_revenues(userId)


@operation_router.get("/getAllSpending/{userId}")
async def getAllSpending(userId):
    return await operation_service.get_all_user_spending(userId)


@operation_router.post("/add")
async def add(operation: Operation):
    return await operation_service.add_operation(operation)


@operation_router.put("/update/{operationId}")
async def update(operationId, operation: Operation):
    return await operation_service.update_operation(operationId, operation)


@operation_router.delete("/delete/{operationId}")
async def delete(operationId):
    return await operation_service.delete_operation(operationId)
