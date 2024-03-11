import streamlit as st
import pandas as pd
import pyodbc


st.set_page_config(
    page_title= "Data",
    page_icon=":house:",
    layout="wide"
)

st.title("Vodafone's Data(A Telecommunications Company)📈")

churn_data = pd.read_csv("data/df_concat.csv")
churn_data = churn_data.drop(['Unnamed: 0','customerID'],axis=1)
churn_data
def show_numeric_features(churn_data):
    numeric_features = churn_data.select_dtypes(include='number').columns
    st.write("Numeric Features:")
    for feature in numeric_features:
        st.write(f"- {feature}")

def show_categorical_features(churn_data):
    categorical_features = churn_data.select_dtypes(include='object').columns
    st.write("Categorical Features:")
    for feature in categorical_features:
        st.write(f"- {feature}")

def main():
    churn_data = pd.read_csv("data/df_concat.csv")
    churn_data = churn_data.drop(['Unnamed: 0','customerID'],axis=1)
    options = st.selectbox(
        'Choose the dataset the features to work with',
        ['Numeric Features', 'Categorical Features']
    )

    if options == 'Numeric Features':
        show_numeric_features(churn_data)
    elif options == 'Categorical Features':
        show_categorical_features(churn_data)

if __name__ == "__main__":
    main()