import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title= "Dashboards",
    page_icon=":small_red_triangle:",
    layout="wide"
)

st.title("Dashboards 📊 & 📈")
st.write("Welcome to the dashboard page")
# function to read the csv file

df = pd.read_csv("data/df_concat.csv")


data = pd.DataFrame(
    np.random.randn(20, 2),
    columns= ["Churn","Gender"],
)

tab1, tab2 = st.tabs(["📈 EDA", "🗃 KPI"])
data = np.random.randn(10, 1)

tab1.subheader("Distribution of Target Variable (Churn)")
#tab1.line_chart(data)
fig, ax = plt.subplots()
sns.countplot(x='Churn', data=df, palette='viridis', ax=ax)
st.pyplot(fig)

# Plot pie chart for Internet Service category
for service_type in df['InternetService'].unique():
        fig, ax = plt.subplots()
        churn_counts = df[df['InternetService'] == service_type]['Churn'].value_counts()
        churn_counts.plot.pie(labels=churn_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff'], ax=ax)
        ax.set_title(f'Churn Distribution for {service_type}')
        st.pyplot(fig)


tab2.subheader("A tab with the data")

