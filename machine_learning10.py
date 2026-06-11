import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/movies_metadata.csv')

model = TfidfVectorizer(stop_words='english')


data = data.drop_duplicates(subset='title', keep='first')
mov_idx = pd.Series(data.index, index=data['title'])

data['overview'] = data['overview'].fillna('').add(' ')

matrix = model.fit_transform(data['overview'])




def recommend(movie):
    idx = mov_idx[movie]
    similarities = linear_kernel(matrix[idx],matrix)
    movie_similarities = similarities.flatten()
    similarity_idxs = np.flip(np.argsort(movie_similarities))
    if idx in similarity_idxs:
        similarity_idxs = np.delete(similarity_idxs, np.where(similarity_idxs == idx))
    similarity_movies = mov_idx.iloc[similarity_idxs]
    return similarity_movies
    
    
print(recommend('Toy Story'))