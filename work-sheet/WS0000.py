#%% ################################## CODEBLOCK ##################################
from IPython import display
from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np


#%% ################################## CONFIG ##################################
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
#from visdom import Visdom
# service postgresql start/stop                           # /etc/postgresql/version/main/postgresql.conf
# python -m visdom.server -p 8097 --hostname 127.0.0.1
# rstudio-server start/stop/restart                       # /etc/rstudio/rserver.conf
config = {}
config['pgAdmin4-server'] = 'http://' + '127.0.0.1'
config['pgAdmin4-port'] = '52631'
config['visdom-server'] = 'http://' + '127.0.0.1'
config['visdom-port'] = '8097'
config['R-server'] = 'http://' + '127.0.0.1'
config['R-port'] = '8787'
config['dash-server'] = '127.0.0.1'
config['dash-port'] = '8050'
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
TAB1.RC01 = Component()
TAB1.RC10 = Component()
TAB1.RC11 = Component()
TAB1.RC20 = Component()
TAB1.RC21 = Component()

TAB1.RC00.values = html.Div([dbc.Button('repl', color='dark', href="https://repl.it/languages/"),
                             dbc.Button('stackoverflow', color='dark', href="https://stackoverflow.com/"),
                             dbc.Button('devkuma', color='dark', href="http://www.devkuma.com/books/"),
                             dbc.Button('wikidocs', color='dark', href="https://wikidocs.net/"),
                             dbc.Button('sololearn', color='dark', href="https://www.sololearn.com/"),
                             dbc.Button('w3schools', color='dark', href="https://www.w3schools.com/"),
                             ])
TAB1.RC01.values = html.Div([dbc.Button('Bash', color='dark', href="http://www.devkuma.com/books/11"),
                             dbc.Button('PostgreSQL', color='dark', href="http://www.devkuma.com/books/16"),
                             ])
TAB1.RC10.values = html.Div([dbc.Button('dash-html', color='dark', href="https://dash.plotly.com/dash-html-components/"),
                             dbc.Button('dash-core', color='dark', href="https://dash.plotly.com/dash-core-components"),
                             dbc.Button('dash-bootstrap', color='dark', href="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/alert/"),
                             dbc.Button('plotly', color='dark', href="https://plotly.com/python-api-reference/"),
                             dbc.Button('scipy', color='dark', href="https://docs.scipy.org/doc/scipy/reference/"),
                             dbc.Button('sympy', color='dark', href="https://docs.sympy.org/latest/py-modindex.html"),
                             dbc.Button('numpy', color='dark', href="https://numpy.org/doc/stable/genindex.html"),
                             dbc.Button('scikit-learn', color='dark', href="https://scikit-learn.org/stable/modules/classes.html"),
                             dbc.Button('statsmodels', color='dark', href="https://www.statsmodels.org/stable/py-modindex.html"),
                             dbc.Button('', color='dark', href=""),
                             ])
TAB1.RC11.values = html.Div([dbc.Button('', color='dark', href=""),
                             dbc.Button('', color='dark', href=""),
                             ])
TAB1.RC20.values = html.Div([dbc.Button('HTML - tag list', color='dark', href="https://www.w3schools.com/tags/default.asp"),
                             dbc.Button('HTML - color code', color='dark', href="https://htmlcolorcodes.com/"),
                             dbc.Button('CSS - properties', color='dark', href="https://www.w3schools.com/cssref/default.asp"),
                             dbc.Button('CSS - selector', color='dark', href="https://www.w3schools.com/cssref/css_selectors.asp"),
                             ])
TAB1.RC21.values = html.Div([dbc.Button('SQL', color='dark', href="https://userdyk-github.github.io/pl00/PL00-SQL.html"),
                             dbc.Button('Linux', color='dark', href="https://userdyk-github.github.io/pl00/PL00-Linux.html"),
                             dbc.Button('System Programming', color='dark', href="https://userdyk-github.github.io/pl00/PL00-System-programming.html"),
                             dbc.Button('Windows', color='dark', href="https://userdyk-github.github.io/pl00/PL00-Windows.html"),
                             ])
################################## DASHBOARD ##################################
T = {}
T['T,0,0'] = 'Computer Engineering : Overall'
T['T,0,1'] = 'Programming Language'
T['T,1,0'] = 'Python Library APIs'
T['T,1,1'] = 'Python Library Tutorials'
T['T,2,0'] = 'Supplementary'
T['T,2,1'] = '_'
O = {}
O['T,_,_'] = None
O['T,0,0'] = TAB1.RC00.values
O['T,0,1'] = TAB1.RC01.values
O['T,1,0'] = TAB1.RC10.values
O['T,1,1'] = TAB1.RC11.values
O['T,2,0'] = TAB1.RC20.values
O['T,2,1'] = TAB1.RC21.values
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader(T['T,0,0']), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,0,1'] = [dbc.Card([dbc.CardHeader(T['T,0,1']), dbc.CardBody(O['T,0,1'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader(T['T,1,0']), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader(T['T,1,1']), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
C['T,2,0'] = [dbc.Card([dbc.CardHeader(T['T,2,0']), dbc.CardBody(O['T,2,0'])], color='light', inverse=False, outline=True)]
C['T,2,1'] = [dbc.Card([dbc.CardHeader(T['T,2,1']), dbc.CardBody(O['T,2,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab'] = [dbc.Row([dbc.Col(C['T,0,0'], width=6), dbc.Col(C['T,0,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                           dbc.Row([dbc.Col(C['T,2,0'], width=6), dbc.Col(C['T,2,1'], width=6)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="References", disabled=False)])
main = dbc.Jumbotron([html.H2(html.A('WS0000', href="/")),
                      html.H6('Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Ailever", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button('AIL CE', color='secondary', href="https://ailever.github.io/education/2020/05/30/Computer-Engineering/"),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/work-sheet/WS0000.py'),
                                dbc.Button("pgAdmin4", color="secondary", href=config['pgAdmin4-server']+':'+config['pgAdmin4-port']),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
