#%%
import plotly.graph_objects as go

top_labels = ['C1', 'C2', 'C3', 'C4', 'C5']
x_data = [[21, 30, 21, 16, 12],
          [24, 31, 19, 15, 11],
          [27, 26, 23, 11, 13],
          [29, 24, 15, 18, 14]]

y_data = ['R1',
          'R2',
          'R3',
          'R4']

colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)',
          'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
          'rgba(190, 192, 213, 1)']

fig = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=80),
    showlegend=False,
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=14,
                                      color='rgb(67, 67, 67)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations)


#%% ################################## CODEBLOCK ##################################
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import pandas as pd

Figure = type('Figure', (dict,), {}) 
figure = Figure()
figure['T1,2,0'] = fig

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

#%% ################################## CONFIG ##################################
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

#%% ################################## DASHBOARD ##################################
T = {}
T['T1,0,0'] = 'Sunburst Chart'
T['T1,1,0'] = 'Tree Map'
T['T1,2,0'] = 'Tree Map'
O = {}
O['T,_,_'] = None
O['T1,0,0'] = dcc.Graph(figure=figure['T1,0,0'])
O['T1,1,0'] = dcc.Graph(figure=figure['T1,1,0'])
O['T1,2,0'] = dcc.Graph(figure=figure['T1,2,0'])
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,0,0']), dbc.CardBody(O['T1,0,0'])], color='light', inverse=False, outline=True)]
C['T1,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,1,0']), dbc.CardBody(O['T1,1,0'])], color='light', inverse=False, outline=True)]
C['T1,2,0'] = [dbc.Card([dbc.CardHeader(T['T1,2,0']), dbc.CardBody(O['T1,2,0'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab1'] = [dbc.Row([dbc.Col(C['T1,0,0'], width=12)]), html.Br(),
                            dbc.Row([dbc.Col(C['T1,1,0'], width=12)]), html.Br(),
                            dbc.Row([dbc.Col(C['T1,2,0'], width=12)]), html.Br(),
                            html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="Part to Whole Charts", disabled=False)])
main = dbc.Jumbotron([html.H2('analysis - review'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/tree/master/analysis/review.py'),
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
