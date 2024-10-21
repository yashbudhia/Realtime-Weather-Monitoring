from . import mongo
import datetime

def store_weather_data(city, temp, weather_condition, timestamp):
    data = {
        "city": city,
        "temp": temp,
        "condition": weather_condition,
        "timestamp": datetime.datetime.fromtimestamp(timestamp)
    }
    mongo.db.weather_data.insert_one(data)

def store_daily_summary(city, summary):
    summary['city'] = city
    summary['date'] = datetime.datetime.now().date()
    mongo.db.daily_summaries.insert_one(summary)
