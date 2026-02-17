import streamlit as st
from datetime import date
from backend.mis_calculator import calculate_mis

st.title("📘 MIS Prematurity Calculator")

principal = st.number_input("Deposit Amount (₹)", min_value=0.0)
rate = st.number_input("Original Rate (%)", min_value=0.0)

deposit_date = st.date_input("Deposit Date")
premature_date = st.date_input("Premature Closing Date")

if st.button("Calculate MIS"):

    result = calculate_mis(principal, rate, deposit_date, premature_date)

    st.subheader("Results")

    st.write(f"Total Days: {result['total_days']}")
    st.write(f"Premature Rate: {result['premature_rate']:.2f}%")
    st.write(f"Original Interest: ₹{result['original_interest']:,.2f}")
    st.write(f"Eligible Interest: ₹{result['eligible_interest']:,.2f}")
    st.write(f"Excess Deducted: ₹{result['excess']:,.2f}")
    st.success(f"Final Settlement: ₹{result['final_settlement']:,.2f}")
