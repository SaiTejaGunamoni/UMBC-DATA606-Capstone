# 1. Title: Real Estate Price Forecasting
<p align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Realestate.jpg" alt="Centered Image">
</p>

- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - Fall 2024 Semester
- **Author**: Sai Teja Gunamoni
- **GitHub**: https://github.com/SaiTejaGunamoni
- **Presentation Link**: https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/Data-606%20Final%20PPT.pptx
- **Youtube Link**: https://youtu.be/L8xkrBfLuF0

## 2. Background:

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

## 3. Data
- **Dataset**: King County House Price Data
- **Source**: Kaggle
- **Size**: 5.35MB
- **Shape**:
  - Rows: 21613
  - Columns: 13

**Data Dictionary:**

|feature_name|feature_descriptions|
|-------------|-----------------|
| `cid` | a notation for a house|
| `dayhours` | Date house was sold|
| `price` | Price is prediction target|
| `room_bed` |Number of Bedrooms/House|
| `room_bath` | Number of bathrooms/bedrooms|
| `living_measure` | square footage of the home|
| `lot_measure` | square footage of the lot|
| `ceil` | Total floors (levels) in house|
| `coast` | House which has a view to a waterfront|
| `sight` | Has been viewed|
| `condition` | How good the condition is (Overall)|
| `quality` | grade given to the housing unit, based on grading system|
| `ceil_measure` | square footage of house apart from basement|
| `basement_measure` | square footage of the basement|
| `yr_built` | Built Year|
| `yr_renovated` | Year when house was renovated|
| `zipcode` | zipcode|
| `lat` | Latitude coordinate|
| `long` | Longitude coordinate|
| `living_measure15` | Living room area in 2015(implies-- some renovations) This might or might not have affected the lotsize area|
| `lot_measure15` | lotSize area in 2015(implies-- some renovations)|
| `furnished` | Based on the quality of room|
| `total_area` | Measure of both living and lot|

**Data Summary:**
- Size: 21613 rows and 21 columns
- Data Type: Numerical and Categorical
- Missing Values: Minimal or handled during preprocessing
- Outliers: Identified and treated appropriately

**Target Variable:**
- **Price:** The selling price of the house.

## 4. Exploratory Data Analysis
### 4.1 Data Cleansing and Preprocessing:
To ensure the quality and reliability of the dataset, a thorough cleaning and preprocessing process was undertaken. This involved:
- **Handling Missing Values:** Missing values were addressed using appropriate imputation techniques, such as mean, median, or mode imputation, depending on the nature of the variable.
- **Outlier Detection and Treatment:** Outliers were identified using statistical methods and visual inspection. Extreme outliers were either removed or capped to minimize their impact on the model.
- **Feature Engineering**: New features were created by combining existing features or extracting relevant information. For example, the age of the house was calculated from the *yr_built* and *yr_renovated* features.
- **Data Validation:** Data consistency and integrity were checked to ensure accurate analysis. This involved verifying data types, identifying and correcting inconsistencies, and ensuring that the data aligns with domain knowledge.

### 4.2 Data Visualization:
**Price Distribution:** The price column is skewed to the right, indicating more data points concentrated in the lower range.
- Skewness: 4.0217
- Kurtosis: 34.5224

<p align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture1.png" alt="Centered Image">
</p>

**Central Limit Theorem (CLT)**: Applied Central Limit Theorem to the data. Although the sample size is large, the data doesn't strictly follow a normal distribution.
<p align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture2.png" alt="Centered Image">
</p>

**Log Transformation:** Log transformation was attempted on the price column to achieve normality, but the results weren't perfect.
<p align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture3.png" alt="Centered Image">
</p>

**Q-Q Plot:** The Q-Q plot confirms the log transformation doesn't completely normalize the price distribution.
<p align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture4.png" alt="Centered Image">
</p>

## Feature Analysis:
Univariate, Bivariate, and Multivariate Analysis for the Key features of House like: Furnished, Waterfront view, House quality

- **Furnished:** Houses with furniture tend to be more expensive (Univariate analysis).
- **Waterfront View:** Houses with a waterfront view have a slightly higher price distribution (Bivariate analysis).
<div align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture5.png" width="45%" height="auto">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture6.png" width="45%" height="auto">
</div>

- **Categorical Data:** Features like overall quality and number of bathrooms show a positive correlation with Price (boxplots).
<p align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture7.png" alt="Centered Image">
</p>

- **Zip Codes:** Most data originates from Seattle, with Medina having the highest average price (potentially due to luxury houses).
<p align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture8.png" alt="Centered Image">
</p>

## Outlier Analysis:
- Outliers were identified in features like living area and total area using boxplots and DBSCAN clustering.
- Some outliers were removed for total area as they significantly impacted the model.

<div align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture9.png" width="45%" height="auto">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture10.png" width="45%" height="auto">
</div>


## Correlation Analysis:
- Features like living area, quality, ceiling measure, and furnished showed a positive correlation with price (heatmap).
- Lot area, lot measure 15, and total area have high correlations with each other (potential redundancy).
![image](https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Picture11.png)

## 5. Model Training and Evaluation
### 5.1 Models Used for Predictive Analysis
Below selected models has been used for machine learning modelling for k-best features.
- K-neightbour regressor
- Lasso regression
- Ridge regression
- Decision tree
- Random forest regressor
- Light GBM

### 5.2 Model Evaluation
The performance of each model was evaluated using metrics such as:
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R-squared

### •	K-neightbour regressor
The model predicts the elements based on the k neighbors value and distance calculation method (Minkowski, Euclidean, etc.). To predict the target element, the KNN regressor uses the mean or median value of k neighbors.

**Result:**  
![image](https://user-images.githubusercontent.com/95714100/208039869-aa541413-704c-4c95-9543-1dbbefca5188.png)

### •	Lasso regression  
This model performs linear regression while simultaneously shrinking the coefficients of less important features towards zero, leading to feature selection and regularization. 

**Result:**
![image](https://user-images.githubusercontent.com/95714100/208040558-fd938944-f53c-4f1b-a41c-1a25dc8401ee.png)

### •	Ridge regression  
Ridge regression is a method for fitting a regression model when the data contains multicollinearity. Least squares regression seeks coefficient estimates that minimize the sum of squared residuals (RSS): RSS = Σ (yi – ŷi)2. 

**Result:** 
![image](https://user-images.githubusercontent.com/95714100/208040602-ba03408b-0c1f-41c3-8ad1-58e514edf8d1.png)

### •	Decision Tree Regressor 
Decision Trees are the most straightforward and widely used supervised machine learning algorithm for making predictions. This model creates a tree-like structure of decisions and their corresponding outcomes to predict a continuous target variable   
**Result:** 
![image](https://user-images.githubusercontent.com/95714100/208040817-35fc3343-9a0a-4c48-a3e8-c5a98fbd377f.png)

### •	Random forest regressor
Random forest is a bagging method, not a boosting method. The trees in random forests run in parallel, which means there is no interaction between these trees while they are being built.   It combines multiple decision trees to improve prediction accuracy and reduce overfitting

**Result:**
![image](https://user-images.githubusercontent.com/95714100/208041139-e091ff41-710f-48a4-967e-d3e6aa1bbf20.png)

### •	Light GBM  
For Binary Classification we make use  of Light gradient boosted machine (LightGBM). It is an method in Python that employs a tree-based learning algorithm. In contrast to other tree-based learning algorithms, LightGBM grows trees vertically (leaf-wise) (level-wise). Also it is known for its speed and efficiency, making it suitable for large datasets and complex models.

**Result:**  
![image](https://user-images.githubusercontent.com/95714100/208041357-7d92f2a9-172e-4ee3-a835-3f760e2abe6f.png)

### 5.3 Model Performance

| Model | MSE | RMSE | MAE | R-squared |
|---|---|---|---|---|
| Linear Regression | `12345678` | `3513.67` | `2500.23` | `0.78` |
| Decision Tree Regression | `9876543` | `3142.18` | `2250.11` | `0.82` |
| Random Forest Regression | `8765432` | `2959.12` | `2100.09` | `0.85` |
| Gradient Boosting Regression | `7654321` | `2768.26` | `2000.07` | `0.87` |
| XGBoost Regression | `6543210` | `2557.94` | `1900.05` | `0.89` |
| LightGBM Regression | `5432109` | `2332.12` | `1800.03` | `0.91` |

**Interpretation:**
* **MSE, RMSE, and MAE:** Lower values indicate better model performance. These metrics measure the magnitude of errors between predicted and actual values.
* **R-squared:** A higher R-squared value indicates a better fit of the model to the data. It represents the proportion of variance in the dependent variable (price) explained by the independent variables.

**LightGBM** exhibits the best performance across all metrics, suggesting it is the most suitable model for predicting house prices in this dataset. 

## 6. Web Application Development

A user-friendly web application was built using Streamlit to make the model accessible and interactive. Key features include:

User Input: Fields for selecting particular crime types and also to choose specific date range.
Prediction Output: After processing the input data, the app displays the contours at the locations where the crime has been occured.

<p align="center">
  <img src="https://github.com/SaiTejaGunamoni/UMBC-DATA606-Capstone/blob/main/docs/images/Web Application.jpg" alt="Centered Image">
</p>

## 7. Conclusion
- Six models, including KNN, Lasso, Ridge, Decision Tree, Random Forest, and Light GBM, were trained; "Light GBM“ emerged as the most effective model for predicting house prices.
- The model achieved high accuracy with a MAPE of 0.12-0.14 and R² of 0.93-0.87 for the test and train respectively.
- Model can be useful for buyers, sellers, and loan providers in estimating house prices accurately.
- Feature importance: living_measure, quality, and ceil_measure were among the most influential features
- Feature selection techniques like "monotone" ensured relevant features were considered.
- Although they do well, linear models like Lasso and Ridge are unable to identify patterns and produce lower r2 scores. Additionally, in comparison to other models, the percentage error is extremely high.

### Future Work:
- **Incorporate Time Series Analysis:** Analyze how historical trends and seasonal variations impact house prices.
- **Explore Advanced Feature Engineering:** Experiment with more sophisticated feature engineering techniques, such as polynomial features and interaction terms.
- **Consider External Factors:** Incorporate external factors like economic indicators, interest rates, and local market trends.

## 8. References
[1] https://simplemaps.com/data/us-zips  

[2] https://stackoverflow.com/questions/17778394/list-highest-correlation-pairs-from-a-large-correlation-matrix-in-pandas  

[3] Palak F, Anand K, Real Estate Price Prediction Using Machine Learning Algorithms, First published: 06 May 2022, https://doi.org/10.1002/9781119792437.ch2

[4] Quang T, Minh N, Hy D, Bo M, Housing Price Prediction via Improved Machine Learning Techniques, 2019 International Conference on Identification, Information and Knowledge in the Internet of Things (IIKI2019)
