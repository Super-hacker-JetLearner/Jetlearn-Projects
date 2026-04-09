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


# knn is k nearest neighbours
# feature scaling is scaling the values
# (xi-minx)/(maxx-minx)
# k should best be odd
# k should be best between 5 and 9

columns = ['longitude','latidue','housingMedianAge','totalRooms','totalBedrooms','population','households','medianIncome','medianHouseValue']

data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/CaliforniaHousing/cal_housing.csv',names=columns)


X = np.array(data[['housingMedianAge','totalRooms','totalBedrooms','population','households','medianIncome']])
Y = np.array(data['medianHouseValue'])

X_train,X_test,Y_train,Y_test = train_test_split(X,Y)




x_scaler = StandardScaler()
# y_scaler = StandardScaler()
X_train = x_scaler.fit_transform(X_train)
# Y_train = y_scaler.fit_transform(Y_train.reshape(-1,1))
X_test = x_scaler.transform(X_test)
# Y_test = y_scaler.transform(Y_test.reshape(-1,1))



poly = PolynomialFeatures(3)
poly_train = poly.fit_transform(X_train)

model = LinearRegression()

model = model.fit(poly_train,Y_train)

# training finished
poly_test = poly.transform(X_test)
predictions = model.predict(poly_test)

mse = mean_squared_error(Y_test, predictions)
print(f"Mean Squared Error: {mse}")

mae = mean_absolute_error(Y_test,predictions)
print(f"Mean Absolute Error: {mae}")

mape = mean_absolute_percentage_error(Y_test,predictions)
print(f"Mean Absolute Percentage Error: {mape}")

thing = pd.DataFrame(columns=['true','pred','difference','percentage_difference'])
thing['true'] = Y_test[:20]
thing['pred'] = predictions[:20]
thing['difference'] = abs(thing['true']-thing['pred'])
thing['percentage_difference']=abs((thing['pred']-thing['true'])/thing['true'])

print(thing)


print(np.mean(Y_train))
print(np.max(Y_train))
print(np.min(Y_train))

# homework, split iris into test and train, perform scaling