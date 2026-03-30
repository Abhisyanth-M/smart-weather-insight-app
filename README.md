# Smart Weather Insight App

A Machine Learning web application that predicts rainfall based on real-time weather inputs like temperature, humidity and wind conditions.

## Live Demo
https://wbykyecfwddzhkyfpdlhx3.streamlit.app/

## Overview
Smart Weather Insight App uses a trained ML model to predict whether it will rain based on weather parameters entered by the user. The goal was to understand how different atmospheric factors contribute to rainfall prediction and deploy it as a working web application.

## Features
- Takes real-time weather inputs from the user
- Uses a trained ML model to predict rainfall (Yes/No)
- Displays results through an interactive web interface
- End-to-end ML pipeline from training to deployment

## Tech Stack
- Python
- Scikit-learn
- FastAPI
- Streamlit
- Pandas
- NumPy

## How It Works
1. User enters weather parameters — temperature, humidity, wind speed and pressure
2. Inputs are passed to the FastAPI backend
3. Trained ML model processes the inputs
4. Prediction is returned — Rain or No Rain
5. Result is displayed on the Streamlit frontend

## Installation and Running Locally
```bash
git clone https://github.com/Abhisyanth-M/smart-weather-insight-app
cd smart-weather-insight-app
pip install -r requirements.txt
python -m streamlit run app.py
```

## Limitations
- Predictions are based on input parameters only — does not use live weather API data
- Model accuracy depends on the quality and size of training dataset
- Does not predict weather for specific geographic locations

## Future Improvements
- Integrate live weather API to fetch real-time data automatically
- Add location-based weather prediction
- Extend prediction to multiple weather conditions beyond rainfall
- Convert to mobile app using Flutter or React Native

## GitHub
https://github.com/Abhisyanth-M/smart-weather-insight-app
```
