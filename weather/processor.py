from datetime import datetime
from database.models import store_daily_summary

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def process_weather_data(weather_data):
    temp = kelvin_to_celsius(weather_data['main']['temp'])
    feels_like = kelvin_to_celsius(weather_data['main']['feels_like'])
    condition = weather_data['weather'][0]['main']
    timestamp = weather_data['dt']

    # Rollup the weather data
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
    
    daily_summary = {
        "date": date,
        "temperature": temp,
        "feels_like": feels_like,
        "condition": condition
    }
    
    store_daily_summary(daily_summary)
