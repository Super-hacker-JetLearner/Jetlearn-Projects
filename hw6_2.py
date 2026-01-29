import pandas as pd
import numpy as np
import os
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('titanic.csv')[['Survived','Pclass','Sex','Age','Fare']]

import sklearn
# print(sklearn.__version__)

# input and output

input = data.iloc[:, 1:] #all columns except last
output = data.iloc[:, 0]

# input['Sex'].replace(to_replace='male',value=1)
# input['Sex'].replace(to_replace='female',value=0)
input['Sex'] = input['Sex'].replace({'male':1, 'female':0})
# print(input.head())


# #categorical to numerical input
# first = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[2])], remainder='passthrough')


# second = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])], remainder='passthrough')

# input = first.fit_transform(input)
# input = second.fit_transform(input)

# print(input)


# from sklearn.preprocessing import LabelEncoder

# encoder = LabelEncoder()
# output = encoder.fit_transform(output)
# print(output)

# print('train')

from sklearn.model_selection import train_test_split

train_x,test_x,train_y,test_y = train_test_split(input,output,test_size=0.2,random_state=1)
# print(train_x,test_x,train_y,test_y)


# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# train_x = scaler.fit_transform(train_x)
# test_x = scaler.fit_transform(test_x)
# print('------------------------------')
# print(train_y, test_y)

# train_y = scaler.fit_transform(train_y.iloc[:,0])
# test_y = scaler.fit_transform(test_y.iloc[:,0])

# print('preprocessing')
# print(train_x,test_x,train_y,test_y)
# train_x = pd.DataFrame(train_x)
# train_y = pd.DataFrame(train_y)
# test_x = pd.DataFrame(test_x)
# test_y = pd.DataFrame(test_y)

alpha = 0.2

import matplotlib.pyplot as plt
plt.subplot(221)
plt.scatter(train_x.iloc[:,0],train_y,alpha=alpha)

plt.subplot(222)
plt.scatter(train_x.iloc[:,1],train_y,alpha=alpha)

plt.subplot(223)
plt.scatter(train_x.iloc[:,2],train_y,alpha=alpha)

plt.subplot(224)
plt.scatter(train_x.iloc[:,3],train_y,alpha=alpha)
plt.show()

# print('trainx------------------------------------')
# print(train_x)
# print('trainy------------------------------------')
# print(train_y)

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor



#round values in x
train_y:pd.DataFrame = train_y.round(0)
test_y:pd.DataFrame = test_y.round(0)


tree = DecisionTreeClassifier(max_depth=5,random_state=1)
tree.fit(train_x,train_y)
prediction = tree.predict(test_x)
# print(prediction)
# print(test_y)

from sklearn import metrics

accuracy = metrics.accuracy_score(test_y,prediction)
print(accuracy)

# print('prediction')
# print(prediction)
# print('testy')
# print(test_y)