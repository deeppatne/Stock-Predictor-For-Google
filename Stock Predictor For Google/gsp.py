# -*- coding: utf-8 -*-
"""gsp.ipynb 

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-RaUtF2Lx0mhc6UuqkpBeybIhUU1FZgw
"""

# Importing required libraries
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Loading data
from google.colab import files # Use to load data on Google Colab
uploaded = files.upload() # Use to load data on Google Colab
df = pd.read_csv('GOOG_30_days.csv')
df.head(7)

#Creating lists for X and Y axis
dates = []
prices = []

# Displaying the  number of rows and columns
df.shape

# Printing the last row
df.tail(1)

# Storing data except the last  row cause we want to make a prediction on that data
df = df.head(len(df)-1) 
df

# New data stored in df
df.shape

# Getting rows from the Date Column
df_dates = df.loc[:, 'Date']
# Getting rows from the Open Column
df_open = df.loc[:, 'Open']

# Independent data - X axis - Dates
for date in df_dates:
  dates.append( [int(date.split('-')[2])])
  
# Dependent data - Y axis - Prices
for open_price in df_open:
  prices.append(float(open_price))

# Printing data stored in dates
print(dates)

def predict_prices(dates, prices, x): #Function to make predictions - taking 3 parameters, x = date on which prediction has to be made
  
  #Creating 3 SVR's
  svr_lin = SVR(kernel='linear', C= 1e3)
  svr_poly= SVR(kernel='poly', C=1e3, degree=2)
  svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)

  #Training the models
  svr_lin.fit(dates,prices)
  svr_poly.fit(dates,prices)
  svr_rbf.fit(dates,prices)

  # Also creating Linear Regression model
  lin_reg = LinearRegression()
  # Training this model
  lin_reg.fit(dates,prices)

  
  # Plotting models on a graph
  plt.scatter(dates, prices, color='black', label='Data')
  plt.plot(dates, svr_rbf.predict(dates), color='blue', label='SVR RBF')
  plt.plot(dates, svr_poly.predict(dates), color='green', label='SVR Poly')
  plt.plot(dates, svr_lin.predict(dates), color='red', label='SVR Linear')
  plt.plot(dates, lin_reg.predict(dates), color='yellow', label='Linear Reg')

  # Naming X axis
  plt.xlabel('Days')

  # Naming Y axis
  plt.ylabel('Price')

  # Graph Title
  plt.title('Regression')
  plt.legend()
  plt.show()
  
  return svr_rbf.predict(x)[0], svr_lin.predict(x)[0],svr_poly.predict(x)[0],lin_reg.predict(x)[0]

#Predict the price of GOOG on day 28
predicted_price = predict_prices(dates, prices, [[28]])
print(predicted_price)
