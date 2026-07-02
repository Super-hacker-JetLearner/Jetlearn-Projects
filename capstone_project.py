import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn.ensemble 


data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/Car_sales.csv')

data = data.drop(axis=1,labels='Latest_Launch')

encoder = LabelEncoder()

data['Manufacturer'] = encoder.fit_transform(data['Manufacturer'])
data['Model'] = encoder.fit_transform(data['Model'])
data['Vehicle_type'] = encoder.fit_transform(data['Vehicle_type'])

imputer = SimpleImputer()

# for column in data.columns:
#     data[column] = imputer.fit_transform([data[column]])
columns = data.columns

data = imputer.fit_transform(data)
data = pd.DataFrame(columns=columns,data=data)

print(data)

X = data.drop('Price_in_thousands')
Y = data['Price_in_thousands']

x_scaler = StandardScaler()
X = x_scaler.fit_transform(X)

preprocessor = PCA(8)
X = preprocessor.fit_transform(X,Y)

model = 