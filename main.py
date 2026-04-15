import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="FitSync",
    page_icon="https://m.media-amazon.com/images/I/5132ky49QkL.png"
)

# --- SIDEBAR LOGO ---
st.sidebar.image("https://m.media-amazon.com/images/I/5132ky49QkL.png", width=80)
st.sidebar.write("### ⚡ FitSync Menu")
st.sidebar.divider()

# --- STYLING ---
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                          url("https://media.istockphoto.com/id/496719837/photo/motivation-fuels-the-human-engine.jpg?s=612x612&w=0&k=20&c=kz5YL7dYzmQpbRTbEafeFshJ3nSslVoJ5Hypf0uxYzI=");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    div[data-testid="stMetricValue"] { font-size: 32px !important; color: #00d4ff !important; }
    .stMetric {
        background-color: rgba(30, 33, 48, 0.6) !important;
        padding: 15px !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENT ---
st.title("⚡ FitSync")
st.subheader("Your Personal Health Analytics Dashboard")
st.info("👈 Use the sidebar to navigate between the Dashboard and Trend insights.")
st.divider()