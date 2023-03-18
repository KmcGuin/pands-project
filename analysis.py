# analysis.py
# Author: Kealan McGuinness
# Pands Project - instructions:
# 1. Outputs a summary of each variable to a single text file,
# 2. Saves a histogram of each variable to png files, and
# 3. Outputs a scatter plot of each pair of variables.
# 4. Performs any other analysis you think is appropriate

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import metrics 
from pandas.api.types import is_numeric_dtype
import sys

data = pd.read_csv('/Users/kealanmcguinness/Desktop/pands/pands-project/iris.csv')

# print(data) - used to test that it read in the data okay

# data columns are labelled
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'species']
"""
# 1. Outputs a summary of each variable to a single text file
# for each label in the data column, print off the mean, standard deviation, minimum and maximum values. This only works for the numerical columns, not the species column.
for col in data.columns:
    if is_numeric_dtype(data[col]):
        print('%s:' % (col))
        print('\t Mean = %2f' % data[col].mean())
        print('\t Standard deviation = %.2f' % data[col].std())
        print('\t Minimum = %.2f' % data[col].min())
        print('\t Maximum = %.2f' % data[col].max())

# this prints the type of species and the number of times they appear in the data.
print(data['species'].value_counts())

# this prints an overall summary of the entire dataset in one place.
print(data.describe(include='all'))

#this was used to save the output of the above to a text file called summary.txt
# sys.stdout = open('summary.txt', 'w')

"""


# 2. Saves a histogram of each variable to png files
''' 
plt.figure(figsize = (12, 9), dpi = (100.0)) # image size, 12wx9h inches
x = data["sepal length"] # identifies variable

plt.hist(x, bins = 20, color = "green", edgecolor = 'white', label = 'Sepal Length')
plt.title("Sepal Length in cm")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Count")
plt.legend()

plt.savefig('sepallength.png')

plt.show()


plt.figure(figsize = (12, 9), dpi = (100.0)) 
x = data["sepal width"] 

plt.hist(x, bins = 20, color = "blue", edgecolor = 'k', label = 'Sepal width')
plt.title("Sepal width in cm")
plt.xlabel("Sepal width in cm")
plt.ylabel("Count")
plt.legend()
plt.savefig('sepalwidth.png')

plt.show()



plt.figure(figsize = (12, 9), dpi = (100.0)) 
x = data["petal width"] 

plt.hist(x, bins = 20, color = "red", edgecolor = 'white', label = 'Petal width')
plt.title("Petal width in cm")
plt.xlabel("Petal width in cm")
plt.ylabel("Count")
plt.legend()
plt.savefig('petalwidth.png')

plt.show()


plt.figure(figsize = (12, 9), dpi = (100.0)) 
x = data["petal length"] 

plt.hist(x, bins = 20, color = "orange", edgecolor = 'k', label = 'Petal length')
plt.title("Petal length in cm")
plt.xlabel("Petal length in cm")
plt.ylabel("Count")
plt.legend()
plt.savefig('petallength.png')

plt.show()

'''

plt.figure(figsize = (12, 9), dpi = (100.0)) 
x = data["species"] 

plt.hist(x, bins = 5, color = "yellow", edgecolor = 'blue', label = 'Species')
plt.title("species")
plt.xlabel("Type of species")
plt.ylabel("Count")
plt.legend()
plt.savefig('species.png')

plt.show()
