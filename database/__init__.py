from flask_pymongo import PyMongo
from config import Config

mongo = None

def mongo_init(app):
    global mongo
    app.config["MONGO_URI"] = Config.MONGO_URI
    mongo = PyMongo(app)
