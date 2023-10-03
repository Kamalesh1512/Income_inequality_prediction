import streamlit as st
import numpy as np
import pandas as pd
from zipfile import ZipFile
import joblib

st.set_page_config(
    page_title="Prediction",
    page_icon="",
)
st.title("Income Inequality Prediction 💵")
st.sidebar.markdown("""
## About
This is a web app that predicts the income inequality of a person based on their demographics.
""")
model=joblib.load(r"Models\ML_Model.joblib")
ohe_encoder=joblib.load(r"Models\OHE_enc.joblib")

#['gender', 'education', 'marital_status', 'is_hispanic', 'tax_status','age', 'working_week_per_year', 'total_employed', 'vet_benefit']
#input features unique values

education_opt=[' Bachelors degree(BA AB BS)',' Masters degree(MA MS MEng MEd MSW MBA)',
 ' Associates degree-occup /vocational',' Some college but no degree',' Associates degree-academic program', ' Children', 
' High school graduate',' Prof school degree (MD DDS DVM LLB JD)' ,' 11th grade', ' 9th grade',' 7th and 8th grade', 
' 10th grade' ,' 12th grade no diploma',' Doctorate degree(PhD EdD)',' 5th or 6th grade',' 1st 2nd 3rd or 4th grade', ' Less than 1st grade'] 

marital_status_opt=[' Married-civilian spouse present',' Never married',' Divorced',
' Married-spouse absent',' Widowed',' Separated',' Married-A F spouse present']
is_hispanic_opt=[' All other',' Mexican-American',' Puerto Rican',' Other Spanish',' Central or South American',
    ' Mexican (Mexicano)',' Chicano',' Cuban',' NA',' Do not know']
tax_status_opt=[' Joint both under 65',' Single',' Nonfiler',' Joint one under 65 & one 65+',' Head of household',' Joint both 65+']
    
vet_benefit_opt=["Yes","No","Not interested in sharing"]

with st.form("Predictions"):
    st.subheader("Enter the Information")
    
    
    education=st.selectbox("Education",options=education_opt)
    marital_status=st.selectbox("Marital Status",options=marital_status_opt)
    is_hispanic=st.selectbox("Is Hispanic",options=is_hispanic_opt)
    tax_status=st.selectbox("Tax Status",options=tax_status_opt)
    age=st.number_input("Age")
    gender=st.radio("Gender",[' Male',' Female'])
    working_week_per_year=st.number_input("Working Week Per Year")
    total_employed=st.number_input("Total Employed")
    vet_benefit=st.selectbox("Vet Benefit",options=vet_benefit_opt)
    
    submit = st.form_submit_button("Predict")
if submit:
    if vet_benefit =="Yes":
        vet_benefit=1
    elif vet_benefit =="No":
        vet_benefit=0
    else:
        vet_benefit=2
    encoded=ohe_encoder.transform(np.array([gender, education, marital_status, is_hispanic, tax_status]).reshape(1,-1))
    num_array=np.array([age, working_week_per_year, total_employed, vet_benefit]).reshape(1,-1)
    inp_data=np.concatenate((num_array, encoded),axis=1) 
    pred=model.predict(inp_data)                    
    if pred==1:
        st.title("Your Income is Above Limit")
    else:
        st.title("Your Income is Below Limit")
