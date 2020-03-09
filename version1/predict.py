#!/usr/bin/env python
# coding: utf-8

###################################### 
#  Multiple Linear Regression Model  #
###################################### 

# Installations
# !pip install keras
# !pip install tensorflow
# !pip install sklearn --upgrade
# !pip install joblib


##################### 
#  Score the Model  #
#####################
def score_model(array):

    import warnings
    warnings.simplefilter('ignore')

    # Load dependencies
    import os
    import pandas as pd
    import numpy as np
    # import matplotlib.pyplot as plt

    # Set the same starting seed number for numpy.random so the results are reproducible
    from numpy.random import seed
    seed(42)


    #########################
    #  Basic Data Cleaning  #
    #########################

    filepath = os.path.join('static','primary_pivot.csv')
    pivot_df = pd.read_csv(filepath)

    # Specify indicator(s)
    indicators = array

    # Initialize features array
    X = []

    # For each row in the df
    for row in range(len(pivot_df)):
        point = []
        # Append each indicator value to the data point
        for i in range(len(indicators)):
            point.append(pivot_df[indicators[i]][row])
            
        # Append the row to the features array
        X.append(point)

    # Flatten the data into arrays
    X = np.array(X)
    y = np.array(pivot_df["hdi"])
    y = y.reshape(-1, 1)


    ###############################
    #  Data Preprocessing for ML  #
    ###############################

    # Split into Test and Train data
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    # Scale the data
    from sklearn.preprocessing import StandardScaler
    X_scaler = StandardScaler().fit(X_train)
    y_scaler = StandardScaler().fit(y_train)

    # Transform the training and test data
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)
    y_train_scaled = y_scaler.transform(y_train)
    y_test_scaled = y_scaler.transform(y_test)


    ########################
    #  Creating the Model  #
    ########################

    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score

    # Create the model using LinearRegression
    linear = LinearRegression()

    # Train the model
    linear.fit(X_train_scaled, y_train_scaled)

    # Use our model to make predictions
    predictions = linear.predict(X_test_scaled)


    ########################
    #  Score the Model  #
    ########################
    r2 = linear.score(X_test_scaled, y_test_scaled)
    mse = mean_squared_error(y_test_scaled, predictions)

    return linear, X_scaler, y_scaler, r2, mse


##########################
#  Predicting HDI value  #
##########################
def predict_hdi(array, values):
    # Create the model
    linear, X_scaler, y_scaler, _, _ = score_model(array)

    # Scale input to the model
    X_scaled = X_scaler.transform([values])
    y_scaled = linear.predict(X_scaled)

    # Predict HDI
    predicted_y = y_scaler.inverse_transform(y_scaled)
    predicted_HDI = predicted_y[0][0]

    return predicted_HDI
