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
import plotly.graph_objs as go


# O[T,0,0] : Korea
KR = html.Div([dbc.Button('Naver', color='dark', href="https://news.naver.com/"),
               dbc.Button('서울신문', color='dark', href="http://www.seoul.co.kr/"),
               dbc.Button('조선일보', color='dark', href="https://www.chosun.com/"),
               dbc.Button('동아일보', color='dark', href="https://www.donga.com/"),
               dbc.Button('경향신문', color='dark', href="http://www.khan.co.kr/"),
               dbc.Button('한국일보', color='dark', href="https://www.hankookilbo.com/"),
               dbc.Button('중앙일보', color='dark', href="https://joongang.joins.com/"),
               dbc.Button('한겨례', color='dark', href="http://www.hani.co.kr/"),
               dbc.Button('국민일보', color='dark', href="http://www.kmib.co.kr/news/index.asp"),
               dbc.Button('세계일보', color='dark', href="http://www.segye.com/"),
               dbc.Button('문화일보', color='dark', href="http://www.munhwa.com/")])
# O[T,0,1] : United States
US = html.Div([html.Embed(src='https://news.naver.com/', style={'width':'100%', 'height':'100%'})])
# O[T,1,0] : Description
# O[T,1,1] : Description





################################## CODEBLOCK ##################################
#%%
################################## DASHBOARD ##################################
T = {}
T['T,0,0'] = 'Korea'
T['T,1,0'] = 'United States'
O = {}
O['T,_,_'] = None
O['T,0,0'] = KR
O['T,1,0'] = US
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader(T['T,0,0']), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader(T['T,1,0']), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(C['T,0,0'], width=12)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=12)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="PAGE1", disabled=False)])
main = dbc.Jumbotron([html.H2('analysis/Politics'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("GitHub", color="secondary", href='https://github.com/ailever/ailever/tree/master/ailever/analysis'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/tree/master/analysis'),
                                dbc.Button("Wiki", color="secondary", href='https://github.com/ailever/ailever/wiki'),
                                dbc.Button("Docs", color="secondary", href='https://ailever.readthedocs.io/en/latest/detection/index.html'),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.Div([dbc.Button('Time Line 1', color='dark', href="https://en.wikipedia.org/wiki/2021"),
                                dbc.Button('Time Line 2', color='dark', href="https://ko.wikipedia.org/wiki/2021%EB%85%84"),
                                dbc.Button('Time Line 3', color='dark', href="https://namu.wiki/w/2021%EB%85%84"),
                                ]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
