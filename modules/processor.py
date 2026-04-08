import pandas as pd
import numpy as np

def load_data():
    data_path = 'data/health_data.csv'
    health_data = pd.read_csv(data_path)

    # Use 'Steps' (Capitalized) to match your CSV screenshot
    if 'Steps' in health_data.columns:
        # Fill missing values (NaN) with 0 first
        health_data['Steps'] = health_data['Steps'].fillna(0)
        
        # If steps are 0, replace with random realistic values
        zero_steps = health_data['Steps'] == 0
        if zero_steps.any():
            health_data.loc[zero_steps, 'Steps'] = np.random.randint(3000, 7000, size=zero_steps.sum())
    
    return health_data

def calculate_recovery_score(df):
    def compute_score(row):
        score = 50

        # Sleep Hours Contribution
        if row['Sleep_Hours'] >= 7:
            score += 20
        elif row['Sleep_Hours'] < 6:
            score -= 20

        # Heart Rate Contribution (Corrected name)
        if row['Heart_rate_BPM'] <= 60:
            score += 15
        elif row['Heart_rate_BPM'] >= 90:
            score -= 10

        # Steps Contribution (Changed to 'Steps' with Capital S)
        if 4000 <= row['Steps'] <= 10000:
            score += 5
        elif row['Steps'] > 16000:
            score -= 5

        return max(0, min(100, score))

    df['Recovery_Score'] = df.apply(compute_score, axis=1)
    return df

def process_data():
    df = load_data()
    
    # Check for Capitalized 'Steps'
    if 'Steps' not in df.columns:
        df['Steps'] = 0

    df = calculate_recovery_score(df)
    return df