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
from ailever.forecast.STOCK import krx, Ailf_KR

"""
Df = krx.kospi('2018-01-01')
ailf = Ailf_KR(Df, filter_period=300, criterion=1.5, V=None)
ailf.KRXIndexReport(ailf.index[0])
ailf.KRXStockReport(ailf.index[0])
ailf.KRXStockForecast(ailf.index[0])
ailf.KRXStockDecompose(ailf.index[0])
"""


#%%
from ailever.forecast import TSA, sarima

"""
proc = sarima.Process(trendparams=(2,1,1), trendAR=[-0.3, 0.2], trendMA=[0.1,],
                      seasonalparams=(1,1,1,20), seasonAR=[0.3,], seasonMA=[0.2,])
tsa = TSA(proc.samples)
tsa.STL(model='ARIMA')
tsa.ETS(steps=10, error='add', trend='add', seasonal='add', seasonal_periods=20)
tsa.SARIMAX(steps=10, order=(2,1,0), seasonal_order=(0,1,0,20))
"""


################################## CODEBLOCK ##################################
#%%
################################## DASHBOARD ##################################
T = {}
T['T,0,0'] = ''
T['T,0,1'] = ''
T['T,1,0'] = ''
T['T,1,1'] = ''
O = {}
O['T,_,_'] = None
O['T,0,0'] = dcc.Markdown('')
O['T,0,1'] = dcc.Markdown('')
O['T,1,0'] = dcc.Markdown('')
O['T,1,1'] = dcc.Markdown('')
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader(T['T,0,0']), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,0,1'] = [dbc.Card([dbc.CardHeader(T['T,0,1']), dbc.CardBody(O['T,0,1'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader(T['T,1,0']), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader(T['T,1,1']), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(C['T,0,0'], width=6), dbc.Col(C['T,0,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="PAGE1", disabled=False)])
main = dbc.Jumbotron([html.H2('forecast'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("GitHub", color="secondary", href='https://github.com/ailever/ailever/tree/master/ailever/forecast'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/tree/master/forecast'),
                                dbc.Button("Wiki", color="secondary", href='https://github.com/ailever/ailever/wiki'),
                                dbc.Button("Docs", color="secondary", href='https://ailever.readthedocs.io/en/latest/forecast/index.html'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/tree/master/forecast'),
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
