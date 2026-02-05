import plotly as plt
import plotly.express as px
import pandas as pd
import os
os.chdir('/Users/s932172@aics.espritscholen.nl/Desktop/game development/data science')


data = pd.read_csv('covid_data.csv')

country = 'India'
country_data = data[data['Country_Region']==country]
confirmed_india = country_data.nlargest(10, keep='all',columns='Confirmed')[['Province_State','Confirmed']]
deaths_india = country_data.nlargest(10, keep='all',columns='Deaths')[['Province_State','Deaths']]

country = 'Brazil'
country_data = data[data['Country_Region']==country]
confirmed_brazil = country_data.nlargest(10, keep='all',columns='Confirmed')[['Province_State','Confirmed']]
deaths_brazil = country_data.nlargest(10, keep='all',columns='Deaths')[['Province_State','Deaths']]

import plotly.graph_objects as go

# india
confirmed_india_graph = px.bar(confirmed_india, x=confirmed_india['Province_State'], y='Confirmed', color=confirmed_india['Province_State'],title='top 10 states of india by confirmed cases')
deaths_india_graph = px.bar(deaths_india, x=deaths_india['Province_State'], y='Deaths', color=deaths_india['Province_State'],title='top 10 states of india by death cases')

confirmed_india_graph.show()
deaths_india_graph.show()

# brazil
confirmed_brazil_graph = px.bar(confirmed_brazil, x=confirmed_brazil['Province_State'], y='Confirmed', color=confirmed_brazil['Province_State'],title='top 10 states of brazil by confirmed cases')
deaths_brazil_graph = px.bar(deaths_brazil, x=deaths_brazil['Province_State'], y='Deaths', color=deaths_brazil['Province_State'],title='top 10 states of brazil by death cases')

confirmed_brazil_graph.show()
deaths_brazil_graph.show()

# print(type(confirmed_brazil_graph))
# print(type(plt.graph_objs.Bar()))


# # confirmed
# confirmed_graph = go.Figure(data=(confirmed_india_graph,confirmed_brazil_graph))
# confirmed_graph.show()

# print(type(plt.graph_objs.Bar()))

"homework: also display top states in brazil and india for total cases and deaths"