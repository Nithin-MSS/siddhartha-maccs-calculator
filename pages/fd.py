import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.fd_calculator import calculate_fd

st.title("📗 FD Prematurity Calculator")

principal = st.number_input("Deposit Amount (₹)", min_value=0.0)
original_rate = st.number_input("Original Rate (%)", min_value=0.1)
completed_months = st.number_input("Completed Months", min_value=1)

if st.button("Calculate FD"):

    result = calculate_fd(principal, original_rate, completed_months)

    st.subheader("FD Prematurity Result")

    st.write(f"Premature Rate: {result['premature_rate']}%")
    st.write(f"Interest: ₹{result['interest']:,.2f}")

    st.success(f"Final Settlement: ₹{result['final_settlement']:,.2f}")
