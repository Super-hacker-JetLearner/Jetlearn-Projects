import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('mpg.csv')



subplots = make_subplots(rows=2,cols=2,subplot_titles=['horsepower vs mpg',None,None,None])


scatter = px.scatter(data,x='horsepower',y='mpg')

for dot in scatter.data:
    subplots.add_trace(dot,row=1,col=1)




subplots.show()