#%% ################################## CODEBLOCK ##################################
from IPython import display
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

#%% ################################## CONFIG ##################################
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
#from visdom import Visdom
# service postgresql start/stop                           # /etc/postgresql/version/main/postgresql.conf
# python -m visdom.server -p 8097 --hostname 127.0.0.1
# rstudio-server start/stop/restart                       # /etc/rstudio/rserver.conf
config = {}
config['pgAdmin4-server'] = 'http://' + '127.0.0.1'
config['pgAdmin4-port'] = '52631'
config['visdom-server'] = 'http://' + '127.0.0.1'
config['visdom-port'] = '8097'
config['R-server'] = 'http://' + '127.0.0.1'
config['R-port'] = '8787'
config['dash-server'] = '127.0.0.1'
config['dash-port'] = '8050'
#vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever [-post, --hostname]
#vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

#%% ################################## REALTIME ##################################
@app.callback(
    Output("visdom-server", "children"),
    Input("real-time", "n_clicks"))
def real_time_analysis(click):
    return 'Real-Time Analysis is over.'
#%% ################################## DASHBOARD ##################################
class MetaClass(type):
    def __new__(cls, clsname, bases, namespace):
        namespace['__str__'] = lambda self: str(self.values)
        namespace['values'] = None
        return type.__new__(cls, clsname, bases, namespace)

Component = MetaClass('Component', (dict,), {})
TAB1 = Component()
TAB1.RC00 = Component()
TAB1.RC10 = Component()
TAB1.RC11 = Component()
TAB1.RC20 = Component()
TAB1.RC21 = Component()


TAB1.RC00.places = [[37.586786, 126.974736, '청와대(Cheong Wh Dae)', '서울(Seoul)', "종로구 세종로"],
                    [37.563184116699055, 126.97959495769867, '한국은행(BOk, Bank of Korea)', '서울(Seoul)', '중구 북창동'],
                   ]
TAB1.RC00.places = pd.DataFrame(TAB1.RC00.places)
TAB1.RC00.places.columns = ["latitude", "longitude", "landmark", "city", "districts"] 
Map = px.scatter_mapbox(TAB1.RC00.places,
                        lat="latitude",
                        lon="longitude",
                        hover_name="landmark",
                        hover_data=["city", "districts"],
                        color_discrete_sequence=["fuchsia"],
                        zoom=12,
                        height=700)
Map.update_layout(mapbox_style="open-street-map")
Map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
TAB1.RC00.values = dcc.Graph(figure=Map)
TAB1.RC10.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
TAB1.RC11.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
TAB1.RC20.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
TAB1.RC21.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD ##################################
T = {}
T['T,0,0'] = 'Map'
T['T,1,0'] = 'T__'
T['T,1,1'] = 'T__'
T['T,2,0'] = 'T__'
T['T,2,1'] = 'T__'
O = {}
O['T,_,_'] = None
O['T,0,0'] = TAB1.RC00.values
O['T,1,0'] = TAB1.RC10.values
O['T,1,1'] = TAB1.RC11.values
O['T,2,0'] = TAB1.RC20.values
O['T,2,1'] = TAB1.RC21.values
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader(T['T,0,0']), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader(T['T,1,0']), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader(T['T,1,1']), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
C['T,2,0'] = [dbc.Card([dbc.CardHeader(T['T,2,0']), dbc.CardBody(O['T,2,0'])], color='light', inverse=False, outline=True)]
C['T,2,1'] = [dbc.Card([dbc.CardHeader(T['T,2,1']), dbc.CardBody(O['T,2,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(C['T,0,0'], width=12)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,2,0'], width=6), dbc.Col(C['T,2,1'], width=6)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="PAGE1", disabled=False)])
main = dbc.Jumbotron([html.H2(html.A('WS0003', href="/")),
                      html.H6('Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Ailever", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/work-sheet/WS0003.py'),
                                dbc.Button("Notion", color="secondary", href="https://www.notion.so/WorkSheet-d64a1a09956d4318ac38b3d7f0131cfb"),
                                dbc.Button("pgAdmin4", color="secondary", href=config['pgAdmin4-server']+':'+config['pgAdmin4-port']),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## SETUP INFO ##################################
"""
[name] : -
[structure] : -
[version] : 0.0
[description] : -
[author] : anonym
[keywords] : map
"""    
