import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = np.array([1,2,3,4,5,6]).reshape(-1,1)
Y = np.array([1,4,9,16,25,36])

model = LinearRegression()
model = model.fit(X,Y)


plt.plot(X,Y)
plt.plot(X,model.predict(X))
plt.legend(labels=['real','predicted'])
# plt.show()


poly = PolynomialFeatures(degree=2)

poly = poly.fit_transform(X)
model = LinearRegression()
model = model.fit(poly,Y)

plt.plot(X,Y)
plt.plot(X,model.predict(poly))
plt.legend(labels=['real','predicted'])
# plt.show()



# from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd


# data = fetch_california_housing()
columns = ['longitude','latidue','housingMedianAge','totalRooms','totalBedrooms','population','households','medianIncome','medianHouseValue']

data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/CaliforniaHousing/cal_housing.csv',names=columns)


print(data.head())

X = np.array(data[['housingMedianAge','medianIncome']])
Y = np.array(data['medianHouseValue'])

poly = PolynomialFeatures((1,4))
poly = poly.fit_transform(X)

model = LinearRegression()

model = model.fit(poly,Y)