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
import math
from sklearn.ensemble import RandomForestClassifier

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning')


# random forest

# when having dataset with many columns, split dataset into parts
# using decision tree on each part
# the results vote on the prediction
# that's why it's called a forest



data = pd.read_csv('student-mat.csv')



X = data.drop(['G3','guardian','romantic','health','freetime','traveltime','Mjob','Fjob'],axis=1)
Y = data['G3']

print(pd.crosstab(Y,Y))


print(len(Y.unique()),Y.unique())


for column in X.columns:
	if X[column].dtype == 'object':
		X[column] = LabelEncoder().fit_transform(X[column])
	X[column] = LabelEncoder().fit_transform(X[column])

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=70)


print(len(Y_train.unique()),len(Y_test.unique()))

model = RandomForestClassifier(n_estimators=6,random_state=70)
model = model.fit(X_train,Y_train)

prediction = model.predict(X_test)


matrix = confusion_matrix(Y_test,prediction)

types = data['G3'].unique()

print(types)

print(matrix)

# matrix = pd.DataFrame(matrix,index=types,columns=types)

sns.heatmap(matrix, annot=True, fmt='d')
plt.show()



print(mean_absolute_error(Y_test,prediction))