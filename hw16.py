import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('heart_disease copy.csv')




print(data)

# columns = ['Age','Gender','chest_pain','resting_blood_pressure','cholesterol','fasting_blood_sugar','ecg','maximum_heart_rate','exercise','old_peak','slope','number_of_major_vessels','blood_disorder_test_result','heart_disease']


# data.columns = columns

# data['Age'] = data.index


# print(data['cholesterol'])

columns = data.columns
# print(data['cholesterol'])

print(data)



# imputer = SimpleImputer(strategy='most_frequent',missing_values='?')
# data = pd.DataFrame(imputer.fit_transform(data))

for column in data.columns:
    data[column] = data[column].replace('?',data[column].mode()[0])

data.columns = columns

print(data)
print(data['cholesterol'])


subplot = make_subplots(rows=3,cols=3)


subplot.add_traces(px.scatter(data,x='heart_disease',y='Age').data,1,2)


data['heart_disease'] = data['heart_disease'].apply(func=lambda x: 1 if x>0 else 0)


print(data['cholesterol'])


print(data['heart_disease'])


subplot.add_traces(px.box(data,x='heart_disease',y='Age',orientation='v').data,1,1)


subplot.add_traces(px.box(data,x='heart_disease',y='cholesterol',orientation='v').data,1,3)

subplot.add_traces(px.histogram(data,x='Gender',y='heart_disease').data,2,1)

subplot.show()