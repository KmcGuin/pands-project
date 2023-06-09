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
import plotly.express as px
import seaborn as sns
import sklearn
from sklearn import metrics 
from sklearn.datasets import load_iris
from pandas.api.types import is_numeric_dtype
import sys
from mpl_toolkits.mplot3d import Axes3D
from seaborn import pairplot
from plotly.express import scatter_3d





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



# 4(b) correlation matrix
# This shows the nature of the relationship between the variables of the iris data set. 
# It shows how similar they are to one another and it displays it as a correlation coefficient between -1 and 1.
# A correlation coefficient of 1 or -1 show a perfect relationship between variables.

corr = data.corr()
print(corr)

# use seaborn to plot a heat map of the coefficient correlation matrix.
# Setting annot to True gives numbers in each cell
# cmap refers to the colour tone of the heat map - set to crest, which give a blue-green colour.
# Linewidth is the line between each square.
# plt.subplot creates a single subplot. You could add another plot by yusing plt.subplots(2 ...)
fig, ax = plt.subplots(figsize=(10,7))
sns.heatmap(corr, annot=True, cmap = 'crest', linewidth=.5)
# plt.savefig('Correlation Coefficient matrix.png')
plt.show()

      
# 4(c) Violin plots 

# This shows the density of the data. The bigger parts of the violin represent the more dense parts of the data.
# The white dot in the middle represents the median, or middle value of the set
# The grey line represents the interquartile range (IQR), or middle values of the range of data
# Use seaborn violin plot function
# define the x and y axes. 

sns.violinplot(x="species", y="petal length", palette="husl", data=data)

sns.violinplot(x="species", y="petal width", palette="husl", data=data)

sns.violinplot(x="species", y="sepal length", palette="husl", data=data)

sns.violinplot(x="species", y="sepal width", palette="husl", data=data)

# plt.savefig('Sepal Width Violin plot.png')
plt.show()
 
     
# 4(d) 3D scatterplot

# used in conjunction with 'from plotly.express import scatter_3d' module

px.scatter_3d(data, x='sepal length', y='sepal width', z='petal length', color="species")\
            .show()

# This opens a result in a web browser - note it has been added to the PNG files of the project under the title '3dscatter.png'
  '''

# 4(e) KDE (Kernel Density Estimation) plots 

# using Seaborn jointplot function
# Shade adds depth to the results and cbar adds in a colour legend on results

sns.jointplot(x = 'sepal length',y = 'sepal width', data = data, kind = 'kde', color = 'blue', shade = True, cbar = True)
sns.jointplot(x = 'petal length',y = 'petal width', data = data, kind = 'kde', color = 'red', shade = True, cbar=True)

# plt.savefig('KDESepal.png')

plt.show()