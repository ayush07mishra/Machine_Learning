# app.py

import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open('breast_cancer_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("🧬 Breast Cancer Prediction App")

st.markdown("""
Predict whether a tumor is benign or malignant based on cell nuclei features.
""")

# Feature inputs
feature_names = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

input_data = []
for feature in feature_names:
    value = st.number_input(f"{feature}", step=0.1)
    input_data.append(value)

if st.button("Predict"):
    input_array = np.array(input_data).reshape(1, -1)
    scaled_input = scaler.transform(input_array)
    prediction = model.predict(scaled_input)

    if prediction[0] == 1:
        st.error("The tumor is Malignant (Cancerous).")
    else:
        st.success("The tumor is Benign (Non-Cancerous).")
