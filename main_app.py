import streamlit as st

# st.set_page_config(layout='wide')
# Set page configuration
st.set_page_config(page_title="My App", layout="wide")#centered


# Title
st.title("Welcome to My App")

st.markdown(
    """
    <style>
    MainMenu {visibility: hidden;}
        
        div[data-testid="column"]:nth-of-type(1)
        {
            # border:1px solid red;
            text-align: end;
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            # border:1px solid blue;
            text-align: start;
        } 
        .sidebar .sidebar-content {
        width: 100px;
    }
    </style>
    """,unsafe_allow_html=True
)






