import streamlit as st
import joblib
import pandas as pd
import os
import datetime


st.set_page_config(
 page_title= "Predict",
 page_icon=":small_red_triangle:",
    layout="wide"
)




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
    col1,col2 = st.columns(2)
    with col1:
         st.selectbox("Please select model",options=['Gradient boosting','Naives bay'],key='selected_model')
    with col2:
         pass
    if st.session_state['selected_model'] == 'Gradient boosting':
           pipeline =load_gradient_pipeline()
    else:
           pipeline =load_naives_pipeline()

    encoder =joblib.load('./models/encoder.joblib')

    return pipeline,encoder

# Initialize session state (prediction)
if 'prediction' not in  st.session_state:
    st.session_state['prediction'] = None

# Initialize session state(probability)
if 'probability' not in  st.session_state:
    st.session_state['probability'] = None

#Create a make_prediction function
def make_prediction(pipeline,encoder):
     
     
     #extract input features from session state
     gender = st.session_state["gender"]
     seniorcitizen = st.session_state["seniorcitizen"]
     partner = st.session_state["partner"]
     dependents = st.session_state["Dependents"]
     tenure = st.session_state["tenure"]
     phoneservice = st.session_state["phoneservice"]
     multiplelines = st.session_state["multiplelines"]
     internetservice = st.session_state["internetservice"]
     onlinesecurity = st.session_state["onlinesecurity"]
     onlinebackup = st.session_state["onlinebackup"]
     deviceprotection = st.session_state["deviceprotection"]
     techsupport = st.session_state["techsupport"]
     streamingtv = st.session_state["StreamingTV"]
     streaming_movies = st.session_state["streamingmovies"]
     contract = st.session_state["contract"]
     paperlessbiling = st.session_state["paperlessbiling"]
     payment_method = st.session_state["paymentmethod"]
     monthly_income = st.session_state["monthlyincome"]
     total_charges = st.session_state['TotalCharges']

     columns =['gender','SeniorCitizen','Partner','Dependents','tenure',
               'PhoneService','MultipleLines','InternetService','OnlineSecurity',
               'OnlineBackup','DeviceProtection','TechSupport','StreamingTV',
               'StreamingMovies','Contract','PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges']
     
     data = [[gender,seniorcitizen,partner,dependents,tenure,
               phoneservice,multiplelines,internetservice,onlinesecurity,
               onlinebackup,deviceprotection,techsupport,streamingtv,
               streaming_movies,contract,paperlessbiling,payment_method,monthly_income,total_charges]]
     # create a dataframe
     df = pd.DataFrame(data,columns= columns)
     
     df['predicted time'] = datetime.date.today()
     df['Churn status'] = st.session_state['prediction']

     #if not os.path.exists("./data/history.csv"):
          #os.makedirs("./data/history.csv")
     
     df.to_csv("./data/history.csv",mode='a',header=not os.path.exists('./data/history.csv'),index=False)
     
     # make predictions
     prediction = pipeline.predict(df)
     
     prediction = prediction[0]
     #prediction = encoder.inverse_transform(prediction)
     
     # Get probabilities
     probability_proba = pipeline.predict_proba(df)

     # updating state
     
     st.session_state['prediction'] = prediction
     
     st.session_state['probability'] =probability_proba

     return prediction,probability_proba

     # create a function to show the input features


def show_features():
    pipeline,encoder = choose_model()
    with st.form("Personal Information"):


        col1,col2 =st.columns(2)
        with col1:
            st.write("### Personal Information")
            st.selectbox("Gender",options=['Female','Male'],key="gender")
            st.selectbox("Dependents",options=['Yes','No'],key='Dependents')
            st.selectbox("Partner",options=['Yes','No'],key='partner')
            st.selectbox("Seniorcitizen",options=['Yes','No'],key='seniorcitizen')
            


            st.write("### Work Information")
            st.selectbox("contract type",options=['Month-to-month','One year','Two year'],key='contract')
            st.number_input("monthly income",step=1000,key='monthlyincome')
            st.number_input("tenure",max_value=60,key="tenure")
            st.number_input("TotalCharges",step=1000,key="TotalCharges")


        with col2:
            st.write("### Services")
            st.selectbox("Phoneservice",options=['Yes','No'],key='phoneservice')
            st.selectbox("Onlinesecurity",options=['Yes','No'],key='onlinesecurity')
            st.selectbox("Internetservice",options=['DSL','Fiber optic','No Service'],key='internetservice')
            st.selectbox("Onlinebackup",options=['Yes','No'],key='onlinebackup')
            st.selectbox("Multiplelines",options=['Yes','No'],key='multiplelines')
            st.selectbox("Deviceprotection",options=['Yes','No'],key='deviceprotection')
            st.selectbox("Techsupport",options=['Yes','No'],key='techsupport')
            st.selectbox("Streaming TV",options=['Yes','No'],key='StreamingTV')
            st.selectbox("Streaming movies",options=['Yes','No'],key='streamingmovies')
            st.selectbox("Paperless biling",options=['Yes','No'],key='paperlessbiling')
            st.selectbox("Payment method",options=['Electronic check','Mailed check','Bank transfer','Credit Card'],key='paymentmethod')
            

        # create a form to submit the data
        st.form_submit_button("Predict",on_click  = make_prediction,kwargs = dict(pipeline=pipeline,encoder=encoder))


if __name__ == "__main__" :
    st.title("Make a prediction ♟️")
    
    show_features()

    prediction = st.session_state['prediction']
    probability = st.session_state['probability']

    if not prediction:
         st.markdown('## predictions will show here' )
    elif prediction == 1:
         probability_of_yes = probability[0][1] * 100
         st.markdown(f'## Employee will leave the company with a probability of {probability_of_yes:.2f}%')
    else:
         probability_of_no = probability[0][0] * 100
         st.markdown(f'## Employee will not leave the company with a probaility of {probability_of_no:.2f}%')

      
    st.write(st.session_state)

