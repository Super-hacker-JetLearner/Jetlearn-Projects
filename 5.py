import numpy as np
import pandas as pd
import os
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('Data.csv')


# input and output

input = data.iloc[:, 0:3] #slicing high is excluded. row first
output = data.iloc[:, -1]

print(input)
print(output)

#fill missing values

replacing_rule = SimpleImputer(missing_values=np.nan, strategy='mean')
replacing_rule.fit(input.iloc[:,1:])
input.iloc[:,1:] = replacing_rule.transform(input.iloc[:,1:])

print(input)


#categorical to numerical input
first_column = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])], remainder='passthrough')
input = np.array(first_column.fit_transform(input))

print(input)