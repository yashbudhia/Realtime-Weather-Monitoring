import os

class Config:
    # OpenWeatherMap API Key
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'bd5e378503939ddaee76f12ad7a97608')
    
    # Weather monitoring interval (in minutes)
    FETCH_INTERVAL = 5

    # MongoDB Configuration
    MONGO_URI = "mongodb://localhost:27017/weather_db"
