import streamlit as st
import numpy as np

# Streamlit app title
st.title("Investment Return Calculator")

# User input: Principal amount
principal = st.number_input("Principal Amount ($)", min_value=0.01)

# User input: Annualized return rate
annual_return = st.number_input("Expected Annualized Return Rate (%)", min_value=0.01)

# User input: Investment period (years)
investment_period = st.number_input("Investment Period (Years)", min_value=1)

# User input: Investment type (Simple or Compound)
investment_type = st.radio("Choose Investment Type:", ("Simple Interest (One-Time)", "Compound Interest (One-Time)", "Compound Interest (Monthly)"))

# User input: Monthly fixed investment
if investment_type == "Compound Interest (Monthly)":
    monthly_investment = st.number_input("Monthly Fixed Investment ($)", min_value=0.01)
else:
    monthly_investment = None

# Calculate investment returns
if st.button("Calculate"):
    if "Compound Interest" in investment_type:
        months = investment_period * 12
        monthly_rate = (annual_return / 100) / 12
        future_value = principal * (1 + monthly_rate) ** months

        if monthly_investment:
            future_value += monthly_investment * (1 + monthly_rate) * (((1 + monthly_rate) ** months)-1) / monthly_rate
    else:
        future_value = principal * (1 + (annual_return / 100) * investment_period)

    st.write(f"Future Value: ${future_value:.2f}")

# Reset button to clear inputs
if st.button("Reset"):
    principal = annual_return = investment_period = monthly_investment = None
    st.write("Inputs have been reset.")
