from modules.processor import load_data, calculate_recovery_score
df = load_data()
df = calculate_recovery_score(df)
print(df[['Date', 'Steps', 'Sleep_Hours', 'Heart_rate_BPM', 'Cal_Burnt',
       'Active_minutes']].head(10))

