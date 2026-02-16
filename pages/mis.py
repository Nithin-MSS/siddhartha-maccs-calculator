import streamlit as st
import sys
import os

# Fix import path for Streamlit Cloud
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.mis_calculator import calculate_mis_prematurity

st.title("📘 MIS Prematurity Calculator")

principal = st.number_input("Deposit Amount (₹)", min_value=0.0)
roi = st.number_input("Original ROI (%)", min_value=0.0)
months = st.number_input("Completed Months", min_value=0)

if st.button("Calculate MIS"):

    result = calculate_mis_prematurity(principal, roi, months)

    st.subheader("Results")
    st.write(f"Premature Rate: {result['premature_rate']:.2f}%")
    st.write(f"Interest Received: ₹{result['interest_received']:,.2f}")
    st.write(f"Eligible Interest: ₹{result['eligible_interest']:,.2f}")
    st.write(f"Adjustment: ₹{result['excess_interest']:,.2f}")
    st.success(f"Final Settlement: ₹{result['final_amount']:,.2f}")
