#%%
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
# rstudio-server start/stop/restart # /etc/rstudio/rserver.conf
# python -m visdom.server -p 8097 --hostname 127.0.0.1
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
#%%
################################## CODEBLOCK ##################################
# O[T,0,0] : Figure
fig1 = make_subplots(rows=1, cols=1, subplot_titles=['합계'])
# O[T,0,1] : Figure
fig2 = make_subplots(rows=1, cols=1, subplot_titles=['서울'])
# O[T,1,0] : Figure
fig3 = make_subplots(rows=1, cols=1, subplot_titles=['경기'])
# O[T,1,1] : Figure
fig4 = make_subplots(rows=1, cols=1, subplot_titles=['인천'])
# O[T,2,0] : Figure
fig5 = make_subplots(rows=1, cols=1, subplot_titles=['부산'])
# O[T,2,1] : Figure
fig6 = make_subplots(rows=1, cols=1, subplot_titles=['울산'])
# O[T,3,0] : Figure
fig7 = make_subplots(rows=1, cols=1, subplot_titles=['대구'])
# O[T,3,1] : Figure
fig8 = make_subplots(rows=1, cols=1, subplot_titles=['광주'])
# O[T,4,0] : Figure
fig9 = make_subplots(rows=1, cols=1, subplot_titles=['대전'])
# O[T,4,1] : Figure
fig10 = make_subplots(rows=1, cols=1, subplot_titles=['세종'])
# O[T,5,0] : Figure
fig11 = make_subplots(rows=1, cols=1, subplot_titles=['강원'])
# O[T,5,1] : Figure
fig12 = make_subplots(rows=1, cols=1, subplot_titles=['전북'])
# O[T,6,0] : Figure
fig13 = make_subplots(rows=1, cols=1, subplot_titles=['전남'])
# O[T,6,1] : Figure
fig14 = make_subplots(rows=1, cols=1, subplot_titles=['경북'])
# O[T,7,0] : Figure
fig15 = make_subplots(rows=1, cols=1, subplot_titles=['경남'])
# O[T,7,1] : Figure
fig16 = make_subplots(rows=1, cols=1, subplot_titles=['충북'])
# O[T,8,0] : Figure
fig17 = make_subplots(rows=1, cols=1, subplot_titles=['충남'])
# O[T,8,1] : Figure
fig18 = make_subplots(rows=1, cols=1, subplot_titles=['제주'])


#%%
from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen, Request
import json

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
KEY = '~~'
queryParams = '?' + quote_plus('ServiceKey') + f'={KEY}&' + urlencode({quote_plus('pageNo'):'1',
                                                                       quote_plus('numOfRows'):'10',
                                                                       quote_plus('startCreateDt'):'20200310',
                                                                       quote_plus('endCreateDt'):'20201231',
                                                                       quote_plus('_type'):'json'})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response = urlopen(request).read().decode('utf-8')
covid19 = json.loads(response)
#%%    
import pandas as pd
import numpy as np
df = pd.DataFrame(covid19['response']['body']['items']['item'])
x1 = df[df.gubun == '합계'].defCnt.values[::-1]
x2 = df[df.gubun == '서울'].defCnt.values[::-1]
x3 = df[df.gubun == '경기'].defCnt.values[::-1]
x4 = df[df.gubun == '인천'].defCnt.values[::-1]
x5 = df[df.gubun == '부산'].defCnt.values[::-1]
x6 = df[df.gubun == '울산'].defCnt.values[::-1]
x7 = df[df.gubun == '대구'].defCnt.values[::-1]
x8 = df[df.gubun == '광주'].defCnt.values[::-1]
x9 = df[df.gubun == '대전'].defCnt.values[::-1]
x10 = df[df.gubun == '세종'].defCnt.values[::-1]
x11 = df[df.gubun == '강원'].defCnt.values[::-1]
x12 = df[df.gubun == '전북'].defCnt.values[::-1]
x13 = df[df.gubun == '전남'].defCnt.values[::-1]
x14 = df[df.gubun == '경북'].defCnt.values[::-1]
x15 = df[df.gubun == '경남'].defCnt.values[::-1]
x16 = df[df.gubun == '충북'].defCnt.values[::-1]
x17 = df[df.gubun == '충남'].defCnt.values[::-1]
x18 = df[df.gubun == '제주'].defCnt.values[::-1]
fig1.add_trace(go.Scatter(y=x1, mode='lines+markers'), row=1, col=1)
fig2.add_trace(go.Scatter(y=x2, mode='lines+markers'), row=1, col=1)
fig3.add_trace(go.Scatter(y=x3, mode='lines+markers'), row=1, col=1)
fig4.add_trace(go.Scatter(y=x4, mode='lines+markers'), row=1, col=1)
fig5.add_trace(go.Scatter(y=x5, mode='lines+markers'), row=1, col=1)
fig6.add_trace(go.Scatter(y=x6, mode='lines+markers'), row=1, col=1)
fig7.add_trace(go.Scatter(y=x7, mode='lines+markers'), row=1, col=1)
fig8.add_trace(go.Scatter(y=x8, mode='lines+markers'), row=1, col=1)
fig9.add_trace(go.Scatter(y=x9, mode='lines+markers'), row=1, col=1)
fig10.add_trace(go.Scatter(y=x10, mode='lines+markers'), row=1, col=1)
fig11.add_trace(go.Scatter(y=x11, mode='lines+markers'), row=1, col=1)
fig12.add_trace(go.Scatter(y=x12, mode='lines+markers'), row=1, col=1)
fig13.add_trace(go.Scatter(y=x13, mode='lines+markers'), row=1, col=1)
fig14.add_trace(go.Scatter(y=x14, mode='lines+markers'), row=1, col=1)
fig15.add_trace(go.Scatter(y=x15, mode='lines+markers'), row=1, col=1)
fig16.add_trace(go.Scatter(y=x16, mode='lines+markers'), row=1, col=1)
fig17.add_trace(go.Scatter(y=x17, mode='lines+markers'), row=1, col=1)
fig18.add_trace(go.Scatter(y=x18, mode='lines+markers'), row=1, col=1)

X = np.stack([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18], axis=1)
X = torch.from_numpy(X)
################################## CODEBLOCK ##################################













#%%
################################## REALTIME ##################################
# Real-Time Analysis
@app.callback(
    Output("visdom-server", "children"),
    Input("real-time", "n_clicks"))
def real_time_analysis(click):
    window = vis.line(Y=torch.Tensor(1, 18).zero_(), opts=dict(title='TITLE'))
    for t, X_ in enumerate(X):
        vis.line(X=torch.tensor([[t]*18]), Y=X_.unsqueeze(0), win=window, update='append')
    return 'Real-Time Analysis is over.'
################################## REALTIME ##################################













#%%
################################## DASHBOARD ##################################
O = {}
O['T,_,_'] = None
O['T,0,0'] = dcc.Graph(figure=fig1)
O['T,0,1'] = dcc.Graph(figure=fig2)
O['T,1,0'] = dcc.Graph(figure=fig3)
O['T,1,1'] = dcc.Graph(figure=fig4)
O['T,2,0'] = dcc.Graph(figure=fig5)
O['T,2,1'] = dcc.Graph(figure=fig6)
O['T,3,0'] = dcc.Graph(figure=fig7)
O['T,3,1'] = dcc.Graph(figure=fig8)
O['T,4,0'] = dcc.Graph(figure=fig9)
O['T,4,1'] = dcc.Graph(figure=fig10)
O['T,5,0'] = dcc.Graph(figure=fig11)
O['T,5,1'] = dcc.Graph(figure=fig12)
O['T,6,0'] = dcc.Graph(figure=fig13)
O['T,6,1'] = dcc.Graph(figure=fig14)
O['T,7,0'] = dcc.Graph(figure=fig15)
O['T,7,1'] = dcc.Graph(figure=fig16)
O['T,8,0'] = dcc.Graph(figure=fig17)
O['T,8,1'] = dcc.Graph(figure=fig18)
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader('T,0,0'), dbc.CardBody(O['T,0,0'])], color='primary', inverse=True, outline=False)]
C['T,0,1'] = [dbc.Card([dbc.CardHeader('T,0,1'), dbc.CardBody(O['T,0,1'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader('T,1,0'), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader('T,1,1'), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
C['T,2,0'] = [dbc.Card([dbc.CardHeader('T,2,0'), dbc.CardBody(O['T,2,0'])], color='light', inverse=False, outline=True)]
C['T,2,1'] = [dbc.Card([dbc.CardHeader('T,2,1'), dbc.CardBody(O['T,2,1'])], color='light', inverse=False, outline=True)]
C['T,3,0'] = [dbc.Card([dbc.CardHeader('T,3,0'), dbc.CardBody(O['T,3,0'])], color='light', inverse=False, outline=True)]
C['T,3,1'] = [dbc.Card([dbc.CardHeader('T,3,1'), dbc.CardBody(O['T,3,1'])], color='light', inverse=False, outline=True)]
C['T,4,0'] = [dbc.Card([dbc.CardHeader('T,4,0'), dbc.CardBody(O['T,4,0'])], color='light', inverse=False, outline=True)]
C['T,4,1'] = [dbc.Card([dbc.CardHeader('T,4,1'), dbc.CardBody(O['T,4,1'])], color='light', inverse=False, outline=True)]
C['T,5,0'] = [dbc.Card([dbc.CardHeader('T,5,0'), dbc.CardBody(O['T,5,0'])], color='light', inverse=False, outline=True)]
C['T,5,1'] = [dbc.Card([dbc.CardHeader('T,5,1'), dbc.CardBody(O['T,5,1'])], color='light', inverse=False, outline=True)]
C['T,6,0'] = [dbc.Card([dbc.CardHeader('T,6,0'), dbc.CardBody(O['T,6,0'])], color='light', inverse=False, outline=True)]
C['T,6,1'] = [dbc.Card([dbc.CardHeader('T,6,1'), dbc.CardBody(O['T,6,1'])], color='light', inverse=False, outline=True)]
C['T,7,0'] = [dbc.Card([dbc.CardHeader('T,7,0'), dbc.CardBody(O['T,7,0'])], color='light', inverse=False, outline=True)]
C['T,7,1'] = [dbc.Card([dbc.CardHeader('T,7,1'), dbc.CardBody(O['T,7,1'])], color='light', inverse=False, outline=True)]
C['T,8,0'] = [dbc.Card([dbc.CardHeader('T,8,0'), dbc.CardBody(O['T,8,0'])], color='light', inverse=False, outline=True)]
C['T,8,1'] = [dbc.Card([dbc.CardHeader('T,8,1'), dbc.CardBody(O['T,8,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(C['T,0,0'], width=6), dbc.Col(C['T,0,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,2,0'], width=6), dbc.Col(C['T,2,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,3,0'], width=6), dbc.Col(C['T,3,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,4,0'], width=6), dbc.Col(C['T,4,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,5,0'], width=6), dbc.Col(C['T,5,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,6,0'], width=6), dbc.Col(C['T,6,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,7,0'], width=6), dbc.Col(C['T,7,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,8,0'], width=6), dbc.Col(C['T,8,1'], width=6)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="PAGE1", disabled=False)])
main = html.Div([html.H2(html.A('Coronavirus Disease 2019 (COVID-19)', href="/")),
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
