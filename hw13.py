import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('WHO-COVID-19-global-data.csv')

data['DateReported'] = pd.to_datetime(data['DateReported'])


region = 'EMRO'
region_data = data[data['WHO_region']==region]
print(region_data)

# region_data = region_data.groupby('Country').max('Cumulative_cases').nlargest(5,'Cumulative_cases')
countries = region_data.sort_values('Cumulative_cases',ascending=False)['Country'].unique()[:5]

print(countries)

countries_with_timeline = region_data[region_data['Country'].isin(countries)]

plot = px.area(countries_with_timeline,x='DateReported',y='Cumulative_cases',line_group='Country',color='Country',title=f'top 5 countries in {region} by cumulative cases')
plot.show()