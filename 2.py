import pandas as pd
import os

folder_path = '/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science'

os.chdir(folder_path)


data = pd.DataFrame({'name':['John','Jack','Joe','Jane'], 'age':[1,2,3,4], 'city':['Amsterdam', 'Berlin', 'Washington D.C.', 'London']})
print(data)
print(data.head(3)) #top rows

print(data.shape) #rows,columns

print(data.info()) #detailed information

print(data.dtypes) #data types of data

print(data['name']) #getting one column
print(data['name'].head()) # getting one column top rows

print(data['age'].max()) #get max of column

print(data.describe()) #shows important numbers about numerical data e.g. count, min, max, 25%, etc.

titanic = pd.read_csv('titanic.csv')

print(titanic)
print(titanic.head())

print(titanic['Name'].head())
print(titanic['Age'].head())
print(titanic[['Age','Name']].head()) #select more than one, give list of columns
print(titanic[titanic['Age'] >35].head())

print(titanic[(titanic['Pclass'] == 2) | (titanic['Pclass'] ==3)].head()) #use brackets

pclass1_male = titanic[(titanic['Pclass']==1) & (titanic['Sex']=='male')]
print(pclass1_male.head())

print(pclass1_male['Fare'].mean())

pclass3_female = titanic[(titanic['Pclass']==3) & (titanic['Sex']=='female')]
print(pclass3_female.head())

print(pclass3_female['Fare'].mean())

print(titanic.iloc[2:4, 3:5]) #slicing high is excluded. row first

adults = titanic[titanic['Age'] >=18]
print(adults[['Age','Name']].head())

adults = titanic.loc[titanic['Age']>=18, ["Age","Name"]] #display the names and ages of people who's age is greater than 18
print(adults)

titanic.iloc[0:2, 2:3] = 'Bartosz' #set values
print(titanic.head())
titanic.to_csv('titanic_changed.csv') #save to file

titanic = pd.read_csv('titanic_changed.csv')
print(titanic.head())

titanic['test'] = titanic['Fare']+10 #add new column

print(titanic.head())

print(titanic['Age'].mean())

male = titanic[titanic['Sex']=='male']
female = titanic[titanic['Sex']=='female']

print(male['Age'].mean())
print(female['Age'].mean())

print(titanic[['Sex','Age']].groupby('Sex').mean())

print(titanic[['Sex','Pclass','Fare']].groupby(['Pclass','Sex']).mean()) #groupby multiple columns

