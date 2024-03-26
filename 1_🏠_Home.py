import streamlit as st
import streamlit_authenticator as stauth
import yaml
from streamlit_authenticator import Authenticate
from yaml.loader import SafeLoader
from utils import column_1, column_2


st.set_page_config(
    page_title='Home',
    page_icon=':)',
    layout= 'wide'
)
st.title("👋 Welcome to Churn Prediction App")

st.image("./assets/churn.jpg")
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


name, authentication_status, usernames = authenticator.login(location='sidebar')


if st.session_state["authentication_status"]:
    authenticator.logout(location='sidebar', key='logout-button')
    col1, col2 = st.columns(2)
    with col1:
        st.write("column1")
        column_1
    with col2:
        st.write('### How to run application')
        st.code('''
        #activate virtual environment
        env/scripts/activate
        streamlit run 1_🏠_Home.py
        ''')
        column_2
        st.link_button('Repository on GitHub', url='https://github.com/CodeGraceWanjiku/Churn_Prediction-StreamlitWebApp', type='primary')

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.info('Enter username and password to use the app.')
    st.code("""
            Test Account
            Username: shix
            Password: wanjiku123""")


with st.expander("click here to find links to the project"):
    st.page_link("https://www.linkedin.com/in/grace-w-wanjiru/", label="Linkedin", icon="🌐")
    st.page_link("https://https://medium.com/@grakashi/", label="Medium", icon="✍")
    st.page_link("https://github.com/CodeGraceWanjiku/Churn_Prediction-App", label="Github", icon="🏞️")