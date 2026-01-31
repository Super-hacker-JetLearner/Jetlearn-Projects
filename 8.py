import plotly as plt
import plotly.express as px
import pandas as pd
import os
os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')

data = pd.read_csv('covid_data.csv')
confirmed = data.groupby('Country_Region').sum().nlargest(10, 'Confirmed')['Confirmed']
deaths = data.groupby('Country_Region').sum().nlargest(10, 'Deaths')['Deaths']
recovered = data.groupby('Country_Region').sum().nlargest(10, 'Recovered')['Recovered']

graph = px.scatter(confirmed, x=confirmed.index, y='Confirmed',size='Confirmed', size_max=100, color=confirmed.index,title='top 10 countries by Confirmed Covid Cases')
# graph.show()
# # graph.write_html('graph',auto_open=True)
# graph.write_html('graph',auto_play=True,auto_open=True)

#make own color gradient
bar = px.bar(deaths, x=deaths.index, y='Deaths', color='Deaths', color_continuous_scale=['blue','red'],color_continuous_midpoint=250000, title='top 10 countries by death Covid Cases')
# bar.show()

#import color gradient
bar = px.bar(recovered, x=recovered.index, y='Recovered', color='Recovered', color_continuous_scale=px.colors.sequential.Viridis, title='top 10 countries by recovered Covid Cases')
# bar.show()



country = 'US'
country_data = data[data['Country_Region']=='US']
# print(country_data)
confirmed = country_data.nlargest(10, keep='all',columns='Confirmed')[['Province_State','Confirmed']]
# print(confirmed)
deaths = country_data.nlargest(10, keep='all',columns='Deaths')[['Province_State','Deaths']]
# print(deaths)
recovered = country_data.nlargest(10, keep='all',columns='Recovered')[['Province_State','Recovered']]
# print(recovered)







import plotly.graph_objects as go

confirmed_graph = px.bar(confirmed, x=confirmed['Province_State'], y='Confirmed', color=confirmed['Province_State'],title='top 10 countries by Confirmed Covid Cases')
deaths_graph = px.bar(deaths, x=deaths['Province_State'], y='Deaths', color=deaths['Province_State'],title='top 10 countries by death Covid Cases')

confirmed_graph.show()
deaths_graph.show()

figure = go.Figure(data=(confirmed_graph,deaths_graph))
figure.show()
