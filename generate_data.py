import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set the seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define date range
start_date = datetime(2025, 1, 1)
date_range = [start_date + timedelta(days=i) for i in range(365)]

# Define realistic ranges
steps_mean, steps_std = 7650, 1000
sleep_hours_mean, sleep_hours_std = 7.3, 1
heart_rate_mean, heart_rate_std = 72, 10
cal_burnt_mean, cal_burnt_std = 2000, 500
active_minutes_mean, active_minutes_std = 160, 50

# Generate data
steps = np.random.normal(steps_mean, steps_std, 365).clip(3000, 18000)
sleep_hours = np.random.normal(sleep_hours_mean, sleep_hours_std, 365).clip(4, 10)
heart_rate = np.random.normal(heart_rate_mean, heart_rate_std, 365).clip(45, 125)
cal_burnt = np.random.normal(cal_burnt_mean, cal_burnt_std, 365).clip(500, 3500)
active_minutes = np.random.normal(active_minutes_mean, active_minutes_std, 365).clip(20, 300)

# Create a DataFrame
data = pd.DataFrame({
    'Date': date_range,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_rate_BPM': heart_rate,
    'Cal_Burnt': cal_burnt,
    'Active_minutes': active_minutes
})

# At the very end of your generate_data.py script
print(f"DataFrame created with {len(data)} rows.")
try:
    data.to_csv('data/health_data.csv', index=False)
    print("Success! Data saved to data/health_data.csv")
except Exception as e:
    print(f"Error saving file: {e}")

    
# Introduce 5% missing values randomly in each column
for column in data.columns[1:]:  # Skip Date column
    data.loc[data.sample(frac=0.05).index, column] = np.nan

# Save the data to a CSV file
data.to_csv('data/health_data.csv', index=False)

