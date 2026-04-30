# SVM, support vector machine

# svm can be used for clasification and regression

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


os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning')


# dataset = datasets.load_breast_cancer()


# data = pd.DataFrame(dataset.data,columns=['mean radius', 'mean texture', 'mean perimeter', 'mean area',
#        'mean smoothness', 'mean compactness', 'mean concavity',
#        'mean concave points', 'mean symmetry', 'mean fractal dimension',
#        'radius error', 'texture error', 'perimeter error', 'area error',
#        'smoothness error', 'compactness error', 'concavity error',
#        'concave points error', 'symmetry error',
#        'fractal dimension error', 'worst radius', 'worst texture',
#        'worst perimeter', 'worst area', 'worst smoothness',
#        'worst compactness', 'worst concavity', 'worst concave points',
#        'worst symmetry', 'worst fractal dimension'])

# data['is_cancer'] = dataset.target

data = pd.read_csv('iris.csv')


for column in data.columns:
    data[column] = LabelEncoder().fit_transform(data[column])



X = data.drop('species',axis=1)
Y = data['species']




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

sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds')
plt.show()




forest = RandomForestClassifier(n_estimators=100,random_state=253)
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


