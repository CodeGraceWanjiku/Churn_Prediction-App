import streamlit as st

st.set_page_config(
    page_title='Home',
    page_icon=':)',
    layout= 'wide'
)
st.title("Churn Prediction App")
st.write("This App Predicts the churn rate of employees in a Telecommunications company using a classification model")

st.image('images/churn.jpeg', caption='Churn rate')
st.button("Login")
st.text_input("Enter your name")

st.subheader("Contact Information")
st.write("This is the links to the project's repository in github")
st.page_link("https://github.com/CodeGraceWanjiku/Churn_Prediction-App", label="Github", icon="🌍")
st.page_link("https://www.linkedin.com/in/grace-w-wanjiru/", label="Linkedin", icon="🌐")
st.page_link("https://www.linkedin.com/in/grace-w-wanjiru/", label="Medium", icon="✍")

