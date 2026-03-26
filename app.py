import streamlit as st
import requests
import pickle

# Load ML model
with open("weather_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page setup
st.set_page_config(page_title="ML Weather App", layout="centered")

# CSS + Font
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #0f172a, #1e293b);
}

.title {
    text-align: center;
    font-size: 34px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 25px;
}

label {
    color: #cbd5f5 !important;
    font-size: 16px !important;
    font-weight: 500;
}

input {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

button {
    width: 100%;
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: 600;
}

.card {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 10px;
    color: white;
    font-size: 16px;
}

.city {
    font-size: 24px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🤖 Weather App</div>', unsafe_allow_html=True)

# Input
city = st.text_input("Enter City")

# Button
if st.button("Get Weather"):

    api_key = "98b6efec3031d1ed252670f76c919618"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        data = requests.get(url).json()

        if data.get("cod") != 200:
            st.error("City not found")
        else:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            # ML Prediction
            prediction = model.predict([[temp, humidity, wind]])[0]

            st.markdown(f'<div class="card city">{city}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card">🌡 Temperature: {temp} °C</div>', unsafe_allow_html=True)

            if prediction == 1:
                st.markdown('<div class="card">🌧 Rain likely (ML Prediction)</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="card">☀ No rain expected (ML Prediction)</div>', unsafe_allow_html=True)

            st.markdown(f'<div class="card">💧 Humidity: {humidity}%</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card">🌬 Wind: {wind} m/s</div>', unsafe_allow_html=True)

    except:
        st.error("Something went wrong")