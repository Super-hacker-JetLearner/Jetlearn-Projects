import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('WHO-COVID-19-global-data.csv')

data['DateReported'] = pd.to_datetime(data['DateReported'])

country1 = 'Brazil'
country2 = 'United States of America'

# country1_data = data[data['Country']==country1]
# country2_data = data[data['Country']==country2]
# plot = px.line(x=country1_data['DateReported'],y=[country1_data['New_cases'],country2_data['New_cases']],labels={'value':'new cases','x':'date reported'})
# plot.show()

# country_data = data[(data['Country']==country1)|(data['Country']==country2)]

# plot = px.line(country_data,x='DateReported',y=['Cumulative_cases'])
# plot.show()


# country_data = data[(data['Country']==country1)|(data['Country']==country2)].groupby('Country')
# print(country_data.head())
# plot = px.line(country_data,x='DateReported',y='New_cases')
# plot.show()

# country1_data = data[data['Country']==country1]
# country2_data = data[data['Country']==country2]
# country_data = pd.DataFrame()
# country_data[country1] = country1_data['New_cases']
# country_data[country2] = country2_data['New_cases']
# country_data['DateReported'] = country1_data['DateReported']
# plot = px.line(country_data,x='DateReported',y=[country1,country2])
# plot.show()


country_data = data[(data['Country']==country1)|(data['Country']==country2)]

plot = px.line(country_data,x='DateReported',y='Cumulative_cases',color='Country',labels={'DateReported':'date reported','Cumulative_cases':'cumulative cases'})
plot.show()




country = 'Trinidad and Tobago'
country_data = data[data['Country']==country]

subplot = make_subplots(2,2,True,subplot_titles=['new cases','cumulative cases','new deaths','cumulative deaths'])
subplot.update_layout(title=f'{country} covid data')

subplot.add_traces(px.line(country_data,x='DateReported',y='New_cases').data,1,1)
subplot.add_traces(px.line(country_data,x='DateReported',y='Cumulative_cases').data,1,2)
subplot.add_traces(px.line(country_data,x='DateReported',y='New_deaths').data,2,1)
subplot.add_traces(px.line(country_data,x='DateReported',y='Cumulative_deaths').data,2,2)

subplot.show()







region = 'EMRO'
region_data = data[data['WHO_region']==region]
region_data = region_data.groupby('DateReported').sum()
print(region_data.head())

subplot = make_subplots(2,2,True,subplot_titles=['new cases','cumulative cases','new deaths','cumulative deaths'])
subplot.update_layout(title=f'{region} covid data')

subplot.add_traces(px.line(region_data,x=region_data.index,y='New_cases').data,1,1)
subplot.add_traces(px.line(region_data,x=region_data.index,y='Cumulative_cases').data,1,2)
subplot.add_traces(px.line(region_data,x=region_data.index,y='New_deaths').data,2,1)
subplot.add_traces(px.line(region_data,x=region_data.index,y='Cumulative_deaths').data,2,2)

subplot.show()



