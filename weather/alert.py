from config import Config

def check_thresholds(weather_data):
    temp = weather_data['temperature']
    if temp > Config.ALERT_THRESHOLD:
        trigger_alert(weather_data)

def trigger_alert(weather_data):
    print(f"ALERT: Temperature in {weather_data['city']} exceeded {Config.ALERT_THRESHOLD}°C!")
    # Optional: Implement email notifications or other alerting systems
