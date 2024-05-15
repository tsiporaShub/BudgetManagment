from app.db_management.config_db import operationsDB
from app.models.operation_model import Operation, OperationType


async def get_balance(userTd):
    """
    A function to get the account balance of the user
    :param userTd: the id of the user
    :return: the balance amount
    """


async def get_all_user_revenues(userId):
    """
    A function to get all the user revenues
    :param userId: the id of the user
    :return: a list of all the user's revenues
    """
    revenues = list(operationsDB.find({'userId': int(userId), 'type': OperationType.REVENUE}))
    for r in revenues:
        r.pop('_id')
    return list(revenues)


async def get_all_user_spending(userId):
    """
    A function to get all the user spending
    :param userId: the id of the user
    :return: a list of all the user's spending
    """
    revenues = list(operationsDB.find({'userId': int(userId), 'type': OperationType.SPENDING}))
    for r in revenues:
        r.pop('_id')
    return list(revenues)


async def add_operation(operation: Operation):
    """
    A function to add new operation - revenue or spending - to the operations collection in the DB
    :param operation: a operation to insert
    :return: the new operation when the add was successful
    """
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


async def delete_operation(operationId):
    """
    A function to delete operation from the collection in the DB
    :param operationId: the id of the operation
    :return: a message if the deletion was successful
    """
