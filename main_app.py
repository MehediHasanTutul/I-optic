import streamlit as st

# st.set_page_config(layout='wide')
# Set page configuration
st.set_page_config(page_title="My App", layout="wide")#centered

# Logo image
# logo_image = Image.open("path_to_logo_image.png")
# st.sidebar.image(logo_image, width=100)

# Title
st.title("Welcome to My App")

st.markdown(
    """
    <style>
#     [data-testid="column"] {
#     border-radius: 0px;
#     padding:0px;
#     gap: 0
#     margin:0
# } 
        
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






