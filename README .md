<a name="readme-top"></a>

<div align="center">
  <h1><b>Churn Prediction WebApp</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Churn Prediction Streamlit WebApp ]
  - [🛠 Built With ](#-built-with-Python)
    - [Tech Stack ](#tech-stack-)
  - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors ](#-authors-)
  - [🔭 Future Features ](#-future-features-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Churn WebApp <a name="about-project"></a>

**Churn WebApp** is a data application that allows users to interact with a machine learning model, view data visualizations on the data and see the values of their input saved for future use.

Features

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
13.**StreamingTV**: Whether the customer has streaming TV or not (Yes, No, No internet service)
14. **StreamingMovies**: Whether the customer has streaming movies or not (Yes, No, No Internet service)
15. **PaperlessBilling**: Whether the customer has paperless billing or not (Yes, No)
16. **Payment Method**: The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))
17. **MonthlyCharges**: The amount charged to the customer monthly
18. **TotalCharges**: The total amount charged to the customer
19. **Churn**: Whether the customer churned or not (Yes or No)
20. **SeniorCitizen**: Whether a customer is a senior citizen or not

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">Streamlit</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="">Microsoft SQL Server</a></li>
  </ul>
</details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<details>
<summary>Model</summary>
  <ul>
    <li><a href="">Sklearn</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Features <a name="key-features"></a>

- **A data application that presents visualizations on both the exploratory data and the KPIs**
- **A predicitons page to predict by specifying the model you want to use**
- **View proprietory data loaded in real-time form the remote server**
- **Predictions are save for further analysis in the future and users can view the history of their prediction input values**


<p align="right">(<a href="#readme-top">back to top</a>)</p>

![image](https://raw.githubusercontent.com/CodeGraceWanjiku/Churn_Prediction-StreamlitWebApp/c225cac302fe431e7e6b0ec622b9cfc70d96ffba/assets/Screenshot%202024-03-11%20at%2020.45.54.png)

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python
- Streamlit

### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/CodeGraceWanjiku/Churn_Prediction-StreamlitWebApp
```

Change into the cloned repository

```sh
  cd churn_prediction_StreamlitWebApp
  
```

Create a virtual environment

```sh

python -m venv virtual_env

```

Activate the virtual environment

```sh
    virtual_env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


### Usage

To run the project, execute the following command:


```sh
    streamlit run 1_🏠_Home.py

```

- A webpage opens up to view the app
- Login to the app with `username=shix` and `Wanjiku123`
- Finally test a prediction by clicking on the predicitons page
- **Note**: Users may not be able to access the Data page as the secrets file is not checked into git

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Grace Wanjiku-Wanjiru**

- GitHub: [GitHub Profile](https://github.com/CodeGraceWanjiku)
- Twitter: [Twitter Handle](https://twitter.com/shixay)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/grace-w-wanjiru/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- PAGE SCREENSHOTS-->

## 🔭 Page Screenshots <a name="Page-Screenshots"></a>

- **login**
![image](https://raw.githubusercontent.com/CodeGraceWanjiku/Churn_Prediction-StreamlitWebApp/main/assets/Screenshot%202024-03-11%20at%2020.45.00.png)
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Live URL <a name="support"></a>

This is the live url to the webApp

<p align="left">(<a href="https://churn-prediction-streamlitwebapp.onrender.com/">Live link</a>)</p>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank all the free available resource made available online

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


