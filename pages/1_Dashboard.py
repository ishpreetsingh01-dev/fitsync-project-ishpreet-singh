import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Title of the dashboard
st.title("📊 Dashboard Overview")

# Sidebar for Time Range Filter
st.sidebar.header("Settings")
time_range = st.sidebar.selectbox("Time Range", ["Last 7 Days", "Last 30 Days", "All Time"], index=2)

COLORS = ["#00d4ff", "#d33682", "#39FF14", "#FFFB00"]

try:
    df = process_data()
    df['Date'] = pd.to_datetime(df['Date'])

    # Filtering Logic
    if time_range == "Last 7 Days":
        filtered_df = df[df['Date'] >= (df['Date'].max() - pd.Timedelta(days=7))]
    elif time_range == "Last 30 Days":
        filtered_df = df[df['Date'] >= (df['Date'].max() - pd.Timedelta(days=30))]
    else:
        filtered_df = df

    # --- Metrics Section ---
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Avg Steps", f"{filtered_df['Steps'].mean():.0f}")
    with m2:
        st.metric("Avg Sleep", f"{filtered_df['Sleep_Hours'].mean():.1f}h")
    with m3:
        st.metric("Avg Recovery", f"{filtered_df['Recovery_Score'].mean():.1f}%")

    st.divider()

    # --- Charts Section ---
    c1, c2 = st.columns(2)
    
    with c1:
        # Fixed: Removed border=True
        with st.container():
            st.subheader("Recovery & Sleep Trend")
            fig1 = px.line(filtered_df, x='Date', y=['Recovery_Score', 'Sleep_Hours'],
                          color_discrete_sequence=[COLORS[0], COLORS[1]], template="plotly_dark")
            fig1.update_layout(margin=dict(l=0, r=0, t=30, b=0), legend=dict(orientation="h", yanchor="bottom", y=1.02))
            st.plotly_chart(fig1, use_container_width=True)

    with c2:
        with st.container():
            st.subheader("Recovery vs Daily Steps")
            fig2 = px.scatter(filtered_df, x="Recovery_Score", y="Steps", color="Sleep_Hours",
                             color_continuous_scale="Viridis", template="plotly_dark")
            st.plotly_chart(fig2, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        with st.container():
            st.subheader("Recovery vs Heart Rate")
            fig3 = px.scatter(filtered_df, x="Recovery_Score", y="Heart_rate_BPM", 
                             template="plotly_dark", color_discrete_sequence=[COLORS[2]])
            st.plotly_chart(fig3, use_container_width=True)

    with c4:
        with st.container():
            st.subheader("Calories Burned Trend")
            fig4 = px.area(filtered_df, x='Date', y='Cal_Burnt', 
                          template="plotly_dark", color_discrete_sequence=[COLORS[0]])
            st.plotly_chart(fig4, use_container_width=True)

except Exception as e:
    st.error(f"Error loading dashboard: {e}")