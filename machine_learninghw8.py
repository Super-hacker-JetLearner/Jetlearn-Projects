import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


data = pd.read_csv('/Users/s932172@aics.espritscholen.nl/Desktop/game development/machine_learning/winequality-red.csv')

X = data.drop('quality',axis=1)
Y = data['quality']



x_scaler = StandardScaler()
X = x_scaler.fit_transform(X)

preprocessor = PCA(9)
X = preprocessor.fit_transform(X,Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y,random_state=312)


model = svm.SVC(kernel='linear')
model.fit(X_train,Y_train)
 
predictions = model.predict(X_test)

print(Y_test)
print(predictions)

print(classification_report(Y_test,predictions))
matrix = confusion_matrix(Y_test,predictions)

sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds')
plt.show()




forest = RandomForestClassifier(n_estimators=30,random_state=253)
forest.fit(X_train,Y_train)
predictions = forest.predict(X_test)
print(classification_report(Y_test,predictions))
matrix = confusion_matrix(Y_test,predictions)

sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds')
plt.show()




logistic_regr = LinearRegression()
logistic_regr.fit(X_train,Y_train)
predictions = logistic_regr.predict(X_test)
# print(classification_report(Y_test,predictions))
# matrix = confusion_matrix(Y_test,predictions)
print(mean_absolute_error(Y_test,predictions))

sns.heatmap(matrix, annot=True, fmt='d', cmap='Reds')
plt.show()


