# 🩺 Breast Cancer Detection using Machine Learning

This project uses the Breast Cancer Wisconsin (Diagnostic) Dataset to build a binary classification model that predicts whether a tumor is **benign** or **malignant** based on 30 real-valued features computed from digitized images of fine needle aspirate (FNA) of a breast mass.

---

## 📊 Dataset Overview

- **Source**: [Kaggle - Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
- **Target Variable**: `diagnosis`
  - `M` = Malignant
  - `B` = Benign
- **Features**:
  - 30 numeric features like `radius_mean`, `texture_mean`, `perimeter_mean`, etc.
- **Rows**: 569
- **Missing Values**: No

---

## 🛠️ Project Structure
```bash
📁 breast-cancer-project/
│
├── breast_cancer.csv # Dataset
├── breast_cancer_model.py # Training script
├── scaler.pkl # Saved scaler
├── breast_cancer_model.pkl # Trained model
├── streamlit_app.py # Streamlit frontend
├── requirements.txt # Dependencies
└── README.md # Project documentation
```


---

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/breast-cancer-predictor.git
cd breast-cancer-predictor
```
### 2.  Install dependencies
pip install -r requirements.txt
### 3.  Train the model (optional, if not using existing .pkl files)
python breast_cancer_model.py

### 4.  Run the Streamlit app
streamlit run streamlit_app.py


###LIVE LINK->https://breast-cancer-prediction01.streamlit.app/
