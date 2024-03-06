import streamlit as st
import pandas as pd
import pyodbc


st.set_page_config(
    page_title= "Data",
    page_icon=":house:",
    layout="wide"
)

st.title("Vodafone's Data(A Telecommunications Company)📈")


@st.cache_resource(show_spinner='connecting to database')
def init_connection():
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["SERVER"]
        + ";DATABASE="
        + st.secrets["DATABASE"]
        + ";UID="
        + st.secrets["USERNAME"]
        + ";PWD="
        + st.secrets["PASSWORD"]
    )
    return connection

conn = init_connection()
# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data()
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        
        df = pd.DataFrame.from_records(data=rows,columns =[column[0]for column in cur.description])

    return df

def churn_first_3000():
    query = run_query("SELECT * dbo.LP2_Telco_churn_first_3000;")
    df = st.write(run_query(query))

    return df

if __name__ == '__main__':
    st.selectbox("select features",options=["All numeric","Numeric"])
    churn_first_3000()
    
# Print results.
#for row in rows:
#    st.write(f"{row[0]} has a :{row[1]}:")
