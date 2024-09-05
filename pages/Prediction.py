import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
import time

st.set_page_config(
    page_title="Prediction",
    page_icon="🤔",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown('''
<div style="background-color: #114232; border-radius: 20px;">
    <h1 style="text-align: center; color:#FCDC2A">Predict Your Car Price 🤔</h1>
</div>
''', unsafe_allow_html=True)
st.divider()

df_eda = pd.read_csv("car_prices_cleaned.csv")

brand = st.selectbox("Select the brand of the car", df_eda['brand'].unique())
filtered_brand = df_eda[df_eda['brand'] == brand]
car_model = st.selectbox("Select the model of the car",filtered_brand['model'].unique())
filtered_model = df_eda[df_eda['model'] == car_model]
trim = st.selectbox("Select the trim of the car", filtered_model['trim'].unique())
filtered_trim = df_eda[df_eda['trim'] == trim]
body = st.selectbox("Select the body of the car", filtered_trim['body'].unique())
year = st.selectbox("Enter the year of manufacture",sorted(filtered_trim['manifacture_year'].unique()))
condition = st.number_input("Select the condition of the car", min_value=0.0, max_value=5.0)
milage = st.number_input("Enter the milage of the car", min_value=0.0, max_value=1000000.0)


try:
    with open('pipeline_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

columns = ['manifacture_year', 'condition', 'milage', 'brand', 'model', 'trim', 'body']
data = pd.DataFrame([[year, condition, milage, brand, car_model, trim, body]],columns=columns)

final_prediction = model.predict(data)

st.divider()

if st.button('Predict', help="Click here to predict price"):
    time.sleep(3)
    st.success(f'Predicted Price : {final_prediction[0].round(2)} USD')
