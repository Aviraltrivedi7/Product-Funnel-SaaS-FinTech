# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.set_page_config(page_title="SaaS FinTech Funnel", layout="centered")
st.title("📊 SaaS FinTech Revenue Funnel Analysis")

# Funnel Data (sample values from your project)
data = {
    'stage': ['Started', 'Interacted', 'Login Attempted', 'Login Complete', 'Order Complete'],
    'count': [3055, 1380, 1053, 320, 351]
}

df = pd.DataFrame(data)

# Show Data
st.subheader("📋 Funnel Data Table")
st.dataframe(df)

# Conversion Rate Calculation
df['conversion_rate'] = (df['count'] / df['count'][0]) * 100

# Show Conversion Rates
st.subheader("📉 Conversion Rates (%)")
st.dataframe(df[['stage', 'conversion_rate']])

# Line Chart
st.subheader("📈 Funnel Drop-off Chart")
st.line_chart(df.set_index('stage')['count'])

# Revenue Impact Estimation
st.subheader("💰 Revenue Simulation")

rev_per_user = st.number_input("Enter Estimated Revenue per User ($)", value=100)

extra_users_interaction = df['count'][0] * 0.01
extra_users_login = df['count'][1] * 0.01

revenue_interaction = extra_users_interaction * rev_per_user
revenue_login = extra_users_login * rev_per_user

st.success(f"📌 1% more user interaction → Estimated +${revenue_interaction:.2f}/day")
st.success(f"📌 1% more login attempts → Estimated +${revenue_login:.2f}/day")

st.markdown("---")
st.caption("Made with ❤️ by Aviral")
