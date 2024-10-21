from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
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
    
    # Set your desired timezone
    my_timezone = timezone('Asia/Kolkata')  # Change this to your desired timezone
    
    # Schedule the fetch_and_process function with the timezone
    scheduler.add_job(fetch_and_process, 'interval', minutes=Config.FETCH_INTERVAL, timezone=my_timezone)
    scheduler.start()
