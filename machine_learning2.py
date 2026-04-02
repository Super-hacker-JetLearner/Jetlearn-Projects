import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import pandas as pd


X = np.array([1,2,3,4,5,6]).reshape(-1,1)
Y = np.array([1,4,9,16,25,36])

# model = LinearRegression()
# model = model.fit(X,Y)


# plt.plot(X,Y)
# plt.plot(X,model.predict(X))
# plt.legend(labels=['real','predicted'])
# # plt.show()


# poly = PolynomialFeatures(degree=2)

# poly = poly.fit_transform(X)
# model = LinearRegression()
# model = model.fit(poly,Y)

# plt.plot(X,Y)
# plt.plot(X,model.predict(poly))
# plt.legend(labels=['real','predicted'])
# # plt.show()



# from sklearn.datasets import fetch_california_housing





columns = ['longitude','latidue','housingMedianAge','totalRooms','totalBedrooms','population','households','medianIncome','medianHouseValue']

data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/CaliforniaHousing/cal_housing.csv',names=columns)


X = np.array(data[['longitude','latidue','housingMedianAge','totalRooms','totalBedrooms','population','households','medianIncome']])
Y = np.array(data['medianHouseValue'])

X_train,X_test,Y_train,Y_test = train_test_split(X,Y)


print(data.head())


poly = PolynomialFeatures(3)
poly_train = poly.fit_transform(X_train)

model = LinearRegression()

model = model.fit(poly_train,Y_train)

# trainining finished




poly_test = poly.transform(X_test)
predictions = model.predict(poly_test)

mse = mean_squared_error(Y_test, predictions)
print(f"Mean Squared Error: {mse}")

mae = mean_absolute_error(Y_test,predictions)
print(f"Mean Absolute Error: {mae}")
