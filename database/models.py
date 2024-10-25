from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.weather_db
summaries = db.daily_summaries

def save_daily_summary(summary):
    """
    Save the daily weather summary to MongoDB.
    """
    summaries.insert_one(summary)