# 🏭 Air Quality Index (AQI) Prediction using Machine Learning

This project aims to predict the **Air Quality Index (AQI)** using historical air pollutant data collected from the **Bawana Air Pollution Monitoring Plant**. The dataset includes various pollutant concentrations, date-based features, holidays, and weekday indicators — making it ideal for time-series forecasting and pollution pattern analysis.

---

## 📊 Dataset Overview

The dataset contains daily pollutant readings and AQI values, with the following features:

### ➤ Pollutant Parameters:
- **PM2.5**, **PM10**, **NO₂**, **SO₂**, **Ozone** — *(µg/m³)*
- **CO** — *(mg/m³)*

### ➤ Temporal Features:
- **Day**, **Month**, **Year**
- **Day of the Week** (Monday to Sunday)
- **Holiday** Indicator  
  - `1` = Holiday  
  - `0` = Working Day

> ⚠️ *Missing values were estimated using previous trends and mathematical approximations.*

---

## 🚀 Project Objectives

- Predict daily **AQI values**
- Analyze the impact of holidays and weekdays on air quality
- Visualize pollution trends over time
- Improve accuracy using temporal + pollutant data

---

## 📌 Model Features

- 📈 Supervised ML models: Linear Regression, Random Forest, etc.
- 📅 Feature engineering for temporal variables
- 📊 Data visualization using Matplotlib & Seaborn
- ✅ Trained and evaluated with performance metrics (e.g., MAE, RMSE)

---

## 🧪 Technologies Used

- Python (Pandas, NumPy)
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook

---

---

## 📈 Sample Visualizations

- Time series trend of AQI
- Correlation heatmaps
- AQI distributions by weekday and holiday

---

## 🏁 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/aqi-prediction.git
   cd aqi-prediction

Create virtual environment
python3 -m venv env
source env/bin/activate

Install dependencies
pip install -r requirements.txt

Open Jupyter Notebook
jupyter notebook





#LIVE LINK-> https://ayushmishraaqi.streamlit.app/
