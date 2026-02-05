import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px
import os

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('iris.csv')


figure = make_subplots(rows=2,cols=2,subplot_titles=['petal width vs petal length','sepal width vs sepal length','histogram of petal width frequency','histogram of sepal width frequency'])
figure.add_trace(px.scatter(data,x='petal_width',y='petal_length',color='species').data[0],row=1,col=1)
figure.add_trace(px.scatter(data,x='petal_width',y='petal_length',color='species').data[1],row=1,col=1)
figure.add_trace(px.scatter(data,x='petal_width',y='petal_length',color='species').data[2],row=1,col=1)
# figure.add_traces(px.scatter(data,x='petal_width',y='petal_length',color='species'),rows=1,cols=1)

figure.add_trace(px.scatter(data,x='sepal_width',y='sepal_length',color='species').data[0],row=1,col=2)
figure.add_trace(px.scatter(data,x='sepal_width',y='sepal_length',color='species').data[1],row=1,col=2)
figure.add_trace(px.scatter(data,x='sepal_width',y='sepal_length',color='species').data[2],row=1,col=2)


figure.add_trace(px.histogram(data,x='petal_length',color='species').data[0],row=2,col=1)
figure.add_trace(px.histogram(data,x='petal_length',color='species').data[1],row=2,col=1)
figure.add_trace(px.histogram(data,x='petal_length',color='species').data[2],row=2,col=1)


figure.add_trace(px.histogram(data,x='petal_width',color='species').data[0],row=2,col=2)
figure.add_trace(px.histogram(data,x='petal_width',color='species').data[1],row=2,col=2)
figure.add_trace(px.histogram(data,x='petal_width',color='species').data[2],row=2,col=2)


figure.show()