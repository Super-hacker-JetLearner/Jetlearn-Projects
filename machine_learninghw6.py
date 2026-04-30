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


data = pd.read_csv('adult.csv')

data.columns = ['age','work_class','statistical_weight','degree','educational_number','married','job','family','skin_tone','gender','profit_investements','loss_investements','working_hours','country','income']


# categorical to numerical
encoder = LabelEncoder()
for column in data.columns:
    if data[column].dtype == 'object':
        data[column] = encoder.fit_transform(data[column])
        
X = data.drop('income', axis=1)
Y = data['income']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,random_state=100)

# random forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=100)
rf_model.fit(X_train, Y_train)
rf_predictions = rf_model.predict(X_test)

# decision tree
dt_model = DecisionTreeClassifier(random_state=100)
dt_model.fit(X_train, Y_train)
dt_predictions = dt_model.predict(X_test)



rf_accuracy = classification_report(Y_test, rf_predictions)
dt_accuracy = classification_report(Y_test, dt_predictions)
print('rf',rf_accuracy)
print('dt',dt_accuracy)
rf_matrix = confusion_matrix(Y_test, rf_predictions)
dt_matrix = confusion_matrix(Y_test, dt_predictions)
sns.heatmap(rf_matrix, annot=True, fmt='d', cmap='Blues')
plt.show()
sns.heatmap(dt_matrix, annot=True, fmt='d', cmap='Reds')
plt.show()