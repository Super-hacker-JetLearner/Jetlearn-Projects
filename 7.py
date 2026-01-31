import pandas as pd
import os

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('covid_data.csv')
print(data.head())


countries:dict[str,list[int]] = {}
i = 0
while True:
    try:
        row = data.iloc[i,:]
    except:
        break
    if row['Country_Region'] in countries:
        countries[row['Country_Region']][0] += row['Confirmed']
        countries[row['Country_Region']][0] += row['Recovered']
        countries[row['Country_Region']][0] += row['Deaths']
    else:
        countries[row['Country_Region']] = [row['Confirmed'],row['Recovered'],row['Deaths']]
        
    i += 1
        
        

print(countries.keys())
print(countries.values())


"homework: top 10 most affected countries (confirmed,death and recovered) using covid data"
"use groupby and sum"