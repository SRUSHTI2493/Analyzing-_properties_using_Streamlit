# Modules:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ... (your setup and styling code)

# loading the data:
BR_real_estate_appreciation = pd.read_csv('D:/BR_real_estate_appreciation_Q1_2023.csv')
# rounding the appreciation column to two decimal places:
BR_real_estate_appreciation['Annual_appreciation'] = round(BR_real_estate_appreciation['Annual_appreciation'], 2) * 100

# Widgets:
cities = sorted(list(BR_real_estate_appreciation['Location'].unique()))
your_city = st.selectbox(
    '🌎 Select a city',
    cities
)

# Selecting features and target variable
X = BR_real_estate_appreciation[['Annual_appreciation']]  # Replace 'YourNumericFeature' with the actual column name
y = BR_real_estate_appreciation['BRL_per_squared_meter']  # Replace 'AnotherNumericFeature' with the actual column name

# Ensure you have enough samples for splitting
if len(BR_real_estate_appreciation) > 1:
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Display regression results
    st.write(f'Mean Squared Error: {mse:.2f}')
    st.write(f'R-squared: {r2:.2f}')

    # Optional: Plot the regression line
    plt.figure(figsize=(6, 4))
    plt.scatter(X_test, y_test, color='black', label='Actual values')
    plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Regression line')
    plt.xlabel('Annual_appreciation')
    plt.ylabel('BRL_per_squared_meter')
    plt.legend()
    st.pyplot(plt)
else:
    st.write("Not enough samples for splitting. Please check your dataset.")
