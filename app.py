import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Siddhartha MACCS Calculator",
    layout="centered",
)

# Load Logo
logo = Image.open("assets/logo.png")

# Sidebar Logo
st.sidebar.image(logo, width=200)

# Main Page Logo
st.image(logo, width=250)

st.title("SIDDHARTHA MACCS LTD")
st.subheader("MIS & FD Prematurity Calculator")

st.markdown("""
### Welcome

Use the sidebar to select:

- 📘 MIS Prematurity Calculator  
- 📗 FD Prematurity Calculator  

""")

st.info("Developed by Nithin MSS")
