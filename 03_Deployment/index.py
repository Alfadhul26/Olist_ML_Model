
import streamlit as st

# Define the pages
main_page = st.Page("intro.py", title="Main Page", icon="🏠")
page_2 = st.Page("final.py", title="Add Medicine", icon="💊")

# Set up navigation
pg = st.navigation([main_page, page_2])

# Run the selected page
pg.run()
