import pandas as pd

# recommender
# simple recommendation


data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/movies_metadata.csv')



C = data['vote_average'].mean()

print(C)

m = data['vote_count'].quantile(0.90)

print(m)

data = data[(data['vote_average']>C) & (data['vote_count']>m)]

def weighted_rating(x, m=m, C=C):
    V = x["vote_count"]
    R = x["vote_average"]
    return (V/ (V + m)*R) + (m / (m + V) * C)

data['score'] = data.apply(axis=1,func=weighted_rating)

data = data.sort_values('score',ascending=False)
print(data[['title','vote_average','vote_count','score']].head())