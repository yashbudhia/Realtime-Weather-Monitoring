from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Load configuration from environment or use defaults
OPENWEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'bd5e378503939ddaee76f12ad7a97608')
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_weather_data(city):
    """
    Fetch weather data for a city using the OpenWeatherMap API.
    Returns weather details as a dictionary.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Convert temperature from Kelvin to Celsius
        temp_celsius = data['main']['temp'] - 273.15
        feels_like_celsius = data['main']['feels_like'] - 273.15
        weather_condition = data['weather'][0]['main']
        
        return {
            "city": city,
            "temp": round(temp_celsius, 2),
            "feels_like": round(feels_like_celsius, 2),
            "condition": weather_condition,
            "dt": data['dt']  # Unix timestamp of the data update
        }
    else:
        print(f"Failed to fetch weather data for {city}")
        return None

@app.route('/')
def index():
    # Get weather data for all cities
    weather_summaries = [get_weather_data(city) for city in CITIES if get_weather_data(city) is not None]
    
    return render_template('index.html', weather_summaries=weather_summaries)

if __name__ == '__main__':
    app.run(debug=True)
