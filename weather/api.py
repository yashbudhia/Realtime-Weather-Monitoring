# api.py

from datetime import datetime, timedelta
import requests

def convert_kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "temp": convert_kelvin_to_celsius(data['main']['temp']),
            "feels_like": convert_kelvin_to_celsius(data['main']['feels_like']),
            "condition": data['weather'][0]['main'],
            "dt": datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')  # Format timestamp
        }
    return None

def calculate_daily_aggregates(weather_data):
    total_temp = 0
    max_temp = -float('inf')
    min_temp = float('inf')
    conditions = {}

    for data in weather_data:
        temp = data['temp']
        total_temp += temp
        max_temp = max(max_temp, temp)
        min_temp = min(min_temp, temp)

        # Track occurrences of weather conditions
        condition = data['condition']
        if condition in conditions:
            conditions[condition] += 1
        else:
            conditions[condition] = 1

    # Find the dominant weather condition
    dominant_condition = max(conditions, key=conditions.get)

    return {
        "average_temp": total_temp / len(weather_data),
        "max_temp": max_temp,
        "min_temp": min_temp,
        "dominant_condition": dominant_condition
    }

def fetch_forecast_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_list = []
        for item in data['list']:
            forecast_list.append({
                "dt": datetime.utcfromtimestamp(item['dt']).strftime('%Y-%m-%d %H:%M:%S'),
                "temp": convert_kelvin_to_celsius(item['main']['temp']),
                "condition": item['weather'][0]['main'],
            })
        return forecast_list
    return None
