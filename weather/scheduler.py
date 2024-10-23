import time
from threading import Timer
from weather.api import get_weather_updates
from weather.processor import process_weather_data

class WeatherScheduler:
    def __init__(self, interval):
        self.interval = interval

    def start(self):
        """
        Start the weather data retrieval and processing at regular intervals.
        """
        self.fetch_and_process()
        Timer(self.interval, self.start).start()

    def fetch_and_process(self):
        """
        Fetch the weather data and process it for rollups/aggregates.
        """
        weather_data = get_weather_updates()
        if weather_data:
            process_weather_data(weather_data)

# In app.py or main script
if __name__ == '__main__':
    scheduler = WeatherScheduler(Config.WEATHER_INTERVAL)
    scheduler.start()
