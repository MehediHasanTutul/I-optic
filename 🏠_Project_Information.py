import streamlit as st

# im = Image.open('icon.jpg')
st.set_page_config(
    page_title="I-OPTIC PROJECT",
    # page_icon=im,
    layout="wide",
)
st.markdown(
     """
     <style>
     #MainMenu {visibility: hidden;}
     footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True)
title = "I-OPTIC: Intelligent Outcome Prediction Tool In Cancer-related malnutrition"
st.markdown(f"<h2 style='text-align: center'>{title}</h2>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: left'>What is i-OPTIC?</h4>", unsafe_allow_html=True)
st.markdown('i-OPTIC is an intelligent online platform enabling real time prediction of the risk of mortality for an individual related to cancer-related malnutrition. The i-OPTIC platform is underpinned by machine learning models that include data from five countries (Australia, United Kingdom, the Netherlands, Brazil, and Canada) and seven databases, representing 5,918 participants with various cancer diagnoses. Further information about the included databases is available in the ‘Dataset Information’ tab.')
st.markdown(f"<h4 style='text-align: left'>How can i-OPTIC support your clinical decision making?</h4>", unsafe_allow_html=True)
st.markdown('Malnutrition occurs in approximately 30% of people with cancer, with prevalence varying depending on factors such as cancer diagnosis, disease stage and treatment type. Malnutrition is associated with poorer quality of life, reduced ability to complete cancer treatment and increased risk of mortality. ')
st.markdown('The Global Leadership Initiative on Malnutrition (GLIM) have developed a consensus definition for malnutrition including phenotypic (unintentional weight loss, low body mass index or reduced muscle mass) and etiological criteria (reduced food intake or assimilation or inflammation). To diagnose malnutrition, at least one phenotypic and one etiologic criteria must be met. The i-OPTIC platform combines the presence of GLIM criteria and other demographic information to predict the risk of mortality at one-year. These prediction models enable healthcare professionals to identify patients who may benefit from early and more aggressive nutrition intervention. Establishing which patients are at greatest risk of malnutrition-related mortality will allow for prioritisation of clinical care and timely interventions to improve patient outcomes. ')
st.markdown(f"<h4 style='text-align: left'>How to use the i-OPTIC platform?</h4>", unsafe_allow_html=True)
st.markdown("i-OPTIC is a purpose-built tool to determine a patient’s risk of malnutrition-related mortality at one-year. To use the i-OPTIC platform, go to the ‘Prediction’ tab. Here you will be asked to input demographic information (age, sex, cancer diagnosis) and the GLIM phenotypic (unintentional weight loss, low body mass index or reduced muscle mass) and etiological criteria (reduced food intake or assimilation or inflammation). If this information is not available, the Patient Generate Subjective Global Assessment (https://pt-global.org/pt-global/) is one tool that can be used to estimate each of the GLIM criteria and diagnose malnutrition. ")
