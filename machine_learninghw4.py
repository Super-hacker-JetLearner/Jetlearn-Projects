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



os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning')

data = pd.read_csv('iris.csv')


encoder = LabelEncoder()
data['species'] = encoder.fit_transform(data['species'])


X = np.array(data.drop('species',axis=1))
Y = np.array(data[['species']])

X_train,X_test,Y_train,Y_test = train_test_split(X,Y)

x_scaler = StandardScaler()
X_train = x_scaler.fit_transform(X_train)
X_test = x_scaler.transform(X_test)

print(X_train,X_test,Y_train,Y_test)


model = KNeighborsClassifier(n_neighbors=5)

model = model.fit(X_train,Y_train)

predictions = model.predict(X_test)

prediction = model.predict(X_test)

species = ['setosa','versicolor','virginica']

matrix = confusion_matrix(Y_test,prediction)

dataframe = pd.DataFrame(matrix,index=species,columns=species)

sns.heatmap(dataframe, annot=True, fmt='d')
plt.show()

error = mean_absolute_percentage_error(Y_test,prediction)
print(error)