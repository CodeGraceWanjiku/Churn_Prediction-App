import streamlit as st

st.set_page_config(
    page_title='Home',
    page_icon=':)',
    layout= 'wide'
)
st.title("Churn Prediction App")
st.button("Login")
st.text_input("Enter your name")