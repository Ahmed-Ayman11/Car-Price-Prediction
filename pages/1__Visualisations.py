import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Visualisations",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown('''
<div style="background-color: #114232; border-radius: 20px;">
    <h1 style="text-align: center; color:#FCDC2A">Car Auction Insights 📊</h1>
</div>
''', unsafe_allow_html=True)
st.divider()

df_eda = pd.read_csv("car_prices_cleaned.csv")

top_10 = df_eda.groupby('brand')['vin'].count().reset_index().sort_values(by = 'vin' , ascending=False).head(10)
fig =px.bar(top_10 , x = 'brand' , y = 'vin', labels={'name':'Brand' , 'vin':'Number of cars'} , color = 'brand' , title = 'Number of top 10 cars each brand', template = 'plotly_dark' , text_auto = True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
    <h3 style="text-align: justify; color:#FCDC2A; -webkit-text-stroke: 0.4px black;">Ford is the leading brand in this chart, with the highest number of cars at around 91.908k. This indicates that Ford has a significant market presence, potentially due to a strong product lineup, brand loyalty, or effective marketing strategies.</h3>
''', unsafe_allow_html=True)
st.divider()

months = df_eda.groupby('sellMonth')['vin'].count().reset_index()
fig =px.bar(months , x = 'sellMonth' , y = 'vin', labels={'sellMonths':'Months' , 'vin':'Number of cars'} , color = 'sellMonth' , title = 'Number of sold cars each Months', template = 'plotly_dark', text_auto = True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
    <h3 style="text-align: justify; color:#FCDC2A; -webkit-text-stroke: 0.4px black;">The highest number of cars sold occurred in February. This months had the tallest bar in the chart, indicating that they were the peak sales months.</h3>
''', unsafe_allow_html=True)
st.divider()

average_price = df_eda.groupby('brand')['sellingprice'].mean().reset_index()
model_counts = df_eda['brand'].value_counts().reset_index()
model_counts.columns = ['brand', 'count']
merged_data = pd.merge(average_price, model_counts, on='brand')
top_10_models = merged_data.sort_values('count', ascending=False).head(10)
fig = px.bar(top_10_models, x='brand', y='sellingprice', title='Average Selling Price of Top 10 Selling Cars', labels={'sellingprice': 'Average Selling Price', 'brand': 'Car Model'}, template='plotly_dark', color='brand')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
    <h3 style="text-align: justify; color:#FCDC2A; -webkit-text-stroke: 0.4px black;">BMW has the highest average selling price. This suggests that BMW models are generally more expensive than the other brands listed.</h3>
''', unsafe_allow_html=True)
st.divider()

state_brand_counts = df_eda.groupby(['state', 'brand']).size().reset_index(name='count')
most_selling_brands = state_brand_counts.loc[state_brand_counts.groupby('state')['count'].idxmax()]
fig = px.bar(most_selling_brands, x='state', y='count', color='brand', title='Most Selling Car Brand in Each State', labels={'count': 'Number of Cars Sold', 'state': 'State'}, text='brand', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
    <h3 style="text-align: justify; color:#FCDC2A; -webkit-text-stroke: 0.4px black;">Ford is the most selling car brand in most states. This suggests that Ford has a strong market presence across the country.</h3>
''', unsafe_allow_html=True)
st.divider()

fig = px.scatter(df_eda, x='milage', y='sellingprice', title='Correlation between Mileage and Selling Price', labels={'milage': 'Mileage (KM)', 'sellingprice': 'Selling Price (USD)'}, template='plotly_dark', color='condition')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
    <h3 style="text-align: justify; color:#FCDC2A; -webkit-text-stroke: 0.4px black;">A car's selling price goes up with less miles driven, and it is more likely to find a well-kept vehicle.</h3>
''', unsafe_allow_html=True)
st.divider()

body_counts = df_eda['body'].value_counts().reset_index()
body_counts.columns = ['body', 'count']
top_10_bodies = body_counts.head(10)
fig = px.bar(top_10_bodies, x='body', y='count', title='Top 10 Selling Car Body Types', labels={'body': 'Car Body Type', 'count': 'Number of Cars Sold'}, color='body', template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
    <h3 style="text-align: justify; color:#FCDC2A; -webkit-text-stroke: 0.4px black;">Sedans are the most popular car body type. This suggests that sedans are still the preferred choice for many car buyers.</h3>
''', unsafe_allow_html=True)
st.divider()


df_eda['year_cat'] = pd.cut(df_eda['manifacture_year'], bins=[1990, 1996, 2001, 2006,2011,2016], labels=['1990 - 1995', '1996 - 2000', '2001 - 2005', '2006 - 2010', '2011 - 2015'])
years_cat = df_eda.groupby(['year_cat'])['vin'].count().reset_index().sort_values(by = 'year_cat' , ascending = False)
fig = px.line(years_cat,x='year_cat', y='vin', labels={'vin':'Number of cars', 'year_cat':'Manifacture Years'},template = 'plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
    <h3 style="text-align: justify; color:#FCDC2A; -webkit-text-stroke: 0.4px black;">We can notice that newer cars are sold more than older cars.</h3>
''', unsafe_allow_html=True)
st.divider()

fig = px.scatter(df_eda,x='body', y='sellingprice', title='Selling Price vs. Car Body Type', labels={'body': 'Car Body Type', 'sellingprice': 'Selling Price (USD)'}, category_orders={'body': df_eda['body'].unique()}, template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)
st.markdown('''
    <h3 style="text-align: justify; color:#FCDC2A; -webkit-text-stroke: 0.4px black;">The blind man can clearly see that the most valuable car types are SUVs, sedans, convertibles, and coupes.</h3>
''', unsafe_allow_html=True)
st.divider()