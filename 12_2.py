import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('WHO-COVID-19-global-data.csv')



data['DateReported'] = pd.to_datetime(data['DateReported'])


data2 = data.groupby('DateReported',sort=True).sum('Cumulative_cases')

print(data2)

scatter = px.line(data2,x=data2.index,y='Cumulative_cases')
scatter.show()


data3 = data.groupby('DateReported',sort=True).sum('New_cases')


scatter = px.line(data3,x=data3.index,y='New_cases')


scatter.show()



country = 'Brazil'

country_data = data[data['Country']==country].sort_values('DateReported')
print(country_data)
scatter = px.line(country_data,x='DateReported',y='Cumulative_cases')

scatter.show()