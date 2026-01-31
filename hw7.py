import pandas as pd
import os
os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('covid_data.csv')
# grouped_data = data.groupby('Country_Region').sum().nlargest(10, ['Confirmed','Deaths','Recovered'])
# print(grouped_data)
# exit()
# top_10_confirmed = grouped_data.sort_values(by='Confirmed', ascending=False).head(10)
# top_10_deaths = grouped_data.sort_values(by='Deaths', ascending=False).head(10)
# top_10_recovered = grouped_data.sort_values(by='Recovered', ascending=False).head(10)
# print("Top 10 countries by confirmed cases:")
# print(top_10_confirmed[['Confirmed']])
# print("\nTop 10 countries by death:")
# print(top_10_deaths[['Deaths']])
# print("\nTop 10 countries recovered:")
# print(top_10_recovered[['Recovered']])

confirmed = data.groupby('Country_Region').sum().nlargest(10, 'Confirmed')['Confirmed']
print(confirmed)
deaths = data.groupby('Country_Region').sum().nlargest(10, 'Deaths')['Deaths']
print(deaths)
recovered = data.groupby('Country_Region').sum().nlargest(10, 'Recovered')['Recovered']
print(recovered)