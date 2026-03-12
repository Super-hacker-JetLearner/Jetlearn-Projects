import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('heart_disease copy.csv')



imputer = SimpleImputer(strategy='most_frequent',missing_values='?')
data = pd.DataFrame(imputer.fit_transform(data))

print(data)

data = data.apply(pd.to_numeric,'columns')

print(data)