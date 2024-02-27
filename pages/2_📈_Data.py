import streamlit as st
import pandas as pd

st.set_page_config(
    page_title= "Data",
    page_icon=":house:",
    layout="wide"
)

st.title("Vodafone's Data(A Telecommunications Company)📈")

df = pd.read_csv("data/df_concat.csv")
df = pd.DataFrame(df)
st.dataframe(df) 
