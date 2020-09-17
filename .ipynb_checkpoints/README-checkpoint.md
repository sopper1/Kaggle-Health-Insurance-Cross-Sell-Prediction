# Kaggle Health Insurance Cross Sell Data Preparation and Brief Analysis
#### by Shawn Oppermann

## Repository Contents

Report: <a href=https://github.com/sopper1/Kaggle-Health-Insurance-Cross-Sell-Prediction/blob/master/notebooks/report.ipynb>Technical Notebook </a>

Additional Code: <a href=https://github.com/sopper1/Kaggle-Health-Insurance-Cross-Sell-Prediction/blob/master/notebooks/response_functions.py>Response Graphing Functions </a>

## README Contents

[Data](https://github.com/sopper1/Kaggle-Health-Insurance-Cross-Sell-Prediction#data)

[Analysis and Results](https://github.com/sopper1/Kaggle-Health-Insurance-Cross-Sell-Prediction#analysis-and-results)

[Future Work](https://github.com/sopper1/Kaggle-Health-Insurance-Cross-Sell-Prediction#future-work)

[Project Specifications](https://github.com/sopper1/Kaggle-Health-Insurance-Cross-Sell-Prediction#project-specifications)

## Overview

A Kaggle client that provides health insurance is interested in providing vehicle insurance to the same customers. To this end, the client wants a model to predict whether a health insurance customer would be interested such an offer. Instead of providing a model, this project is focused on preparing the data provided on Kaggle and briefly analyzing customer data to determine which variables most significantly affect the likelyhood of a customer being interested in vehicle insurance.

## Data

The data as available for download at https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction#.

### Data Contents
   * train.csv - dataset that includes whether the customer was interested in vehicle insurance
   * test.csv - dataset for predicting the customer's interest
   * sample_submission.csv - a sample csv that would be submitted to the competition on Kaggle
   
This project will only be concerned with train.csv, which contains 381109 entries with the following data:

![train.png](https://github.com/sopper1/Kaggle-Health-Insurance-Cross-Sell-Prediction/blob/master/images/train_desc.png)

## Analysis and Results

The response rate, or the percent likelyhood of a customer being interestied in vehicle insurance, is essentially the mean of all of the responses in a set.

Since the response rate over the entire train set is 12.25%, even an ideal customer may have a low response rate.

In order to determine the features that most significantly affect the response rate, I compare the response rate over different categories for a given feature. For instance, I compare the response rate of men with the response rate of women. For continuous features, I compare brackets.

![response.png](https://github.com/sopper1/Kaggle-Health-Insurance-Cross-Sell-Prediction/blob/master/images/response_analysis.png)

Many categorical features heavily affect the response rate:
   * If a customer was previously insured, then the response rate is almost 0%
   * For every year the the customer has owned the vehicle up until 2 years, the response rate goes up by about 15%
   * If the customer's vehicle was never damaged, then the reponse rate is near 0%
   
Age is the continuous feature most strongly correlated with response rate. The response rate would peak between age 30 and 45 at about 20%, then falls by about 1% every three years.

In theory, an ideal customer that maximizes response rate was not previously insured, owned their vehicle for more than two years, previously damaged their vehicle, and is between the ages of 30 and 45.

## Future Work

I would like to analyze the data more closely, calculate correlation coefficients, and see how multiple variables intermingle when it comes to response rate. Since there is a train and test set, it would also be interesting to use machine learning to create a model instead.

## Project Specifications

### Publishing
    - Contributor: Shawn Oppermann
    - Start date: 9/16/20

### Usage
    - Language: Python
    - Tools/IDE: Anaconda, Jupyter Notebook
    - Libraries: pandas, matplotlib

