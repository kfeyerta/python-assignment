import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the provided source
try:
    df = pd.read_excel("WeatherData.xlsx")
except FileNotFoundError:
    print("Error: WeatherData.xlsx not found. Please ensure the file is in the same directory as the script.")
    exit()

# Rename columns for clarity
df.columns = ['Time', 'GlobalRadiation', 'DiffusRadiation', 'AmbientAirTemperature', 'AmbientAirHumidity']

# Convert 'Time' to numeric, handling potential errors
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')

# Drop rows with missing values in 'Time'
df = df.dropna(subset=['Time'])

# Ensure numeric columns are actually numeric
for col in ['GlobalRadiation', 'DiffusRadiation', 'AmbientAirTemperature', 'AmbientAirHumidity']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with missing values after numeric conversion
df = df.dropna()

# Calculate monthly averages
df['Month'] = df['Time'] // 24  # Assuming hourly data, 24 hours per day
monthly_averages = df.groupby('Month').mean()

# Plot individual columns
for col in ['GlobalRadiation', 'DiffusRadiation', 'AmbientAirTemperature', 'AmbientAirHumidity']:
    plt.figure(figsize=(12, 6))
    plt.plot(df['Time'], df[col])
    plt.title(f'{col} over Time')
    plt.xlabel('Hour of the Year')
    plt.ylabel(col)
    plt.grid(True)
    plt.show()

# Plot monthly average bar diagrams
for col in ['GlobalRadiation', 'DiffusRadiation', 'AmbientAirTemperature', 'AmbientAirHumidity']:
    plt.figure(figsize=(12, 6))
    monthly_averages[col].plot(kind='bar')
    plt.title(f'Average {col} per Month')
    plt.xlabel('Month')
    plt.ylabel(col)
    plt.xticks(range(len(monthly_averages)) )  # Ensure x-axis ticks are integers
    plt.grid(True)
    plt.show()