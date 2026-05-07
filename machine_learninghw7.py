from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer


columns = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']



data1 = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/heart+disease/processed.cleveland.data',names=columns)
data2 = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/heart+disease/processed.hungarian.data',names=columns)
data3 = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/heart+disease/processed.switzerland.data',names=columns)
data4 = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/heart+disease/processed.va.data',names=columns)
data = pd.concat([data1, data2, data3, data4], ignore_index=True)
print(data)

print(data.info())


data = data.replace('?', np.nan)

X = data.drop('target', axis=1)
Y = data['target']

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X = imputer.fit_transform(X)  # Only impute X, not the entire data



# what should the target variable be?






X_train, X_test, Y_train, Y_test = train_test_split(X, Y,random_state=253)


x_scaler = StandardScaler()

X_train = x_scaler.fit_transform(X_train)
X_test = x_scaler.transform(X_test)

model = svm.SVC(kernel='linear')
model.fit(X_train,Y_train)

predictions = model.predict(X_test)

print(Y_test)
print(predictions)

print(classification_report(Y_test,predictions))
matrix = confusion_matrix(Y_test,predictions)

sns.heatmap(matrix, annot=True, fmt='d')
plt.show()




forest = RandomForestClassifier(n_estimators=100,random_state=253)
forest.fit(X_train,Y_train)
predictions = forest.predict(X_test)
print(classification_report(Y_test,predictions))
matrix = confusion_matrix(Y_test,predictions)

sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds')
plt.show()
