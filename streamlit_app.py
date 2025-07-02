import streamlit as st
import requests

st.set_page_config(page_title="Boston House Price Predictor")
st.title("🏠 Boston House Price Predictor")

st.markdown("Enter the features below to get a house price prediction:")

# Input fields
features = {
    "CRIM": st.number_input("CRIM", value=0.1),
    "ZN": st.number_input("ZN", value=12.5),
    "INDUS": st.number_input("INDUS", value=7.5),
    "CHAS": st.selectbox("CHAS", [0, 1]),
    "NOX": st.number_input("NOX", value=0.5),
    "RM": st.number_input("RM", value=6.2),
    "AGE": st.number_input("AGE", value=45.0),
    "DIS": st.number_input("DIS", value=4.5),
    "RAD": st.number_input("RAD", value=5),
    "TAX": st.number_input("TAX", value=300),
    "PTRATIO": st.number_input("PTRATIO", value=16.0),
    "B": st.number_input("B", value=395.0),
    "LSTAT": st.number_input("LSTAT", value=9.0)
}

# Replace with your actual deployed FastAPI URL
API_URL = "https://boston-price-api.onrender.com/predict"


if st.button("Predict"):
    try:
        with st.spinner("Predicting..."):
            response = requests.post(API_URL, json=features)
            result = response.json()
            price = result["predicted_price"]
            st.success(f"💰 Predicted House Price: **${price * 1000:,.2f}**")
    except Exception as e:
        st.error(f"❌ Error: {e}")
