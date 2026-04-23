import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning')

data = pd.read_csv('bank-full.csv',sep=';')

X = data.drop('y',axis=1)
Y = data['y']

Y = pd.Series(LabelEncoder().fit_transform(Y))

for column in X.columns:
	if X[column].dtype == 'object':
		X[column] = LabelEncoder().fit_transform(X[column])
	X[column] = LabelEncoder().fit_transform(X[column])

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=33)

model = DecisionTreeClassifier(random_state=33)

model = model.fit(X_train,Y_train)

prediction = model.predict(X_test)

matrix = confusion_matrix(Y_test,prediction)

types = data['y'].unique()

matrix = pd.DataFrame(matrix,index=types,columns=types)

sns.heatmap(matrix, annot=True, fmt='d')
plt.show()



correct = 0
for col in matrix.columns:
    for row in matrix:
        if col==row:
            correct += matrix.loc[row,col]
            
print(correct)

print(correct/matrix.values.sum())