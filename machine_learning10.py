import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# content recommendation
# based on the content
data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/movies_metadata.csv')

model = TfidfVectorizer()


data['overview'] = data['overview'].fillna(' ')


matrix = model.fit_transform(data['overview'])


sim_values = linear_kernel(matrix[:100],matrix[:100])

print(sim_values)

mov_idx = pd.Series(data.index, index=data["title"]).drop_duplicates()

def recommend(movie):
    idx = mov_idx[movie]
    similarities = sim_values[idx]
    list(enumerate(similarities))