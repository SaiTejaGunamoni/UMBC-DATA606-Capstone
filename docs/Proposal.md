# PROJECT PROPOSAL

## Project Title: Real Estate Price Forecasting
![ProfilePic](./Realestate.jpg)  
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author: Sai Teja Gunamoni
- GitHub: https://github.com/SaiTejaGunamoni

# INTRODUCTION
Real estate is a complex market where numerous factors influence property value. Accurately predicting house prices is crucial for both buyers and sellers.

# Research Questions:
- How can machine learning and statistical techniques be used to predict house prices accurately?
- Which factors have the most significant impact on house prices?
- Can building a model help us understand business factors like pricing strategies?

# Data Source and Description:
Source: Kaggle

#### Data Description:
- Type: Relational dataset
- Size: 26,613 rows and 23 columns
- Time Period: 1 year
- Location: Washington, King County
- Features: House characteristics (area, build year, condition, rooms etc)
- Target Variable: House price

## Exploratory Data Analysis (EDA):
- Data Cleaning: Handle missing values, outliers, and inconsistencies.
- Data Exploration: Analyze summary statistics, feature distributions, and correlations between features and the target variable.
- Data Visualization: Create informative visualizations to understand data patterns.
- Feature Engineering: Create potentially relevant features from existing data.
- Feature Selection: Identify the most important features for price prediction using techniques like correlation analysis or feature importance scores.

## Model Training: 
### Machine Learning Models:
- Linear Regression: Baseline model for understanding linear relationships with the target variable.
- Decision Trees, Random Forests, Gradient Boosting: Ensemble methods to capture non-linearity and feature interactions.
- Deep Learning Models: 1D CNN or RNN for incorporating sequential information.

### Model Training and Evaluation:
- Split the data into training and testing sets.
- Train each model on the training set.
- Evaluate model performance using metrics like mean squared error (MSE) and R-squared on the testing set.
- Compare and select the best-performing model based on evaluation metrics.

### Hyperparameter Tuning: 
Optimize hyperparameters of the chosen models to improve performance.

# Expected Outcome:
The results should be able to reveal the most crucial characteristics impacting home value as well as the accuracy of the best model and also insights into commercial elements like pricing policies.

# References:
[1] Quang T, Minh N, Hy D, Bo M, Housing Price Prediction via Improved Machine Learning Techniques, 2019 International Conference on Identification, Information and Knowledge in the Internet of Things (IIKI2019)
[2] Bhagat , N. , Mohokar , A. , and Mane , S. , House price forecasting using data mining . Int. J. Comput. Appl. 152 ( 2 ), 23 – 26 , 2016 .
[3] Palak F, Anand K, Real Estate Price Prediction Using Machine Learning Algorithms, First published: 06 May 2022, https://doi.org/10.1002/9781119792437.ch2
