# -*- coding: utf-8 -*-

'''
Created on 10th of March, 2014

@author: David K. Laundav
'''

#===========================================================================
# IMPORTS
#===========================================================================
from scipy import stats
from numpy import arange, poly1d, random
import matplotlib.pyplot as plt
from math import sqrt

#===========================================================================
# DATA
# ----------------------------------
# Notes:
#     This is only example data, and should be substitued with your own
#===========================================================================
x = arange(0,9) 
y = [int(20*random.random()) for i in range(len(x))]

#===========================================================================
# LINEAR REGRESSION
# ----------------------------------
# Notes:
#     alpha = the slope of the curve
#     beta = the point at which the slope intercepts at x = 0
#     r_value = the correlation coefficient
#     p_value = the p-value which the h0 hypothesis is tested against
#         In this case, a p-value of 0.0 would be a 100% match, indicating that the linear regression is perfectly aligned with the data points
#     std_err = the standard deviation
#===========================================================================
alpha, beta, r_value, p_value, std_err = stats.linregress(x, y) # Use scipy to calculate the variables of the least squares fit
polynomial = poly1d([alpha, beta]) # Calculate the polynomial least squares fit as: "y = ax * b"
line = polynomial(x) # Returns an array containing the carry sum of "beta -/+ alpha" for each element in x (+ if the slope is positive, otherwise -)
sose = sqrt(sum((line-y)**2)/len(y)) # Calculate the Sum of Squared Errors

#===========================================================================
# PLOTTING
#===========================================================================
fig = plt.figure()
ax = fig.add_subplot(111)

""" Writing the variables to the plot """
text_string = "Alpha: %f" % (alpha)
text_string += "\nBeta: %f" % (beta)
text_string += "\nCorrelation coefficient: %f" % (r_value)
text_string += "\nP-value: %f" % (p_value)
text_string += "\nStandard deviation: %f" % (std_err)
text_string += "\nSum of squared error: %f" % (sose)
ax.text(0.022, 0.972, text_string, transform=ax.transAxes, verticalalignment='top', bbox=dict(facecolor='none', pad=10), fontsize=8)

""" Plotting the data """
ax.scatter(0, beta, color='red', label='Intercept')
ax.scatter(x, y, color='grey', label='Data')
ax.plot(line, color='blue', label='Linear Regression')
ax.legend(loc=1, fontsize=10)
plt.show()