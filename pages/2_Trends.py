import streamlit as st
import pandas as pd
import plotly.express as px
from modules.processor import process_data

st.set_page_config(layout="wide", page_title="FitSync Trends")
st.title("📈 Trends & Deep Insights")

@st.cache_data
def process_and_prepare_data():
    df = process_data()
    df['Date'] = pd.to_datetime(df['Date'])
    return df
    
try:
    df = process_and_prepare_data()

    # Simple Tabbed Interface
    tab1, tab2 = st.tabs(["📊 Summary Statistics", "🔍 Distribution Analysis"])

    with tab1:
        st.subheader("Performance Summary")
        summary = df[['Recovery_Score', 'Sleep_Hours', 'Steps', 'Cal_Burnt']].agg(['mean', 'min', 'max']).T
        st.dataframe(summary.style.highlight_max(axis=0, color='#2e7d32'), use_container_width=True)
        
        st.subheader("Monthly Progress")
        df['Month'] = df['Date'].dt.strftime('%b %Y')
        monthly = df.groupby('Month')['Recovery_Score'].mean().reset_index()
        fig = px.bar(monthly, x='Month', y='Recovery_Score', color='Recovery_Score', template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(px.histogram(df, x='Steps', title="Step Distribution", template="plotly_dark", color_discrete_sequence=['#00d4ff']), use_container_width=True)
            st.plotly_chart(px.histogram(df, x='Recovery_Score', title="Recovery Distribution", template="plotly_dark", color_discrete_sequence=['#d33682']), use_container_width=True)
        with col2:
            st.plotly_chart(px.histogram(df, x='Cal_Burnt', title="Calorie Distribution", template="plotly_dark", color_discrete_sequence=['#39FF14']), use_container_width=True)
            st.plotly_chart(px.histogram(df, x='Sleep_Hours', title="Sleep Distribution", template="plotly_dark", color_discrete_sequence=['#FFFB00']), use_container_width=True)

except Exception as e:
    st.error(f"Error loading trends: {e}")