import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title= "Dashboards",
    page_icon=":small_red_triangle:",
    layout="wide"
)

st.title("Dashboards")

df = pd.read_csv("customer_churn.csv")
df = pd.DataFrame(df)
st.dataframe(df) 
st.bar_chart(data=df, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Bar Chart")
   st.bar_chart(data=df, x="Churn", y="Gender", color="Blue",use_container_width=True)

with col2:
   st.header("Linkedin Link")
   st.page_link("https://www.linkedin.com/in/grace-w-wanjiru/",label="Linkedin")

with col3:
   st.header("Medium Link")
   st.page_link("https://medium.com/@grakashi",label="Medium")