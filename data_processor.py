import random

def fetch_weather_data():
    # Simulating real-time weather data fetching
    data = {
        "temperature": random.uniform(15, 35),  # Celsius
        "humidity": random.uniform(40, 80),     # Percentage
        "wind_speed": random.uniform(5, 30)     # km/h
    }
    return data
