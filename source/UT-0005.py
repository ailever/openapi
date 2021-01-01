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
config['dash-server'] = '127.0.0.1'
config['dash-port'] = '8050'
vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever
vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
################################## CONFIG ##################################
################################## CODEBLOCK ##################################





# O[T,0,0] : Figure
fig = make_subplots(rows=1, cols=1, subplot_titles=['TITLE'])
fig.add_trace(go.Scatter(x=[1,2,3], y=[3,2,1], mode='lines+markers'), row=1, col=1)

# O[T,0,1] : Description
description = "Description"

# Real-Time Analysis
@app.callback(
    Output("visdom-server", "children"),
    Input("real-time", "n_clicks"))
def real_time_analysis(click):
    window = vis.line(Y=torch.Tensor(1).zero_(), opts=dict(title='TITLE'))
    white_noise = torch.Tensor(500).normal_()
    time_series = torch.zeros_like(white_noise)
    for t, noise in enumerate(white_noise):
        time_series[t] = time_series[t-1] + noise
        vis.line(X=torch.tensor([t]), Y=torch.tensor([time_series[t]]), win=window, update='append')
    return 'Real-Time Analysis is over.'





################################## CODEBLOCK ##################################
################################## DASHBOARD ##################################
O = {}
O['T,0,0'] = dcc.Graph(figure=fig)
O['T,0,1'] = dcc.Markdown(description)
O['T,1,0'] = None
O['T,1,1'] = None
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(O['T,0,0'], width=6), dbc.Col(O['T,0,1'], width=6)]),
                           dbc.Row([dbc.Col(O['T,1,0'], width=6), dbc.Col(O['T,1,1'], width=6)]),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="AILEVER1", disabled=False)])
main = html.Div([html.H2(html.A('PROJECT TITLE', href="/")),
                 html.H6('Promulgate values for a better tomorrow'),
                 html.Div([dbc.Button("Ailever", color="secondary", href='https://github.com/ailever/ailever/wiki'),
                           dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                 html.P(id='visdom-server'),
                 html.Br()])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
