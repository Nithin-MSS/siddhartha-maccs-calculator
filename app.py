import streamlit as st

st.set_page_config(
    page_title="Siddhartha MACCS Calculator",
    layout="centered",
)

# Sidebar Logo
st.sidebar.image("assets/logo.png", width=200)

# Main Logo
st.image("assets/logo.png", width=250)

st.title("SIDDHARTHA MACCS LTD")
st.subheader("MIS & FD Prematurity Calculator")

st.markdown("""
### Welcome

Use the sidebar to select:

- 📘 MIS Prematurity Calculator  
- 📗 FD Prematurity Calculator  
""")

st.info("Developed by Nithin MSS")
