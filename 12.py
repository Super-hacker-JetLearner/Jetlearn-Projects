import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('winequality-red.csv')

subplot = make_subplots(rows=2,cols=2,subplot_titles=['alcohol content histogram','alcohol vs density, size is sulphates, and color is quality'])

subplot

histogram = px.histogram(data,x='alcohol',color='quality')


# scatter alcohol vs density
subplot.add_traces(histogram.data,rows=1,cols=1)

scatter = px.scatter(data,x='alcohol',y='density',size='sulphates',color='quality')

subplot.update_layout(xaxis_title='alcohol',yaxis_title='frequency',xaxis2_title='alcohol',yaxis2_title='density')

subplot.add_traces(scatter.data,rows=1,cols=2)










subplot.show()