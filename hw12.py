import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('WHO-COVID-19-global-data.csv')
data['DateReported'] = pd.to_datetime(data['DateReported'])

country = 'Netherlands'

country_data = data[data['Country']==country].sort_values('DateReported')

# dual line graph
plot = px.line(country_data,x='DateReported',y=['New_cases','New_deaths' ],title=f'{country} COVID-19 Cases',labels={'value':'Number of Cases','DateReported':'Date'})

plot.show()