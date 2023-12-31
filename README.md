# 💵 Income_inequality_prediction - Machine Learning Project

## Overview 
Income inequality - when income is distributed in an uneven manner among a population, is a growing problem in developing nations across the world. 
With the rapid rise of AI and worker automation, this problem could continue to grow if steps are not taken to address the issue. 
This solution can potentially reduce the cost and improve the accuracy of monitoring key population indicators such as income level in between census years. 
This information will help policymakers to better manage and avoid income inequality globally

## Problem Statement
The central problem in this project is binary classification, specifically predicting whether an individual's income is above or below a certain predefined threshold. 
The target feature for this classification task is "income_above_limit." 
The project aims to build a machine learning model that can make these income predictions effectively. 
The evaluation metric chosen for assessing the model's performance is the F1-score, which is a balanced measure that takes both precision and recall into account. 
Achieving a high F1-score indicates that the model can make accurate predictions while minimizing false positives and false negatives.

## Approach - Project Flow:
![image](https://github.com/Kamalesh1512/Income_inequality_prediction/assets/81355463/5442f76c-08b9-4ff0-94da-da311b15c730)

To build a Machine Learning Model - Random Forest Classifier model for this project, I typically followed these steps:
### Data Collection: 
Gathered a dataset containing information about individuals, including features related to income and the binary target variable, "income_above_limit."
Source of data is from The Machine Learning Company. (Confindential not Disclosed)
### Data Preprocessing:
Cleaned and preprocessed the data, which involved handling missing values,and treating imbalanced Data.
### Feature Engineering:
Performed Feature Engineering, Which involved the Encoding Techniques like One hot Encoding for Categorical features, feature selection on numerical and categorical  
columns.
### Model Building:
Trained few Supervised Machine Learning Algorithmns namely Logistic Regression , K-Nearest Neighbors, Decision Tree Classifier.
Based on the F1 scores, the Random Forest Classifier (0.9059) outperformed other algorithms including Logistic Regression (0.8911), K-Nearest Neighbors (0.8884), and Decision Tree Classifier (0.8975).
I made use of Random Forest Classifier as My Final Model and Performed Hyper Parameter tunning , which results in slight improvement from 90.59% to 90.70%.
### Model Evaluation:
Used the F1-score as the primary evaluation metric to assess the model's performance on a test dataset.
Confusion Matrix and ROC Curve is also used to check the Performance of the Model.

### Model deployment:
Model deployed using AWS EC2 cloud service.

## Summary
**Impact:**
The project's impact lies in its potential to provide policymakers and governments with a valuable tool for monitoring and managing income inequality. By accurately predicting individuals' income levels, it can help identify areas where income inequality is most pronounced and where interventions are needed. This information can inform policies and initiatives aimed at reducing income inequality in developing nations, ultimately improving the economic well-being of their populations.

In summary, this project leverages machine learning, specifically a Random Forest Classifier, to predict income levels and address income inequality in developing countries, with the F1-score of 90.70% accuracy as the key evaluation metric to measure model performance.

## webapp url- http://ec2-13-48-45-121.eu-north-1.compute.amazonaws.com:8501/ 
(ec2 instance is stopped, in order to avoid unwanted bills- aws account is free tier.) 
