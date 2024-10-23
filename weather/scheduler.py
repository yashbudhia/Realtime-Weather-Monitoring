import time
import threading
from weather.api import get_weather_data
from weather.processor import process_weather_data
from config import Config

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def fetch_and_process_weather():
    for city in CITIES:
        weather_data = get_weather_data(city)
        if weather_data:
            process_weather_data(weather_data)

def start_weather_scheduler():
    def run_scheduler():
        while True:
            fetch_and_process_weather()
            time.sleep(Config.WEATHER_INTERVAL)
    
    weather_thread = threading.Thread(target=run_scheduler)
    weather_thread.daemon = True
    weather_thread.start()
