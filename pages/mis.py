import streamlit as st
from backend.mis_calculator import calculate_mis

st.title("📘 MIS Prematurity Calculator")

principal = st.number_input("Deposit Amount (₹)", min_value=0.0)
rate = st.number_input("Original Rate (%)", min_value=0.0)
months = st.number_input("Completed Months", min_value=0)

if st.button("Calculate MIS"):

    result = calculate_mis(principal, rate, months)

    st.subheader("Current Prematurity Result")

    st.write(f"Premature Rate: {result['premature_rate']}%")
    st.write(f"Interest Received: ₹{result['interest_received']:,.2f}")
    st.write(f"Eligible Interest: ₹{result['eligible_interest']:,.2f}")
    st.write(f"Excess Deducted: ₹{result['excess_deducted']:,.2f}")
    st.success(f"Final Settlement: ₹{result['final_settlement']:,.2f}")
    st.write(f"Total Effective Amount: ₹{result['total_effective']:,.2f}")
