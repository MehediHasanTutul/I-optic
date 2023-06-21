import streamlit as st

import pandas as pd
import numpy as np


st.set_page_config(page_title="I-OPTIC PROJECT", layout="wide")#centered

st.markdown(
     """
     <style>
     #MainMenu {visibility: hidden;}
     footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center'>Dataset Information</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1,5])

with col1:
    with st.container():
            
        selected = st.radio(
            'Select datset:',
            ["Victoria", "UK Biobank" ,"Prime",'Colon','Silvia','Mater'],
            horizontal=False,
        )
        
with col2:
    if selected=="Victoria":
        html_file = 'VIC.html'
    elif selected=="UK Biobank":
        html_file = 'UKB.html'
    elif selected=="Prime":
        html_file = 'PRM.html'
    elif selected=='Colon':
        html_file = 'CLN.html'
    elif selected=='Silvia':
        html_file = 'SIL.html'
    elif selected=='Mater':
        html_file = 'MAT.html'

    # Read the HTML file
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Render HTML in the first column
    st.components.v1.html(html_content, width=800, height=600, scrolling=True)

