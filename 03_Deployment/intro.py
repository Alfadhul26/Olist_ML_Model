import streamlit as st
import pandas as pd

# Main page title
st.title("Olist Delivery Time Prediction")
st.sidebar.title("Main Page")

# Display Olist image
st.image(
    "https://storage.googleapis.com/kaggle-organizations/1942/thumbnail.png?r=51",
    width=300
)

# Introduction
st.header("Introduction")

st.write(
    "Aim - Predict how many days an order will take to arrive, "
    "using only what is known when the customer chooses a product. "
    "Built on the public Olist Brazilian e-commerce dataset "
    "(96,470 delivered orders, 2016–2018)."
)

# Methods
st.header("Methods")

st.write(
    "Data: Orders, items, products, sellers, customers and payments "
    "joined into one row per order."
)

st.write(
    "Missing values: Filled with the median for numerical features "
    "or the most common value for categorical features; no orders are dropped."
)

st.write(
    "Split: 64% training, 16% validation and 20% testing, "
    "using random_state=42."
)

st.write(
    "Metric: Mean Absolute Error (MAE), the average number of days "
    "the prediction differs from the actual delivery time."
)

st.write(
    "Deployment: The customer selects a product category and a state. "
    "Other inputs are filled with typical values for that category and state."
)

# Load dataset
data = pd.read_csv("01_Data/olist_delivery_model_dataset.csv")

# Data tab
tab1 = st.tabs(["Data"])[0]

with tab1:
    st.subheader("Dataset Preview")
    st.write("Here is the dataset used for the delivery time prediction model.")
    st.dataframe(data, use_container_width=True)
```

with st.spinner("Loading Tab 1..."):
    time.sleep(2)
with tab1:
    st.dataframe(data)



