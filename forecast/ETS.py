#%%
################################## CONFIG ##################################
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
import plotly.graph_objs as go
# rstudio-server start/stop/restart # /etc/rstudio/rserver.conf
# python -m visdom.server -p 8097 --hostname 127.0.0.1
config = {}
config['visdom-server'] = 'http://' + '127.0.0.1'
config['visdom-port'] = '8097'
config['R-server'] = 'http://' + '127.0.0.1'
config['R-port'] = '8787'
config['dash-server'] = '127.0.0.1'
config['dash-port'] = '8050'
#import torch
#import torch.nn as nn
#from visdom import Visdom
#vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever [-post, --hostname]
#vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
################################## CONFIG ##################################
#%%
################################## CODEBLOCK ##################################





# O[T,0,0] : Figure
fig = make_subplots(rows=1, cols=1, subplot_titles=['TITLE'])
fig.add_trace(go.Scatter(x=[1,2,3], y=[3,2,1], mode='lines+markers'), row=1, col=1)
# O[T,0,1] : Description
description1 = "Description"
# O[T,1,0] : Description
description2 = "Description"
# O[T,1,1] : Description
description3 = "Description"





################################## CODEBLOCK ##################################
#%%
################################## DASHBOARD ##################################
O = {}
O['T,_,_'] = None
O['T,0,0'] = dcc.Graph(figure=fig)
O['T,0,1'] = dcc.Markdown(description1)
O['T,1,0'] = dcc.Markdown(description2)
O['T,1,1'] = dcc.Markdown(description3)
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader('T,0,0'), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,0,1'] = [dbc.Card([dbc.CardHeader('T,0,1'), dbc.CardBody(O['T,0,1'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader('T,1,0'), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader('T,1,1'), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(C['T,0,0'], width=6), dbc.Col(C['T,0,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="PAGE1", disabled=False)])
main = dbc.Jumbotron([html.H2('Ailever : forecast/ETS'),
                      html.H6('Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("GitHub", color="secondary", href='https://github.com/ailever/ailever/tree/master/ailever/forecast'),
                                dbc.Button("Wiki", color="secondary", href='https://github.com/ailever/ailever/wiki'),
                                dbc.Button("Docs", color="secondary", href='https://ailever.readthedocs.io/en/latest/forecast/index.html'),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
