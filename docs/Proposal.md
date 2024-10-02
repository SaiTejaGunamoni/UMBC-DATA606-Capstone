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

Data Source: Kaggle.com (specify dataset name)

Data Description:

Type: Relational dataset
Size: 26,613 rows (observations) and 23 columns (features)
Time Period: May 2014 - May 2015
Location: Washington State, King County
Features: House characteristics (area, build year, condition, rooms)
Target Variable: House price (USD)

  
## Exploratory Data Analysis (EDA):
- Data Cleaning: Handle missing values, outliers, and inconsistencies.
- Data Exploration: Analyze summary statistics, feature distributions, and correlations between features and the target variable.
- Data Visualization: Create informative visualizations (histograms, boxplots, scatter plots) to understand data patterns.
- Feature Engineering: Create potentially relevant features (e.g., age of house, neighborhood indicators) from existing data.
- Feature Selection: Identify the most important features for price prediction using techniques like correlation analysis or feature importance scores.

## Model Training: 
### Machine Learning Models:
- Linear Regression: Baseline model for understanding linear relationships with the target variable.
- Decision Trees, Random Forests, Gradient Boosting: Ensemble methods to capture non-linearity and feature interactions.
- Deep Learning Models: 1D CNN or RNN for incorporating sequential information (e.g., location data).

### Model Training and Evaluation:
Split the data into training and testing sets (e.g., 80/20 split).
Train each model on the training set.
Evaluate model performance using metrics like mean squared error (MSE) and R-squared on the testing set.
Compare and select the best-performing model based on evaluation metrics.

### Hyperparameter Tuning: 
Optimize hyperparameters of the chosen model(s) to improve performance.


# Expected Outcome:
The intended outcomes will be factors and features important to build a machine learning regression model on such datasets. The model will help creating business understandings, where to spend, where to focus to increase the house sales with a dynamic pricing.

# Sources:
[1] Palak F, Anand K, Real Estate Price Prediction Using Machine Learning Algorithms, First published: 06 May 2022, https://doi.org/10.1002/9781119792437.ch2

[2] Quang T, Minh N, Hy D, Bo M, Housing Price Prediction via Improved Machine Learning Techniques, 2019 International Conference on Identification, Information and Knowledge in the Internet of Things (IIKI2019)
