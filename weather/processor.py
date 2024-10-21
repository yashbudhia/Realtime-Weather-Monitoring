from database.models import store_weather_data, store_daily_summary
import time

def process_weather_data(data, city):
    # Extract relevant data
    temp_k = data['main']['temp']
    temp_c = kelvin_to_celsius(temp_k)
    weather_condition = data['weather'][0]['main']
    timestamp = data['dt']
    
    # Store raw weather data
    store_weather_data(city, temp_c, weather_condition, timestamp)

    # Perform daily aggregation (simplified example)
    daily_summary = calculate_daily_aggregates(city)
    store_daily_summary(city, daily_summary)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def calculate_daily_aggregates(city):
    # Fetch daily data from MongoDB and calculate aggregates
    # This is a placeholder logic, you need to implement MongoDB queries
    avg_temp = 25  # Placeholder
    max_temp = 30  # Placeholder
    min_temp = 20  # Placeholder
    dominant_condition = "Clear"  # Placeholder
    return {
        "avg_temp": avg_temp,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "dominant_condition": dominant_condition
    }
