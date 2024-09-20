# PROJECT PROPOSAL

## Project Title: Real Estate Price Forecasting
![ProfilePic]()  
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author: Sai Teja Gunamoni
- GitHub: https://github.com/SaiTejaGunamoni


# INTRODUCTION
A house is a structure where people can reside. It is simply more than location and square footage. It is often constructed/bought for a family. Most modern homes include designated spaces or rooms where individuals can perform their requirements to live peacefully. The current home has a kitchen, a dining room, sleeping quarters, and a laundry room. These activities are typically carried out in different rooms known as the kitchen, living room, bedrooms, bathroom, and toilet (or lavatory).

Like the features that make up a person, an educated buyer would want to know all aspects that give a house its value. For example, if you're going to sell a home and don't see the price you may expect, it can't be too low or too high. To find a house price, you usually try to find similar properties in your neighborhood and based on gathered data, and you will try to assess your house price.

# Questions to Answer:

Sometimes, estimating the price of a house depends on several aspects, and it's tough to identify and keep track of every angle dynamically. So figuring out a house price using various statistical techniques and machine learning methods can take all underlying patterns into action and be dynamically active to understand the factors affecting the price of a house.

This way can help us evaluate the house prices effectively. We can add various aspects/features which may not seem important to us but may have significant importance on an overall basis.

The problem statement we will discuss here is the prediction of house prices using various machine learning techniques and statistical learning. The objective here is to predict the price as close as possible, not too high, not too low.

The project looks at several questions regarding price of houses in a US neighborhood.

1.	How a condition of a house affects the price of it?
2.	How total rooms, total area, living measures, matters in case of price prediction?

To investigate these parts, statistical and exploratory data analysis is an important part. We must do extensive data analysis to each into a conclusion of data behavior. Then the problem statement will be solved using machine learning regression analysis.

# Data Source and Description:

The dataset is taken from Kaggle.com from source. It is a relational dataset having several input features which belongs to the area of the house, build year, renovation years, condition, total rooms, etc. The output feature is the house price in dollars.

The dataset consists of a total 26,613 number of house price details along with 22 input features and 1(price) output feature.

![Capture](https://user-images.githubusercontent.com/95714100/192626432-13e1d487-d9b9-42de-af24-f458d34429ef.JPG)

All the house data falls between May 2014 to May 2015. All the data belongs to the state of Washington and King County. For such kind of data, machine learning algorithms with explain ability is the best method to approach. There are several models such as Bayesian Model, Linear Models, Bagging, Boosting, Stacking can be used to create models.

# Methodologies:
This project will involve several steps that will utilize various techniques of a data science project:
1.	Data Cleaning and Anomaly Detection:

Such relational data has majority time null values, anomalies, and duplicate entries. Need to analyses the data and clean it at the start.

2.	Exploratory Data Analysis:

Exploratory data analysis includes various statistical analysis, plots, graphs, correlation checks to understand the dataset clearly from all angles. It helps in understanding the data along with draw important insights from it.

3.	Feature Engineering and Feature Selection:

Feature engineering is an important part as to create some important features form existing features. Allows to explore feature selection method to reduce unnecessary columns.

4.	Model Building:

Going to build several models and compare them to understand the behavior of the data on different learning models.

## Machine Learning:
1.	Naive Bayes
2.	Logistic Regression
3.	Bagging and Boosting based models

## Deep Learning:
1.	1D CNN (1D Convolutional Neural Network)
2.	RNN (Recurrent Neural Networks)
3.	Attention 

# Expected Outcome:
The intended outcomes will be factors and features important to build a machine learning regression model on such datasets. The model will help creating business understandings, where to spend, where to focus to increase the house sales with a dynamic pricing.

# Sources:
[1] Palak F, Anand K, Real Estate Price Prediction Using Machine Learning Algorithms, First published: 06 May 2022, https://doi.org/10.1002/9781119792437.ch2

[2] Quang T, Minh N, Hy D, Bo M, Housing Price Prediction via Improved Machine Learning Techniques, 2019 International Conference on Identification, Information and Knowledge in the Internet of Things (IIKI2019)
