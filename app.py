import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.data_analysis import analyze_data

st.set_page_config(page_title="Job Market Trends", layout="wide")
st.title("📊 Job Listing Data Analysis Dashboard")

# Load data
df = pd.read_csv('data/jobs_clean.csv')
skills_df, exp_df = analyze_data()

# Overview
st.subheader("Dataset Overview")
st.dataframe(df.head())

# Skill Demand
st.subheader("🔥 Top 10 In-Demand Skills")
fig1 = px.bar(skills_df, x='Skill', y='Count', color='Skill', title='Most In-Demand Skills')
st.plotly_chart(fig1, use_container_width=True)

# Experience Distribution
st.subheader("👨‍💼 Experience Level Distribution")
fig2 = px.pie(exp_df, names='Experience', values='Count', title='Experience Demand')
st.plotly_chart(fig2, use_container_width=True)

st.markdown("**Project by Shyam Dodway — Job Market Insights using Python & Streamlit**")
