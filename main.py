import streamlit as st
from modules.processor import process_data
import pandas as pd

# Set the page configuration
st.set_page_config(layout="wide", page_title="FitSync")

# Title of the dashboard
st.title("FitSync - Personal Health Analytics")

# Sidebar for Time Range Filter
st.sidebar.header("Filters")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All Time"],
    index=2
)

# Load and process data
try:
    df = process_data()
    
    # 1. Ensure 'Date' is datetime (Capital 'D')
    df['Date'] = pd.to_datetime(df['Date'])

    # 2. Fix the Filtering Logic
    if time_range == "Last 7 Days":
        # Filter relative to the NEWEST date in your data, not today's date
        latest_date = df['Date'].max()
        df = df[df['Date'] >= (latest_date - pd.Timedelta(days=7))]
    elif time_range == "Last 30 Days":
        latest_date = df['Date'].max()
        df = df[df['Date'] >= (latest_date - pd.Timedelta(days=30))]
    # "All Time" doesn't need a filter, so it stays as is

    # Check if the dataframe is empty after filtering
    if df.empty:
        st.warning("No data found for the selected time range.")
    else:
        # 3. Use 'Steps' (Capital 'S') to match your processor.py
        average_steps = df['Steps'].mean()
        average_sleep_hours = df['Sleep_Hours'].mean()
        average_recovery_score = df['Recovery_Score'].mean()

        # Display the metrics
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Average Steps", value=f"{average_steps:.0f}")
        col2.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}")
        col3.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}")

        # Display the table
        st.write("### Recent Health Logs", df.head())

except Exception as e:
    st.error("An error occurred while processing the data.")
    st.exception(e)