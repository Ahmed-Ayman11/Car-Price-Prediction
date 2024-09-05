import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Home",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown('''
<div style="background-color: #114232; border-radius: 20px;">
    <h2 style="text-align: center; color:#FCDC2A">Welcome to Car Price Prediction Based on US Used Car Auction 🚗</h2>
</div>
<br>
<br>
''', unsafe_allow_html=True)
st.image("wuJhPcWTS1qpWMsgX2nJeQ.webp")

df = pd.read_csv("car_prices_cleaned.csv")
st.divider()

st.markdown('''
        <div style="background-color: #114232; border-radius: 20px; -webkit-text-stroke: 0.01px black">
            <h1 style="color: #FCDC2A; font-size: 30px; text-align: center">Car Sales Data Overview</h1>
        </div>
        <div style=" -webkit-text-stroke: .4px black">
            <p style="color: #f0f0f0; font-size: 20px; text-align: justify">This dataset provides comprehensive information about car sales, capturing various aspects that can help us analyze trends, correlations, and patterns in the automotive market. By exploring this data, we aim to understand the factors influencing car sales and identify key metrics that drive performance.</p>
        </div>
        <br>
        <br>
        <div style="background-color: #114232; border-radius: 20px; ">
            <h1 style="color: #FCDC2A; font-size: 30px; text-align: center">Column Descriptions</h1>
        </div>
        <div style="font-size: 20px;  -webkit-text-stroke: 0.4px black">
            <div>
                <span style="color: #FCDC2A;">Manufacture Year:</span>
                <span style="color: #f0f0f0;">  The year when the vehicle was manufactured, indicating the model year of the car.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Brand:</span>
                <span style="color: #f0f0f0;">  The brand or make of the car, such as Kia, BMW, or Volvo.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Model:</span>
                <span style="color: #f0f0f0;"> The specific model of the car within the brand's lineup, like Sorento, 3 Series, or S60.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Trim:</span>
                <span style="color: #f0f0f0;">The trim level of the car, which refers to the specific version or configuration of a car model, often indicating different levels of features or equipment.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Body:</span>
                <span style="color: #f0f0f0;">The body type of the car, such as SUV or Sedan, describing the general shape and design of the vehicle.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Transmission:</span>
                <span style="color: #f0f0f0;"> The type of transmission system in the car, specifying whether it is automatic or manual.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">state:</span>
                <span style="color: #f0f0f0;">The state abbreviation where the car was sold, providing geographic context to the sale (e.g., CA for California).</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Condition:</span>
                <span style="color: #f0f0f0;">A numerical rating of the car's condition, typically on a scale where higher numbers indicate better condition.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Millage:</span>
                <span style="color: #f0f0f0;">The total distance the car has traveled, measured in miles, which can indicate how much the car has been used.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Color:</span>
                <span style="color: #f0f0f0;">The exterior color of the car, such as white, gray, or black.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Interior:</span>
                <span style="color: #f0f0f0;">The color of the car's interior, often influencing the aesthetic appeal and comfort of the vehicle.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Seller:</span>
                <span style="color: #f0f0f0;">The entity or organization selling the car, which could be a dealership or a leasing company.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Sell Year:</span>
                <span style="color: #f0f0f0;">The year in which the car was sold, useful for analyzing sales trends over time.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Sell Months:</span>
                <span style="color: #f0f0f0;">The month in which the car was sold, providing more granular insights into seasonal sales patterns.</span>
            </div>
            <div>
                <span style="color: #FCDC2A;">Selling Price:</span>
                <span style="color: #f0f0f0;">The final price at which the car was sold, reflecting market demand and vehicle value.</span>
            </div>
        </div>
        <br>
        <br>
        <div style="background-color: #114232; border-radius: 20px;">
            <h1 style="color: #FCDC2A; font-size: 30px; text-align: center">Sample Dataset</h1>
        </div>
        <br>
        
        
            ''', unsafe_allow_html=True)


if st.checkbox('Show Sample From Dataset'):
    st.dataframe(df.head(10))

st.divider()


st.markdown('''
        <div style=" -webkit-text-stroke: .4px black">
            <span style="color:#FCDC2A; font-size:25px">Data Source:</span>
            <span><a style="color:#3795BD; text-decoration:none; font-size:30px" href="https://www.kaggle.com/datasets/tunguz/used-car-auction-prices/data">kaggle</a></span>
        </div>
            ''', unsafe_allow_html=True)
