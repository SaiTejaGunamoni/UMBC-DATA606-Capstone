# Streamlit application for Visualizing Inner City House Price Data with Price Range Filter

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
@st.cache_data
def load_data():
    return pd.read_excel("innercity_house_price_details.xlsx")

data = load_data()

# App title
st.title("Inner City House Price Visualizations")

# Price Range Slider
st.sidebar.header("Filter by Price Range")
min_price, max_price = int(data['price'].min()), int(data['price'].max())
price_range = st.sidebar.slider("Select Price Range", min_price, max_price, (min_price, max_price))

# Filter data based on price range
filtered_data = data[(data['price'] >= price_range[0]) & (data['price'] <= price_range[1])]

# Display selected price range
st.write(f"Showing houses with prices between {price_range[0]} and {price_range[1]}")

# 1. Price Distribution Histogram
st.header("Price Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_data['price'], kde=True, ax=ax)
ax.set_title("Distribution of House Prices")
ax.set_xlabel("Price")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# 2. Scatter Plot of Price vs. Living Area
st.header("Price vs Living Area")
fig, ax = plt.subplots()
sns.scatterplot(x='living_measure', y='price', data=filtered_data, ax=ax)
ax.set_title("House Price vs Living Area")
ax.set_xlabel("Living Area (sq ft)")
ax.set_ylabel("Price")
st.pyplot(fig)

# 3. Correlation Heatmap
st.header("Correlation Heatmap of Features")
numeric_data = filtered_data.select_dtypes(include=['float64', 'int64'])  # Only numeric columns for correlation
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Feature Correlations")
st.pyplot(fig)

# 4. Scatter Plot of Price vs. Lot Size
st.header("Price vs Lot Size")
fig, ax = plt.subplots()
sns.scatterplot(x='lot_measure', y='price', data=filtered_data, ax=ax)
ax.set_title("House Price vs Lot Size")
ax.set_xlabel("Lot Size (sq ft)")
ax.set_ylabel("Price")
st.pyplot(fig)

# 5. Box Plot of Price by Number of Bedrooms
st.header("Price by Number of Bedrooms")
fig, ax = plt.subplots()
sns.boxplot(x='room_bed', y='price', data=filtered_data, ax=ax)
ax.set_title("House Price by Number of Bedrooms")
ax.set_xlabel("Number of Bedrooms")
ax.set_ylabel("Price")
st.pyplot(fig)

# 6. Box Plot of Price by Condition
st.header("Price by Condition")
fig, ax = plt.subplots()
sns.boxplot(x='condition', y='price', data=filtered_data, ax=ax)
ax.set_title("House Price by Condition")
ax.set_xlabel("Condition")
ax.set_ylabel("Price")
st.pyplot(fig)

# Run the application with `streamlit run app.py`
