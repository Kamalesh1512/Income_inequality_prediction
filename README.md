# Income_inequality_prediction

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

## Approach - Model Building:
To build a Machine Learning Model - Random Forest Classifier model for this project, I typically followed these steps:

1. **Data Collection:** Gathered a dataset containing information about individuals, including features related to income and the binary target variable, "income_above_limit."

2. **Data Preprocessing:** Cleaned and preprocessed the data, which involved handling missing values, encoding categorical variables, and treating imbalanced Data.

3. **Feature Engineering:** Select relevant features,and performed feature selection if certain attributes are less informative.

4. **Model Building:** Train a Random Forest Classifier using the preprocessed dataset. Tune hyperparameters like the number of trees in the forest, maximum depth of trees, etc., to optimize model performance.

5. **Model Evaluation:** Use the F1-score as the primary evaluation metric to assess the model's performance on a validation or test dataset. 

## Model deployment:

**Impact:**
The project's impact lies in its potential to provide policymakers and governments with a valuable tool for monitoring and managing income inequality. By accurately predicting individuals' income levels, it can help identify areas where income inequality is most pronounced and where interventions are needed. This information can inform policies and initiatives aimed at reducing income inequality in developing nations, ultimately improving the economic well-being of their populations.

In summary, this project leverages machine learning, specifically a Random Forest Classifier, to predict income levels and address income inequality in developing countries, with the F1-score of 96% accuracy as the key evaluation metric to measure model performance.
