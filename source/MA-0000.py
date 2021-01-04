################################## CONFIG ##################################
import torch
import torch.nn as nn
from visdom import Visdom
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
import plotly.graph_objs as go
config = {}
config['visdom-server'] = 'http://' + '127.0.0.1'
config['visdom-port'] = '8097'
config['R-server'] = 'http://' + '127.0.0.1'
config['R-port'] = '8787'
config['dash-server'] = '127.0.0.1'
config['dash-port'] = '8050'
vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever [-post, --hostname]
vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
################################## CONFIG ##################################
################################## CODEBLOCK ##################################





# O[T,0,0] : Figure
fig = make_subplots(rows=1, cols=1, subplot_titles=['TITLE'])
fig.add_trace(go.Scatter(x=[1,2,3], y=[3,2,1], mode='lines+markers'), row=1, col=1)

# O[T,0,1] : Description
description = "Description"

opts = {}
opts['legend'] = ['1', '2', '3', '4', '5']
opts['showlegend'] = True
# Real-Time Analysis
@app.callback(
    Output("visdom-server", "children"),
    Input("real-time", "n_clicks"))
def real_time_analysis(click):
    window = vis.line(Y=torch.Tensor(1,5).zero_(), opts=dict(title='TITLE', showlegend=True))
    white_noise = torch.Tensor(1500).normal_()
    time_series1 = torch.empty_like(white_noise)
    time_series2 = torch.empty_like(white_noise)
    time_series3 = torch.empty_like(white_noise)
    time_series4 = torch.empty_like(white_noise)
    time_series5 = torch.empty_like(white_noise)
    for t, noise in enumerate(white_noise):
        time_series1[t] = 0.1*time_series1[t-1] + 0.9*time_series5[t-2] - 0.09*time_series5[t-3] + noise + 1*t**1
        time_series2[t] = 0.1*time_series2[t-1] + 0.9*time_series5[t-5] - 0.09*time_series5[t-6] + noise + 1*t**1 + 0*white_noise[t-1]
        time_series3[t] = 0.1*time_series3[t-1] + 0.9*time_series5[t-10] - 0.09*time_series5[t-11] + noise + 1*t**1
        time_series4[t] = 0.1*time_series4[t-1] + 0.9*time_series5[t-15] - 0.09*time_series5[t-16] + noise + 1*t**1 + 0*white_noise[t-1]
        time_series5[t] = 0.1*time_series5[t-1] + 0.9*time_series5[t-30] - 0.09*time_series5[t-31] + noise + 1*t**1 + 0*white_noise[t-1]
        vis.line(X=torch.tensor([[t,t,t,t,t]]), Y=torch.tensor([[time_series1[t], time_series2[t], time_series3[t], time_series4[t], time_series5[t]]]), win=window, update='append', opts=opts)
    return 'Real-Time Analysis is over.'





################################## CODEBLOCK ##################################
################################## DASHBOARD ##################################
O = {}
O['T,0,0'] = dcc.Graph(figure=fig)
O['T,0,1'] = dcc.Markdown(description)
O['T,1,0'] = None
O['T,1,1'] = None
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader('Linkedin List'), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,0,1'] = [dbc.Card([dbc.CardHeader('T,0,1'), dbc.CardBody(O['T,0,1'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader('T,1,0'), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader('T,1,1'), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(C['T,0,0'], width=6), dbc.Col(C['T,0,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="PAGE1", disabled=False)])
main = html.Div([html.H2(html.A('ARIMA', href="/")),
                 html.H6('Promulgate values for a better tomorrow'),
                 html.Div([dbc.Button("Ailever", color="secondary", href='https://github.com/ailever/ailever/wiki'),
                           dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                           dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                 html.P(id='visdom-server'),
                 html.Br()])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
