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

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning')

data = pd.read_csv('titanicai.csv')
print(data.head())

data = data.drop(['Embarked','Ticket','Parch','Name','PassengerId'],axis=1)

encoder = LabelEncoder()

data['Sex'] = encoder.fit_transform(data['Sex'])
data['Cabin'] = encoder.fit_transform(data['Cabin'])

print(data)



imputer = SimpleImputer()
data = imputer.fit_transform(data)
print(data)


X = data[:,1:]
Y = data[:,0]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y)

print(X_train)
print(Y_train)



model = LogisticRegression()
model = model.fit(np.array([X_train]),Y_train.reshape(-1))

prediction = model.predict(X_test)

matrix = confusion_matrix(Y_test,prediction)
sns.heatmap(matrix)
plt.show()