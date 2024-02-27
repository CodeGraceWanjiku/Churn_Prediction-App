import streamlit as st
import joblib
import pandas as pd



st.set_page_config(
 page_title= "Predict",
 page_icon=":small_red_triangle:",
    layout="wide"
)

#st.title("Make your predictions here")


# cache the models
st.cache_resource(show_spinner="Model loading")


# create two functions to load the models
def load_gradient_pipeline():
    pipeline = joblib.load("./models/gradient_pipeline.joblib")
    return pipeline

def load_naives_pipeline():
    pipeline = joblib.load("./models/naives_pipeline.joblib")
    return pipeline


# create a function to select the model to use
def choose_model():
    st.selectbox("select model",options=['Gradient boosting','Naives bay'],key='selected_model')
    
    if st.session_state['selected_model'] == 'Gradient boosting':
           pipeline =load_gradient_pipeline()
    else:
           pipeline =load_naives_pipeline()

    encoder =joblib.load('./models/encoder.joblib')

    return pipeline,encoder

#Create a make_prediction function
def make_prediction(pipeline,encoder):
     #extract input features from session state
     gender = st.session_state["gender"]
     seniorcitizen = st.session_state["seniorcitizen"]
     partner = st.session_state["partner"]
     dependants = st.session_state["dependants"]
     tenure = st.session_state["tenure"]
     phoneservice = st.session_state["phoneservice"]
     multiplelines = st.session_state["multiplelines"]
     internetservice = st.session_state["internetservice"]
     onlinesecurity = st.session_state["onlinesecurity"]
     onlinebackup = st.session_state["onlinebackup"]
     deviceprotection = st.session_state["deviceprotection"]
     techsupport = st.session_state["techsupport"]
     streamingtv = st.session_state["streamingTV"]
     streaming_movies = st.session_state["streamingmovies"]
     contract = st.session_state["contract"]
     paperlessbiling = st.session_state["paperlessbiling"]
     payment_method = st.session_state["paymentmethod"]
     monthly_income = st.session_state["monthlyincome"]

     columns =['Gender','SeniorCitizen','Partner','Dependants','Tenure',
               'PhoneService','MultipleLines','InternetService','OnlineSecurity',
               'OnlineBackup','DeviceProtection','TechSupport',' StreamingTV',
               'StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges']
     
     data = [[gender,seniorcitizen,partner,dependants,tenure,
               phoneservice,multiplelines,internetservice,onlinesecurity,
               onlinebackup,deviceprotection,techsupport,streamingtv,
               streaming_movies,contract,paperlessbiling,payment_method,monthly_income]]
     # create a dataframe
     df = pd.DataFrame(data,columns= columns)
     # make predictions
     pred = pipeline.predict(df)
     
     prediction = int(pred[0])
     
     prediction =encoder.inverse_transform([prediction])
     
     # Get probabilities
     probability_proba = pipeline.predict_proba(df)

     # updating state
     
     st.session_state['prediction'] =prediction
     
     
     st.session_state['probability'] =probability_proba

     return prediction,probability_proba

     # create a function to show the input features


def show_features():
    pipeline,encoder = choose_model()
    with st.form("Personal Information"):


        col1,col2,col3 =st.columns(3)
        with col1:
            st.write("### Personal Information")
            st.selectbox("Gender",options=['Female','Male'],key="gender")
            st.selectbox("Dependants",options=['Yes','No'],key='dependants')
            st.selectbox("Partner",options=['Yes','No'],key='partner')
            st.selectbox("Seniorcitizen",options=['Yes','No'],key='seniorcitizen')

        with col2:
            st.write("### Work Information")
            st.selectbox("contract type",options=['Month to Month','One Year','Two Year'],key='contract')
            st.number_input("monthly income",min_value=18,max_value=60,step=1000,key='monthlyincome')
            st.slider("Tenure",min_value=18,max_value=60,key='tenure')
            
        with col3:
            st.write("### Services")
            st.selectbox("Phoneservice",options=['Yes','No'],key='phoneservice')
            st.selectbox("Onlinesecurity",options=['Yes','No'],key='onlinesecurity')
            st.selectbox("Internetservice",options=['DSL','Fiberoptic','No Service'],key='internetservice')
            st.selectbox("Onlinebackup",options=['Yes','No'],key='onlinebackup')
            st.selectbox("Multiplelines",options=['Yes','No'],key='multiplelines')
            st.selectbox("Deviceprotection",options=['Yes','No'],key='deviceprotection')
            st.selectbox("Techsupport",options=['Yes','No'],key='techsupport')
            st.selectbox("Streaming TV",options=['Yes','No'],key='streamingTV')
            st.selectbox("Streaming movies",options=['Yes','No'],key='streamingmovies')
            st.selectbox("Paperless biling",options=['Yes','No'],key='paperlessbiling')
            st.selectbox("Payment method",options=['Electronic','Mailed check','Bank Transfer','Credit Card'],key='paymentmethod')
        # create a form to submit the data
        

        st.form_submit_button("submit",on_click  = make_prediction,kwargs = dict(pipeline=pipeline,encoder=encoder))


if __name__ == "__main__" :
    st.title("Make a prediction")
    #choose_model()
    show_features()


    final_prediction =st.session_state['prediction']
    
    st.markdown("###(final_prediction)")
    
    st.write(st.session_state)