#%%
################################## CODEBLOCK ##################################
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import pandas as pd

Figure = type('Figure', (dict,), {}) 
figure = Figure()
levels = {}
levels[1] = ([5,5,5,5,5], ['L1-1', 'L1-2', 'L1-3', 'L1-4', 'L1-5'])
levels[2] = ([5,5,5], ['L2-1', 'L2-2', 'L2-3'])
levels[3] = ([5,5,5,5], ['L3-1', 'L3-2', 'L3-3', 'L3-4'])
levels[4] = ([7,3], ['L4-1', 'L3-2'])

ratios = {}
labels = {}
for level, sector in levels.items():
    ratios[level] = sector[0]
    labels[level] = sector[1]

shape = (100,1+len(ratios))
graphing_data = np.random.uniform(0,1,shape).astype(np.object)
graphing_data[:,0] = 1

for level in levels.keys():
    ratio = ratios[level]
    label = labels[level]
    gd = graphing_data[:,level]

    c_ = 0
    idx_set = []
    spliter = np.cumsum(np.exp(ratio)/np.exp(ratio).sum())
    for i, c in enumerate(spliter):
        idx = np.where((gd>c_)&(gd<c))[0]
        idx_set.append(idx)
        c_ = c
    for idx, l in zip(idx_set, label):
        graphing_data[idx,level] = l

df = pd.DataFrame(graphing_data)
alphabets = 'ABCDEFGHIZKLMNOPQRSTUVWXYZ'
columns = ['Base']
path = []
for level in ratios.keys():
    sector = f'Sector {alphabets[level]}'
    columns.append(sector)
    path.append(sector)
df.columns = columns

figure['T1,0,0'] = px.sunburst(df, path=path, values='Base')
figure['T1,1,0'] = px.treemap(df, path=path, values='Base')
################################## CODEBLOCK ##################################
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
################################## DASHBOARD ##################################
T = {}
T['T1,0,0'] = 'Sunburst Chart'
T['T1,1,0'] = 'Tree Map'
O = {}
O['T,_,_'] = None
O['T1,0,0'] = dcc.Graph(figure=figure['T1,0,0'])
O['T1,1,0'] = dcc.Graph(figure=figure['T1,1,0'])
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,0,0']), dbc.CardBody(O['T1,0,0'])], color='light', inverse=False, outline=True)]
C['T1,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,1,0']), dbc.CardBody(O['T1,1,0'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab1'] = [dbc.Row([dbc.Col(C['T1,0,0'], width=12)]), html.Br(),
                            dbc.Row([dbc.Col(C['T1,1,0'], width=12)]), html.Br(),
                            html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="Part to Whole Charts", disabled=False)])
main = dbc.Jumbotron([html.H2('analysis'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/tree/master/analysis'),
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
