import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.mis_calculator import calculate_mis, compare_wait

st.title("📘 MIS Prematurity Calculator")

principal = st.number_input("Deposit Amount (₹)", min_value=0.0)
original_rate = st.number_input("Original Rate (%)", min_value=0.1)
completed_months = st.number_input("Completed Months", min_value=1)

st.markdown("---")

if st.button("Calculate Prematurity"):

    result = calculate_mis(principal, original_rate, completed_months)

    st.subheader("Current Prematurity Result")

    st.write(f"Premature Rate: {result['premature_rate']}%")
    st.write(f"Interest Received: ₹{result['interest_received']:,.2f}")
    st.write(f"Eligible Interest: ₹{result['eligible_interest']:,.2f}")
    st.write(f"Excess Deducted: ₹{result['excess']:,.2f}")

    st.success(f"Final Settlement: ₹{result['final_settlement']:,.2f}")
    st.info(f"Total Effective Amount: ₹{result['total_effective']:,.2f}")

st.markdown("----")

st.subheader("Compare: Break Now vs Wait")

wait_months = st.number_input("Wait Additional Months", min_value=1)

if st.button("Compare Now vs Wait"):

    comparison = compare_wait(principal, original_rate, completed_months, wait_months)

    now = comparison["now"]
    future = comparison["future"]

    st.write("### Break Now")
    st.write(f"Total Effective: ₹{now['total_effective']:,.2f}")

    st.write("### After Waiting")
    st.write(f"Total Effective: ₹{future['total_effective']:,.2f}")

    st.success(f"Extra Gain by Waiting: ₹{comparison['gain']:,.2f}")
