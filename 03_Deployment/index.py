
import streamlit as st

# Define the pages
main_page = st.Page("03_Deployment/intro.py", title="Main Page", icon="🏠")
page_2 = st.Page("03_Deployment/final.py", title="Prediction Model", icon="📊")

# Set up navigation
pg = st.navigation([main_page, page_2])

# Run the selected page
pg.run()
