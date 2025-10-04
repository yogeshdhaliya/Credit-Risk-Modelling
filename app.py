import streamlit as st
import pandas as pd
import joblib

# Set page configuration for better layout
st.set_page_config(layout="wide")

# ---
# 1. Load Model and Encoders (Error Handling Added for Robustness)
# ---

# NOTE: This code assumes the .pkl files exist in the same directory.
try:
    model = joblib.load('extra_trees_credit_model.pkl')
    encoders = {
        "Sex": joblib.load("Sex_encoder.pkl"),
        "Housing": joblib.load("Housing_encoder.pkl"),
        "Saving accounts": joblib.load("Saving accounts_encoder.pkl"),
        "Checking account": joblib.load("Checking account_encoder.pkl")
    }
except FileNotFoundError as e:
    st.error(f"Error loading required file: {e}. Please ensure all .pkl files are in the directory.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred during file loading: {e}")
    st.stop()

st.title("Credit Risk Prediction App 🏦")
st.write("Enter the details below to predict credit risk (**1**: Good/Lower Risk, **0**: Bad/Higher Risk)")

# ---
# 2. User Inputs (Organized with columns for clean UI)
# ---

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=18, max_value=80, value=30)
    sex = st.selectbox("Sex", ["male", "female"])
    job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1, help="0: unskilled - non-resident, 1: unskilled - resident, 2: skilled, 3: highly skilled")

with col2:
    housing = st.selectbox("Housing", ["own", "rent", "free"])
    saving_accounts = st.selectbox("Saving Accounts", encoders["Saving accounts"].classes_)
    checking_accounts = st.selectbox("Checking Accounts", encoders["Checking account"].classes_)

with col3:
    credit_amount = st.number_input("Credit Amount", min_value=100, value=1000)
    duration = st.number_input("Duration (months)", min_value=1, value=12)

st.divider()

# ---
# 3. Data Preparation & Display (ALWAYS VISIBLE)
# ---

# Prepare input data with encoded values
# This block runs every time an input changes, updating the dataframe below.
input_data_encoded = pd.DataFrame({
    "Age": [age],
    "Sex": [encoders["Sex"].transform([sex])[0]],
    "Job": [job],
    "Housing": [encoders["Housing"].transform([housing])[0]],
    "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
    "Checking account": [encoders["Checking account"].transform([checking_accounts])[0]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

st.subheader("Input Data for Model (Encoded Values)")
st.dataframe(input_data_encoded, use_container_width=True) # Display the DataFrame here!

st.divider()

# ---
# 4. Prediction Logic (Triggered by button)
# ---

if st.button("Predict Credit Risk"):
    
    # Use the already prepared and encoded data for prediction
    prediction = model.predict(input_data_encoded)[0]
    
    st.subheader("Prediction Result")
    
    if prediction == 1:
        st.success("The predicted credit risk is: **GOOD** (Lower Risk) ✅")
    else:
        st.error("The predicted credit risk is: **BAD** (Higher Risk) 🚨")