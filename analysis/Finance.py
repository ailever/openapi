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

Component = type('Component', (dict,), {})

KR = Component()
# O[T1,T1,-1,0] : Korean Financial Organization
KR['T1,T1,-1,0'] = html.Div([dbc.Button("Bank of Korea", color="dark", href="http://www.bok.or.kr/portal/main/main.do"),
                             dbc.Button("Financial Service Commision", color="dark", href="http://www.fsc.go.kr/index"),
                             dbc.Button("Financial Supervisory Service", color="dark", href="http://www.fss.or.kr/fss/kr/main.html"),
                             dbc.Button("Korea Finance Consumer Federation", color="dark", href="http://kfco.org/index.asp"),
                             dbc.Button("Korea Capital Market Institue", color="dark", href="https://www.kcmi.re.kr/"),
                             ])
                                

# O[T1,T1,0,0] : Map
KR.places = [[37.586786, 126.974736, '청와대(Cheong Wh Dae)', '서울(Seoul)', "종로구 세종로"],
             [37.563184116699055, 126.97959495769867, '한국은행(BOk, Bank of Korea)', '서울(Seoul)', '중구 북창동'],
             [37.51911603308306, 126.92754466951683, '금융투자협회(KOFIA, Korea Financial Investment Association), 자본시장연구원(Korea Capital Market Institue)', '서울(Seoul)', '영등포구 의사당대로'],
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
             [37.57461475785703, 126.97359235602721, '금융소비자연맹(Korea Finance Consumer Federation)', '서울(Seoul)', '종로구 사직동'],
             [37.329024241677914, 127.12361975602158, '금융보안원(Financial Security Institute)', '용인(Youngin)', '수지구'],
             ]
KR.places = pd.DataFrame(KR.places)
KR.places.columns = ["latitude", "longitude", "landmark", "city", "districts"] 

#df.to_csv('file.csv')
#df = pd.read_csv("https://raw.githubusercontent.com/ailever/openapi/master/analysis/file.csv")
Map_korea = px.scatter_mapbox(KR.places, lat="latitude", lon="longitude",
                              hover_name="landmark",
                              hover_data=["city", "districts"],
                              color_discrete_sequence=["fuchsia"],
                              zoom=12,
                              height=700)
Map_korea.update_layout(mapbox_style="open-street-map")
Map_korea.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
KR['T1,T1,0,0'] = dcc.Graph(figure=Map_korea)


# O[T1,T1,1,0] : KCCI
KR['T1,T1,1,0'] = html.Div([dbc.Button("KCCI", color="dark", href='http://www.korcham.net/nCham/Service/Main/appl/Main.asp'),
                            dbc.Button("Organization", color="dark", href="http://www.korcham.net/nCham/Service/Kcci/appl/SeoulMemberStatus.asp"),
                            ])

# O[T1,T1,1,1] : KFI
KR['T1,T1,1,1'] = html.Div([dbc.Button("FKI", color="dark", href="http://www.fki.or.kr/Main.aspx"),
                            dbc.Button("Organization", color="dark", href="http://www.fki.or.kr/member/ceo.aspx"),
                            ])
# O[T1,T1,2,0] : KITA
KR['T1,T1,2,0'] = html.Div([dbc.Button("KITA", color="dark", href="https://www.kita.net/"),
                            dbc.Button("Organization", color="dark", href="https://www.kita.net/asocGuidance/asocGuidance/orgnztIntrcn/structure.do"),
                            ])
# O[T1,T1,2,1] : KBIZ
KR['T1,T1,2,1'] = html.Div([dbc.Button("KBIZ", color="dark", href="https://www.kbiz.or.kr/ko/index/index.do"),
                            dbc.Button("Organization", color="dark", href="https://www.kbiz.or.kr/ko/contents/contents/contents.do?mnSeq=725"),
                            ])
# O[T1,T1,3,0] : KEF
KR['T1,T1,3,0'] = html.Div([dbc.Button("KEF", color="dark", href="http://www.kefplaza.com/index.jsp"),
                            dbc.Button("Organization", color="dark", href="http://www.kefplaza.com/kef/kef_kor_intro_4.jsp"),
                            ])
# O[T1,T1,3,1] : FOMEK
KR['T1,T1,3,1'] = html.Div([dbc.Button("FOMEK", color="dark", href="https://www.fomek.or.kr/main/index.php"),
                            dbc.Button("Organization", color="dark", href="https://www.fomek.or.kr/main/intro/group.php"),
                            ])
# O[T1,T1,4,0] : KFME
KR['T1,T1,4,0'] = html.Div([dbc.Button("KFME", color="dark", href="http://www.kfme.or.kr/home/homeIndex.do"),
                            dbc.Button("Organization", color="dark", href="http://www.kfme.or.kr/user/nd30524.do"),
                            ])
# O[T1,T1,4,1] : KFB
KR['T1,T1,4,1'] = html.Div([dbc.Button("KFB", color="dark", href="https://www.kfb.or.kr/main/main.php"),
                            dbc.Button("Organization", color="dark", href="https://www.kfb.or.kr/kfb/kfb_organization.php"),
                            ])

# O[T1,T2,0,0] : Corporate finance
KR['T1,T2,0,0'] = html.Div([dbc.Button("NH투자증권", color="dark", href="https://www.nhqv.com/"),
                            dbc.Button("한국투자증권", color="dark", href="https://www.truefriend.com/bankis/main.jsp"),
                            dcc.Markdown("""
## 2020 Best Firms

NH투자증권, 한국투자증권, 삼성증권, 신한금융투자, KB증권, 미래에셋대우, 메리츠종합금융증권 , 하나금융투자, 키움증권,
씨티그룹글로벌마켓증권, 유화증권, 교보증권, 한화투자증권, 메릴린치인터내셔날엘엘씨증권 서울지점, 유안타증권, 모간스탠리인터내셔날증권회사서울지점,
ING증권 서울지점, 제이피모간증권회사서울지점, 현대차증권, 크레디트스위스증권서울지점, 신영증권, 도이치증권, BNK투자증권, 대신증권,
미즈호증권아시아리미티드 서울지점, 노무라금융투자, 크레디 아그리콜 아시아증권 서울지점, 한국 에스지증권 ,  카카오페이증권, 골드만삭스증권회사서울지점,
UBS증권리미티드서울지점, 부국증권, 흥국증권, 이베스트투자증권, DB금융투자, CGS-CIMB증권 한국지점, 하이투자증권, SK증권, IBK투자증권, 한양증권,
맥쿼리증권, 한국스탠다드차타드증권, KTB 투자증권, 리딩투자증권, CLSA코리아증권, 다이와증권캐피탈마켓코리아, 초상증권(한국), 상상인증권,
비엔피파리바증권, 코리아에셋투자증권, KIDB채권중개, KR투자증권, 케이프투자증권, DS투자증권, 홍콩상하이증권서울지점, 유진투자증권
""")])


US = Component()
# O[T2,T1,-1,0] : USA Financial Organization
US['T2,T1,-1,0'] = html.Div([dbc.Button("United States Federal Reserve System", color="dark", href="https://www.federalreserve.gov/"),
                             dbc.Button("U.S. DEPARTMENT OF THE TREASURY", color="dark", href="https://home.treasury.gov/"), html.Br(),
                             dcc.Markdown("""
- [List of investment banks](https://en.wikipedia.org/wiki/List_of_investment_banks)
- [List of asset management firms](https://en.wikipedia.org/wiki/List_of_asset_management_firms)
- [List of hedge funds](https://en.wikipedia.org/wiki/List_of_hedge_funds)
- [List of private-equity firms](https://en.wikipedia.org/wiki/List_of_private-equity_firms)
- [List of venture capital firms](https://en.wikipedia.org/wiki/List_of_venture_capital_firms)
- [List of financial institutions that invest in infrastructure](https://en.wikipedia.org/wiki/List_of_financial_institutions_that_invest_in_infrastructure)
""")])

# O[T2,T1,0,0] : Map
US.places = [[38.89785584308, -77.03649226586968, 'The White House', '1600 Pennsylvania Avenue NW', "Washington, DC 20500"],
             ]
US.places = pd.DataFrame(US.places)
US.places.columns = ["latitude", "longitude", "landmark", "city", "districts"] 

#df.to_csv('file.csv')
#df = pd.read_csv("https://raw.githubusercontent.com/ailever/openapi/master/analysis/file.csv")
Map_usa = px.scatter_mapbox(US.places, lat="latitude", lon="longitude",
                              hover_name="landmark",
                              hover_data=["city", "districts"],
                              color_discrete_sequence=["fuchsia"],
                              zoom=4,
                              height=700)
Map_usa.update_layout(mapbox_style="open-street-map")
Map_usa.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
US['T2,T1,0,0'] = dcc.Graph(figure=Map_usa)

# O[T2,T2,0,0] : Corporate finance
US['T2,T2,0,0'] = html.Div([])



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
# KOREA Titles 
T['T1,T1,-1,0'] = 'Korean Financial Organization(KFO)'
T['T1,T1,0,0'] = 'Map'
T['T1,T1,1,0'] = '대한상공회의소(KCCI)'
T['T1,T1,1,1'] = '전국경제인연합회(FKI)'
T['T1,T1,2,0'] = '한국무협협회(KITA)'
T['T1,T1,2,1'] = '중소기업중앙회(KBIZ)'
T['T1,T1,3,0'] = '한국경영자총협회(KEF)'
T['T1,T1,3,1'] = '한국중견기업연합회(FOMEK)'
T['T1,T1,4,0'] = '소상공인연합회(KFME)'
T['T1,T1,4,1'] = '전국은행연합회(KFB)'
T['T1,T2,0,0'] = 'Corporate Finance'
# USA Titles 
T['T2,T1,-1,0'] = 'USA Financial Organization(UFO)'
T['T2,T1,0,0'] = 'Map'
T['T2,T2,0,0'] = 'Corporate Finance'

O = {}
O['T,T,_,_'] = None
# KOREA Objects
O['T1,T1,-1,0'] = KR['T1,T1,-1,0']
O['T1,T1,0,0'] = KR['T1,T1,0,0']
O['T1,T1,1,0'] = KR['T1,T1,1,0']
O['T1,T1,1,1'] = KR['T1,T1,1,1']
O['T1,T1,2,0'] = KR['T1,T1,2,0']
O['T1,T1,2,1'] = KR['T1,T1,2,1']
O['T1,T1,3,0'] = KR['T1,T1,3,0']
O['T1,T1,3,1'] = KR['T1,T1,3,1']
O['T1,T1,4,0'] = KR['T1,T1,4,0']
O['T1,T1,4,1'] = KR['T1,T1,4,1']
O['T1,T2,0,0'] = KR['T1,T2,0,0']
# USA Objects
O['T2,T1,-1,0'] = US['T2,T1,-1,0']
O['T2,T1,0,0'] = US['T2,T1,0,0']
O['T2,T2,0,0'] = US['T2,T2,0,0']

C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
# KOREA Components
C['T1,T1,-1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,-1,0']), dbc.CardBody(O['T1,T1,-1,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,0,0']), dbc.CardBody(O['T1,T1,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,1,0']), dbc.CardBody(O['T1,T1,1,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,1,1'] = [dbc.Card([dbc.CardHeader(T['T1,T1,1,1']), dbc.CardBody(O['T1,T1,1,1'])], color='light', inverse=False, outline=True)]
C['T1,T1,2,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,2,0']), dbc.CardBody(O['T1,T1,2,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,2,1'] = [dbc.Card([dbc.CardHeader(T['T1,T1,2,1']), dbc.CardBody(O['T1,T1,2,1'])], color='light', inverse=False, outline=True)]
C['T1,T1,3,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,3,0']), dbc.CardBody(O['T1,T1,3,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,3,1'] = [dbc.Card([dbc.CardHeader(T['T1,T1,3,1']), dbc.CardBody(O['T1,T1,3,1'])], color='light', inverse=False, outline=True)]
C['T1,T1,4,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,4,0']), dbc.CardBody(O['T1,T1,4,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,4,1'] = [dbc.Card([dbc.CardHeader(T['T1,T1,4,1']), dbc.CardBody(O['T1,T1,4,1'])], color='light', inverse=False, outline=True)]
C['T1,T2,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T2,0,0']), dbc.CardBody(O['T1,T2,0,0'])], color='light', inverse=False, outline=True)]
# USA Components
C['T2,T1,-1,0'] = [dbc.Card([dbc.CardHeader(T['T2,T1,-1,0']), dbc.CardBody(O['T2,T1,-1,0'])], color='light', inverse=False, outline=True)]
C['T2,T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T1,0,0']), dbc.CardBody(O['T2,T1,0,0'])], color='light', inverse=False, outline=True)]
C['T2,T2,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T2,0,0']), dbc.CardBody(O['T2,T2,0,0'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
# KOREA Tabs
contents['page']['tab1'] = {}
contents['page']['tab1']['tab1'] = [dbc.Row([dbc.Col(C['T1,T1,-1,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,1,0'], width=6), dbc.Col(C['T1,T1,1,1'], width=6)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,2,0'], width=6), dbc.Col(C['T1,T1,2,1'], width=6)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,3,0'], width=6), dbc.Col(C['T1,T1,3,1'], width=6)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,4,0'], width=6), dbc.Col(C['T1,T1,4,1'], width=6)]), html.Br(),
                                    html.Br()]
contents['page']['tab1']['tab2'] = [dbc.Row([dbc.Col(C['T1,T2,0,0'], width=12)]), html.Br(),
                                    ]
# USA Tabs
contents['page']['tab2'] = {}
contents['page']['tab2']['tab1'] = [dbc.Row([dbc.Col(C['T2,T1,-1,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T2,T1,0,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab2']['tab2'] = [dbc.Row([dbc.Col(C['T2,T2,0,0'], width=12)]), html.Br(),
                                    ]

# TAB1 : KOREA
contents['page']['tab1']['tabs'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab1'])), label="Main", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab2'])), label="Corporate Finance", disabled=False),
                                             ])
# TAB2 : USA
contents['page']['tab2']['tabs'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab1'])), label="Main", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab2'])), label="Corporate Finance", disabled=False),
                                             ])

page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tabs'])), label="Korea", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tabs'])), label="USA", disabled=False),
                                 ])

main = dbc.Jumbotron([html.H2('analysis/Finance'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("GitHub", color="secondary", href='https://github.com/ailever/ailever/tree/master/ailever/analysis'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/analysis/Finance.py'),
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
