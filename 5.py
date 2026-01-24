import numpy as np
import pandas as pd
import os
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('Data.csv')

import sklearn
print(sklearn.__version__)

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
input = first_column.fit_transform(input)

if not isinstance(input, np.ndarray):
    input = input.toarray()
    print('not')

# input = np.around(input,-1)

print(input)



from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
output = encoder.fit_transform(output)
print(output)





from sklearn.model_selection import train_test_split

train_x,test_x,train_y,test_y = train_test_split(input,output,test_size=0.2,random_state=1)
print(train_x,test_x,train_y,test_y)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_x[:,3:5] = scaler.fit_transform(train_x[:,3:5])
test_x[:,3:5] = scaler.fit_transform(test_x[:,3:5])



