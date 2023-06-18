import streamlit as st

# Define the options
options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

# Create the toggle buttons
selected_options = st.multiselect('Select Options', options)

# Display the selected options
st.write('Selected Options:', selected_options)
