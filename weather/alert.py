# alert.py

def check_alert_condition(weather_data, threshold):
    """
    Check if the temperature exceeds the threshold for two consecutive updates.
    """
    alerts = []
    for i in range(len(weather_data) - 1):
        current_temp = weather_data[i]['temp']
        next_temp = weather_data[i + 1]['temp']
        if current_temp > threshold and next_temp > threshold:
            alerts.append(f"Alert! Temperature in {weather_data[i]['city']} exceeded {threshold}°C for two consecutive updates.")
    return alerts
