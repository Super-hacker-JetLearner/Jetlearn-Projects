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
from sklearn.decomposition import PCA


# PCA
# principal component analysis
# it's a preprocessing step
# it's used for reducing the dimensioinality
# 1. standardize the data, scale it
# 2. co-variance matrix, a matrix of similarities
# 3. remove the rebundant data, remove the noise


data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/student-mat.csv')

X = data.drop('G3',axis=1)
Y = data['G3']

X['G1'] = X['G1'].apply(func=lambda x: int(x))
X['G2'] = X['G2'].apply(func=lambda x: int(x))

print(X['G1'])

for column in X.columns:
    if X[column].dtype == 'object':
        X[column] = LabelEncoder().fit_transform(X[column])


print(X['G1'])




a = X['G1']-Y
a = a.abs()
print(a.mean())


x_scaler = StandardScaler()
X = x_scaler.fit_transform(X)

preprocessor = PCA(20)
X = preprocessor.fit_transform(X,Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y,random_state=312)




model = svm.SVC(kernel='linear')
model.fit(X_train,Y_train)

predictions = model.predict(X_test)

print(Y_test)
print(predictions)

print(classification_report(Y_test,predictions))
matrix = confusion_matrix(Y_test,predictions)

sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds')
plt.show()




forest = RandomForestClassifier(n_estimators=30,random_state=253)
forest.fit(X_train,Y_train)
predictions = forest.predict(X_test)
print(classification_report(Y_test,predictions))
matrix = confusion_matrix(Y_test,predictions)

sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds')
plt.show()




logistic_regr = LogisticRegression()
logistic_regr.fit(X_train,Y_train)
predictions = logistic_regr.predict(X_test)
print(classification_report(Y_test,predictions))
matrix = confusion_matrix(Y_test,predictions)

sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds')
plt.show()


