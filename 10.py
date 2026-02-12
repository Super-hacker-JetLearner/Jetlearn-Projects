import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('population.csv')

plt.figure(figsize=(15,7))

plt.suptitle('population dataset',fontsize=30)

plt.subplot(2,2,1)

top10 = data[data['Year']==2020].nlargest(10,columns='Value')
print(top10)



plt.bar(x=top10['Country Name'],height=top10['Value'])
plt.xticks(rotation=45)


plt.subplot(2,2,2)

plt.pie(top10['Value'],labels=top10['Country Name'])


plt.subplot(2,2,3)

all_countries = data.sort_values(by='Value',ascending=False)
all_countries = all_countries[~(all_countries['Country Name'].duplicated(keep='first'))]
# print(all_countries['Country Name'].duplicated(keep='last'))
# exit()
print(all_countries)

top3_countries = all_countries.head(3)
print('top3 countries')
print(top3_countries)
top3_countries_with_timeline = data[data['Country Name'].isin(top3_countries['Country Name'])]


print('timeline')
print(top3_countries_with_timeline)

top3_countries_with_timeline = top3_countries_with_timeline[(top3_countries_with_timeline['Year']>=1999) & (top3_countries_with_timeline['Year']<=2020)]

print(top3_countries_with_timeline)


plt.plot(top3_countries_with_timeline['Year'], top3_countries_with_timeline['Value'],label=top3_countries_with_timeline['Country Name'])
plt.xlabel('year')
plt.ylabel('population')
plt.title('top3 countries with timeline')













plt.tight_layout()
plt.show()