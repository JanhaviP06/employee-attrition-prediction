import streamlit as st
import home
import dashboard
import prediction
import analysis
from streamlit_navigation_bar import st_navbar

# Set page configuration
st.set_page_config(page_title="Employee Attrition Prediction",
        page_icon="📊")

# Define the pages for navigation
page_names = ["Employee Attrition Prediction","Home", "Analysis","Dashboard", "Prediction"]

# Define styles for the navbar, ensuring text color is white
styles = {
    "nav": {
        "background-color": "#5a1e82",  # Dark purple background
        "justify-content": "middle",    # Align navigation items to the center
    },
    "span": {  # This affects the text inside the navigation items
        "color": "#ffffff",  # White text by default
        "padding": "14px",
    },
    "active": {
        "background-color": "#5a1e82",  # Keep active item background the same
        "color": "#ffffff",  # White text for active items
        "font-weight": "bold",  # Bold text for active page
        "padding": "14px",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",  # Background color on hover
    },
}

# Create the navbar (pass the list of page names)
selected_page = st_navbar(page_names, styles=styles)

# Define a dictionary to map page names to their respective functions
pages = {
    "Employee Attrition Prediction": home.show_home,
    "Home": home.show_home,
    "Analysis": analysis.show_analysis,
    "Dashboard": dashboard.show_dashboard,
    "Prediction": prediction.show_prediction
}

# Call the function corresponding to the selected page
if selected_page in pages:
    pages[selected_page]()
