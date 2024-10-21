def check_alerts(city, current_temp):
    # Example threshold: alert if temperature exceeds 35°C for 2 consecutive updates
    threshold = 35
    if current_temp > threshold:
        print(f"ALERT: {city} temperature exceeds {threshold}°C!")
        # Implement logic to send email or trigger another alert system
