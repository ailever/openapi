#%% ################################## CODEBLOCK ##################################
from IPython import display
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import base64

#%% ################################## CONFIG ##################################
import argparse
parser = argparse.ArgumentParser(description="set your environment")
parser.add_argument('--HostDash', type=str, required=False, default='PassToken', help="Host : Dashboard")
parser.add_argument('--PortDash', type=str, required=False, default='PassToken', help="Port : Dashboard")
parser.add_argument('--HostDB', type=str, required=False, default='PassToken', help="Host : DataBase")
parser.add_argument('--PortDB', type=str, required=False, default='PassToken', help="Port : DataBase")
parser.add_argument('--HostJupyter', type=str, required=False, default='PassToken', help="Host : Jupyter")
parser.add_argument('--PortJupyter', type=str, required=False, default='PassToken', help="Port : Jupyter")
parser.add_argument('--HostRV', type=str, required=False, default='PassToken', help="Host : Real-time Visualization")
parser.add_argument('--PortRV', type=str, required=False, default='PassToken', help="Port : Real-time Visualization")
parser.add_argument('--HostR', type=str, required=False, default='PassToken', help="Host : language R")
parser.add_argument('--PortR', type=str, required=False, default='PassToken', help="Port : language R")
args = parser.parse_args()
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
#from visdom import Visdom
# service postgresql start/stop                           # /etc/postgresql/version/main/postgresql.conf
# python -m visdom.server -p 8097 --hostname 127.0.0.1
# rstudio-server start/stop/restart                       # /etc/rstudio/rserver.conf
config = {}
config['dash-server'] = args.HostDash if args.HostDash != 'PassToken' else '127.0.0.1'
config['dash-port'] = args.PortDash if args.PortDash != 'PassToken' else '8050'
config['pgAdmin4-server'] = args.HostDB if args.HostDB != 'PassToken' else 'http://' + '127.0.0.1'
config['pgAdmin4-port'] = args.PortDB if args.PortDB != 'PassToken' else '52631'
config['jupyter-server'] = args.HostJupyter if args.HostJupyter != 'PassToken' else 'http://' + '127.0.0.1'
config['jupyter-port'] = args.PortJupyter if args.PortJupyter != 'PassToken' else '8888'
config['visdom-server'] = args.HostRV if args.HostRV != 'PassToken' else 'http://' + '127.0.0.1'
config['visdom-port'] = args.PortRV if args.PortRV != 'PassToken' else '8097'
config['R-server'] = args.HostR if args.HostR != 'PassToken' else 'http://' + '127.0.0.1'
config['R-port'] = args.PortR if args.PortR != 'PassToken' else '8787'
#vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever [-post, --hostname]
#vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

#%% ################################## REALTIME ##################################
@app.callback(
    Output("visdom-server", "children"),
    Input("real-time", "n_clicks"))
def real_time_analysis(click):
    return 'Real-Time Analysis is over.'
#%% ################################## DASHBOARD ##################################
class MetaClass(type):
    def __new__(cls, clsname, bases, namespace):
        namespace['__str__'] = lambda self: str(self.values)
        namespace['values'] = None
        return type.__new__(cls, clsname, bases, namespace)

Component = MetaClass('Component', (dict,), {})
TAB1 = Component()
TAB1.RC00 = Component()
TAB1.RC10 = Component()
TAB2 = Component()
TAB2.RC00 = Component()
TAB2.RC10 = Component()
TAB3 = Component()
TAB3.RC00 = Component()
TAB3.RC10 = Component()
TAB4 = Component()
TAB4.RC00 = Component()
TAB4.RC10 = Component()
TAB5 = Component()
TAB5.RC00 = Component()
TAB5.RC10 = Component()
TAB6 = Component()
TAB6.RC00 = Component()
TAB6.RC10 = Component()
TAB6.RC20 = Component()
TAB6.RC30 = Component()
TAB6.RC40 = Component()
################################## DASHBOARD : TAB1, ROW0, COL0 ##################################
TAB1.RC00.values = html.Div([html.Img()])
################################## DASHBOARD : TAB1, ROW1, COL0 ##################################
TAB1.RC10.values = dcc.Markdown("""
## This is a worksheet.
""")
################################## DASHBOARD : TAB2, ROW0, COL0 ##################################
TAB2.RC00.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB2, ROW1, COL0 ##################################
TAB2.RC10.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB3, ROW0, COL0 ##################################
TAB3.RC00.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB3, ROW1, COL0 ##################################
TAB3.RC10.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB4, ROW0, COL0 ##################################
TAB4.RC00.values = dcc.Markdown("""
""")
################################## DASHBOARD : TAB4, ROW1, COL0 ##################################
TAB4.RC10.values = dcc.Markdown("""
""")
################################## DASHBOARD : TAB5, ROW0, COL0 ##################################
TAB5.RC00.values = dcc.Markdown("""
""")
################################## DASHBOARD : TAB5, ROW1, COL0 ##################################
TAB5.RC10.values = dcc.Markdown("""
""")
################################## DASHBOARD : TAB6, ROW0, COL0 ##################################
TAB6.RC00.values = dcc.Graph()
################################## DASHBOARD : TAB6, ROW1, COL0 ##################################
TAB6.RC10.values = dcc.Graph()
################################## DASHBOARD : TAB6, ROW2, COL0 ##################################
TAB6.RC20.values = dcc.Graph()
################################## DASHBOARD : TAB6, ROW3, COL0 ##################################
TAB6.RC30.values = dcc.Graph()
################################## DASHBOARD : TAB6, ROW4, COL0 ##################################
TAB6.RC40.values = dcc.Graph()
################################## DASHBOARD ##################################
T = {}
T['T1,0,0'] = 'T__'
T['T1,1,0'] = 'T__'
T['T2,0,0'] = 'T__'
T['T2,1,0'] = 'T__'
T['T3,0,0'] = 'T__'
T['T3,1,0'] = 'T__'
T['T4,0,0'] = 'T__'
T['T4,1,0'] = 'T__'
T['T5,0,0'] = 'T__'
T['T5,1,0'] = 'T__'
T['T6,0,0'] = 'Treemap'
T['T6,1,0'] = 'Sunburst'
T['T6,2,0'] = 'Parallel Coordinates'
T['T6,3,0'] = 'Parallel Categories'
T['T6,4,0'] = 'Icicle'
O = {}
O['T1,_,_'] = None
O['T1,0,0'] = TAB1.RC00.values
O['T1,1,0'] = TAB1.RC10.values
O['T2,0,0'] = TAB2.RC00.values
O['T2,1,0'] = TAB2.RC10.values
O['T3,0,0'] = TAB3.RC00.values
O['T3,1,0'] = TAB3.RC10.values
O['T4,0,0'] = TAB4.RC00.values
O['T4,1,0'] = TAB4.RC10.values
O['T5,0,0'] = TAB5.RC00.values
O['T5,1,0'] = TAB5.RC10.values
O['T6,0,0'] = TAB5.RC00.values
O['T6,1,0'] = TAB5.RC10.values
O['T6,2,0'] = TAB5.RC10.values
O['T6,3,0'] = TAB5.RC10.values
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,0,0']), dbc.CardBody(O['T1,0,0'])], color='light', inverse=False, outline=True)]
C['T1,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,1,0']), dbc.CardBody(O['T1,1,0'])], color='light', inverse=False, outline=True)]
C['T2,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,0,0']), dbc.CardBody(O['T2,0,0'])], color='light', inverse=False, outline=True)]
C['T2,1,0'] = [dbc.Card([dbc.CardHeader(T['T2,1,0']), dbc.CardBody(O['T2,1,0'])], color='light', inverse=False, outline=True)]
C['T3,0,0'] = [dbc.Card([dbc.CardHeader(T['T3,0,0']), dbc.CardBody(O['T3,0,0'])], color='light', inverse=False, outline=True)]
C['T3,1,0'] = [dbc.Card([dbc.CardHeader(T['T3,1,0']), dbc.CardBody(O['T3,1,0'])], color='light', inverse=False, outline=True)]
C['T4,0,0'] = [dbc.Card([dbc.CardHeader(T['T4,0,0']), dbc.CardBody(O['T4,0,0'])], color='light', inverse=False, outline=True)]
C['T4,1,0'] = [dbc.Card([dbc.CardHeader(T['T4,1,0']), dbc.CardBody(O['T4,1,0'])], color='light', inverse=False, outline=True)]
C['T5,0,0'] = [dbc.Card([dbc.CardHeader(T['T5,0,0']), dbc.CardBody(O['T5,0,0'])], color='light', inverse=False, outline=True)]
C['T5,1,0'] = [dbc.Card([dbc.CardHeader(T['T5,1,0']), dbc.CardBody(O['T5,1,0'])], color='light', inverse=False, outline=True)]
C['T6,0,0'] = [dbc.Card([dbc.CardHeader(T['T6,0,0']), dbc.CardBody(O['T6,0,0'])], color='light', inverse=False, outline=True)]
C['T6,1,0'] = [dbc.Card([dbc.CardHeader(T['T6,1,0']), dbc.CardBody(O['T6,1,0'])], color='light', inverse=False, outline=True)]
C['T6,2,0'] = [dbc.Card([dbc.CardHeader(T['T6,2,0']), dbc.CardBody(O['T6,2,0'])], color='light', inverse=False, outline=True)]
C['T6,3,0'] = [dbc.Card([dbc.CardHeader(T['T6,3,0']), dbc.CardBody(O['T6,3,0'])], color='light', inverse=False, outline=True)]
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
                            dbc.Row([dbc.Col(C['T6,1,0'], width=12)]), html.Br(),
                            dbc.Row([dbc.Col(C['T6,2,0'], width=12)]), html.Br(),
                            dbc.Row([dbc.Col(C['T6,3,0'], width=12)]), html.Br(),
                            html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="Problem & Issue", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2'])), label="Data Collection", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab3'])), label="Exploratory Data Analysis", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab4'])), label="Statistical Inference", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab5'])), label="Applications", disabled=True),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab6'])), label="Additionals", disabled=False),
                                 ])
main = dbc.Jumbotron([html.H2(html.A('Analytic Consulting', href="/")),
                      html.H6('Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Ailever", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/analysis/consulting.py'),
                                dbc.Button("Notion", color="secondary", href="https://www.notion.so/ANALYSIS-DASHBOARD-1c1f5a01e4bd490a8c14892d0359031b"),                                
                                dbc.Button("pgAdmin4", color="secondary", href=config['pgAdmin4-server']+':'+config['pgAdmin4-port']),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Jupyter", color="secondary", href=config['jupyter-server']+':'+config['jupyter-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.Div([dbc.Button('dash-html', color='dark', href="https://dash.plotly.com/dash-html-components/"),
                                dbc.Button('dash-core', color='dark', href="https://dash.plotly.com/dash-core-components"),
                                dbc.Button('dash-bootstrap', color='dark', href="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/"),
                                dbc.Button('plotly', color='dark', href="https://plotly.com/python/"),
                                dbc.Button('plotly-ref', color='dark', href="https://plotly.com/python-api-reference/"),
                                dbc.Button('updating figure', color='dark',  href="https://plotly.com/python/creating-and-updating-figures/"),                                
                                ]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## SETUP INFO ##################################
"""
[name] : analytic consulting
[structure] : analysis
[version] : 0.0
[description] : -
[author] : anonym
[keywords] : -
"""
