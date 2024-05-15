import requests
import json

BASE_URL = "http://127.0.0.1:8000/user"


def test_signup():
    data = {
        "id": 0,
        "name": "Tzipi",
        "password": "12345678",
        "email": "t101010@gmail.com",
        "age": 19,
        "city": "Modiin Elit"
    }
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 200
    data["name"] = 'a'
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422
    data["name"] = 'Tzipi'
    data["password"] = '123'
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422
    data["password"] = "12345678"
    data["email"] = '101010.com'
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422
    data["email"] = 't101010@gmail.com'
    data["age"] = -5
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 422
    data["age"] = 19
    response = requests.post(BASE_URL + "/signup", data=json.dumps(data))
    assert response.status_code == 409


def test_login():
    data = {
        "name": "Tzipi",
        "password": "12345678"
    }
    response = requests.post(BASE_URL + "/login", data=json.dumps(data))
    assert response.status_code == 200
    assert response.json() == 0
    data["name"] = 'a'
    data["password"] = '123'
    response = requests.post(BASE_URL + "/login", data=json.dumps(data))
    assert response.status_code == 404


def test_updateDetails():
    userId = 0
    data = {
        "id": 0,
        "name": "Tzipi",
        "password": "123456",
        "email": "t2222@gmail.com",
        "age": 20,
        "city": "Jerusalem"
    }
    response = requests.put(BASE_URL + f"/updateDetails/{userId}", data=json.dumps(data))
    assert response.status_code == 200
    userId = -100
    response = requests.put(BASE_URL + f"/updateDetails/{userId}", data=json.dumps(data))
    assert response.status_code == 404
    userId = 0
    data["email"] = '101010.com'
    response = requests.put(BASE_URL + f"/updateDetails/{userId}", data=json.dumps(data))
    assert response.status_code == 422
