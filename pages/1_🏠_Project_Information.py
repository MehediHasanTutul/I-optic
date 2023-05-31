import streamlit as st


st.set_page_config(page_title="My App", layout="wide")#centered


col1, col2 = st.columns([1.2,5])

with col1:
    with st.container():
            
        st.radio(
            'Select model:',
            ["Victoria", "UK" ,"Canada"],
            horizontal=False,
        )
    st.markdown('**Set inputs:**')
    
    st.radio(
        "Unintetional weight loss 🧍‍♀️",
        ["Yes", "No" ],
        
        horizontal=True,
    )
    st.radio(
        "Reduced food intake 🥪",
        ["Yes", "No" ],
        
        horizontal=True,
    )
    st.radio(
        "Low BMI 🕴️",
        ["Yes", "No" ],
        
        horizontal=True,
    )
    st.radio(
        "Reduced mussle mass 🧍‍♀️",
        ["Yes", "No" ],
        
        horizontal=True,
    )
    st.radio(
        "Inflamation 🧍‍♀️",
        ["Yes", "No" ],
      
        horizontal=True,
    )
    st.radio(
        "Gender 🧍‍♀️",
        ["Yes", "No" ],
       
        horizontal=True,
    )

    st.slider("Age 🧍‍♀️", min_value=1, max_value=100, value=50, step=1)





