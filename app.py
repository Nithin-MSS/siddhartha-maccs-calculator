import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SIDDHARTHA MACCS LTD",
    layout="centered",
)

# ---------------- SIDEBAR CAPITAL FIX ----------------
st.markdown("""
<style>
/* Make sidebar page names uppercase */
section[data-testid="stSidebar"] ul li span {
    text-transform: uppercase;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGO ----------------
st.sidebar.image("assets/logo.png", width=200)
st.image("assets/logo.png", width=250)

# ---------------- TITLE ----------------
st.title("SIDDHARTHA MACCS LTD")
st.subheader("MIS & FD PREMATURITY CALCULATOR")

st.markdown("---")

st.markdown("""
### Welcome

Use the sidebar to select:

🔹 MIS Prematurity Calculator  
🔹 FD Prematurity Calculator
""")

st.markdown("---")

st.info("Developed by Nithin MSS")
