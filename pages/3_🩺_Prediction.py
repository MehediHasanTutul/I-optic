import streamlit as st
import pandas as pd
import pickle

import matplotlib.pyplot as plt


st.set_page_config(page_title="I-OPTIC PROJECT", layout="wide")#centered
st.markdown(
     """
     <style>
     #MainMenu {visibility: hidden;}
     footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center'>Patient Status Prediction</h2>", unsafe_allow_html=True)


# st.markdown('''<style>
# div.css-1r6slb0.e1tzin5v2 {
#     background-color: #EEEEEE;
#     border: 1px solid #CCCCCC;
#     padding: 1% 1% 1% 1%;
#     border-radius: 5px;
#     width: 169px;
# }
# div.row-widget.stRadio {
#     background-color: #EEEEEE;
#     border: 1px solid #CCCCCC;
#     padding: 1% 1% 1% 1%;
#     border-radius: 5px;
#     width: 169px;
# }
# div.stSlider {
#     background-color: #EEEEEE;
#     border: 1px solid #CCCCCC;
#     padding: 1% 1% 1% 1%;
#     border-radius: 5px;
#     width: 169px;
# }
# </style>''', unsafe_allow_html=True)

inputs = []
col31, col32 = st.columns(2)
st.markdown('Set inputs:')
col1, col2,col3,col4 = st.columns(4)

col5, col6, col7,col8 = st.columns(4)
col9, col10, col11,col12 = st.columns([2,1,1,1])
# with col1:
with col31:
        
    model = st.radio(
        'Select model:',
        ["Model 1", "Model 2"],
        horizontal=True,
    )

with col1: 
    inputs.append(st.slider("Age 🧍‍♀️", min_value=1, max_value=100, value=50, step=1)/94)
    
    
with col2:
    inputs.append(st.radio(
        "Gender 🧍‍♀️",
        ["Female", "Male" ],
        
        horizontal=True,
    ))
    
with col3:
    inputs.append(st.radio(
        "Reduced food intake 🥪",
        ["Yes", "No" ],
        
        horizontal=True,
    ))
    
with col4:
    inputs.append(st.radio(
        "Inflamation 🧍‍♀️",
        ["Yes", "No" ],
       
        horizontal=True,
    ))
    
with col5:
    inputs.append(st.radio(
        "Unintetional weight loss 🧍‍♀️",
        ["Yes", "No" ],
        
        horizontal=True,
    ))
with col6:
    inputs.append(st.radio(
        "Low BMI 🕴️",
        ["Yes", "No" ],
        
        horizontal=True,
    ))
with col7:
    inputs.append(st.radio(
        "Reduced muscle mass 🧍‍♀️",
        ["Yes", "No" ],
        
        horizontal=True,
    ))
with col8:
    inputs.append(st.radio(
        "Malnutrition 🧍‍♀️",
        ["Yes", "No" ],
        
        horizontal=True,
    ))
with col9:
    inputs.append(st.selectbox('Primary Malignancy:',['Breast', 'Bone and soft tissue','Central Nervous System','Colorectal',
    'Endocrine and thyroid','Genitourinary','Haematological','Head and neck','Lung',
    'Skin and melanoma','Upper GI','Other thoracic or abdominal',
    'CUP','Gynaecological','Unknown']))

df = pd.DataFrame(inputs).T
df.columns = ['Age','Gender','Food intake','Inflammation','Weight loss','BMI','Muscle mass','Malnutrition','Malignancy']
df = df.replace(["Female", "Male","Yes","No",'Breast', 'Bone and soft tissue','Central Nervous System','Colorectal',
'Endocrine and thyroid','Genitourinary','Haematological','Head and neck','Lung',
'Skin and melanoma','Upper GI','Other thoracic or abdominal',
'CUP','Gynaecological','Unknown'],[1,0,1,0,1/14,2/14,3/14,4/14,5/14,6/14,7/14,8/14,9/14,10/14,11/14,12/14,13/14,14/14,1])

if model=='Model 1':
    filename = f'Ioptic_model.sav'
else:
    filename = f'Ioptic_model_1.sav'

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
# pred = loaded_model.predict(df.values)
pred = loaded_model.predict_proba(df.values)
st.markdown("============================")
if pred.argmax()==0:
    st.error(f"Predicted status after 1 year : **Deceased** (with {float(pred.max()*100):.2f}% probability)")
else:
    st.success(f"Predicted status after 1 year : **Alive** (with {float(pred.max()*100):.2f}% probability)")



# import shap
# @st.cache
# def create_explainer(loaded_model):
#     explainer = shap.TreeExplainer(loaded_model) 
#     return explainer

# def show_shap(df):
#     explainer = create_explainer(loaded_model)
#     shap_values = explainer(df)

#     shap.initjs()

#     fig, ax = plt.subplots()
#     shap.plots.waterfall(shap_values[0][:,1])
#     st.pyplot(fig)
# with st.expander("See feature importance"):
    
#     show_shap(df)
