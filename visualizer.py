import matplotlib.pyplot as plt

def plot_weather_data(weather_data_store):
    if not weather_data_store:
        print("No data to plot yet.")
        return

    # Extract data for plotting
    temperatures = [data["temperature"] for data in weather_data_store]
    humidities = [data["humidity"] for data in weather_data_store]
    wind_speeds = [data["wind_speed"] for data in weather_data_store]
    times = list(range(1, len(weather_data_store) + 1))

    # Create subplots for temperature, humidity, and wind speed
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

    ax1.plot(times, temperatures, label="Temperature (°C)", color="red")
    ax1.set_title("Temperature over Time")
    ax1.set_ylabel("Temperature (°C)")
    
    ax2.plot(times, humidities, label="Humidity (%)", color="blue")
    ax2.set_title("Humidity over Time")
    ax2.set_ylabel("Humidity (%)")
    
    ax3.plot(times, wind_speeds, label="Wind Speed (km/h)", color="green")
    ax3.set_title("Wind Speed over Time")
    ax3.set_ylabel("Wind Speed (km/h)")
    ax3.set_xlabel("Time (Minutes)")

    plt.tight_layout()
    plt.show()
