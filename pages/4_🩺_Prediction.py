import streamlit as st


st.set_page_config(page_title="My App", layout="wide")#centered


st.markdown('''<style>
div.css-1r6slb0.e1tzin5v2 {
    background-color: #EEEEEE;
    border: 2px solid #CCCCCC;
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
}
div.row-widget.stRadio {
    background-color: #EEEEEE;
    border: 2px solid #CCCCCC;
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
}
div.stSlider {
    background-color: #EEEEEE;
    border: 2px solid #CCCCCC;
    padding: 5% 5% 5% 10%;
    border-radius: 5px;
}

</style>''', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col21, col22 = st.columns(2)
col31, col32 = st.columns(2)
# with col1:
with col21:
        
    st.radio(
        'Select model:',
        ["Victoria", "UK" ,"Canada"],
        horizontal=False,
    )

with col31: 
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
        key="visibility",
        horizontal=True,
    )
    st.radio(
        "Inflamation 🧍‍♀️",
        ["Yes", "No" ],
        key="visibility",
        horizontal=True,
    )
    st.radio(
        "Gender 🧍‍♀️",
        ["Yes", "No" ],
        key="visibility",
        horizontal=True,
    )

    st.slider("Age 🧍‍♀️", min_value=1, max_value=100, value=50, step=1)





