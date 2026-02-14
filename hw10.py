import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')





eliminated_words = ['world','ibrd','income','dividend','ida','asia','pacific','europe','oecd','sub-saharan','countries','situations','africa eastern','latin america','middle east','north africa','africa western','africa central','north america','euro area']



data = pd.read_csv('filtered_population.csv')


# for word in eliminated_words:
#     data = data[~data['Country Name'].str.contains(word,case=False)]
    

# data.to_csv('filtered_population.csv')


plt.figure(figsize=(15,7))

top10 = data[data['Year']==2020].nlargest(30,columns='Value')
print(top10['Country Name'])


top3 = top10.head(3)
# 2000 to 2020
top3_with_timeline = data[(data['Country Name'].isin(top3['Country Name'])) & (data['Year']>=2000) & (data['Year']<=2020)]

print(top3_with_timeline)
# top3_with_timeline = top3_with_timeline.sort_values(by='Country Name')
unique_countries = top3_with_timeline['Country Name'].unique()
countries_timelines = {}
for country in unique_countries:
    country_data = top3_with_timeline[top3_with_timeline['Country Name'] == country]
    countries_timelines[country] = country_data
    

for country, timeline in countries_timelines.items():
    plt.plot(timeline['Year'], timeline['Value'], label=country,marker='o')
    
plt.xlabel('year')
plt.ylabel('population')
plt.title('top3 countries with timeline')
plt.legend()
plt.show()