import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/Car_sales.csv')

data = data.drop(columns=['Latest_Launch'])


data['Manufacturer'] = LabelEncoder().fit_transform(data['Manufacturer'])
data['Model'] = LabelEncoder().fit_transform(data['Model'])
data['Vehicle_type'] = LabelEncoder().fit_transform(data['Vehicle_type'])

imputer = SimpleImputer(strategy='mean')
data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)


X = data.drop(columns=['Price_in_thousands'])
Y = data['Price_in_thousands']

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


print('error', mean_absolute_error(y_test, y_pred))
