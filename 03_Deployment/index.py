
import streamlit as st

# Define the pages
main = st.Page("intro.py", title="Main Page", icon="🏠")
page_2 = st.Page("final.py", title="Prediction Model", icon="📊")

# Set up navigation
pg = st.navigation([main, page_2])

# Run the selected page
pg.run()
