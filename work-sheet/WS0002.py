#%% ################################## CODEBLOCK ##################################
class N:
    def __init__(self, tab_info=(None, None), title=None, contents=None):
        self.layout = tab_info[0]
        self.label = tab_info[1]
        self.title = title
        self.contents = contents

note = N()
note.N00 = N(('T01,0,0', 'Work & School'), 'title 1', """
tab1 - contents block
""")
note.N00_00 = N(('T01,1,0', 'Work & School'), 'work on', """
- A: I'm so **stressed out** these days.
- B: Oh? Do you have to **work on a big project**?
---
- A: Hey Nick, How about we **get some beer**?
- B: I'd like to, but I have to **get back to work**.
---
- A: This needs to **be done** quickly.
- B: Don't worry, I'll **get right on it**.
---
- A: Have you **finished cleaning up**?
- B: **I'm on it**. I'll **be done in an hour**.
""")
note.N00_01 = N(('T01,2,0', 'Work & School'), 'do a good job', """
- A: You have to **work hard**. Don't let me down.
- B: I'll **do my best**, boss. Believe me. 
---
- A: This wedding cake **looks great**.
- B: I **worked all night** baking it.
---
- A: 
- B: 
---
- A: 
- B: 
""")
note.N00_02 = N(('T01,3,0', 'Work & School'), 'work hard', """
- A: 
- B: 
---
- A: 
- B: 
---
- A: 
- B: 
---
- A: 
- B: 
""")
note.N00_03 = N(('T01,4,0', 'Work & School'), 'have a lot of work', """
- A: 
- B: 
---
- A: 
- B: 
---
- A: 
- B: 
---
- A: 
- B: 
""")
note.N01 = N(('T02,0,0', 'Computer & Networking'), 'title 1', """
tab1 - contents block
""")
note.N02 = N(('T03,0,0', 'Social Life with Others'), 'title 1', """
tab1 - contents block
""")
note.N03 = N(('T04,0,0', 'Everyday Life Activies'), 'title 1', """
tab1 - contents block
""")
note.N04 = N(('T05,0,0', 'Information & Understanding'), 'title 1', """
tab1 - contents block
""")
note.N05 = N(('T06,0,0', 'Thoughts & Attitude'), 'title 1', """
tab1 - contents block
""")
note.N06 = N(('T07,0,0', 'Emotions & Situations'), 'title 1', """
tab1 - contents block
""")
note.N07 = N(('T08,0,0', 'Various Actions'), 'title 1', """
tab1 - contents block
""")
note.N08 = N(('T09,0,0', 'Time, Place & etc.'), 'title 1', """
tab1 - contents block
""")
note.N09 = N(('T10,0,0', 'Additionals'), 'title 1', """
tab1 - contents block
""")

#%% ################################## CONFIG ##################################
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

#%% ################################## DASHBOARD ##################################
T = {}; O = {}; C = {}
contents = {}; contents['page'] = {}; page_layouts = {}
tab_infos = set()
for i, N in enumerate(vars(note).values()):
    if i < 4 : continue
    tab_infos.add((N.layout[:3], N.label))
tab_infos = list(tab_infos)
tab_infos.sort()

tabs = list()
labels = list()
for layout, label in tab_infos:
    tabs.append(layout)
    labels.append(label)
for tab in tabs:
    contents['page'][tab] = list()
for i, N in enumerate(vars(note).values()):
    if i < 4 : continue
    T[N.layout] = N.title
    O[N.layout] = dcc.Markdown(N.contents)
    C[N.layout] = [dbc.Card([dbc.CardHeader(T[N.layout]), dbc.CardBody(O[N.layout])], color='light', inverse=False, outline=True)]
    contents['page'][N.layout[:3]].extend([dbc.Row([dbc.Col(C[N.layout], width=12)]), html.Br()])
cards = list()
for tab, label in zip(tabs, labels):
    contents['page'][tab].append(html.Br())
    cards.append(dbc.Tab(dbc.Card(dbc.CardBody(contents['page'][tab])), label=label, disabled=False))
page_layouts['page'] = dbc.Tabs(cards)
################################## DASHBOARD ##################################
main = dbc.Jumbotron([html.H2('WS0002 : English Conversation'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/work-sheet/WS0002.py'),
                                dbc.Button("Wikipedia", color="secondary", href="https://en.wikipedia.org/wiki/Main_Page"),
                                dbc.Button("Youtube", color="secondary", href="https://www.youtube.com/"),
                                dbc.Button("Google", color="secondary", href="https://www.google.com/"),
                                dbc.Button("Google Trend", color="secondary", href="https://trends.google.com/trends/explore"),
                                dbc.Button("Naver", color="secondary", href="https://www.naver.com/"),
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
