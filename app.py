# app.py

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model and feature columns
model = joblib.load("house_price_model.pkl")
model_features = joblib.load("model_features.pkl")

st.title("🏠 House Price Prediction App")

# Sidebar inputs
st.sidebar.header("Enter House Details")

def user_input():
    GrLivArea = st.sidebar.slider("Above Ground Living Area (sq ft)", 500, 4000, 1500)
    BedroomAbvGr = st.sidebar.slider("Bedrooms Above Ground", 0, 10, 3)
    GarageCars = st.sidebar.slider("Garage Cars", 0, 4, 2)
    TotalBsmtSF = st.sidebar.slider("Basement Area (sq ft)", 0, 3000, 1000)
    YearBuilt = st.sidebar.slider("Year Built", 1900, 2022, 2000)

    # Minimal input
    data = {
        'GrLivArea': GrLivArea,
        'BedroomAbvGr': BedroomAbvGr,
        'GarageCars': GarageCars,
        'TotalBsmtSF': TotalBsmtSF,
        'YearBuilt': YearBuilt
    }

    return pd.DataFrame([data])

# Get user input
input_df = user_input()

# Create a full input with all model features
full_input = pd.DataFrame(columns=model_features)
for col in model_features:
    full_input[col] = 0  # default all values to 0

# Overwrite only the columns the user filled
for col in input_df.columns:
    if col in full_input.columns:
        full_input[col] = input_df[col].values

# Predict
prediction = model.predict(full_input)[0]
st.subheader("Predicted Selling Price")
st.write(f"${prediction:,.2f}")
