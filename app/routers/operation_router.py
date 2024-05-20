from fastapi import APIRouter, Request
from app.models.operation_model import Operation
import app.services.operation_service as operation_service
from utils.logger import log_request

operation_router = APIRouter()


@operation_router.get("/getBalance/{userId}")
@log_request
async def getBalance(userId, request: Request):
    return await operation_service.get_balance(userId)


@operation_router.get("/getAllRevenues/{userId}")
@log_request
async def getAllRevenues(userId, request: Request):
    return await operation_service.get_all_user_revenues(userId)


@operation_router.get("/getAllSpending/{userId}")
@log_request
async def getAllSpending(userId, request: Request):
    return await operation_service.get_all_user_spending(userId)


@operation_router.post("/add")
@log_request
async def add(operation: Operation, request: Request):
    return await operation_service.add_operation(operation)


@operation_router.put("/update/{operationId}")
@log_request
async def update(operationId, operation: Operation, request: Request):
    return await operation_service.update_operation(operationId, operation)


@operation_router.delete("/delete/{operationId}")
@log_request
async def delete(operationId, request: Request):
    return await operation_service.delete_operation(operationId)
