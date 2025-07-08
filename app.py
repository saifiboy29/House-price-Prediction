import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('house_price_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Location name ➜ code mapping
location_mapping = {
    'Sector 107, Noida': 4,
    'Sector 50, Noida': 28,
    'Sector 120, Noida': 8,
    'Sector 73, Noida': 31,
    'Other': 0,
    'Sector 150, Noida': 16,
    'Sector 143B, Noida': 14,
    'Sector 77, Noida': 35,
    'Sector 62, Noida': 29,
    'Sector 41, Noida': 23,
    'Sector 75, Noida': 33,
    'Sector 79, Noida': 37,
    'Sector 128, Noida': 10,
    'Sector 74, Noida': 32,
    'Sector 152, Noida': 17,
    'Sector 78, Noida': 36,
    'Sector 108, Noida': 5,
    'Sector 144, Noida': 15,
    'Sector 49, Noida': 27,
    'Sector 93, Noida': 39,
    'Sector 94, Noida': 41,
    'Sector 137, Noida': 12,
    'Sector 19 Yamuna Expressway, Noida': 21,
    'Sector 105, Noida': 3,
    'Sector 44, Noida': 25,
    'Sector 76, Noida': 34,
    'Sector 121, Noida': 9,
    'Sector 45, Noida': 26,
    'Sector 43, Noida': 24,
    'Sector 17A Yamuna Expressway, Noida': 19,
    'Sector 72, Noida': 30,
    'Sector 93A, Noida': 40,
    'Sector 110, Noida': 6,
    'Sector 100, Noida': 1,
    'Sector 15A, Noida': 18,
    'Sector 37, Noida': 22,
    'Sector 82, Noida': 38,
    'Sector 134, Noida': 11,
    'Sector 104, Noida': 2,
    'Sector 143, Noida': 13,
    'Sector 18, Noida': 20,
    'Sector 119, Noida': 7
}

# UI Design
st.markdown("<h1 style='text-align: center; color: white;'>🏠 House Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Enter the details below to predict the house price:</p>", unsafe_allow_html=True)

# Inputs
area = st.number_input("Area in Sq Ft", min_value=100, step=50)
bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, max_value=10, step=1)
location_name = st.selectbox("Select Location", list(location_mapping.keys()))

# Convert location name to code
location_code = location_mapping[location_name]

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[area, bhk, location_code]])
    prediction = model.predict(input_data)
    st.success(f"🏷️ Estimated House Price: ₹ {prediction[0]:,.2f} Lakhs")
