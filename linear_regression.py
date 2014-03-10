from scipy import stats
from numpy import arange, poly1d, random
import matplotlib.pyplot as plt
from math import sqrt

""" Data """
x = arange(0,9) 
y = [int(20*random.random()) for i in range(len(x))]

""" Linear Regression """
alpha, beta, r_value, p_value, std_err = stats.linregress(x, y) # Use scipy to calculate the variables of the least squares fit
polynomial = poly1d([alpha, beta]) # Calculate the polynomial least squares fit as: "y = ax * b"
line = polynomial(x) # Returns an array containing the carry sum of "beta -/+ alpha" for each element in x
sose = sqrt(sum((line-y)**2)/len(y)) # Calculate the Sum of Squared Errors

""" Wriring the variables to the plot """
text_string = "Alpha: %f" % (alpha)
text_string += "\nBeta: %f" % (beta)
text_string += "\nCorrelation coefficient: %f" % (r_value)
text_string += "\nP-value: %f" % (p_value)
text_string += "\nStandard deviation: %f" % (std_err)
text_string += "\nSum of squared error: %f" % (sose)

""" Plotting """
fig = plt.figure()
ax = fig.add_subplot(111)
ax.text(0.022, 0.972, text_string, transform=ax.transAxes, verticalalignment='top', bbox=dict(facecolor='none', pad=10), fontsize=8)
ax.scatter(0, beta, color='red')
ax.scatter(x, y, color='grey')
ax.plot(line)
plt.show()