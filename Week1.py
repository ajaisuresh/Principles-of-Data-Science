# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:52:37 2021

@author: Ajai
"""

# PART 1
# Question 1
num_rows = 0 # nubmer of rows = 0
for row in open("TB.csv"): # for every row in the CSV file
    num_rows += 1 # add number of rows by 1 

print("Number of rows =", num_rows) # print the number of rows



# Question 2
import csv
import sys

opened = open('TB.csv')
    
    
with open('tb.csv', newline = '') as opened:
    reader = csv.reader(opened)
    next(reader)
    # r1 = [float(row[1]) for row in reader]
    # avg1 = round(sum(r1) / len(r1),2)
    # r2 = [float(row[2]) for row in reader]
    # avg2 = round(sum(r2) / len(r2),2)
    r3 = [float(row[3]) for row in reader]
    avg3 = round(sum(r3) / len(r3),2)

    try:
        avg3 = round(sum(r3) / len(r3),2)
    except ZeroDivisionError:
        avg3
    print("")
    print("The average for the 4th column =", avg3)


# Question 3 
with open('tb.csv', newline = '') as opened:
    reader = csv.reader(opened)
    next(reader)
    for row in reader:
        if row[5] == '1990':
            r5 = [float(row[5]) for row in reader]
            avg5 = round(sum(r5) / len(r5),2)
    try:
        avg5 = round(sum(r5) / len(r5),2)
    except ZeroDivisionError:
        avg5

    print("")
    print(avg5)
    print("")
    
with open('tb.csv', newline = '') as opened:
    reader = csv.reader(opened)
    next(reader)
    for row in reader:
        if row[5] == '2011':
            r5 = [float(row[5]) for row in reader]
            avg5 = round(sum(r5) / len(r5),2)
    try:
        avg5 = round(sum(r5) / len(r5),2)
    except ZeroDivisionError:
        avg5

    print("")
    print(avg5)
    print("")
    
    # I am pretty sure I have done this question wrong, and I am confused.
    # From what I see the average for the both are same, which I think is wrong. 
    
    # Part 2
    # Question 1
    import numpy as np
    import matplotlib.pyplot as plt
    
    array_a = np.arange(5,16)
    print(array_a)
    
    # Question 2
    array_b = np.linspace(0,23,7)
    print("")
    print(array_b)
    
    # Question 3
    array_c = np.random.uniform(-1,1, size = 10)
    print("")
    print(array_c)
    
    # Question 4
    plt.hist(array_c)
    plt.show()
    
    # Question 5
    array_d = np.random.normal(size = 10)
    array_e = np.random.normal(size = 10)
    print("")
    print(array_d)
    print("")
    print(array_e)
    
    distance = np.sum(np.square(array_d-array_e))
    print("")
    print("The Euclidean distance between the arrays is", distance)