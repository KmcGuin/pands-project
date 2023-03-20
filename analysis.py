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
from sklearn.datasets import load_iris
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
# Sepal length
plt.figure(figsize = (12, 9), dpi = (100.0)) # image size, 12wx9h inches
x = data["sepal length"] # identifies variable

plt.hist(x, bins = 20, color = "green", edgecolor = 'white', label = 'Sepal Length')
plt.title("Sepal Length in cm")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Count")
plt.legend()

plt.savefig('sepallength.png')

plt.show()

# Sepal Width
plt.figure(figsize = (12, 9), dpi = (100.0)) 
x = data["sepal width"] 

plt.hist(x, bins = 20, color = "blue", edgecolor = 'k', label = 'Sepal width')
plt.title("Sepal width in cm")
plt.xlabel("Sepal width in cm")
plt.ylabel("Count")
plt.legend()
plt.savefig('sepalwidth.png')

plt.show()


# Petal Width
plt.figure(figsize = (12, 9), dpi = (100.0)) 
x = data["petal width"] 

plt.hist(x, bins = 20, color = "red", edgecolor = 'white', label = 'Petal width')
plt.title("Petal width in cm")
plt.xlabel("Petal width in cm")
plt.ylabel("Count")
plt.legend()
plt.savefig('petalwidth.png')

plt.show()

# Petal length
plt.figure(figsize = (12, 9), dpi = (100.0)) 
x = data["petal length"] 

plt.hist(x, bins = 20, color = "orange", edgecolor = 'k', label = 'Petal length')
plt.title("Petal length in cm")
plt.xlabel("Petal length in cm")
plt.ylabel("Count")
plt.legend()
plt.savefig('petallength.png')

plt.show()

#species
plt.figure(figsize = (12, 9), dpi = (100.0)) 
x = data["species"] 

plt.hist(x, bins = 5, color = "yellow", edgecolor = 'blue', label = 'Species')
plt.title("species")
plt.xlabel("Type of species")
plt.ylabel("Count")
plt.legend()
plt.savefig('species.png')

plt.show()


# 3. Outputs a scatter plot of each pair of variables.

# sepal length and petal length scatter plot
# data sets defined
x = data["sepal length"] 
y = data["petal length"]

# plot output formatted by quality and size
plt.figure(dpi = (100.0), figsize = (10,7))

# additional labelling formatting, including modifying font size
plt.scatter(x, y, c = 'red', label = 'Sepal and Petal Length')
plt.title('Sepal v Petal Comparison', fontsize = 25)
plt.xlabel('Sepal size in cm', fontsize = 15)
plt.ylabel('Petal size in cm', fontsize = 15)
plt.legend()

# width comparison
a = data['sepal width']
b = data['petal width']

# plot second scatter plot on same graph with width comparison
plt.scatter(a, b, c = 'green', label = 'Sepal and Petal Width')

plt.legend()
#plt.savefig('Scatterplot MatPlotLib.png')
plt.show()

# a scatterplot using Seaborn. Set style adds a grid to the output. FacetGrid  are the variables used to structure the plot. 
# The hue parameter plots the species in different colours. Height sets the height of the plot. 
# I set the title with .set(Title ...) function.
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue='species', height=6).set(title='Sepal v Petal length')\
.map(plt.scatter, "sepal length", "petal length",)\
.add_legend()

#plt.savefig('Scatterplot Seaborn Sepal v Petal length.png')
plt.show()

sns.set_style("whitegrid") 
sns.FacetGrid(data, hue='species', height=6).set(title='Sepal v Petal Width')\
.map(plt.scatter, "sepal width", "petal width",)\
.add_legend()

plt.savefig('Scatterplot Seaborn Sepal v Petal Width.png')
plt.show()

'''
# 4. Performs any other analysis you think is appropriate

# (a) Calculate sum, mean and mode of a column
# It uses the Pandas dataframe methods to simply calculate the sum, mean and mode of the data set. 

sum_data = data["sepal length"].sum() # this adds all values in the colmn and outputs the sum
mean_data = data["sepal length"].mean() # this gives the mean or average value of the column
median_data = data["sepal length"].median() # this gives the median or middle value of the column 
print("The sepal length stats are:" 
      "\nSum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)


sum_data = data["sepal width"].sum()
mean_data = data["sepal width"].mean()
median_data = data["sepal width"].median()
print("The sepal width stats are:" 
      "\nSum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)

sum_data = data["petal length"].sum()
mean_data = data["petal length"].mean()
median_data = data["petal length"].median()
print("The petal length stats are:" 
      "\nSum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)

sum_data = data["petal width"].sum()
mean_data = data["petal width"].mean()
median_data = data["petal width"].median()
print("The petal width stats are:" 
      "\nSum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)