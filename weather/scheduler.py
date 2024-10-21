from apscheduler.schedulers.background import BackgroundScheduler
from weather.api import fetch_weather_data
from weather.processor import process_weather_data
from config import Config

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

def fetch_and_process():
    for city in CITIES:
        data = fetch_weather_data(city)
        if data:
            process_weather_data(data, city)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_process, 'interval', minutes=Config.FETCH_INTERVAL)
    scheduler.start()
