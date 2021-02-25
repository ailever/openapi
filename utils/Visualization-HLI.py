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


#%%
Figures = dict()

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
T['T7,0,0'] = ''
T['T7,1,0'] = ''
T['T8,0,0'] = ''
T['T9,0,0'] = ''
T['T10,0,0'] = ''
T['T11,0,0'] = ''
O = {}
O['T,_,_'] = None
O['T1,0,0'] = dcc.Markdown("""""")
O['T2,0,0'] = dcc.Markdown("""""")
O['T3,0,0'] = dcc.Markdown("""""")
O['T4,0,0'] = dcc.Markdown("""""")
O['T5,0,0'] = dcc.Markdown("""""")
O['T6,0,0'] = dcc.Markdown("""""")
O['T7,0,0'] = dcc.Markdown("""""")
O['T7,1,0'] = dcc.Markdown("""""")
O['T8,0,0'] = dcc.Markdown("""""")
O['T9,0,0'] = dcc.Markdown("""""")
O['T10,0,0'] = dcc.Markdown("""""")
O['T11,0,0'] = dcc.Markdown("""""")
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
C['T9,0,0'] = [dbc.Card([dbc.CardHeader(T['T9,0,0']), dbc.CardBody(O['T9,0,0'])], color='light', inverse=False, outline=True)]
C['T10,0,0'] = [dbc.Card([dbc.CardHeader(T['T10,0,0']), dbc.CardBody(O['T10,0,0'])], color='light', inverse=False, outline=True)]
C['T11,0,0'] = [dbc.Card([dbc.CardHeader(T['T11,0,0']), dbc.CardBody(O['T11,0,0'])], color='light', inverse=False, outline=True)]
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
contents['page']['tab9'] = [dbc.Row([dbc.Col(C['T9,0,0'], width=12)]), html.Br(),
                            html.Br()]
contents['page']['tab10'] = [dbc.Row([dbc.Col(C['T10,0,0'], width=12)]), html.Br(),
                             html.Br()]
contents['page']['tab11'] = [dbc.Row([dbc.Col(C['T11,0,0'], width=12)]), html.Br(),
                             html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="Basics", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2'])), label="Part of Whole", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab3'])), label="1D Distributions", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab4'])), label="2D Distributions", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab5'])), label="Matrix Input", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab6'])), label="3-Dimensional", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab7'])), label="Multidimensional", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab8'])), label="Tile Maps", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab9'])), label="Outline Maps", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab10'])), label="Polar Charts", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab11'])), label="Ternary Charts", disabled=False),
                                 ])
main = dbc.Jumbotron([html.H2('utils/Visualization - High Level Interface(express)'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/utils/Visualization-HLI.py'),
                                dbc.Button("Google Trend", color="secondary", href="https://trends.google.com/trends/explore"),
                                dbc.Button("DataLab", color="secondary", href="https://datalab.naver.com/"),
                                dbc.Button('Kakao Map', color='secondary', href="https://map.kakao.com/"),
                                dbc.Button('Google Map', color='secondary', href="https://www.google.co.kr/maps/"),
                                dbc.Button("Plotly", color="secondary", href="https://plotly.com/python/"),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
