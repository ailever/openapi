#%% ################################## CODEBLOCK ##################################
class N:
    def __init__(self, layout=None, title=None, contents=None):
        self.layout = layout
        self.title = title
        self.contents = contents

note = N()
note.N00 = N('T1,0,0', 'title 1', """
- You will have to **prepare for 30 seconds** and **speak for 60 seconds**.
- The structure **has remained the same**.
- **A couple of small changes** are nothing too big.
- There are less **questions there used to be 12 to 14 questions per passage**. 
- The structure is **a little bit different about reading passage**.
- Everything **is desgined to see you if** you're ready for a freshman year
- This is **what you are going to know by** the end of this little lecture.
- I don't have a lot of time, **Let's get into it right now**.
- **This is for you to** do your homework. 
- This is **when you arrive at a destination**.
- I am gonna become a real American student just for a day to show you **how it all looks like housing life of American works**.
- We use them **when we meet someone for a first time**.
- As an example, I will show the usual **low-budget life style**.
- How much does **it costs to live here**.
- A lot of people that want to move to LA want to move here to **be closer to a beach**.
- This is probably **one of the most important ones**.
- Obviously, LA **is becomming** very **impacted**.
- then you **might be okay**.
- You might think because your friend **lives five miles away**.
- It'**s** so|super **common**.
- Let them know that you want to see them again.  
""")
note.N01 = N('T1,1,0', 'title 2', """
""")
note.N02 = N('T2,0,0', 'title 2', """
""")
note.N03 = N('T2,1,0', 'title 2', """
""")
note.N04 = N('T2,2,0', 'title 2', """
""")
note.N05 = N('T2,3,0', 'title 2', """
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
################################## DASHBOARD ##################################
T = {}; O = {}; C = {}
contents = {}; contents['page'] = {}; page_layouts = {}

tabs = set()
for i, N in enumerate(vars(note).values()):
    if i < 3 : continue
    tabs.add(N.layout[:2])
tabs = list(tabs); tabs.sort()
for tab in tabs:
    contents['page'][tab] = list()

for i, N in enumerate(vars(note).values()):
    if i < 3 : continue
    T[N.layout] = N.title
    O[N.layout] = dcc.Markdown(N.contents)
    C[N.layout] = [dbc.Card([dbc.CardHeader(T[N.layout]), dbc.CardBody(O[N.layout])], color='light', inverse=False, outline=True)]
    contents['page'][N.layout[:2]].extend([dbc.Row([dbc.Col(C[N.layout], width=12)]), html.Br()])

cards = list()
for tab in tabs:
    contents['page'][tab].append(html.Br())
    cards.append(dbc.Tab(dbc.Card(dbc.CardBody(contents['page'][tab])), label=tab, disabled=False))
page_layouts['page'] = dbc.Tabs(cards)
################################## DASHBOARD ##################################
main = dbc.Jumbotron([html.H2('WS0001'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/work-sheet/WS0001.py'),
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
