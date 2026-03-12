import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt


os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

uber = pd.read_csv('Uber.csv')

uber['date'] = pd.to_datetime(uber['date'])

uber['day'] = uber['date'].dt.day
uber['month'] = uber['date'].dt.month






day_dataframe = pd.DataFrame(uber.groupby('day').sum(True)['trips'])



month_dataframe = pd.DataFrame(uber.groupby('month').sum(True)['trips'])


subplot = make_subplots(2,2)
subplot.add_traces(px.density_heatmap(uber,x='day',y='month',z='trips').data,1,1)





subplot.add_traces(px.line(month_dataframe,x=month_dataframe.index,y='trips').data,1,2)
subplot.add_traces(px.line(day_dataframe,x=day_dataframe.index,y='trips').data,2,1)


subplot.show()