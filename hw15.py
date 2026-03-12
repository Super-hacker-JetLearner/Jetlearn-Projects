import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('titanic2.csv')

print(data)

mode = data['Embarked'].mode()[0]

# replacing_rule = SimpleImputer(missing_values=np.nan,strategy='constant',fill_value=mode)
# data['Embarked'] = replacing_rule.fit_transform(pd.DataFrame(data['Embarked']))
# print(type(replacing_rule.fit_transform(pd.DataFrame(data['Embarked']))))

data['Embarked'] = data['Embarked'].fillna(mode)

replacing_rule = SimpleImputer(strategy='mean')
data['Age'] = replacing_rule.fit_transform(pd.DataFrame(data['Age']))
# print(type(replacing_rule.fit_transform(pd.DataFrame(data['Age']))))

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
data['Sex'] = encoder.fit_transform(data['Sex'])


print(data)

gender_survival = data.groupby('Sex')['Survived'].mean()

print(gender_survival)

subplot = make_subplots(2,2,subplot_titles=['gender','passenger class','family size'])
subplot.add_traces(px.bar(gender_survival,x=gender_survival.index,y=gender_survival.values).data,rows=1,cols=1)




# pclass_survival = data.groupby(['Pclass','Survived'])

# print(pclass_survival.head())

# subplot.add_traces(px.area(pclass_survival,x=pclass_survival['Pclass'],y=pclass_survival['Survived'],line_group='Survived').data,rows=1,cols=2)

# subplot.show()

pclass_survival = pd.crosstab(data['Pclass'],data['Survived'])

subplot.add_traces(px.bar(pclass_survival,x=pclass_survival.index,y=pclass_survival[0]).data,rows=1,cols=2)
subplot.add_traces(px.bar(pclass_survival,x=pclass_survival.index,y=pclass_survival[1]).data,rows=1,cols=2)


subplot.update_layout(barmode='stack')

# add sibsp and parch together
family_size = data['SibSp'] + data['Parch']+1


family_survival = pd.crosstab(family_size,data['Survived'])

subplot.add_traces(px.bar(family_survival,x=family_survival.index,y=family_survival[0]).data,rows=2,cols=1)
subplot.add_traces(px.bar(family_survival,x=family_survival.index,y=family_survival[1]).data,rows=2,cols=1)


subplot.update_layout(barmode='stack')

subplot.show()