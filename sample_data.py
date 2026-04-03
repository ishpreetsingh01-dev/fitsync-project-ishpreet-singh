import pandas as pd

# Load the dataset
data_path = 'data/health_data.csv'
health_data = pd.read_csv(data_path)

# Print the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(health_data.head())

# Print the number of missing values in each column
missing_values = health_data.isnull().sum()
print("\nNumber of missing values in each column:")
print(missing_values)