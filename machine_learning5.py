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

data = pd.read_csv('car_evaluation.csv')

encoder = LabelEncoder()

columns = ['buying_price','maintenance_cost','number_of_doors','number_of_people','luggage_boot_size','safety']
for column in columns:
    data[column] = encoder.fit_transform(data[column])
    

X = data.drop('acceptability',axis=1)
Y = data['acceptability']

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=29)

tree = DecisionTreeClassifier(criterion='entropy',random_state=29)

tree = tree.fit(X_train,Y_train)

prediction = tree.predict(X_test)


matrix = confusion_matrix(Y_test,prediction)

types = Y.unique()

dataframe = pd.DataFrame(matrix,index=types,columns=types)

sns.heatmap(dataframe, annot=True, fmt='d')
plt.show()

error = mean_absolute_percentage_error(Y_test,prediction)
print(error)