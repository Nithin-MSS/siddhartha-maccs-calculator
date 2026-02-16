import streamlit as st

st.set_page_config(
    page_title="Siddhartha MACCS Calculator",
    layout="centered"
)

# ONLY main logo (not sidebar)
st.image("assets/logo.png", width=300)

st.title("SIDDHARTHA MACCS LTD")
st.subheader("MIS & FD PREMATURITY CALCULATOR")

st.markdown("---")

st.header("Welcome")

st.write("Use the sidebar to select:")

st.markdown("""
- 🔹 MIS Prematurity Calculator  
- 🔹 FD Prematurity Calculator
""")

st.markdown("---")

st.info("Developed by Nithin MSS")
