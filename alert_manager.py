def check_weather_alerts(data):
    alerts = []
    if data["temperature"] > 30:
        alerts.append(f"High Temperature Alert: {data['temperature']}°C")
    if data["wind_speed"] > 25:
        alerts.append(f"High Wind Speed Alert: {data['wind_speed']} km/h")
    if data["humidity"] < 45:
        alerts.append(f"Low Humidity Alert: {data['humidity']}%")

    return alerts
