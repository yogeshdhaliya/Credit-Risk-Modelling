# 1 Good (Lower Risk) 0 Bad (Higher Risk)

import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load('extra_trees_credit_model.pkl')
encoders = {
    "Sex": joblib.load("Sex_encoder.pkl"),
    "Housing": joblib.load("Housing_encoder.pkl"),
    "Saving accounts": joblib.load("Saving accounts_encoder.pkl"),
    "Checking account": joblib.load("Checking account_encoder.pkl")
}

st.title("Credit Risk Prediction App")
st.write("Enter the details below to predict credit risk (1: Good, 0: Bad)")

# Inputs
age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", ["male","female"])
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ["own","rent","free"])
saving_accounts = st.selectbox("Saving Accounts", encoders["Saving accounts"].classes_)
checking_accounts = st.selectbox("Checking Accounts", encoders["Checking account"].classes_)
credit_amount = st.number_input("Credit Amount", min_value=100, value=1000)
duration = st.number_input("Duration (months)", min_value=1, value=12)

# Prepare input data
input_data = pd.DataFrame({
    "Age": [age],
    "Sex": [encoders["Sex"].transform([sex])[0]],
    "Job": [job],
    "Housing": [encoders["Housing"].transform([housing])[0]],
    "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
    "Checking account": [encoders["Checking account"].transform([checking_accounts])[0]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("The predicted credit risk is: **GOOD**")
    else:
        st.error("The predicted credit risk is: **BAD**")
