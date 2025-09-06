import streamlit as st
import requests

API_URL = 'http://127.0.0.1:8000/predict'

st.title('Diabetes Prediction App')

st.markdown('Fill the form below')

gender_input = st.selectbox("What's your gender?", options=['Male', 'Female'])

gender = 1 if gender_input == 'Male' else 0
age = st.number_input('Age?', min_value=1, max_value=120, step=1)
Urea = st.number_input('Urea?')
Cr = st.number_input('Cr (Cretinine)')
HbA1c = st.number_input('HbA1c(Hemoglobin A1c)')
Chol = st.number_input('Chol(Total Cholesterol)') 
TG = st.number_input('TG (Triglycerides)')
HDL = st.number_input('HD (High Density Lipoprotein Cholesterol)')
LDL = st.number_input('LDL (Lowe-Density Lipoprotein Cholesterol)')
VLDL = st.number_input('VLDL (Very Low-Density Lipoprotein)')	
BMI = st.number_input('Body Mass Index')

if st.button('Predict'):
 input_data = {
  'Gender': gender,
  'AGE': age,
  'Urea': Urea,
  'Cr': Cr,
  'HbA1c': HbA1c,
  'Chol': Chol,
  'TG': TG,
  'HDL': HDL,
  'LDL': LDL,
  'VLDL': VLDL,
  'BMI': BMI
 }

 try:
  response = requests.post(API_URL, json=input_data)
  if response.status_code == 200:
   result = response.json()
   st.success(f'The patient is {result["message"]}')
  else:
   st.error(f'API error {response.status_code}')
 except requests.exceptions.ConnectionError:
  st.error('Could not connect. Please, ensure it is connected to the server')