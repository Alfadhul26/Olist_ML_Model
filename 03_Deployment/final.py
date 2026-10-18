
import streamlit as st
import joblib
import sys
from pathlib import Path
from model import predict_delivery

st.title("Olist")
st.header("Predict Delivery Time")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #57488a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

bundle = joblib.load("03_Deployment/delivery_model.pkl")

# Select product category and customer state
category = st.selectbox(
    "Product Category",
    bundle["typical"]["product"].index.tolist()
)

state = st.selectbox(
    "Customer State",
    bundle["typical"]["state"].index.tolist()
)

# Make prediction
if st.button("Predict Delivery Days"):
    result = predict_delivery(category, state, bundle)

    st.success(
        f"Estimated delivery time: {result['days']} days"
    )

    st.write(
        f"Estimated delivery date: {result['date']}"
    )

    st.caption(
        f"Typical prediction error: approximately "
        f"±{result['typical_error_days']} days."
    )
