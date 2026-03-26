import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt


os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('car_evaluation.csv')

print(data.head())

subplot = make_subplots(4,2)


for i, col in enumerate(data.columns):
    row = i // 2 + 1
    col_num = i % 2 + 1
    subplot.add_trace(
        go.Histogram(x=data[col], name=col),
        row=row, col=col_num
    )

subplot.show()