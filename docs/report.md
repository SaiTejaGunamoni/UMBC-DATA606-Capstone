# Project Title: Real Estate Price Forecasting
![RealeastePic](./Realestate.jpg)  

- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - Fall 2024 Semester
- **Author**: Sai Teja Gunamoni
- **GitHub**: https://github.com/SaiTejaGunamoni

## Background:

### What is it about?
This project focuses on predicting house prices using machine learning techniques. It involves collecting and cleaning a dataset containing various features related to houses, such as square footage, number of bedrooms, bathrooms, and location. The goal is to develop a model that can accurately estimate the price of a house based on these features.

### Why does it matter?
Accurate house price prediction has several important applications:
- **Real Estate Professionals**: Real estate agents and appraisers can use this model to provide more accurate valuations to clients.
- **Homebuyers and Sellers**: Homeowners can make informed decisions about buying or selling their homes by understanding market trends and potential property values.
- **Financial Institutions**: Banks and mortgage lenders can assess the risk associated with home loans by accurately valuing properties.
- **Urban Planning and Policymakers**: Understanding housing market trends can help policymakers make informed decisions about urban development and housing policies.

### Research Questions:

- **Feature Importance**: Which features have the most significant impact on house prices?
- **Model Performance**: Which machine learning model (e.g., linear regression, decision tree, random forest, gradient boosting) performs best in predicting house prices?
- **Model Interpretability**: How can we interpret the predictions of the model to understand the underlying factors influencing house prices?
- **Generalizability**: How well does the model generalize to other regions or time periods?

## Data
- **Dataset**: King County House Price Data
- **Source**: Kaggle
- **Size**: 5.35MB

**Data Dictionary:**

| Feature Name | Description | Data Type |
|---|---|---|
| id | Unique identifier for each house | Integer |
| date | Date the house was sold | Date |
| price | Price of the house | Numeric |
| bedrooms | Number of bedrooms | Integer |
| bathrooms | Number of bathrooms | Numeric |
| sqft_living | Square footage of the living space | Integer |
| sqft_lot | Square footage of the lot | Integer |
| floors | Number of floors | Numeric |
| waterfront | Whether the house has a waterfront view (0 = no, 1 = yes) | Integer |
| view | Index of view (0-4) | Integer |
| condition | Condition rating (1-5) | Integer |
| grade | Overall grade given to the house | Integer |
| sqft_above | Square footage of house above ground level | Integer |
| sqft_basement | Square footage of the basement | Integer |
| yr_built | Year the house was built | Integer |
| yr_renovated | Year the house was renovated | Integer |
| zipcode | ZIP code | Integer |
| lat | Latitude coordinate | Numeric |
| long | Longitude coordinate | Numeric |
| sqft_living15 | Average square footage of the nearest 15 neighbors | Integer |
| sqft_lot15 | Average square footage of the lot of the nearest 15 neighbors | Integer |

**Data Summary:**
- Size: 21613 rows and 21 columns
- Data Type: Numerical and Categorical
- Missing Values: Minimal or handled during preprocessing
- Outliers: Identified and treated appropriately

**Target Variable:**

* **price:** The selling price of the house.
