import pandas as pd
import numpy as np
import os
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('iris2.csv')

import sklearn
print(sklearn.__version__)

# input and output

input = data.iloc[:, 0:4] #slicing high is excluded. row first
output = data.iloc[:, -1]

print(input)
print(output)



from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
output = encoder.fit_transform(output)
print(output)

print('train')

from sklearn.model_selection import train_test_split

train_x,test_x,train_y,test_y = train_test_split(input,output,test_size=0.2,random_state=1)
print(train_x,test_x,train_y,test_y)


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.fit_transform(test_x)


print('preprocessing')
print(train_x,test_x,train_y,test_y)


import matplotlib.pyplot as plt
plt.subplot(221)
plt.scatter(train_x[:,0],train_y)

plt.subplot(222)
plt.scatter(train_x[:,1],train_y)

plt.subplot(223)
plt.scatter(train_x[:,2],train_y)

plt.subplot(224)
plt.scatter(train_x[:,3],train_y)
plt.show()


from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=5,random_state=1)
tree.fit(train_x,train_y)
prediction = tree.predict(test_x)
print(prediction)
print(test_y)

from sklearn import metrics

accuracy = metrics.accuracy_score(test_y,prediction)
print(accuracy)

