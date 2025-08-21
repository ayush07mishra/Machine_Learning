import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("aqi_model.pkl", "rb"))

st.set_page_config(page_title="AQI Predictor", layout="centered")

st.title("🌫️ Air Quality Index (AQI) Predictor")
st.markdown("Enter air pollution data and date details to predict AQI.")

# ----- Input Fields -----
st.subheader("📅 Date and Temporal Information")
month = st.number_input("Month", min_value=1, max_value=12, step=1)
year = st.number_input("Year", min_value=2015, max_value=2030, step=1)
days = st.number_input("Day of Month", min_value=1, max_value=31, step=1)
holidays_count = st.number_input("Number of Holidays", min_value=0, max_value=10, step=1)

st.subheader("🧪 Pollution Metrics")
pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0)
pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0)
no2 = st.number_input("NO₂ (µg/m³)", min_value=0.0)
so2 = st.number_input("SO₂ (µg/m³)", min_value=0.0)
co = st.number_input("CO (mg/m³)", min_value=0.0)
ozone = st.number_input("Ozone (µg/m³)", min_value=0.0)

st.subheader("📆 Day of the Week")
weekday = st.selectbox("Weekday", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

# One-hot encode weekday
weekday_list = ["Friday", "Monday", "Saturday", "Sunday", "Thursday", "Tuesday", "Wednesday"]
weekday_encoded = [1 if weekday == day else 0 for day in weekday_list]

# Construct final input in correct order
input_data = np.array([
    month, year, holidays_count, days,
    pm25, pm10, no2, so2, co, ozone,
    *weekday_encoded
]).reshape(1, -1)

# Prediction
if st.button("🔍 Predict AQI"):
    prediction = model.predict(input_data)[0]
    st.success(f"🟢 Predicted AQI: **{prediction:.2f}**")
