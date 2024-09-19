# PROJECT PROPOSAL

## Project Title: Predicting Solar Output Using Weather Data
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- Author: Sai Teja Gunamoni
- GitHub: https://github.com/SaiTejaGunamoni

## Overview:

With the global shift towards renewable energy sources, precise solar power generation forecasting has become crucial for effective grid management and energy planning. Our capstone project attempts to address the inherent variability of solar power generation by creating a machine learning model to predict solar energy output using weather data.

With the analysis of historical solar farm data, including hourly power generation readings and associated weather variables like wind speed, cloud cover, temperature, and solar irradiance I'll try to identify critical weather parameters that have a major impact on solar output by using thorough data preprocessing, exploratory data analysis, and feature engineering.

I'll attempt to apply and contrast a variety of machine learning models, such as neural networks, ARIMA, LSTM, and Random Forest, Gradient Boosting, and Linear Regression. Cross-validation techniques will be employed to validate these models after they have been trained on a subset of the data. Metrics like Mean Absolute Error (MAE), Root Mean Square Error (RMSE), and R-squared values are used to assess performance.

## Dataset and Description:

#### Data Source: https://nsrdb.nrel.gov/data-viewer

With the help of weather data, solar output can be predicted using this dataset.  The information on solar output, the weather, the date, and the time was gathered from a variety of sources. Previous weather patterns and data are the foundation for the solar output projections. Utilizing the dataset, one can train a model that forecasts solar output according to meteorological conditions.

Time-series data for the United States and other countries at a 30-minute resolution can be found in the National Solar Radiation Database (NSRDB), a comprehensive collection of meteorological and solar irradiance data. It includes important variables like temperature, wind speed, and other meteorological parameters, as well as surface cells that span an area of about 4 km in size. Examples of these include global horizontal irradiance (GHI), direct normal irradiance (DNI), and diffuse horizontal irradiance (DHI).

## Research Questions
- Can weather data be effectively used to predict solar output?
- Which weather variables have the most significant impact on solar output?
- Which algorithms are the most efficient for weather-derived predictions ?
- What is the optimal machine learning model for predicting solar output based on weather data?

## Variables in dataset:
The dataset contains weather data collected from various sources. The data includes information on solar output, weather, date, and zip code. The predictions are based on a new approach that uses artificial intelligence to learn patterns from the data

WBAN: 
Date: 
Time: 
SkyCondition: 
Visibility: 
Temperature: The temperature at the time of the observation (Column Type: Integer)
DewPoint: The dew point at the time of the observation (Column Type: Integer)
WindSpeed: The wind speed at the time of the observation (Column Type: Integer)
StationPressure: The station pressure at the time of the observation (Column Type: Integer)
Altimeter: The altimeter at the time of the observation (Column Type: Integer)


| **Column Name**                        | **Details**                                                                    |
|----------------------------------------|------------------------------------------------------------------------------------|
| `WBAN`                                 | Weather Bureau Air Force Navy (Column Type: Integer)                               |
| `Date`                                 | The date of the observation (Column Type: Date)                                    |
| `Time`                                 | The time of the observation (Column Type: Time)                                    |
| `SkyCondition`                         | The visibility at the time of the observation (Column Type: Integer)               |
| `Visibility`                           | The temperature at the time of the observation (Column Type: Integer)              |
| `Temperature`                          | The temperature at the time of the observation (Column Type: Integer)              |
| `DewPoint`                             | The dew point at the time of the observation (Column Type: Integer)                |
| `WindSpeed`                            | The wind speed at the time of the observation (Column Type: Integer)               |
| `StationPressure`                      | The station pressure at the time of the observation (Column Type: Integer)         |
| `Altimeter`                            | The altimeter at the time of the observation (Column Type: Integer                 |

## Methodology 
#### Data Preprocessing:
- Handle missing values (e.g., imputation).
- Normalize or standardize features for consistency.
- Explore correlations between variables to identify significant features.
- Model Selection:
- Consider various machine learning algorithms:
- Linear Regression
- Random Forest
- Support Vector Machines (SVM)
- Neural Networks
- Evaluate performance metrics (e.g., mean squared error, R-squared) to select the optimal model.
#### Model Training:
- Split the dataset into training and testing sets.
- Train the chosen model using the training data.
#### Model Evaluation:
- Evaluate the model's performance on the testing set.
- Fine-tune hyperparameters as needed.

## Expected Outcome:

This project offers a data-driven method for predicting solar output, which advances the rapidly expanding field of renewable energy forecasting. The developed model may enhance the integration of solar power into the electrical grid and optimize energy distribution strategies. It is useful for solar plant operators, grid managers, and energy traders.

## References:

- http://www.ncdc.noaa.gov/
- https://nsrdb.nrel.gov/data-viewer
- Oeda S, Kurimoto I and Ichimura T 2006 Time series data classification using recurrent neural network with ensemble learning Lecture Notes Comput. Sci. 4253 742-8
