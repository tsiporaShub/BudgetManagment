from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1")

db = client['budget_management_DB']

usersDB = db['users']
operationsDB = db['operations']
