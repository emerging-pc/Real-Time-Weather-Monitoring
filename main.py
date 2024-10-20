import schedule
import time
from data_processor import fetch_weather_data
from alert_manager import check_weather_alerts
from visualizer import plot_weather_data

# In-memory data store
weather_data_store = []

def log_weather_data():
    data = fetch_weather_data()
    print(f"New Weather Data: {data}")
    weather_data_store.append(data)

    # Check for alerts
    alerts = check_weather_alerts(data)
    if alerts:
        for alert in alerts:
            print(alert)

# Schedule the data fetch every minute
schedule.every(1).minute.do(log_weather_data)

def display_visualization():
    plot_weather_data(weather_data_store)

schedule.every(5).minutes.do(display_visualization)

if __name__ == "__main__":
    print("Starting real-time weather monitoring system...")
    while True:
        schedule.run_pending()
        time.sleep(1)

