from fastapi import HTTPException

from app.db_management.config_db import operationsDB
from app.models.operation_model import Operation, OperationType
from app.services.user_service import is_exist


async def get_balance(userId):
    """
    A function to get the account balance of the user
    :param userId: the id of the user
    :return: the balance amount
    """
    sum_revenues = sum(r['amount'] for r in await get_all_user_revenues(userId))
    sum_spending = sum(s['amount'] for s in await get_all_user_spending(userId))
    return sum_revenues - sum_spending


async def get_all_user_revenues(userId):
    """
    A function to get all the user revenues
    :param userId: the id of the user
    :return: a list of all the user's revenues
    """
    revenues = list(operationsDB.find({'userId': int(userId), 'type': OperationType.REVENUE}))
    [r.pop('_id') for r in revenues]
    return revenues


async def get_all_user_spending(userId):
    """
    A function to get all the user spending
    :param userId: the id of the user
    :return: a list of all the user's spending
    """
    spending = list(operationsDB.find({'userId': int(userId), 'type': OperationType.SPENDING}))
    [s.pop('_id') for s in spending]
    return spending


async def add_operation(operation: Operation):
    """
    A function to add new operation - revenue or spending - to the operations collection in the DB
    :param operation: a operation to insert
    :return: the new operation when the add was successful
    """
    if not await is_exist(operation.userId):
        raise HTTPException(status_code=404, detail='The user is not exist')
    operations = list(operationsDB.find())
    if len(operations) == 0:
        operation.id = 0
    else:
        operation.id = int(operations[len(operations) - 1]['id'] + 1)
    operationsDB.insert_one(operation.__dict__)
    return operation


async def update_operation(operationId, operation: Operation):
    """
    A function to edit operation information
    :param operationId: the id of the operation
    :param operation: the new details of the operation
    :return: the updated operation
    """
    if operationsDB.find_one({"id": int(operationId)}) is None:
        raise HTTPException(status_code=404, detail='The operation is not exist')
    operationsDB.update_one({"id": int(operationId)},
                            {"$set": {'description': operation.description, 'amount': operation.amount}})
    return "Editing of the description and amount was successful"


async def delete_operation(operationId):
    """
    A function to delete operation from the collection in the DB
    :param operationId: the id of the operation
    :return: a message if the deletion was successful
    """
    if operationsDB.find_one({"id": int(operationId)}) is None:
        raise HTTPException(status_code=404, detail='The operation is not exist')
    operationsDB.delete_one({"id": int(operationId)})
    return "Delete operation "+operationId+" passed successfully"
