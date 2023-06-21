
import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="I-OPTIC PROJECT", layout="wide")#centered
st.markdown(
     """
     <style>
     #MainMenu {visibility: hidden;}
     footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center'>Model Information</h2>", unsafe_allow_html=True)

col1,col2=st.columns([1,5])
with col1:
    model=st.radio('Select Model:',['Model 1','Model 2'])

if model == 'Model 1':
    perf_file = 'performance.csv'
    model_inf_file = 'model_info.csv'
    feat_impt_file = 'feat_imp.png'
else:
    perf_file = 'performance_1.csv'
    model_inf_file = 'model_info_1.csv'
    feat_impt_file = 'feat_imp_1.png'

with col2:
    
    df = pd.read_csv(perf_file)
    df_model = pd.read_csv(model_inf_file)


    st.markdown("**Model Information:**")
    st.dataframe(df_model)


    st.markdown('**Model Performance:**')
    st.dataframe(df)

    image = Image.open(f'{feat_impt_file}')
    st.markdown("**Feature importance**:")
    st.image(image)
