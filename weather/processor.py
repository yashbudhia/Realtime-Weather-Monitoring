import datetime
from collections import defaultdict
from database.models import save_daily_summary

def process_weather_data(weather_data):
    """
    Process weather data for rollups and daily aggregates.
    """
    current_date = datetime.datetime.utcnow().date()
    weather_summary = defaultdict(list)

    for data in weather_data:
        city = data['city']
        weather_summary[city].append(data)
    
    for city, city_weather in weather_summary.items():
        temps = [entry['temp'] for entry in city_weather]
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        dominant_condition = get_dominant_condition(city_weather)
        
        # Save daily summary to the database
        summary = {
            'city': city,
            'date': current_date,
            'average_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }
        save_daily_summary(summary)

def get_dominant_condition(weather_data):
    """
    Determine the dominant weather condition based on frequency.
    """
    condition_counts = defaultdict(int)
    for entry in weather_data:
        condition_counts[entry['condition']] += 1
    return max(condition_counts, key=condition_counts.get)