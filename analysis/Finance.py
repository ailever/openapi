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
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

#vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever [-post, --hostname]
#vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
################################## CONFIG ##################################
#%%
################################## CODEBLOCK ##################################


# O[T,0,0] : Map
data = {}
data["latitude"] = [37.586786]
data["longitude"] = [126.974736]
data["landmark"] = ['cheongwhdae']
data["city"] = ['seoul']

df = pd.DataFrame(data)
#df.to_csv('file.csv')
#df = pd.read_csv("https://raw.githubusercontent.com/ailever/openapi/master/analysis/file.csv")
Map = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="landmark", hover_data=["city"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
Map.update_layout(mapbox_style="open-street-map")
Map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# O[T,0,0] : Tower Research
TR = """
[Home](https://www.tower-research.com/)
"""

# O[T,0,1] : KCG
KCG = """
"""

# O[T,1,0] : PDT Partners
PDT = """
"""

# O[T,1,1] : Citadel
Cit = """
"""

# O[T,2,0] : Two Sigma
TS = """
"""

# O[T,2,1] : IMC
IMC = """
"""

# O[T,3,0] : Hudson River Trading
HRT = """
"""

# O[T,3,1] : Jane Street
JS = """
"""


################################## CODEBLOCK ##################################
#%%
################################## DASHBOARD ##################################
T = {}
T['T,0,0'] = 'Map'
T['T,0,1'] = 'KCG'
T['T,1,0'] = 'PDT Partners'
T['T,1,1'] = 'Citadel'
T['T,2,0'] = 'Two Sigma'
T['T,2,1'] = 'IMC'
T['T,3,0'] = 'Hudson River Trading'
T['T,3,1'] = 'Jane Street'
O = {}
O['T,_,_'] = None
O['T,0,0'] = dcc.Graph(figure=Map)
O['T,0,1'] = dcc.Markdown(KCG)
O['T,1,0'] = dcc.Markdown(PDT)
O['T,1,1'] = dcc.Markdown(Cit)
O['T,2,0'] = dcc.Markdown(TS)
O['T,2,1'] = dcc.Markdown(IMC)
O['T,3,0'] = dcc.Markdown(HRT)
O['T,3,1'] = dcc.Markdown(JS)
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader(T['T,0,0']), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,0,1'] = [dbc.Card([dbc.CardHeader(T['T,0,1']), dbc.CardBody(O['T,0,1'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader(T['T,1,0']), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader(T['T,1,1']), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
C['T,2,0'] = [dbc.Card([dbc.CardHeader(T['T,2,0']), dbc.CardBody(O['T,2,0'])], color='light', inverse=False, outline=True)]
C['T,2,1'] = [dbc.Card([dbc.CardHeader(T['T,2,1']), dbc.CardBody(O['T,2,1'])], color='light', inverse=False, outline=True)]
C['T,3,0'] = [dbc.Card([dbc.CardHeader(T['T,3,0']), dbc.CardBody(O['T,3,0'])], color='light', inverse=False, outline=True)]
C['T,3,1'] = [dbc.Card([dbc.CardHeader(T['T,3,1']), dbc.CardBody(O['T,3,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab1'] = [dbc.Row([dbc.Col(C['T,0,0'], width=6), dbc.Col(C['T,0,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,2,0'], width=6), dbc.Col(C['T,2,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,3,0'], width=6), dbc.Col(C['T,3,1'], width=6)]), html.Br(),
                           html.Br()]
contents['page']['tab2'] = [dbc.Row([dbc.Col(C['T,0,0'], width=6), dbc.Col(C['T,0,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,2,0'], width=6), dbc.Col(C['T,2,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,3,0'], width=6), dbc.Col(C['T,3,1'], width=6)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="Korea", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="USA", disabled=False),
                                 ])
main = dbc.Jumbotron([html.H2('analysis/Finance'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("GitHub", color="secondary", href='https://github.com/ailever/ailever/tree/master/ailever/analysis'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/tree/master/analysis'),
                                dbc.Button("Wiki", color="secondary", href='https://github.com/ailever/ailever/wiki'),
                                dbc.Button("Docs", color="secondary", href='https://ailever.readthedocs.io/en/latest/detection/index.html'),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.Div([dbc.Button("Bank of Korea", color="dark", href="http://www.bok.or.kr/portal/main/main.do"),
                                dbc.Button("United States Federal Reserve System", color="dark", href="https://www.federalreserve.gov/"),
                                dbc.Button("Investopedia", color="dark", href="https://www.investopedia.com/"),
                                dbc.Button("Investing", color="dark", href="https://www.investing.com/"),
                                dbc.Button("Economist", color="dark", href="https://www.economist.com/"),
                                dbc.Button("Bloomberg", color="dark", href="https://www.bloomberg.com/"),
                                dbc.Button("The Wall Street Journal", color='dark', href="https://www.wsj.com/"),
                                ]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
