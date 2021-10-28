# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 23:52:57 2021

@author: Ajai
"""

import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

car = pd.read_csv("accord_sedan.csv")

# print(car)

# Task 1.2
ax=plt.axes() #get the axes
plt.scatter(car.price, car.mileage)
ax.set_xlabel('Price')
ax.set_ylabel('Mileage')
ax.set_title('Price vs Mileage')


# TASK 2
TB = pd.read_csv("TB_burden_countries.csv")

print(TB)

# mean and standard deviation
mean = TB["e_prev_100k"].mean()
stds = TB["e_prev_100k"].std()

tbs = np.random.normal(mean, stds, 1000)

count, bins, ignored = plt.hist(tbs, 100)
plt.plot(bins, 1/(stds * np.sqrt(2 * np.pi)) *
np.exp( - (bins - mean)**2 / (2 * stds**2) ),
linewidth=1.5, color='r')
plt.show()

