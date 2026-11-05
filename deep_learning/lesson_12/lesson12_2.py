import numpy as np
import nltk
import networkx as nx
from scipy.spatial import distance
from nltk.tokenize import sent_tokenize
import re
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('stopwords')

def load_glove_model(glove_file):
    print(f"Loading GloVe model from {glove_file}...")
    glove_model = {}
    with open(glove_file, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')

            glove_model[word] = vector

    print(f"GloVe model loaded with {len(glove_model)} words.")

    return glove_model


!wget http://nlp.stanford.edu/data/glove.6B.zip