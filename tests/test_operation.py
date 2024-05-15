import requests
import json

BASE_URL = "http://127.0.0.1:8000/operation"


def test_add_operation():
    data = {
        "id": 0,
        "userId": 0,
        "type": 1,
        "description": "salary from balance",
        "amount": 20000,
        "date": "15/05/2024"
    }
    response = requests.post(BASE_URL + "/add", data=json.dumps(data))
    assert response.status_code == 200
    data["userId"] = 100
    response = requests.post(BASE_URL + "/add", data=json.dumps(data))
    assert response.status_code == 404
    data["userId"] = 0
    data["amount"] = '-500'
    response = requests.post(BASE_URL + "/add", data=json.dumps(data))
    assert response.status_code == 422
    data["amount"] = '20000'
    data["type"] = 9
    response = requests.post(BASE_URL + "/add", data=json.dumps(data))
    assert response.status_code == 422


def test_update_operation():
    operationId = 0
    data = {
        "id": 0,
        "userId": 0,
        "type": 1,
        "description": "salary from balance + bonus",
        "amount": 30000,
        "date": "15/05/2024"
    }
    response = requests.put(BASE_URL + f"/update/{operationId}", data=json.dumps(data))
    assert response.status_code == 200
    operationId = 100
    response = requests.put(BASE_URL + f"/update/{operationId}", data=json.dumps(data))
    assert response.status_code == 404


def test_get_balance():
    userId = 0
    response = requests.get(BASE_URL + f"/getBalance/{userId}")
    assert response.status_code == 200
    assert response.json() == 30000
    userId = 100
    response = requests.get(BASE_URL + f"/getBalance/{userId}")
    assert response.status_code == 404


def test_get_all_user_revenues():
    userId = 0
    response = requests.get(BASE_URL + f"/getAllRevenues/{userId}")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 0,
            "userId": 0,
            "type": 1,
            "description": "salary from balance + bonus",
            "amount": 30000,
            "date": "15/05/2024"
        }
    ]
    userId = 100
    response = requests.get(BASE_URL + f"/getAllRevenues/{userId}")
    assert response.status_code == 404


def test_get_all_user_spending():
    userId = 0
    response = requests.get(BASE_URL + f"/getAllSpending/{userId}")
    assert response.status_code == 200
    assert response.json() == []
    userId = 100
    response = requests.get(BASE_URL + f"/getAllSpending/{userId}")
    assert response.status_code == 404


def test_delete_operation():
    operationId = 0
    response = requests.delete(BASE_URL + f"/delete/{operationId}")
    assert response.status_code == 200
    operationId = 100
    response = requests.delete(BASE_URL + f"/delete/{operationId}")
    assert response.status_code == 404
