import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('adult.csv')



print(data.columns)


data.loc[len(data)] = data.columns
print(data)




data.columns = ['age','work_class','statistical_weight','degree','educational_number','married','job','family','skin_tone','gender','profit_investements','loss_investements','working_hours','country','income']

print(data)

data['income'] = data['income'].replace({' >50K':70000,' <=50K':3000})

print(data)

data['gender'] = data['gender'].replace({' Male':1, ' Female':2}) #replace value

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
data['job'] = encoder.fit_transform(data['job'])
data['married'] = encoder.fit_transform(data['married'])
data['work_class'] = encoder.fit_transform(data['work_class'])
data['family'] = encoder.fit_transform(data['family'])
data['degree'] = encoder.fit_transform(data['degree'])
data['country'] = encoder.fit_transform(data['country'])
data['skin_tone'] = encoder.fit_transform(data['skin_tone'])


subplot = make_subplots(4,4,True,subplot_titles=data.columns)

for row in range(4):
    for col in range(4):
        try:
            subplot.add_traces(px.scatter(data,x='income',y=data.columns[row*4+col]).data, rows=row+1,cols=col+1)
        except:
            pass
        
        
subplot.show()


# 70,000
# 3,000

