from pymongo import MongoClient

client = MongoClient("")

db = client['budget_management_DB']

users = db['users']
operations = db['operations']
