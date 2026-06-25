import nltk
import re
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/emotions_labels/emotion-labels-train.csv')
test = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/emotions_labels/emotion-labels-test.csv')



nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

word_lemmatizer = WordNetLemmatizer()
stopwords = set(stopwords.words('english'))

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
            
    lemmatized_test_text.append(" ".join(sentence_list))
    
    
# print(lemmatized_train_text[:50])
    
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(ngram_range=(1,2))

cv_train_text = cv.fit_transform(lemmatized_train_text)
cv_test_text = cv.transform(lemmatized_test_text)

from sklearn.ensemble import RandomForestClassifier

# print(cv_train_text)

# for i in range(200,300,10):

model = RandomForestClassifier(n_estimators=100)

model = model.fit(cv_train_text,train['label'])
# print(train['label'])

# predictions = model.predict(cv_test_text)
text = 'i laughed a lot because i was very cheerful because i went on amazing holidays'
cv_test_text = cv.transform([text])
predictions = model.predict(cv_test_text)
# print('here')
# print(predictions)
# print(test['label'])
# print(i)
# print(classification_report(test['label'],predictions))
print(f'the emotion is {predictions}')