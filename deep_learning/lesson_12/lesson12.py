import numpy as np
import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from scipy.sparse import triu
from gensim.models import Word2Vec
from scipy import spatial
import networkx as nx

nltk.download('punkt_tab')
nltk.download('stopwords')

text = """What is Artificial Intelligence?
Artificial Intelligence, widely known as AI, is a rapidly evolving branch of computer science dedicated to building machines and software capable of simulating human intelligence. At its core, AI seeks to empower computers to perform complex tasks that traditionally require human cognition, such as reasoning, learning from experience, solving problems, recognizing speech, and understanding visual information.

Unlike traditional software that follows strict, pre-written rules and linear instructions, modern AI systems—particularly those powered by machine learning and deep neural networks—learn dynamically from vast quantities of data. By analyzing this data, algorithms identify hidden patterns, form predictions, and adapt their behavior independently without human intervention. This shift allows technology to evolve and improve over time based on new experiences.

The applications of AI are vast and deeply integrated into our modern world. In everyday life, we encounter AI through smartphone voice assistants, personalized streaming recommendations, predictive text keyboards, and automated navigation apps. In professional and academic fields, AI accelerates scientific research, assists in diagnosing medical conditions, optimizes supply chains, and fuels creative tools in art, music, and writing.

Ultimately, AI serves as a powerful collaborative tool designed to augment human potential. As it continues to advance, understanding how AI works, recognizing its limitations, and ensuring it is developed responsibly are essential skills for shaping a positive technological future."""

sentences = sent_tokenize(text)

sentences_clean = [re.sub(r'[^\w\s]', '', sentence.lower()) for sentence in sentences]

stop_words = stopwords.words('english')
sentence_tokens = [[word for word in sentence.split(' ') if word not in stop_words] for sentence in sentences_clean]
print(sentence_tokens)

w2v = Word2Vec(
    sentence_tokens,
    vector_size=1,
    min_count=1,
    epochs=1000
)

sentence_embeddings = [[w2v.wv[word][0] for word in words] for words in sentence_tokens]

max_len = max([len(tokens) for tokens in sentence_tokens])

sentence_embeddings = [np.pad(embedding, (0,max_len-len(embedding)), 'constant') for embedding in sentence_embeddings]

similarity_matrix = np.zeros([len(sentence_tokens), len(sentence_tokens)])

for i, row_embedding in enumerate(sentence_embeddings):
    for j, column_embedding in enumerate(sentence_embeddings):
        similarity_matrix[i][j] = 1 - spatial.distance.cosine(row_embedding, column_embedding)

nx_graph = nx.from_numpy_array(similarity_matrix)

scores = nx.pagerank(nx_graph)
print(scores)

top_sentence = {sentence: scores[index] for index,sentence in enumerate(sentences)}

top = dict(sorted(top_sentence.items(),key=lambda x: x[1], reverse=True)[:4])

for sent in sentences:
    if sent in top.keys():
        print(sent)


