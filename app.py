import streamlit as st
import pandas as pd
import plotly.express as px
import os
print("Working directory:", os.getcwd())

# Read the vehicles dataset into a DataFrame
df = pd.read_csv("vehicles_us.csv")

# 1. Header
st.header("Vehicle Data Explorer")

# 2. Histogram
fig_hist = px.histogram(df, x="paint_color", title="Distribution of Paint Color")
st.plotly_chart(fig_hist)

# 3and4. Scatter Plot/Checkbox for Trendline
if st.checkbox("Show Trendline on Scatterplot"):
    fig_scatter = px.scatter(df, x="model_year", y="odometer", title="Mileage vs Year", trendline="ols")
else:
    fig_scatter = px.scatter(df, x="model_year", y="odometer", title="Mileage vs Year")
st.plotly_chart(fig_scatter)