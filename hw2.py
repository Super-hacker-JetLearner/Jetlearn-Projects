import pandas as pd
import os

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

titanic = pd.read_csv('titanic.csv')
print(titanic.head())

died = titanic[titanic['Survived']==0]
print(died[['Sex','Age']].groupby('Sex').mean())
print(died[['Sex','Age']].groupby('Sex').median())


iris = pd.read_csv('iris.csv')
print(iris.head())
print(iris.info())

print(iris['sepal_length'].describe())
print(iris['sepal_width'].describe())
print(iris['petal_length'].describe())
print(iris['petal_width'].describe())

print(iris.groupby('species')['species'].count())