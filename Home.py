import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="",
    layout='centered',
)

st.title("Welcome to Home Page")

st.caption("🧾Description:")
st.markdown(
''' Income inequality - when income is distributed in an uneven manner among a population, is a growing problem in developing nations across the world. 
    With the rapid rise of AI and worker automation, this problem could continue to grow if steps are not taken to address the issue. 
    This solution can potentially reduce the cost and improve the accuracy of monitoring key population indicators such as income level in between census years. 
    This information will help policymakers to better manage and avoid income inequality globally
'''
)
st.caption("🧭Problem Statement:")
st.markdown(
    '''
The central problem in this project is binary classification, specifically predicting whether an individual's income is above or below a certain predefined threshold. 
The target feature for this classification task is "income_above_limit." 
The project aims to build a machine learning model that can make these income predictions effectively. 
The evaluation metric chosen for assessing the model's performance is the F1-score, which is a balanced measure that takes both precision and recall into account. 
Achieving a high F1-score indicates that the model can make accurate predictions while minimizing false positives and false negatives.
'''
)

st.sidebar.markdown("""
# About
## Approach:
To build the Random Forest Classifier Model for this project, 
## I Typically followed these steps:
### Data Collection: 
Gather a dataset with income-related features and the binary target variable, "income_above_limit"/"Income_below_limit"
### Data Preprocessing: 
Clean, handle missing values, encode categorical variables, and scale numerical features.
### Feature Engineering: 
Select and create relevant features and consider feature selection.
### Model Building: 
Train a Random Forest Classifier, optimize hyperparameters.
### Model Evaluation: 
Assess with F1-score and other metrics like accuracy, precision, recall, and ROC AUC.
### Model Deployment: 
Deploy the model for real-world predictions if it performs well.
""")
