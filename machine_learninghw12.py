import nltk
import re
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder



train = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/LanguageDetection.csv')

encoder = LabelEncoder()

train['Language'] = encoder.fit_transform(train['Language'])



nltk.download('stopwords')
nltk.download('wordnet')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

word_lemmatizer = WordNetLemmatizer()
stopwords = set(stopwords.words('english'))

lemmatized_train_text = []
for sentence in train['Text']:
    sentence_list = []
    words = re.sub(r'[^a-zA-Z]',' ',str(sentence))
    words = words.lower()
    words = words.split()
    for word in words:
        if word not in stopwords:
            lemmatized_word = word_lemmatizer.lemmatize(word)
            sentence_list.append(lemmatized_word)
            
    lemmatized_train_text.append(" ".join(sentence_list))
    
    

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(ngram_range=(1,2))

cv_train_text = cv.fit_transform(lemmatized_train_text)


from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model = model.fit(cv_train_text,train['Language'])

test_text = 'Jeg lyttede ikke til en anden sætning, som jeg bruger hele tiden.'
cv_test_text = cv.transform([test_text])

predictions = model.predict(cv_test_text)

print('language is ',encoder.inverse_transform(predictions))

 