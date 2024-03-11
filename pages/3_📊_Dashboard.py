import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import altair as alt
#from streamlit_metrics import metric, metric_row
#import pygal
#import leather
import plotly.express as px

st.set_page_config(
    page_title= "Dashboards",
    page_icon=":small_red_triangle:",
    layout="wide"
)

st.title("Dashboards 📊 & Visualizations 📈")

#function to read the csv file

df = pd.read_csv("data/df_concat.csv")
df = df.drop(['Unnamed: 0','customerID'],axis=1)

tab1, tab2 ,tab3 = st.tabs(["📈 EDA","Dashboard","🗃 KPI"])

with tab1:
     st.subheader("EDA Visualizations")

     col1,col2 = st.columns(2)

     with col1:
         df_long = pd.melt(df, value_vars=df.columns)
         histogram = px.histogram(df_long, x='value')
         histogram.update_layout(title="Histogram of Distribution of Target Variables")

         boxplot = px.box(df_long, orientation='h', title='Box Plot of Services')
        
        #Show plots
         st.plotly_chart(histogram)
         st.plotly_chart(boxplot)


with col2:

     corr = df.corr(numeric_only=True)
 # Create correlation heatmap with Plotly Express
     corr_fig = px.imshow(corr, labels=dict(x="Features", y="Features"), x=corr.columns, y=corr.columns)
# Set title
     
     corr_fig.update_layout(title="Correlation Heatmap")
     data = df[['gender','SeniorCitizen','MonthlyCharges']]
     sns.pairplot(data,hue='gender')
# Create a scatter chart using Plotly Express
     fig_scatter = px.scatter(data, x='SeniorCitizen', y='MonthlyCharges', color='gender', 
                 title='Scatter Chart of SeniorCitizen vs MonthlyCharges with Gender Color')


# Display the plot using st.plotly_chart()
     st.plotly_chart(corr_fig)
     st.plotly_chart(fig_scatter)
    

with tab2:
     
     col1,col2 = st.columns(2)
     with col1:
         
      st.subheader("Dashboard visualizations")
      barchart = px.bar(df, x='InternetService', color='Churn', barmode='group',
                category_orders={'InternetService': ['DSL', 'Fiber optic', 'No']},
                color_discrete_map={'No': 'lightgreen', 'Yes': 'yellow'})
      barchart.update_xaxes(title="Internet Service Type")
      barchart.update_yaxes(title="Count")
      barchart.update_layout(title= 'Churn Distribution for Internet Service Types')

     # Convert 'Churn' column to boolean (0 for No, 1 for Yes)
      df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})
 
    # Group data by Billing Preference and calculate churn
      billing_churn = df.groupby('PaperlessBilling')['Churn'].sum().reset_index()
 
    # Plot using Plotly Express
      bar_fig = px.bar(billing_churn, x='PaperlessBilling', y='Churn',
                labels={'PaperlessBilling': 'Billing Preference', 'Churn': 'Churn Count'},
                title='Churn Distribution By Billing Preference')
    
 
     # show plotly_chart
      st.plotly_chart(barchart)
      st.plotly_chart(bar_fig)

with col2:
     
     fig = px.histogram(df, x='Contract', color='Churn', barmode='group')
     fig.update_layout(title="Contract Type vs. Churn")

     bar = px.histogram(df, x='PaymentMethod', color='Churn', barmode='group', title='Payment Method vs. Churn')

# Rotate x-axis labels for better readability
     bar.update_xaxes(tickangle=45)


# show plotly figures
     st.plotly_chart(fig)
     st.plotly_chart(bar)

with tab3:
    col1, col2 = st.columns(2)

    with col1:
   
    # Calculate churn rate
     total_customers = len(df)
     churned_customers = df['Churn'].sum()
     churn_rate = churned_customers / total_customers

# Calculate customer retention rate
     retained_customers = total_customers - churned_customers
     retention_rate = retained_customers / total_customers

# Display the results
     
    st.write("Churn Rate:", churn_rate)
    st.write("Customer Retention Rate:", retention_rate)
with col2:
    pass
        # # Calculate average monthly income by department
        # average_income_df = df.groupby('Contract')['MonthlyCharges'].mean().reset_index()

        # colors = {'Month-to-month': 'deepskyblue', 'One year': 'pink', 'Two year': 'skyblue'}

        # print(average_income_df)
        


    