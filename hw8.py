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
confirmed_india_graph = go.Bar(x=confirmed_india['Province_State'], y=confirmed_india['Confirmed'], name='top 10 states of india by confirmed cases')
deaths_india_graph = go.Bar(x=deaths_india['Province_State'], y=deaths_india['Deaths'], name='top 10 states of india by death cases')

# confirmed_india_graph.show()
# deaths_india_graph.show()

# brazil
confirmed_brazil_graph = go.Bar(x=confirmed_brazil['Province_State'], y=confirmed_brazil['Confirmed'] ,name='top 10 states of brazil by confirmed cases')
deaths_brazil_graph = go.Bar(x=deaths_brazil['Province_State'], y=deaths_brazil['Deaths'], name='top 10 states of brazil by death cases')

# confirmed_brazil_graph.show()
# deaths_brazil_graph.show()


# confirmed_graph = go.Figure(data=(confirmed_india_graph,confirmed_brazil_graph))
# confirmed_graph.show()


india_graph = go.Figure(data=(confirmed_india_graph,deaths_india_graph))
india_graph.show()


brazil_graph = go.Figure(data=(confirmed_brazil_graph,deaths_brazil_graph))
brazil_graph.update_layout(title='confirmed and deaths in states in brazil',barmode='stack')
brazil_graph.show()



"homework: also display top states in brazil and india for total cases and deaths"