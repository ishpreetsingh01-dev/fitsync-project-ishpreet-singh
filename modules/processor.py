import pandas as pd

# Define a function to load and preprocess the health data

def load_data():
    """
    Loads health data from a CSV file, handles missing values, and returns the cleaned DataFrame.
    """
    # Load the dataset
    data_path = 'data/health_data.csv'
    health_data = pd.read_csv(data_path)
    
    # Fill missing values for 'steps' with the median value
    if 'steps' in health_data.columns:
        steps_median = health_data['steps'].median()
        health_data['steps'].fillna(steps_median, inplace=True)

    # Fill missing values for 'Sleep_Hours' with 7.0
    if 'Sleep_Hours' in health_data.columns:
        health_data['Sleep_Hours'].fillna(7.0, inplace=True)

    # Fill missing values for 'Hear_Rate_Bpm' with 68
    if 'Heart_rate_BPM' in health_data.columns:
        health_data['Heart_rate_BPM'].fillna(68, inplace=True)

    # Fill missing values for other columns with their median
    for column in health_data.columns:
        if health_data[column].isnull().any():
            median_value = health_data[column].median()
            health_data[column].fillna(median_value, inplace=True)

    # Convert the 'date' column to datetime objects
    if 'date' in health_data.columns:
        health_data['date'] = pd.to_datetime(health_data['date'])

    # Return the cleaned DataFrame
    return health_data

# Define a function to calculate the recovery score for each entry in the DataFrame

def calculate_recovery_score(df):
    """
    Adds a 'Recovery_Score' column to the DataFrame based on Sleep_Hours, Hear_Rate_Bpm, and steps.
    The score ranges from 0 to 100, reflecting the recovery quality.
    """
    def compute_score(row):
        # Start with a neutral score
        score = 50

        # Sleep Hours Contribution
        if row['Sleep_Hours'] >= 7:
            score += 20  # Good sleep boosts the score
        elif row['Sleep_Hours'] < 6:
            score -= 20  # Poor sleep reduces the score

        # Heart Rate Contribution
        if row['Hear_Rate_Bpm'] <= 60:
            score += 15  # Lower resting heart rate boosts the score
        elif row['Hear_Rate_Bpm'] >= 90:
            score -= 10  # Higher heart rate reduces the score

        # Steps Contribution
        if 4000 <= row['steps'] <= 10000:
            score += 5  # Moderate activity slightly boosts the score
        elif row['steps'] > 16000:
            score -= 5  # Very high activity slightly reduces the score

        # Ensure the score remains between 0 and 100
        score = max(0, min(100, score))
        return score

    # Apply the compute_score function to each row in the DataFrame
    df['Recovery_Score'] = df.apply(compute_score, axis=1)
    return df

