import nltk
import re
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


train = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/emotions_for_nlp/train.txt',delimiter=';',names=['text','labels'])

test = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/emotions_for_nlp/test.txt',delimiter=';',names=['text','labels'])

train['labels'] = train['labels'].replace({'joy':1,'love':1,'surprise':1,'fear':0,'anger':0,'sadness':0})
test['labels'] = test['labels'].replace({'joy':1,'love':1,'surprise':1,'fear':0,'anger':0,'sadness':0})



nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

word_lemmatizer = WordNetLemmatizer()
stopwords = set(stopwords.words('english'))

# re can be used to clean data, but this data is already cleaned

lemmatized_train_text = []
for sentence in train['text']:
    sentence_list = []
    words = re.sub(r'[^a-zA-Z]',' ',str(sentence))
    words = words.lower()
    words = words.split()
    for word in words:
        if word not in stopwords:
            lemmatized_word = word_lemmatizer.lemmatize(word)
            sentence_list.append(lemmatized_word)
            
    lemmatized_train_text.append(" ".join(sentence_list))

lemmatized_test_text = []
for sentence in test['text']:
    sentence_list = []
    words = re.sub(r'[^a-zA-Z]',' ',str(sentence))
    words = words.lower()
    words = words.split()
    for word in words:
        if word not in stopwords:
            lemmatized_word = word_lemmatizer.lemmatize(word)
            sentence_list.append(lemmatized_word)
            
    lemmatized_test_text.append(" ".join(lemmatized_word))
    
    

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(ngram_range=(1,2))

cv_train_text = cv.fit_transform(lemmatized_train_text)
cv_test_text = cv.transform(lemmatized_test_text)


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model = model.fit(cv_train_text,train['labels'])

predictions = model.predict(cv_test_text)

print(classification_report(test['labels'],predictions))

