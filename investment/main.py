#%% ################################## CODEBLOCK ##################################
from IPython import display
from ipywidgets import interact
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import os
import base64
import FinanceDataReader as fdr


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
TAB3 = Component()
TAB3.RC00 = Component()
TAB4 = Component()
TAB4.RC00 = Component()
TAB5 = Component()
TAB5.RC00 = Component()
TAB6 = Component()
TAB6.RC00 = Component()
################################## DASHBOARD : TAB1, ROW0, COL0 ##################################
@app.callback(
    Output("reits-candelstick", "figure"),
    Input("reits-dropdown", "value"))
def real_time_analysis(value):
    df = fdr.DataReader(value).reset_index()
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])
    return fig

df = fdr.DataReader('ARE').reset_index()
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
TAB1.RC00._graph01 = dcc.Graph(id='reits-candelstick', figure=fig)
TAB1.RC00.reits_list = ['ARE', 'BXP', 'BDN', 'CMCT', 'CIO', 'CXP', 'OFC', 'CUZ', 'DEI', 'DEA', 'ESRT', 'EQC', 'FSP', 'HIW', 'HPP', 'KRC', 'NYC', 'OPI', 'PGRE', 'PDM', 'SLG', 'COLD', 'DRE', 'EGP', 'FR', 'ILPT', 'INDT', 'IIPR', 'LXP', 'MNR', 'PLYM', 'PLD', 'PSB', 'REXR', 'STAG', 'TRNO', 'AKR', 'AFIN', 'BRX', 'CDR', 'FRT', 'KIM', 'KRG', 'REG', 'ROIC', 'RPAI', 'RVI', 'RPT', 'BFS', 'SITC', 'SKT', 'UE', 'UBA', 'WRI', 'WHLR', 'WSR', 'BPYU', 'MAC', 'PEI', 'SPG', 'WPG', 'ADC', 'PINE', 'EPRT', 'FCPT', 'GTY', 'NNN', 'NTST', 'PSTL', 'O', 'SRG', 'SRC', 'STOR', 'ACC', 'AIRC', 'AIV', 'AVB', 'BRG', 'BRT', 'CPT', 'CSR', 'CLPR', 'EQR', 'ESS', 'IRT', 'MAA', 'NXRT', 'APTS', 'UDR', 'ELS', 'SUI', 'UMH', 'AMH', 'INVH', 'ALEX', 'ALX', 'AAT', 'AHH', 'BNL', 'CLNY', 'GOOD', 'GNL', 'HMG', 'JBGS', 'CLI', 'MDRR', 'OLP', 'SQFT', 'SVC', 'VER', 'VNO', 'WPC', 'WRE', 'CTRE', 'CHCT', 'DHC', 'GMRE', 'HR', 'HTA', 'PEAK', 'LTC', 'MPW', 'NHI', 'SNR', 'OHI', 'DOC', 'SBRA', 'UHT', 'VTR', 'WELL', 'APLE', 'AHT', 'BHR', 'CLDT', 'CDOR', 'CPLG', 'DRH', 'HT', 'HST', 'IHT', 'PK', 'PEB', 'RLJ', 'RHP', 'SOHO', 'INN', 'SHO', 'XHR', 'CUBE', 'EXR', 'SELF', 'LSI', 'NSA', 'PSA', 'CTT', 'PCH', 'RYN', 'WY', 'AMT', 'CORR', 'CCI', 'PW', 'SBAC', 'UNIT', 'COR', 'CONE', 'DLR', 'EQIX', 'QTS', 'EPR', 'FPI', 'GLPI', 'GEO', 'LAND', 'IRM', 'LAMR', 'OUT', 'SAFE', 'VICI', 'MITT', 'AGNC', 'NLY', 'AAIC', 'ARR', 'CMO', 'CHMI', 'CIM', 'DX', 'EFC', 'EARN', 'AJX', 'IVR', 'LFT', 'MFA', 'NRZ', 'NYMT', 'ORC', 'PMT', 'RC', 'RWT', 'TWO', 'WMC', 'ACR', 'ARI', 'ABR', 'ACRE', 'BXMT', 'BRMK', 'CLNC', 'GPMT', 'HASI', 'STAR', 'KREF', 'LADR', 'NREF', 'SACH', 'STWD', 'TRTX', 'TRMT']
TAB1.RC00._reits_labels = [ {'label' : symbol, 'value' : symbol} for symbol in TAB1.RC00.reits_list ]
TAB1.RC00.values = html.Div([
    dcc.Dropdown(
        id='reits-dropdown',
        options=TAB1.RC00._reits_labels,
        value='ARE',
        placeholder="Select a ticker",

    ),
    html.Div(TAB1.RC00._graph01)
])
################################## DASHBOARD : TAB1, ROW1, COL0 ##################################
################################## DASHBOARD : TAB2, ROW0, COL0 ##################################
TAB2.RC00.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB3, ROW0, COL0 ##################################
TAB3.RC00.values = html.Div([dbc.Button('A', color='dark', href=""),
                             dbc.Button('B', color='dark', href=""),
                             ])
################################## DASHBOARD : TAB4, ROW0, COL0 ##################################
TAB4.RC00.values = dcc.Markdown("""
""")
################################## DASHBOARD : TAB5, ROW0, COL0 ##################################
TAB5.RC00.values = dcc.Markdown("""
""")
################################## DASHBOARD : TAB6, ROW0, COL0 ##################################
TAB6.RC00.values = dcc.Graph()
################################## DASHBOARD ##################################
T = {}
T['T1,0,0'] = 'Reits'
T['T2,0,0'] = 'T__'
T['T3,0,0'] = 'T__'
T['T4,0,0'] = 'T__'
T['T5,0,0'] = 'T__'
T['T6,0,0'] = 'T__'
O = {}
O['T1,_,_'] = None
O['T1,0,0'] = TAB1.RC00.values
O['T2,0,0'] = TAB2.RC00.values
O['T3,0,0'] = TAB3.RC00.values
O['T4,0,0'] = TAB4.RC00.values
O['T5,0,0'] = TAB5.RC00.values
O['T6,0,0'] = TAB5.RC00.values
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,0,0']), dbc.CardBody(O['T1,0,0'])], color='light', inverse=False, outline=True)]
C['T2,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,0,0']), dbc.CardBody(O['T2,0,0'])], color='light', inverse=False, outline=True)]
C['T3,0,0'] = [dbc.Card([dbc.CardHeader(T['T3,0,0']), dbc.CardBody(O['T3,0,0'])], color='light', inverse=False, outline=True)]
C['T4,0,0'] = [dbc.Card([dbc.CardHeader(T['T4,0,0']), dbc.CardBody(O['T4,0,0'])], color='light', inverse=False, outline=True)]
C['T5,0,0'] = [dbc.Card([dbc.CardHeader(T['T5,0,0']), dbc.CardBody(O['T5,0,0'])], color='light', inverse=False, outline=True)]
C['T6,0,0'] = [dbc.Card([dbc.CardHeader(T['T6,0,0']), dbc.CardBody(O['T6,0,0'])], color='light', inverse=False, outline=True)]
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
                            html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="MARKET", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2'])), label="TAB2", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab3'])), label="TAB3", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab4'])), label="TAB4", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab5'])), label="TAB5", disabled=True),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab6'])), label="TAB6", disabled=False),
                                 ])
main = dbc.Jumbotron([html.H2(html.A('Investment', href="/")),
                      html.H6('Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Ailever", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/investment/main.py'),
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
[name] : main
[structure] : investment
[version] : 0.0
[description] : -
[author] : anonym
[keywords] : -
"""
