import streamlit as st
import time
import pandas as pd
import numpy as np

# Main page content
st.markdown("# Olist Delivery Time Prediction")
st.sidebar.markdown("# Main page")
<img width="300" height="350" alt="image" src="https://storage.googleapis.com/kaggle-organizations/1942/thumbnail.png?r=51" />

#st.image(https://storage.googleapis.com/kaggle-organizations/1942/thumbnail.png?r=51)
#main points of the application
header = st.container()
header.write("Aim - Predict how many days an order will take to arrive, using only what is known when the customer chooses a product. Built on the public Olist Brazilian e-commerce dataset (96,470 delivered orders, 2016–2018)")

st.header("Methods - ")

#features of the application

st.write("Data: orders, items, products, sellers, customers and payments joined into one row per order.")
st.write("Missing values: filled with the median (numbers) or most common value (categories); no orders are dropped.")
st.write("Split: 64% train, 16% validation, 20% test, random_state=42.")
st.write("Metric: Mean Absolute Error (MAE), the average number of days the prediction is off.")
st.write("Deployment: the customer enters a category and a state; other inputs are filled with typical values for that category and state.")

#with st.expander("Show details"):
    #st.write("Here are the details...")
#st.image( )
data = pd.read_csv("01_Data/olist_delivery_model_dataset.csv")

#added animation to process the data smoothly

tab1= st.tabs(["Data"])[0]

with st.spinner("Loading Tab 1..."):
    time.sleep(2)
with tab1:
    st.dataframe(data)
