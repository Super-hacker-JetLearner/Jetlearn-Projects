import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/anime.csv')


model = TfidfVectorizer(stop_words='english')


mov_idx = pd.Series(data.index, index=data['name'])

data['genre'] = data['genre'].fillna(' ')

matrix = model.fit_transform(data['genre'])


def recommend(movie):
    idx = mov_idx[movie]
    similarities = linear_kernel(matrix[idx],matrix).flatten()
    similarity_idxs = np.flip(np.argsort(similarities))
    similarity_idxs = similarity_idxs
    if idx in similarity_idxs:
        similarity_idxs = np.delete(similarity_idxs, np.where(similarity_idxs == idx))
    similarity_titles = mov_idx.iloc[similarity_idxs]
    sorted_similarities = similarities[similarity_idxs]
    similarity_movies = pd.DataFrame({'title':similarity_titles,'similarity':sorted_similarities})
    similarity_movies = similarity_movies.drop('title',axis=1)
    return similarity_movies


print(recommend('One Piece').head(10))

