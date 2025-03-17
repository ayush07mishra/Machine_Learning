import streamlit as st
import joblib
import numpy as np

# Load trained model and scaler
@st.cache_resource
def load_model():
    return joblib.load("titanic_model.pkl")

@st.cache_resource
def load_scaler():
    return joblib.load("scaler.pkl")  # Load the saved scaler

model = load_model()
scaler = load_scaler()

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details to predict survival")

# Input fields for all features
pclass = st.selectbox("Passenger Class", [1, 2, 3])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
fare = st.number_input("Fare", min_value=0.0, value=50.0)
gender = st.radio("Gender", ("Male", "Female"))
sibsp = st.number_input("Number of Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of Parents/Children Aboard", min_value=0, max_value=10, value=0)
embarked = st.selectbox("Embarked Port", ["C", "Q", "S"])

# Convert categorical values to numerical (same encoding as training)
gender = 1 if gender == "Male" else 0
embarked_mapping = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_mapping[embarked]

# Apply same scaling as during training
input_data = np.array([[pclass, age, fare, gender, sibsp, parch, embarked]])
input_data[:, [1, 2]] = scaler.transform(input_data[:, [1, 2]])  # Scale Age and Fare

# Predict button
if st.button("Predict Survival"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ Survived")
    else:
        st.error("❌ Not Survived")
