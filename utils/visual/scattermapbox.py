#%% ################################## CODEBLOCK ##################################
from IPython import display
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np


#%% ################################## CONFIG ##################################
import argparse
parser = argparse.ArgumentParser(description="set your environment")
parser.add_argument('--HostDash', type=str, required=False, default='PassToken', help="Host : Dashboard")
parser.add_argument('--PortDash', type=str, required=False, default='PassToken', help="Port : Dashboard")
parser.add_argument('--HostDB', type=str, required=False, default='PassToken', help="Host : DataBase")
parser.add_argument('--PortDB', type=str, required=False, default='PassToken', help="Port : DataBase")
parser.add_argument('--HostRV', type=str, required=False, default='PassToken', help="Host : Real-time Visualization")
parser.add_argument('--PortRV', type=str, required=False, default='PassToken', help="Port : Real-time Visualization")
parser.add_argument('--HostR', type=str, required=False, default='PassToken', help="Host : language R")
parser.add_argument('--PortR', type=str, required=False, default='PassToken', help="Port : language R")
args = parser.parse_args()
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
#from visdom import Visdom
# service postgresql start/stop                           # /etc/postgresql/version/main/postgresql.conf
# python -m visdom.server -p 8097 --hostname 127.0.0.1
# rstudio-server start/stop/restart                       # /etc/rstudio/rserver.conf
config = {}
config['dash-server'] = args.HostDash if args.HostDash != 'PassToken' else '127.0.0.1'
config['dash-port'] = args.PortDash if args.PortDash != 'PassToken' else '8050'
config['pgAdmin4-server'] = args.HostDB if args.HostDB != 'PassToken' else 'http://' + '127.0.0.1'
config['pgAdmin4-port'] = args.PortDB if args.PortDB != 'PassToken' else '52631'
config['visdom-server'] = args.HostRV if args.HostRV != 'PassToken' else 'http://' + '127.0.0.1'
config['visdom-port'] = args.PortRV if args.PortRV != 'PassToken' else '8097'
config['R-server'] = args.HostR if args.HostR != 'PassToken' else 'http://' + '127.0.0.1'
config['R-port'] = args.PortR if args.PortR != 'PassToken' else '8787'
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
################################## DASHBOARD : TAB1, ROW0, COL0 ##################################
fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon = [10, 20, 30],
    lat = [10, 20,30],
    marker = {'size': 10}))

fig.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [-50, -60,40],
    lat = [30, 10, -20],
    marker = {'size': 10}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})
TAB1.RC00.values = dcc.Graph(figure=fig)
################################## DASHBOARD : TAB1, ROW1, COL0 ##################################
TAB1.RC10.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB1, ROW1, COL1 ##################################
TAB1.RC11.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB1, ROW2, COL0 ##################################
TAB1.RC20.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB1, ROW2, COL1 ##################################
TAB1.RC21.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD ##################################
T = {}
T['T,0,0'] = 'T__'
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
main = dbc.Jumbotron([html.H2(html.A('scattermapbox', href="/")),
                      html.H6('Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Ailever", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/utils/visual/scattermapbox.py'),
                                dbc.Button("Notion", color="secondary", href="https://www.notion.so/UTILS-VISUAL-92f5f296304a4db4be3fd63135230c14"),
                                dbc.Button("pgAdmin4", color="secondary", href=config['pgAdmin4-server']+':'+config['pgAdmin4-port']),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.Div([dbc.Button('dash-html', color='dark', href="https://dash.plotly.com/dash-html-components/"),
                                dbc.Button('dash-core', color='dark', href="https://dash.plotly.com/dash-core-components"),
                                dbc.Button('dash-bootstrap', color='dark', href="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/"),
                                dbc.Button('plotly', color='dark', href="https://plotly.com/python/"),
                                dbc.Button('plotly-ref', color='dark', href="https://plotly.com/python-api-reference/"),
                                dbc.Button('updating figure', color='dark',  href="https://plotly.com/python/creating-and-updating-figures/"),                                
                                dbc.Button('API(GO)', color='danger', href="https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scattermapbox.html"),
                                dbc.Button('API(PX)', color='danger', href="https://plotly.com/python-api-reference/generated/plotly.express.scatter_mapbox.html"),                                
                                dbc.Button('Example', color='danger', href="https://plotly.com/python/lines-on-mapbox/"),
                                ]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## SETUP INFO ##################################
"""
[name] : scattermapbox
[structure] : utils/visual
[version] : 0.0
[description] : -
[author] : anonym
[keywords] : -
"""    
