import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('mpg.csv')



subplots = make_subplots(rows=2,cols=2,subplot_titles=['horsepower vs mpg','weight histogram','acceleration vs mpg with horsepower as size',None])


scatter = px.scatter(data,x='horsepower',y='mpg')

# for dot in scatter.data:
#     subplots.add_trace(dot,row=1,col=1)
subplots.add_traces(scatter.data,rows=1,cols=1)


# histogram, weight distribution
histogram = px.histogram(data,x='weight')
# for bar in histogram.data:
#     subplots.add_trace(bar,row=1,col=2)
subplots.add_traces(histogram.data,rows=1,cols=2)


print(data['horsepower'])
import numpy as np
data['horsepower'] = data['horsepower'].replace(np.nan,data['horsepower'].mean())

# acceleration vs mpg
scatter2 = px.scatter(data,x='acceleration',y='mpg',size=data['horsepower'])
subplots.add_traces(scatter2.data,cols=1,rows=2)


subplots.show()