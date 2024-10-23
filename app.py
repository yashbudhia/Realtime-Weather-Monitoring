from flask import Flask, render_template
from weather.scheduler import start_weather_scheduler
from database import init_db
import random  # Simulating weather data for now

app = Flask(__name__)

# Initialize database
init_db()

# Start weather data scheduler
start_weather_scheduler()

@app.route('/')
def index():
    # Simulating weather summaries
    weather_summaries = [
        {"city": "Delhi", "avg_temp": random.uniform(20, 30), "max_temp": random.uniform(30, 40), "min_temp": random.uniform(15, 20), "condition": "Clear"},
        {"city": "Mumbai", "avg_temp": random.uniform(25, 35), "max_temp": random.uniform(35, 40), "min_temp": random.uniform(20, 25), "condition": "Rain"},
        {"city": "Bangalore", "avg_temp": random.uniform(18, 28), "max_temp": random.uniform(28, 33), "min_temp": random.uniform(15, 20), "condition": "Cloudy"}
    ]
    
    return render_template('index.html', weather_summaries=weather_summaries)

if __name__ == '__main__':
    app.run(debug=True)
