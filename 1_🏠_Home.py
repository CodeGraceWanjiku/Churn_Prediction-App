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

#add_selectbox = st.sidebar.selectbox(
    #"Contacts",
    #("Email", "Home phone", "Mobile phone")
#)


st.subheader("More Information")
st.write("This are the links to the project's Github,Medium and Linkedin")
st.page_link("https://github.com/CodeGraceWanjiku/Churn_Prediction-App", label="Github", icon="🌍")
st.page_link("https://www.linkedin.com/in/grace-w-wanjiru/", label="Linkedin", icon="🌐")
st.page_link("https://www.linkedin.com/in/grace-w-wanjiru/", label="Medium", icon="✍")

st.link_button("Github", "https://github.com/CodeGraceWanjiku/Churn_Prediction-App")