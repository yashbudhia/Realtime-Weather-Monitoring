from flask import Flask, render_template
import os
from weather.api import fetch_weather_data, calculate_daily_aggregates
from weather.alert import check_alert_condition

app = Flask(__name__)

# Load configuration from environment or use defaults
OPENWEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'bd5e378503939ddaee76f12ad7a97608')
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
ALERT_THRESHOLD = 35  # Celsius

@app.route('/')
def index():
    # Get weather data for all cities
    weather_data = [fetch_weather_data(city, OPENWEATHER_API_KEY) for city in CITIES if fetch_weather_data(city, OPENWEATHER_API_KEY) is not None]

    # Calculate daily aggregates for all cities
    daily_summary = calculate_daily_aggregates(weather_data)

    # Check for any alerts based on the temperature threshold
    alerts = check_alert_condition(weather_data, ALERT_THRESHOLD)

    return render_template('index.html', weather_data=weather_data, daily_summary=daily_summary, alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)
