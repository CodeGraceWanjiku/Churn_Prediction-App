import streamlit as st

feature_descriptions = """

1. **gender**: gender of employee
2. **churn**: Employee churn status
3. **contract**: contract type
4. **tenure**: what is their distance from hime
5. **dependents**: Yes or No
6. **Phone Service**: Whether the customer has a phone service or not (Yes, No)
7. **Multiple Lines**: Whether the customer has multiple lines or not
8. **Internet Service**: Customer's internet service provider (DSL, Fiber Optic, No)
9. **OnlineSecurity**: Whether the customer has online security or not (Yes, No, No Internet)
10. **OnlineBackup**: Whether the customer has online backup or not (Yes, No, No Internet
11. **DeviceProtection**: Whether the customer has device protection or not (Yes, No, No internet service)
12. **Techsupport**: Whether the customer has tech support or not (Yes, No, No internet)
13. **StreamingTV **: Whether the customer has streaming TV or not (Yes, No, No internet service)
14. **StreamingMovies **: Whether the customer has streaming movies or not (Yes, No, No Internet service)
15. **PaperlessBilling **: Whether the customer has paperless billing or not (Yes, No)
16. **Payment Method **: The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))
17. **MonthlyCharges **: The amount charged to the customer monthly
18. **TotalCharges **: The total amount charged to the customer
19. **Churn **: Whether the customer churned or not (Yes or No)
20. **SeniorCitizen **: Whether a customer is a senior citizen or not

"""

column_1 = """
### Streamlit churn prediction webApp
Streamlit churn prediction webApp is a Machine Learning application that predicts the likelihood of an employee to leave the company based on various demographic and job-related factors.

### Key Features
- **Data:** Vodafone's Data(A Telecommunications Company.
- **Dashboard:** Explore interactive data visualizations for insights.
- **Prediction:** Instantly see predictions for employee churn.
- **History:** See past predictions made.

### User Benefits
- **Data-driven Decisions:** Make informed decisions backed by data analytics.
- **Easy Machine Learning:** Utilize powerful machine learning algorithms effortlessly.

"""

column_2 = """
### Machine Learning Integration
- **Model Selection:** Choose between two advanced models for accurate predictions.
- **Seamless Integration:** Integrate predictions into your workflow with a user-friendly interface.
- **Probability Estimates:** Gain insights into the likelihood of predicted outcomes.

### Let's Collaborate?
For collaborations contact me at [wanjiku.grace9@gmail.com](mailto:wanjiku.grace9@gmail.com).
"""


#Build command
# mkdir .streamlit; cp /etc/secrets/secrets.toml ./.streamlit/; pip install --upgrade pip && pip install -r requirements.txt