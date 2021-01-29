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
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objs as go

#vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever [-post, --hostname]
#vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
################################## CONFIG ##################################
#%%
################################## CODEBLOCK ##################################
import pandas as pd
import numpy as np

# O[T,0,0] : Map
data = [[37.586786, 126.974736, '청와대(Cheong Wh Dae)', '서울(Seoul)', "종로구 세종로"],
        [37.563184116699055, 126.97959495769867, '한국은행(BOk, Bank of Korea)', '서울(Seoul)', '중구 북창동'],
        [37.51911603308306, 126.92754466951683, '금융투자협회(KOFIA, Korea Financial Investment Association)', '서울(Seoul)', '영등포구 의사당대로'],
        [37.56087546167136, 126.97387594068131, '대한상공회의소(KCCI, Korea Chamber of Commerce and Industry)', '서울(Seoul)', '중구 소공동 세종대로'],
        [37.52301011750094, 126.92795401181027, '전국경제인연합회(FKI, The Federation of Korean Industries)', '서울(Seoul)', '영등포구 여의도동'],
        [37.51047697000619, 127.06099061184375, '한국무협협회(KITA, Korea International Trade Association)', '서울(Seoul)', '강남구 삼성1동'],
        [37.52830693340214, 126.92255203882621, '중소기업중앙회(KBIZ, Korea Federation of SMEs)', '서울(Seoul)', '영등포구 여의도동'],
        [37.548006902013455, 126.94109689835375, '한국경영자총협회(KEF, Korea Enterprises Federation)', '서울(Seoul)', '마포구 대흥동'],
        [37.545534365123046, 126.9445712830084, '한국중견기업연합회(FOMEK, Federation of Middle Market Enterprises of Korea)', '서울(Seoul)', '마포구 대흥동'],
        [37.486869191907694, 126.90606444067956,'소상공인연합회(KFME, Korea Federation of Micro Enterprise)', '서울(Seoul)', '동작구 신대방동'],
        [37.56510714476617, 126.98540256951776, '전국은행연합회(KFB, Korea Federation of Banks)', '서울(Seoul)', '중구 명동1가'],
        [37.575084756569005, 126.97518044068164, '금융위원회(FSC, Financial Services Commission)', '서울(Seoul)', '종로구'],
        [37.52575687234709, 126.92104460890528, '금융감독원(FSS, Financial Supervisory Service)', '서울(Seoul)', '영등포구 여의도동'],
        [37.50792709581974, 127.03907666284147, '금융결제원(KFTC, Korea Financial Telecommunications)', '서울(Seoul)', '강남구 역삼동'],
        [37.56863623872196, 126.98072144068145, '예금보험공사(KDIC, Korea Deposit Insurance Corporation)', '서울(Seoul)', '중구 청계천'],
        [37.52299321954385, 126.92820920395349, '한국거래소(KRX, Korea Exchange)', '서울(Seoul)', '영등포구 여의도동'],
        [37.57442767966258, 126.97994133813648, '서울지방국세청(Seoul National Tax Service)', '서울(Seoul)', '종로구 수송동'],
        [37.56650510474183, 126.98650968300878, 'IBK기업은행(Industrial Bank of Korea)', '서울(Seoul)', '중구 을지로'],
        [37.52817756116918, 126.9211435188903, '한국산업은행(Korea Development Bank)', '서울(Seoul)', '영등포구 여의도동'],
        [37.56756126904132, 126.97790426369977, '서민금융진흥원(Korea INclusive Finance Agency)', '서울(Seoul)', '중구 명동 세종대로'],
        [37.329024241677914, 127.12361975602158, '금융보안원(Financial Security Institute)', '용인(Youngin)', '수지구'],
        ]
df = pd.DataFrame(data)
df.columns = ["latitude", "longitude", "landmark", "city", "districts"] 

#df.to_csv('file.csv')
#df = pd.read_csv("https://raw.githubusercontent.com/ailever/openapi/master/analysis/file.csv")
Map = px.scatter_mapbox(df, lat="latitude", lon="longitude",
                        hover_name="landmark",
                        hover_data=["city", "districts"],
                        color_discrete_sequence=["fuchsia"],
                        zoom=12,
                        height=700)
Map.update_layout(mapbox_style="open-street-map")
Map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# O[T,1,0] : KCCI
KCCI = html.Div([dbc.Button("KCCI", color="dark", href='http://www.korcham.net/nCham/Service/Main/appl/Main.asp'),
                 dbc.Button("Organization", color="dark", href="http://www.korcham.net/nCham/Service/Kcci/appl/SeoulMemberStatus.asp"),
                 ])

# O[T,1,1] : KFI
FKI = html.Div([dbc.Button("FKI", color="dark", href="http://www.fki.or.kr/Main.aspx"),
                dbc.Button("Organization", color="dark", href="http://www.fki.or.kr/member/ceo.aspx"),
                ])
# O[T,2,0] : KITA
KITA = html.Div([dbc.Button("KITA", color="dark", href="https://www.kita.net/"),
                 dbc.Button("Organization", color="dark", href="https://www.kita.net/asocGuidance/asocGuidance/orgnztIntrcn/structure.do"),
                 ])
# O[T,2,1] : KBIZ
KBIZ = html.Div([dbc.Button("KBIZ", color="dark", href="https://www.kbiz.or.kr/ko/index/index.do"),
                 dbc.Button("Organization", color="dark", href="https://www.kbiz.or.kr/ko/contents/contents/contents.do?mnSeq=725"),
                 ])
# O[T,3,0] : KEF
KEF = html.Div([dbc.Button("KEF", color="dark", href="http://www.kefplaza.com/index.jsp"),
                dbc.Button("Organization", color="dark", href="http://www.kefplaza.com/kef/kef_kor_intro_4.jsp"),
                ])
# O[T,3,1] : FOMEK
FOMEK = html.Div([dbc.Button("FOMEK", color="dark", href="https://www.fomek.or.kr/main/index.php"),
                  dbc.Button("Organization", color="dark", href="https://www.fomek.or.kr/main/intro/group.php"),
                  ])
# O[T,4,0] : KFME
KFME = html.Div([dbc.Button("KFME", color="dark", href="http://www.kfme.or.kr/home/homeIndex.do"),
                 dbc.Button("Organization", color="dark", href="http://www.kfme.or.kr/user/nd30524.do"),
                 ])
# O[T,4,1] : KFB
KFB = html.Div([dbc.Button("KFB", color="dark", href="https://www.kfb.or.kr/main/main.php"),
                dbc.Button("Organization", color="dark", href="https://www.kfb.or.kr/kfb/kfb_organization.php"),
                ])






TR = """
[Home](https://www.tower-research.com/)
"""
KCG = """
"""

# O[T,1,0] : PDT Partners
PDT = """
"""

# O[T,1,1] : Citadel
Cit = """
"""

# O[T,2,0] : Two Sigma
TS = """
"""

# O[T,2,1] : IMC
IMC = """
"""

# O[T,3,0] : Hudson River Trading
HRT = """
"""

# O[T,3,1] : Jane Street
JS = """
"""


################################## CODEBLOCK ##################################
#%%
################################## DASHBOARD ##################################
T = {}
T['T,0,0'] = 'Map'
T['T,1,0'] = '대한상공회의소(KCCI)'
T['T,1,1'] = '전국경제인연합회(FKI)'
T['T,2,0'] = '한국무협협회(KITA)'
T['T,2,1'] = '중소기업중앙회(KBIZ)'
T['T,3,0'] = '한국경영자총협회(KEF)'
T['T,3,1'] = '한국중견기업연합회(FOMEK)'
T['T,4,0'] = '소상공인연합회(KFME)'
T['T,4,1'] = '전국은행연합회(KFB)'
O = {}
O['T,_,_'] = None
O['T,0,0'] = dcc.Graph(figure=Map)
O['T,1,0'] = KCCI
O['T,1,1'] = FKI
O['T,2,0'] = KITA
O['T,2,1'] = KBIZ
O['T,3,0'] = KEF
O['T,3,1'] = FOMEK
O['T,4,0'] = KFME
O['T,4,1'] = KFB
C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
C['T,0,0'] = [dbc.Card([dbc.CardHeader(T['T,0,0']), dbc.CardBody(O['T,0,0'])], color='light', inverse=False, outline=True)]
C['T,1,0'] = [dbc.Card([dbc.CardHeader(T['T,1,0']), dbc.CardBody(O['T,1,0'])], color='light', inverse=False, outline=True)]
C['T,1,1'] = [dbc.Card([dbc.CardHeader(T['T,1,1']), dbc.CardBody(O['T,1,1'])], color='light', inverse=False, outline=True)]
C['T,2,0'] = [dbc.Card([dbc.CardHeader(T['T,2,0']), dbc.CardBody(O['T,2,0'])], color='light', inverse=False, outline=True)]
C['T,2,1'] = [dbc.Card([dbc.CardHeader(T['T,2,1']), dbc.CardBody(O['T,2,1'])], color='light', inverse=False, outline=True)]
C['T,3,0'] = [dbc.Card([dbc.CardHeader(T['T,3,0']), dbc.CardBody(O['T,3,0'])], color='light', inverse=False, outline=True)]
C['T,3,1'] = [dbc.Card([dbc.CardHeader(T['T,3,1']), dbc.CardBody(O['T,3,1'])], color='light', inverse=False, outline=True)]
C['T,4,0'] = [dbc.Card([dbc.CardHeader(T['T,4,0']), dbc.CardBody(O['T,4,0'])], color='light', inverse=False, outline=True)]
C['T,4,1'] = [dbc.Card([dbc.CardHeader(T['T,4,1']), dbc.CardBody(O['T,4,1'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
contents['page']['tab1'] = [dbc.Row([dbc.Col(C['T,0,0'], width=12)]), html.Br(),
                            dbc.Row([dbc.Col(C['T,1,0'], width=6), dbc.Col(C['T,1,1'], width=6)]), html.Br(),
                            dbc.Row([dbc.Col(C['T,2,0'], width=6), dbc.Col(C['T,2,1'], width=6)]), html.Br(),
                            dbc.Row([dbc.Col(C['T,3,0'], width=6), dbc.Col(C['T,3,1'], width=6)]), html.Br(),
                            dbc.Row([dbc.Col(C['T,4,0'], width=6), dbc.Col(C['T,4,1'], width=6)]), html.Br(),
                            html.Br()]
contents['page']['tab2'] = [dbc.Row([dbc.Col(C['T,0,0'], width=12)]), html.Br(),
                           html.Br()]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="Korea", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1'])), label="USA", disabled=False),
                                 ])
main = dbc.Jumbotron([html.H2('analysis/Finance'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("GitHub", color="secondary", href='https://github.com/ailever/ailever/tree/master/ailever/analysis'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/tree/master/analysis'),
                                dbc.Button("Wiki", color="secondary", href='https://github.com/ailever/ailever/wiki'),
                                dbc.Button("Docs", color="secondary", href='https://ailever.readthedocs.io/en/latest/detection/index.html'),
                                dbc.Button("Naver", color="secondary", href="https://news.naver.com/"),
                                dbc.Button("Google Trend", color="secondary", href="https://trends.google.com/trends/explore"),
                                dbc.Button("DataLab", color="secondary", href="https://datalab.naver.com/"),
                                dbc.Button('Kakao Map', color='secondary', href="https://map.kakao.com/"),
                                dbc.Button('Google Map', color='secondary', href="https://www.google.co.kr/maps/"),
                                dbc.Button("Plotly", color="secondary", href="https://plotly.com/python/"),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.Div([dbc.Button("Bank of Korea", color="dark", href="http://www.bok.or.kr/portal/main/main.do"),
                                dbc.Button("egroup", color="dark", href="https://www.egroup.go.kr/egps/wi/mainPage.do"),
                                dbc.Button("dart", color="dark", href="http://dart.fss.or.kr/"),
                                dbc.Button("United States Federal Reserve System", color="dark", href="https://www.federalreserve.gov/"),
                                dbc.Button("OECD", color="dark", href="http://www.oecd.org/"),
                                dbc.Button("Investopedia", color="dark", href="https://www.investopedia.com/"),
                                dbc.Button("Investing", color="dark", href="https://www.investing.com/"),
                                dbc.Button("Economist", color="dark", href="https://www.economist.com/"),
                                dbc.Button("Bloomberg", color="dark", href="https://www.bloomberg.com/"),
                                dbc.Button("The Wall Street Journal", color='dark', href="https://www.wsj.com/"),
                                ]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
