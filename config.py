import os

class Config:
    # OpenWeatherMap API Key
    OPENWEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'bd5e378503939ddaee76f12ad7a97608')
    WEATHER_INTERVAL = int(os.getenv('WEATHER_INTERVAL', 300))  # Default to 5 minutes (300 seconds)
    ALERT_THRESHOLD = 35  # Default alert threshold in Celsius
    MONGO_URI = 'mongodb://localhost:27017/weather_db'

