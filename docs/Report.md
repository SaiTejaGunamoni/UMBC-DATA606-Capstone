# House Price Prediction Analysis
*An analysis of the amount of the price being tagged to a US neighborhood houses.*
# DATA_606 Capstone in Data Science - Chaojie Wang
## By Sathyam Chanumolu

![img2](https://user-images.githubusercontent.com/95714100/207893681-d58e83a9-60b6-4110-a0b4-e6331a6917cc.jpg)


## INTRODUCTION

A house is a structure where people can reside. It is simply more than location and square footage. It is often constructed or bought for a family. Most modern homes include designated spaces or rooms where individuals can perform their requirements to live peacefully. The current home has a kitchen, a dining room, sleeping quarters, and a laundry room. These activities are typically carried out in different rooms known as the kitchen, living room, bedrooms, bathroom, and toilet (or lavatory).

Like the features that make up a person, an educated buyer would want to know all aspects that give a house its value. For example, if you're going to sell a home and don't see the price you may expect, it can't be too low or too high. To find a house price, you usually try to find similar properties in your neighborhood and based on gathered data, and you will try to assess your house price.

## Motivation

* A house is a building in which people can live. It is simply more than a matter of location and square footage.

* It is frequently built or purchased for a family. Most modern homes include designated spaces or rooms where individuals can perform their needs to live peacefully.

* There is a kitchen, a dining room, sleeping quarters, and a laundry room in the current residence. 

* These activities are usually performed in various rooms such as the kitchen, living room, bedrooms, bathroom, and toilet.

## Problem Statement

* Simply said, a house's worth goes beyond its location and size.

* Like the characteristics that make up a person, a knowledgeable individual would want to know all the factors that contribute to a home's worth.

* For instance, if you want to sell a property but are unsure of the price you could receive, it must not be too low or too expensive. You often look for comparable homes in your community to determine your home's price, and then you try to estimate it using the information you have acquired.

* Determination of house price not only influenced the buyer, or seller, but also impacts a lot to the loan providers such as banks and loan institution. Determining correct price will make sure it won’t go into NPA (Non-Performing Asset).

* The objective here is to predict the correct price/close price of the house by looking into the factors given in the dataset.

## Questions to Answer

Sometimes, estimating the price of a house depends on several aspects, and it's tough to identify and keep track of every angle dynamically. So, figuring out a house price using various statistical techniques and machine learning methods can take all underlying patterns into action and be dynamically active to understand the factors affecting the price of a house.

This way can help us evaluate the house prices effectively. We can add various aspects/features which may not seem important to us but may have significant importance on an overall basis.

The problem statement we will discuss here is the prediction of house prices using various machine learning techniques and statistical learning. The objective here is to predict the price as close as possible, not too high, not too low.

The project looks at several questions regarding price of houses in a US neighborhood.

1. How a condition of a house affects the price of it?
2. How total rooms, total area, living measures, matters in case of price prediction?

To investigate these parts, statistical and exploratory data analysis is an important part. We must do extensive data analysis to each into a conclusion of data behavior. Then the problem statement will be solved using machine learning regression analysis.

## Data Collection

* All the house data falls between May 2014 to May 2015. 

* All the data belongs to the state of Washington and King County.

* The dataset was obtained from Kaggle.com via the source <provide source>. It is a relational dataset with several input features related to the house's area, build year, renovation years, condition, total rooms, and so on.

* The output feature is the house price in dollars.

* The dataset consists of a total 21,613 number of house price details along with 22 input features and 1(price) output feature.
  
* For such kind of data, machine learning algorithms with explain ability is the best method to approach.

## Data Cleaning

* Dataset has 21613 rows and 22 input columns, along with 1 output column which is price.

* Columns present in the dataset indicates the house quality, condition, year of building, area, address etc.

* From initial description of numerical features, we can say that dataset has outliers present in it.

* This is a regression problem with target variable price.

* The house price range is between 75000 and 7700000.

* categorical variable based on the logic of other features relation, class mode.

* As a result, no rows were removed.

  Duplicates:

  * There were no duplicate rows discovered.
  
  Null Values:
  
  * There were no more than 5% null values present in any of the features.
  
  * The price output column is skewed to the right and has a longer tail.

## Exploratory Data Analysis

My project's first stage entails creating a machine-learning model. But before I start modeling, I need to understand the data and how it is represented in the dataset. This is for the output column price itself.
  
  ![image](https://user-images.githubusercontent.com/95714100/207910764-6e8d40b2-170a-4b0b-adb0-e9dfdbae34c7.png)

  Now, we can see that the price column is $100,000. Most of the data is present between 0 and 30K. We can see that most of the data is skew to the right. The skewness cut is 4.0217, and the kurtosis cut is 34.5224.
  
## Central limit theorem
  The central limit theorem states that for large sample sizes, the sample mean will be approximately normally distributed, regardless of the distribution from which we are sampling. Python, statistics, and probability. One of the fundamental principles of probability and statistics is the central limit theorem. so much so that a significant portion of inferential statistical testing is based on it.
  
![image](https://user-images.githubusercontent.com/95714100/207913801-2a982058-eeb4-49bc-ae9c-02c6e9543096.png)

Let's expand the data set to include 10, 20, 30, and eventually 1,000 data points. If we divide ten groups of samples into thirty. The central limit theorem was attempted, but there was no 100% normal distribution.
  
### Normal Distribution:  
  
The standard normal distribution is a type of probability distribution that is symmetric about the average or mean, implying that data near the average or mean occurs more frequently than data far from the average or mean.  
  
  ![image](https://user-images.githubusercontent.com/95714100/207915483-74ea21f3-69df-4bbd-a064-e42cba58cfdb.png)

From above distribution plots of mean values of samples, we can say that CLT doesn't hold true. I experimented with normal distribution by taking logs. I attempted to convert in this.  

## Q-Q Plot(Quantile-Quantile Plot):  
  
When the quantiles of two variables are plotted against each other, the resulting plot is known as a quantile - quantile plot, abbreviated as Q-Q plot. This plot summarizes whether the distributions of two variables are similar or not in terms of location.  
  
![image](https://user-images.githubusercontent.com/95714100/207916273-b5d72c2b-755a-4fbb-8b68-df77512b14c9.png)

Q-Q plot says that the log transformation of price column doesn't follow normality completely. The tail towards both ends is curvy and not in line. If you say that all points are in a straight line, you can only say that this is the normal distribution. When the output is normally distributed in regression, the model performs extremely well.  

## 1. Univariate, Bivariate, and Multivariate Analysis   
  
  ### 1.1 Furnished:
     
   **Univariate Analysis:**

* Furnished column has many of the data without furnished.

* There is a clear distinction, as furnished houses are more expensive than unfurnished houses.

* This model is called Univariate analysis.

  ![image](https://user-images.githubusercontent.com/95714100/207931080-011e2927-a266-49b9-9e02-8596084adf0f.png)

* Furnished column has most of the data without furnished.

* Only 20% of the houses are furnished, while the other 80% are unfurnished.

   **Bivariate Analysis:**
  
* There is a clear segregation, as furnished has higher price as compared to the non-furnished house.

* This histogram is called bivariant analysis. 

* when comparing two things at once. This is known as a bivariant analysis. 
 
  ![image](https://user-images.githubusercontent.com/95714100/207949749-f55cb3ad-42bb-41ca-9b91-807d832c317c.png)

* If you have a furnished home, the prices are slightly higher than the distribution for unfurnished homes. 

* The houses are numbered from zero to one million; this is referred to as bivariant analysis.

  ### 1.2 Waterfront view - Price:
  
    **Univariate Analysis:**
* This is a Univariate analysis. The Pie chart depicts the proportion of waterfront views. Weather the house belonging to coastal feature.

  ![image](https://user-images.githubusercontent.com/95714100/207956072-ba7b6810-6e2e-4b60-8143-c2a7de5f0c37.png)

* Only 1% of the data has waterfront view.

* In the state of Washington and King County 65% of the house has no basement present.

    **Bivariate analysis**  
  
* This histogram is called bivariant analysis. 

* There is a clear segregation, as no waterfront view has higher price as compared to the waterfront view house.

* When comparing two things at once. This is known as a bivariant analysis. 

* If you have a waterfront view home, the prices are slightly higher than the distribution for unfurnished homes. 

* No waterfront view: The houses are numbered from zero to one million; this is referred to as bivariant analysis.
  
![image](https://user-images.githubusercontent.com/95714100/208034271-96ba92b0-429c-4b03-8ec8-78f4ab4d2634.png)
  
* House with waterfront view has higher price.
  
### 1.3 Categorical data box plot with price column:

The salient features are that as the quality of the house improves, so does the price. We do salient features analysis to better understand the data set.
  
![image](https://user-images.githubusercontent.com/95714100/208035135-1c4502dd-271a-4538-9497-d021ff0466d8.png)

There is a relationship between the price column and the overall quality column. Other columns, such as sight, have some collinearity with the price data. In many cases, the number of bathrooms in a home can raise the price. However, the overall condition and number of floors (ceiling) have little impact on the price columns.  
  
### 1.4 ceil and ceil measure
  
A factor plot is a ceil and ceil measure plot. If the line rises, there is correlation between the Ceil and the ceil measure. However, there is no correlation between the ceil and ceil measures.
  
  ![image](https://user-images.githubusercontent.com/95714100/208035403-427d51e3-b353-4ec0-952d-cf25b5b1b66f.png)

## Bivariate and multivariate analysis  
  
  **Basement**

* The tail of the violin plot is long for the house with a basement. Even though most of the house price is the same for both houses with and without a basement.

*	With the latest year the count of house data is also increasing in the dataset.

* There isn't much of a price difference between houses built before and after 2000.
   
  **Price with house renovated**
  
* There is no impact in price to the house renovation.

* Ceil_measure, and lost_measure15 has some correlation present with the output price column.
  
## Zip codes
  
This Zip code contains the Latitude and Longitude. We can determine which locality the dataset is from by using Zip codes. We have a dataset for the US state of Washington and the county of King.
  
![image](https://user-images.githubusercontent.com/95714100/208035726-a3828571-03e0-43a2-be14-35cc6802ef53.png)

![image](https://user-images.githubusercontent.com/95714100/208035825-19366750-ce69-4b93-be9a-156879f0e251.png)
  
Most of the data in the dataset is from Seattle. The density of Seattle is very high, and most of the data belongs to the same city.  
  
![image](https://user-images.githubusercontent.com/95714100/208035970-9fff0291-70ca-49df-87cc-628c65252548.png)
  
Houses in Medina City have higher values. It could be because most of the posh houses will be present. Let's look at the house quality in that city.  
  
## 2. Outlier Analysis  
  
In Outlier Analysis, I examine the data to see if there are any outliers. I'm using the Univariant analysis box plot for this.
  
![image](https://user-images.githubusercontent.com/95714100/208037651-e755a2b7-816f-478d-bb04-2c38993f789b.png)

In box plot analysis we can say that there are outliers present in the dataset for each continuous column.
  
### 2.1 Outlier between living measure and price  
  
* I'm using the DBSCAN method analysis to see if there are any outliers.

* Living measure and price are crucial because they are inextricably linked. We can see the word direct relationship up close.

* If the leveling area is large, we must pay a high rate whether we live in a posh house or not.
  
  ![image](https://user-images.githubusercontent.com/95714100/208037934-19da8fa6-6e27-46e5-9cca-b84f81d25c05.png)

* The five outlier points shown above in the DBSCAN clustering plot.  
  
### 2.2 Outlier analysis between total area and price:
  
* We can see that total area is high and price is also high in outlier detection using DBSCAN clustering.  
  
![image](https://user-images.githubusercontent.com/95714100/208038456-691f71a6-7eec-48b2-990a-baa29fc26f8c.png)
  
* In this box plot, I found four outlier layers and removed them. Because this has a significant impact on this model. Outliers are removed in these cases.

* The house price has not changed.
  
## Correlation  
  
* Price is the column I want to focus on. Potential machine learning features from this heatmap include "living_measure", "quality", "ceil_measure", "living_measure15", "furnished", and so on.

* lot_measure , lot_measure15 and total_area has correlation.
  
![image](https://user-images.githubusercontent.com/95714100/208038827-758597d4-1382-43ee-8444-27e159595973.png)

* Most of the features such as furnished, ceil_measure, quality also correlated with each other and can make the input data redundent.

* Living_measure has the highest correlation with the output which is more than 0.7.  
  
![image](https://user-images.githubusercontent.com/95714100/208038880-8dc7ff3e-e402-455e-916c-d60705df8fa0.png)
  
## Prediction Modelling
  
Below selected models has been used for machine learning modelling for k-best features.  
  
•	K-neightbour regressor

•	Lasso regression

•	Ridge regression

•	Decision tree 

•	Random forest regressor

•	Light GBM
  
## •	K-neightbour regressor
  
The model predicts the elements based on the k neighbors value and distance calculation method (Minkowski, Euclidean, etc.). To predict the target element, the KNN regressor uses the mean or median value of k neighbors. In this post, we'll go over how to use the sklearn KNN regressor model in Python to solve a regression problem.  
  
**Result:**  
  
Fitting 3 folds for each of 21 candidates, totalling 63 fits

The optimal K for the dataset is 6.
  
![image](https://user-images.githubusercontent.com/95714100/208039869-aa541413-704c-4c95-9543-1dbbefca5188.png)

## •	Lasso regression
  
In Python, implement Lasso Regression. To implement Lasso regression in Python, we use the "sklearn.linear_model.Lasso" class. Using this class, we can build a model and use it to make predictions with the necessary train and test data.
  
**Result:**
  
Fitting 3 folds for each of 6 candidates, totalling 18 fits

The optimal alpha for the dataset is 0.001.
  
![image](https://user-images.githubusercontent.com/95714100/208040558-fd938944-f53c-4f1b-a41c-1a25dc8401ee.png)

## •	Ridge regression  
  
Python Ridge Regression (Step-by-Step) Ridge regression is a method for fitting a regression model when the data contains multicollinearity. Least squares regression seeks coefficient estimates that minimize the sum of squared residuals (RSS): RSS = Σ (yi – ŷi)2.
  
**Result:** 

Fitting 3 folds for each of 6 candidates, totalling 18 fits

The optimal alpha for the dataset is 10.

![image](https://user-images.githubusercontent.com/95714100/208040602-ba03408b-0c1f-41c3-8ad1-58e514edf8d1.png)

## •	Decision Tree Regressor 
  
In this article, we'll go over the fundamentals of decision trees in Python. So, let's get this party started. Decision Trees are the most straightforward and widely used supervised machine learning algorithm for making predictions. The decision trees algorithm is applied to both regression and classification problems.  
  
**Result:**  

Fitting 3 folds for each of 120 candidates, totalling 360 fits

train_r2: 0.901268

![image](https://user-images.githubusercontent.com/95714100/208040817-35fc3343-9a0a-4c48-a3e8-c5a98fbd377f.png)
  
## •	Random forest regressor

Random forest is a bagging method, not a boosting method. The trees in random forests run in parallel, which means there is no interaction between these trees while they are being built.  
  
**Result:**
  
Fitting 2 folds for each of 20 candidates, totalling 40 fits

The optimal parameters for the dataset are - n_estimators : 118.

![image](https://user-images.githubusercontent.com/95714100/208041139-e091ff41-710f-48a4-967e-d3e6aa1bbf20.png)

## •	Light GBM  
  
For Binary Classification, Use LightGBM Light gradient boosted machine (LightGBM) is an ensemble method in Python that employs a tree-based learning algorithm. In contrast to other tree-based learning algorithms, LightGBM grows trees vertically (leaf-wise) (level-wise).  
  
**Result:**  
  
Did not meet early stopping. Best iteration is: [1000]	
  
valid_0's mape: 0.13702
  
![image](https://user-images.githubusercontent.com/95714100/208041357-7d92f2a9-172e-4ee3-a835-3f760e2abe6f.png)
  
## Conclusion
  
* I have trained 6 models such as knn, lasso, ridge, decision_tree, random_forest, and lightGBM and we can see that the best performing model is lightGBM.

* The mean absolute percentage error for the model is 0.12 and 0.14 for train and test respectively whereas the r2 scores are 0.93 and 0.87 respectively for train and test.

* I have used monotone to make sure the features which is correlated to the input and has an impact should affect during the model building.

* Linear models such as lasso and ridge are also performing well, but not able to capture the pattern and generating less r2 score. Also, the percentage error is very high as compared to other models.
  
## Reference:

[1] https://simplemaps.com/data/us-zips  
  
[2] https://stackoverflow.com/questions/17778394/list-highest-correlation-pairs-from-a-large-correlation-matrix-in-pandas  
  
[3] Palak F, Anand K, Real Estate Price Prediction Using Machine Learning Algorithms, First published: 06 May 2022, https://doi.org/10.1002/9781119792437.ch2

[4] Quang T, Minh N, Hy D, Bo M, Housing Price Prediction via Improved Machine Learning Techniques, 2019 International Conference on Identification, Information and Knowledge in the Internet of Things (IIKI2019)  
  
  
## Project PPT link:
  https://github.com/DATA-606-FALL-2022/Data606_Sathyam/blob/main/Final%20PPT_House%20Price%20Prediction%20Analysis.pptx
  
## Presentation recording YouTube link:
  https://youtu.be/kJ94LoO4-7k
