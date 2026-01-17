import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

titanic = pd.read_csv('titanic.csv')

#Plot the bar graphs of total number of men and women on the titanic, average fare of men and women, titanic dataset should be interpreted to complete this task.

# men, women = titanic['Sex'].value_counts()
men, women = titanic['Sex'].value_counts()
print(men, women)

plt.bar(['Men','Women'],[men,women], color=['b','r'])
plt.show()


#average fare of men and women
men_fare = titanic[titanic['Sex'] == 'male']['Fare'].mean()
women_fare = titanic[titanic['Sex'] == 'female']['Fare'].mean()

plt.bar(['Men','Women'],[men_fare,women_fare], color=['b','r'])
plt.show()