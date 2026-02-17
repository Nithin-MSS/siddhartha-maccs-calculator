import streamlit as st
from datetime import date
from backend.mis_calculator import calculate_mis

st.title("📘 MIS Prematurity Calculator")

principal = st.number_input("Deposit Amount (₹)", min_value=0.0)

deposit_date = st.date_input("Deposit Date")
premature_date = st.date_input("Premature Closing Date")

if st.button("Calculate MIS"):

    if premature_date <= deposit_date:
        st.error("Premature date must be after deposit date.")
    else:
        result = calculate_mis(principal, deposit_date, premature_date)

        st.subheader("Results")

        st.write(f"Total Days: {result['days']}")
        st.write(f"Slab Rate: {result['slab_rate']}%")
        st.write(f"Monthly Effective Rate: {result['monthly_effective_rate']}%")
        st.write(f"Premature Rate: {result['premature_rate']}%")

        st.write(f"Interest Already Paid: ₹{result['interest_paid']:,.2f}")
        st.write(f"Eligible Interest: ₹{result['eligible_interest']:,.2f}")
        st.write(f"Excess Deducted: ₹{result['excess']:,.2f}")

        st.success(f"Final Settlement: ₹{result['final_settlement']:,.2f}")
