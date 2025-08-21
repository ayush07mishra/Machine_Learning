# Weather-Related Disease Prediction

## Overview

This project aims to predict the likelihood of disease outbreaks based on weather data and medical symptoms. The model uses machine learning, specifically a Random Forest Classifier, to predict the prognosis of various diseases based on features such as temperature, humidity, wind speed, and patient symptoms. The project is designed for healthcare research, and it allows users to input real-time data through an interactive interface to predict potential health issues.

---

## Features

- **User Input Interface**: The model accepts user input for weather data (temperature, humidity, wind speed) and patient symptoms (e.g., fever, cough, nausea).
- **Machine Learning Model**: The backend uses a trained Random Forest Classifier to predict the prognosis based on input data.
- **Interactive Widgets**: The application uses `ipywidgets` to create an interactive experience, allowing users to input values easily.

---

## Dataset

The dataset used for this project is a combination of **weather data** and **medical symptoms**:

- **Weather Data**: Temperature (°C), Humidity (%), Wind Speed (km/h).
- **Medical Symptoms**: Nausea, joint pain, abdominal pain, fever, chills, fatigue, etc.
- **Pre-existing Conditions**: Asthma, diabetes, high blood pressure, etc.

The dataset is preprocessed by removing any missing values and encoding categorical variables. It has been used to train a **Random Forest Classifier** to predict the possible diagnosis (prognosis).

---

## Installation and Setup

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/weather-disease-prediction.git
cd weather-disease-prediction
