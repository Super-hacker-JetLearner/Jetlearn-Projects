import pandas as pd
import plotly.express as px
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots

os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('filtered_population.csv')

top10 = data[data['Year']==2020].nlargest(30,columns='Value')
print(top10['Country Name'])

subplots = make_subplots(2,2,subplot_titles=['top3 countries timeline from 2000 to 2020','bar graph of population of top 10 countries','pie chart by population of top 10 countries','something'],specs=[[{},{}],[{'type':'domain'},{}]])


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
    print(timeline)
    subplots.add_trace(go.Scatter(x=timeline['Year'],y=timeline['Value'],name=country),row=1,col=1)
    





subplots.add_trace(go.Bar(x=top10['Country Name'],y=top10['Value'],marker=dict(color=top10['Value'], colorscale='Viridis')),row=1,col=2)



subplots.add_trace(go.Pie(values=top10['Value'],labels=top10['Country Name']),col=1,row=2)




























subplots.show()



