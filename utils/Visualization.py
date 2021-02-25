#%%
################################## CONFIG ##################################
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--vs', type=str, default='127.0.0.1', help='visdom server')
parser.add_argument('--vp', type=str, default='8097', help='visdom port')
parser.add_argument('--rs', type=str, default='127.0.0.1', help='Rstudio server')
parser.add_argument('--rp', type=str, default='8787', help='Rstudio port')
parser.add_argument('--ds', type=str, default='127.0.0.1', help='dash server')
parser.add_argument('--dp', type=str, default='8050', help='dash port')
args = parser.parse_args()

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# rstudio-server start/stop/restart # /etc/rstudio/rserver.conf
# python -m visdom.server -p 8097 --hostname 127.0.0.1
config = {}
config['visdom-server'] = 'http://' + args.vs
config['visdom-port'] = args.vp
config['R-server'] = 'http://' + args.rs
config['R-port'] = args.rp
config['dash-server'] = args.ds
config['dash-port'] = args.dp
#import torch
#import torch.nn as nn
#from visdom import Visdom
#vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever [-post, --hostname]
#vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
################################## CONFIG ##################################
#%%
################################## CODEBLOCK ##################################
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
df
#%%
Figures = dict()

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
               fill_color='lavender',
               align='left'))
])

Figures['T7,0,0'] = px.treemap(
    names = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
)

df = px.data.tips()
Figures['T7,1,0'] = px.treemap(df, path=['day', 'time', 'sex'], values='total_bill')

################################## CODEBLOCK ##################################
#%%
################################## DASHBOARD ##################################
T = {}
T['T1,0,0'] = ''
T['T2,0,0'] = ''
T['T3,0,0'] = ''
T['T4,0,0'] = ''
T['T5,0,0'] = ''
T['T6,0,0'] = ''
T['T7,0,0'] = 'Tree Map'
T['T7,1,0'] = 'Tree Map'
T['T8,0,0'] = ''
O = {}
O['T,_,_'] = None
O['T1,0,0'] = dcc.Markdown("""""")
O['T2,0,0'] = dcc.Markdown("""""")
O['T3,0,0'] = dcc.Markdown("""""")
O['T4,0,0'] = dcc.Markdown("""""")
O['T5,0,0'] = dcc.Markdown("""""")
O['T6,0,0'] = dcc.Markdown("""""")
O['T7,0,0'] = dcc.Graph(figure=Figures['T7,0,0'])
O['T7,1,0'] = dcc.Graph(figure=Figures['T7,1,0'])
O['T8,0,0'] = dcc.Markdown("""""")
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,0,0']), dbc.CardBody(O['T1,0,0'])], color='light', inverse=False, outline=True)]
C['T2,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,0,0']), dbc.CardBody(O['T2,0,0'])], color='light', inverse=False, outline=True)]
C['T3,0,0'] = [dbc.Card([dbc.CardHeader(T['T3,0,0']), dbc.CardBody(O['T3,0,0'])], color='light', inverse=False, outline=True)]
C['T4,0,0'] = [dbc.Card([dbc.CardHeader(T['T4,0,0']), dbc.CardBody(O['T4,0,0'])], color='light', inverse=False, outline=True)]
C['T5,0,0'] = [dbc.Card([dbc.CardHeader(T['T5,0,0']), dbc.CardBody(O['T5,0,0'])], color='light', inverse=False, outline=True)]
C['T6,0,0'] = [dbc.Card([dbc.CardHeader(T['T6,0,0']), dbc.CardBody(O['T6,0,0'])], color='light', inverse=False, outline=True)]
C['T7,0,0'] = [dbc.Card([dbc.CardHeader(T['T7,0,0']), dbc.CardBody(O['T7,0,0'])], color='light', inverse=False, outline=True)]
C['T7,1,0'] = [dbc.Card([dbc.CardHeader(T['T7,1,0']), dbc.CardBody(O['T7,1,0'])], color='light', inverse=False, outline=True)]
C['T8,0,0'] = [dbc.Card([dbc.CardHeader(T['T8,0,0']), dbc.CardBody(O['T8,0,0'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab1'] = [dbc.Row([dbc.Col(C['T1,0,0'], width=12)]), html.Br(),
                            html.Br()]
contents['page']['tab2'] = [dbc.Row([dbc.Col(C['T2,0,0'], width=12)]), html.Br(),
                            html.Br()]
contents['page']['tab3'] = [dbc.Row([dbc.Col(C['T3,0,0'], width=12)]), html.Br(),
                            html.Br()]
contents['page']['tab4'] = [dbc.Row([dbc.Col(C['T4,0,0'], width=12)]), html.Br(),
                            html.Br()]
contents['page']['tab5'] = [dbc.Row([dbc.Col(C['T5,0,0'], width=12)]), html.Br(),
                            html.Br()]
contents['page']['tab6'] = [dbc.Row([dbc.Col(C['T6,0,0'], width=12)]), html.Br(),
                            html.Br()]
contents['page']['tab7'] = [dbc.Row([dbc.Col(C['T7,0,0'], width=12)]), html.Br(),
                            dbc.Row([dbc.Col(C['T7,1,0'], width=12)]), html.Br(),
                            html.Br()]
contents['page']['tab8'] = [dbc.Row([dbc.Col(C['T8,0,0'], width=12)]), html.Br(),
                            html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="Table", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2'])), label="Line&Scatter", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab3'])), label="Bar Chart", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab4'])), label="Matrix Plot", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab5'])), label="Pie/Polar Chart", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab6'])), label="Parallel/Sankey Diagram", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab7'])), label="Tree Map/Sunbrust Chart", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab8'])), label="Dendrogram/Network", disabled=False),
                                 ])
main = dbc.Jumbotron([html.H2('utils/Visualization'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("GitHub", color="secondary", href='https://github.com/ailever/ailever/tree/master/ailever/analysis'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/utils/Visualization.py'),
                                dbc.Button("Wiki", color="secondary", href='https://github.com/ailever/ailever/wiki'),
                                dbc.Button("Google Trend", color="secondary", href="https://trends.google.com/trends/explore"),
                                dbc.Button("DataLab", color="secondary", href="https://datalab.naver.com/"),
                                dbc.Button('Kakao Map', color='secondary', href="https://map.kakao.com/"),
                                dbc.Button('Google Map', color='secondary', href="https://www.google.co.kr/maps/"),
                                dbc.Button("Plotly", color="secondary", href="https://plotly.com/python/"),
                                dbc.Button("Docs", color="secondary", href='https://ailever.readthedocs.io/en/latest/detection/index.html'),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
