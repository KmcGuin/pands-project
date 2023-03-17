# irisdataset.py
#Author: Kealan McGuinness

#downloading and installing irish data set. Downloaded to desktop as a csv file and read in below.

# go to https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ for info on how to manipulate the dataset and output specific parts of the data.



import pandas as pd

data = pd.read_csv('/Users/kealanmcguinness/Desktop/pands/pands-project/iris.csv')

print(data)
