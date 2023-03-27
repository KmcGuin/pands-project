# **pands-project**
## **Author: Kealan McGuinness**

# **First Steps**
### I downloaded the iris data set as a csv from: 
(https://datahub.io/machine-learning/iris)
### I was having difficulty getting the data set from the URL provided in the project lesson plan. t wouldn't work on my computer. The above link was mentioned by:
(https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/)
### There is lots of interesting information in that link too. 
### Other references:
(https://www.angela1c.com/projects/iris_project/downloading-iris/)
(https://gist.github.com/curran/a08a1080b88344b0c8a7#file-iris-csv)
### I also created a python file called irisdataset.py, in which I read in the csv file and tested it to make sure it was working. 
- I imported Pandas to put the data set into a data frame, which displays it as rows and columns. 
### I created the Project repository on Git Hub and linked it up on my computer. 

# **Project plan**
- Set up repository and download data set by week ending 19 March
- Carry out initial research and complete the research summary by week ending 26 March
- Create analysis.py program file and start the analysis process by week ending 2 April
- Make the file output a summary of each variable to a single text file, and save a histogram of each variable to png files by week ending 16 April
- Outputs a scatter plot of each pair of variable and continue ad-hoc analyses and complete by week ending 30 April
- Final checks on project by week enfing 7 May
- Submit project before deadline of 12 May.


# **Iris Data Set research**

## *Summary*

### The Iris data is a small data set of 150 lines examining 3 different classes of the iris flower. It was used by Ronald A. Fisher in his 1936 paper 'The Use of Multiple Measurements in Taxonomic Problems'. It was first published by Edgar Anderson, a botanist with an interest in statistics. It is a common data set used in Data Science and Machine Learning. 

### It is a popular teaching tool as the data is small but not too small, the data is real and of good quality. It also lends itself to data visualisation, such as using histograms and other plots to display the data.

### In the data set, there are 150 lines. It includes three different species of iris: 
- *Setosa*
- *Versicolor*
- *Virginica*

### Lines 1-50 of the set are the setosa iris, lines 51-100 are the versicolor and lines 101-150 are the virginica.

### As well as being separated species, each species is further distinguised using the following properties:
- sepal length in cm
- sepal width in cm
- petal length in cm
- petal width in cm

## *Potential tests to carry out*

### Based on my reading there are a lot of different ways researchers have analysed the data on the Iris data set. It is often referred to as Exploratory Data Analysis. Some examples include: 

- statistical summaries of the data set, with the count, mean and standard deviation, minimum values, maximum values
- the number of iris flowers in each species
- comparing sepal length and width
- comparing petal length and width
- comparing each column's relationship with each other
- highest frequency of sepal length and sepal width
- highest frequency of petal length and petal width
- heatmap showing correlation between each of the variables in the dataset
- Violin plot showing density and width of each species

## *Outputs*

### Some of the outputs I have come across include:
- histograms
- scatter plots
- line plots
- heatmaps
- boxplots
- Violin plot
- text based information

## *Modules to import*

### Based on my reading, I will need these modules:
- numpy
- pandas
- matplotlib
- seaborn (added visual element)
- from sklearn import metrics 

## *References*
(https://www.kaggle.com/datasets/uciml/iris)
(http://archive.ics.uci.edu/ml/datasets/Iris)
(http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html)
(https://towardsdatascience.com/classification-basics-walk-through-with-the-iris-data-set-d46b0331bf82_)
(https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda)



# **Analysis**

### I created a python file called analysis.py, labelled it and imported the modules I need to carry out analysis.
- numpy
- pandas
- matplotlib
- seaborn (added visual element)
- from sklearn import metrics 

### I read in the Iris data set CSV file and called it 'data' and tested it - using 'print(data)' to make sure it worked.

## *Pands Project Instructions*:
- 1. Outputs a summary of each variable to a single text file,
- 2. Saves a histogram of each variable to png files, and
- 3. Outputs a scatter plot of each pair of variables.
- 4. Performs any other analysis you think is appropriate

### 1. A summary of each variable in a single text file
- petal length
- petal width
- sepal length
- sepal width
- species

### Extra import - is_numeric_type from pandas - it can be used to determine if the information in a column is numerical. Code taken from the reference below to find the mean, standard deviation, minimum value and maximum value of the numerical columns (petal length, petal width, sepal length, sepal width). %2f is used to format float numbers and round them up to 2 decimal places.

### imported sys because it seemed to provide the simplest way of saving the output of the summary analysis as a text file. The code used to do this is taken from the website geeksforgeeks.org - referenced below.

## *References*
(https://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html)
(https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/)
(https://www.geeksforgeeks.org/inputoutput-external-file-cc-java-python-competitive-programming/_)

### 2. Saves a histogram of each variable to png files

- I set the figure size to be 12 incheswide by 9 inches high and a resolution of 100 dpi. 
- In each individual case, I defined the variable I wanted to represent in the histogram - petal length, petal width, sepal width, sepal length and species. 
- I created 20 bins on the histogram to show the data results over a wide range, with the exception of species. I reduced the bin number to 5 for species as there are only 3 data sets, or species, so a bin number of 5 will reduce the distance between each column. 
- In each case, I changed the colour and the edge colour and added in title of histogram, a legend, and labels for the x and y axes.
- I used the plt.savefig command to save each histogram as a PNG file.
- The file references contains a version of the code used for this.

## *References*
(https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/)


### 3. Outputs a scatter plot of each pair of variables.
- I created two different scatter plots, one using the matplotlib module and one using the seaborn module.
*Matplotlib*
- In the matplotlib version, I defined the data sets x, y for length and a, b for width. 
- First I set the scatter plot for the x and y set. This included setting figure size, resolution as well as formatting the data in the output, colour, fontsize, axes labels and title of the output.
- I then created the scatter plot for a and b set - the petal and sepal width. I then formatted this and plotted it on the same output as the x and y axis.

*Seaborn*
- To help distinguish more between the species and represent them in different colours, I read that the Seaborn module would do this better.
- I found code - referenced below - and I adapted it to the Iris data set ,by changing the name of the data sets, adding in the species information and using the hue parameter to set different colours to the species. 
- I also formatted this scatterplot wit a grid background, a title, and labels on the axes. 
- I repeated this process to creat a plot comparing petal and sepal width and a second comparing petal and sepal length.

- I saved all Matplotlub and Seaborn scatter plots as PNGs.

## *References*
(https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/)
(https://www.nickmccullum.com/python-visualization/scatterplot/)
(https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-32d09a52f322_)


### 4. Performs any other analysis you think is appropriate

### (a) Calculate sum, mean and mode of a column
- this calculates some statistics of each column - petal length, petal width, sepal length and sepal width. 
- I used the Pandas module to caluclate the sum (total), mean (average) and median (middle value) of the four numerical columns. 

## *References*
(https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/)
(https://www.w3schools.com/python/pandas/ref_df_sum.asp)
(https://www.w3schools.com/python/pandas/ref_df_mean.asp)
(https://www.w3schools.com/python/pandas/ref_df_median.asp)


### (b) correltion coefficients matrix
### This shows the nature of the relationship between the variables of the iris data set. 
### It shows how similar they are to one another and it displays it as a correlation coefficient between -1 and 1.
### A correlation coefficient of 1 or -1 show a perfect relationship between variables. In the results, 'sepal length' and 'sepal length' have a correlation of 1 as they have a perfect relationship with one another. Same with each variable when paired with itself.
### The data.corr() method ignores non-numerical column - ie species.

- I used Seaborn  (sns.heatmap()) to export the correlation coefficient matrix as a heatmap. 
- I amended the parameters to control the style of the heatmap produced. 
- I saved the figure as a png. 

## *References*
(https://realpython.com/numpy-scipy-pandas-correlation-python/)
(hackersrealm.net/post/iris-dataset-analysis-using-python)
(https://www.w3schools.com/python/pandas/pandas_correlations.asp_)
(https://pythonbasics.org/seaborn-heatmap/)
(https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html)
(https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html)

### (c) violin plots
- This shows the density of the data. The bigger parts of the violin represent the more dense parts of the data.
- The white dot in the middle represents the median, or middle value of the set
- The grey line represents the interquartile range (IQR), or middle values of the range of data
- Use seaborn.violinplot function as per the link referenced below.
- Uses the husl colour palette 
- I created graphs for each of the columns and saved them as PNGs.

## *References*
(https://www.kaggle.com/code/zachgold/python-iris-data-visualizations)
(https://mode.com/blog/violin-plot-examples/#:~:text=What%20is%20a%20violin%20plot%3F,the%20density%20of%20each%20variable.)
(https://www.statisticshowto.com/probability-and-statistics/interquartile-range/)
(https://seaborn.pydata.org/generated/seaborn.violinplot.html)
(https://seaborn.pydata.org/generated/seaborn.husl_palette.html)


### (d) 3D scatter plot
- imported - from plotly.express import scatter_3d - module
- used px.scatter3d (px is plotly.express) command to create the 3d graph
- labelled x, y and z axes. 
- Set colour to represent the species
- created a result in the web browser - I downloaded and saved it as a PNG called '3dscatter.png'.

## *References*
(https://stackoverflow.com/questions/66521229/visualization-of-iris-data-set-and-a-model-for-naive-bayes)
(https://plotly.com/python/3d-scatter-plots/)
(https://www.delftstack.com/howto/plotly/plotly-3d-scatter-plot/?utm_content=cmp-true_)
(https://plotly.com/python-api-reference/generated/plotly.express.scatter_3d.html)

### (e) KDE (Kernel Density Estimation) plots 
- KDE shows the probablity density function of the non-parametric data variables.
- this is generated using th jointplot function of seaborn. 
- it is important to set the 'kind' parameter to 'KDE' to make sure it plots a kenel density estimation.
- Setting kind to 'KDE' results in both a univariate and bivariate KDE plot.
- A univariate works with only one variable in a dataset, while a bivariate works with two. There are contours at the top and right hand side of the graph produced, and the data in the middle.
- I set the colours to blue and red respectively, to distinguish between the petal and sepal results and I used the shade parameter todarken the areas with the highest density.
- CBar is set to True to create a colour density legend along the graphs.

## *References*
(https://www.tutorialspoint.com/how-seaborn-library-used-to-display-a-kernel-density-estimation-plot-joinplot-in-python#)
(https://jakevdp.github.io/PythonDataScienceHandbook/05.13-kernel-density-estimation.html)
(https://seaborn.pydata.org/generated/seaborn.jointplot.html)
(https://blog.devgenius.io/exploratory-data-analysis-using-seaborn-part-2-kernel-density-estimation-plot-kde-6087a8552cd0)