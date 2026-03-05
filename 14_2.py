import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('student-mat.csv')

print(data)

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
data['school'] = encoder.fit_transform(data['school'])
data['sex'] = encoder.fit_transform(data['sex'])
data['address'] = encoder.fit_transform(data['address'])
data['famsize'] = encoder.fit_transform(data['famsize'])
data['Pstatus'] = encoder.fit_transform(data['Pstatus'])
data['Mjob'] = encoder.fit_transform(data['Mjob'])
data['Fjob'] = encoder.fit_transform(data['Fjob'])
data['reason'] = encoder.fit_transform(data['reason'])
data['guardian'] = encoder.fit_transform(data['guardian'])
data['schoolsup'] = encoder.fit_transform(data['schoolsup'])
data['famsup'] = encoder.fit_transform(data['famsup'])
data['paid'] = encoder.fit_transform(data['paid'])
data['activities'] = encoder.fit_transform(data['activities'])
data['nursery'] = encoder.fit_transform(data['nursery'])
data['higher'] = encoder.fit_transform(data['higher'])
data['internet'] = encoder.fit_transform(data['internet'])
data['romantic'] = encoder.fit_transform(data['romantic'])
data['G1'] = encoder.fit_transform(data['G1'])
data['G2'] = encoder.fit_transform(data['G2'])



