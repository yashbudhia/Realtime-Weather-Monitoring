from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.weather_db

def init_db():
    print("Database initialized.")
