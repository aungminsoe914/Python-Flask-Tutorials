import pandas as pd
import matplotlib.pyplot as plt

# Sample weather data
data = {
    'Date': ['2024-10-20', '2024-10-21', '2024-10-22', '2024-10-23'],
    'Temperature (°C)': [22, 21, 19, 23],
    'Humidity (%)': [60, 65, 70, 75]
}

# Create a DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Create a figure and axis
fig, ax1 = plt.subplots()

# Plot temperature on the primary y-axis
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)', color='tab:red')
ax1.plot(df['Date'], df['Temperature (°C)'], color='tab:red', label='Temperature', marker='o')
ax1.tick_params(axis='y', labelcolor='tab:red')

# Create a second y-axis for humidity
ax2 = ax1.twinx()
ax2.set_ylabel('Humidity (%)', color='tab:blue')
ax2.plot(df['Date'], df['Humidity (%)'], color='tab:blue', label='Humidity', marker='o')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Add a title and legend
plt.title('Weather Data: Temperature and Humidity')
fig.tight_layout()  # to make room for the second y-axis
plt.show()
