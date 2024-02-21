import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title= "Dashboards",
    page_icon=":small_red_triangle:",
    layout="wide"
)

st.title("Dashboards")
st.write("This are the EDAs")

df = pd.read_csv("customer_churn.csv")
df = pd.DataFrame(df)

data = pd.DataFrame(
    np.random.randn(20, 2),
    columns= ["Churn","Gender"],
)

col1, col2 = st.columns(2)

with col1:
   st.header("Bar Chart")
   st.bar_chart(data)

with col2:
   st.header("Pie Chart")
   st.bar_chart(data)
