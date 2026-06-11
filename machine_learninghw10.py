import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np


data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/books.csv')

data = data.drop_duplicates(subset='title',keep='first')

# using simple recommendation due to lack of description


C = data['average_rating'].mean()


m = data['ratings_count'].quantile(0.90)


data = data[(data['average_rating']>C) & (data['ratings_count']>m)]

def weighted_rating(x, m=m, C=C):
    V = x["ratings_count"]
    R = x["average_rating"]
    return (V/ (V + m)*R) + (m / (m + V) * C)

data['score'] = data.apply(axis=1,func=weighted_rating)

data = data.sort_values('score',ascending=False)
print(data[['title','average_rating','ratings_count','score']].head())
