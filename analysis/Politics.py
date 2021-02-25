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
#vis = Visdom(server=config['visdom-server'], port=config['visdom-port'], env='main') # python -m visdom.sever [-post, --hostname]
#vis.close(env='main')
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
################################## CONFIG ##################################
#%%
################################## CODEBLOCK ##################################
from plotly.subplots import make_subplots
import plotly.graph_objs as go

Component = type('Component', (dict,), {})

# O[T1,T1] : Korea/Press
KR = Component()
KR['T1,T1,0,0'] = html.Div([html.Div([html.P('MAIN'),
                                      dbc.Button('Naver', color='dark', href="https://news.naver.com/"),
                                      dbc.Button('서울신문', color='dark', href="https://www.seoul.co.kr/"),
                                      dbc.Button('조선일보', color='dark', href="https://www.chosun.com/"),
                                      dbc.Button('동아일보', color='dark', href="https://www.donga.com/"),
                                      dbc.Button('경향신문', color='dark', href="http://www.khan.co.kr/"),
                                      dbc.Button('한국일보', color='dark', href="https://www.hankookilbo.com/"),
                                      dbc.Button('중앙일보', color='dark', href="https://joongang.joins.com/"),
                                      dbc.Button('한겨례', color='dark', href="http://www.hani.co.kr/"),
                                      dbc.Button('국민일보', color='dark', href="http://www.kmib.co.kr/news/index.asp"),
                                      dbc.Button('세계일보', color='dark', href="http://www.segye.com/"),
                                      dbc.Button('문화일보', color='dark', href="http://www.munhwa.com/")]),
                            html.Div([html.P('Opinion'),
                                      dbc.Button('서울신문', color='secondary', href="https://www.seoul.co.kr/news/newsList.php?section=editorial"),
                                      dbc.Button('조선일보', color='secondary', href="https://www.chosun.com/opinion/"),
                                      dbc.Button('동아일보', color='secondary', href="https://www.donga.com/news/Opinion"),
                                      dbc.Button('경향신문', color='secondary', href="http://news.khan.co.kr/kh_opinion/"),
                                      dbc.Button('한국일보', color='secondary', href="https://www.hankookilbo.com/Opinion"),
                                      dbc.Button('중앙일보', color='secondary', href="https://news.joins.com/opinion?cloc=joongang-home-megatop"),
                                      dbc.Button('한겨례', color='secondary', href="http://www.hani.co.kr/arti/opinion/editorial/home01.html"),
                                      dbc.Button('국민일보', color='secondary', href="http://www.kmib.co.kr/opinion/index.asp"),
                                      dbc.Button('세계일보', color='secondary', href="http://www.segye.com/news/opinion"),
                                      dbc.Button('문화일보', color='secondary', href="http://www.munhwa.com/news/section.html?sec=opinion"),
                                      ])])
KR['T1,T1,1,0'] = html.Embed(src='https://news.naver.com/', style={'width':'100%', 'height':'700px'})
KR['T1,T1,2,0'] = html.Embed(src='https://www.seoul.co.kr/', style={'width':'100%', 'height':'700px'})
KR['T1,T1,3,0'] = html.Embed(src='https://www.chosun.com/', style={'width':'100%', 'height':'700px'})
KR['T1,T1,4,0'] = html.Embed(src='https://www.donga.com/', style={'width':'100%', 'height':'700px'})
KR['T1,T1,5,0'] = html.Embed(src='https://www.hankookilbo.com/', style={'width':'100%', 'height':'700px'})
KR['T1,T1,6,0'] = html.Embed(src='https://joongang.joins.com/', style={'width':'100%', 'height':'700px'})
KR['T1,T1,7,0'] = html.Embed(src='http://www.hani.co.kr/', style={'width':'100%', 'height':'700px'})
KR['T1,T1,8,0'] = html.Embed(src='http://www.kmib.co.kr/news/index.asp', style={'width':'100%', 'height':'700px'})
KR['T1,T1,9,0'] = html.Embed(src='http://www.segye.com/', style={'width':'100%', 'height':'700px'})
KR['T1,T1,10,0'] = html.Embed(src='http://www.munhwa.com/', style={'width':'100%', 'height':'700px'})


# O[T1,T2] : Korea/Adminstration
KR['T1,T2,0,0'] = html.Div([dbc.Button('Order of Precedence', color='dark', href="https://en.wikipedia.org/wiki/South_Korean_order_of_precedence"),
                            dbc.Button('Korea', color='dark', href="https://www1.president.go.kr/about/government-organization"),
                            dbc.Button('청와대', color='dark', href="https://www1.president.go.kr/about/organization"),
                            dbc.Button('국무회의', color='dark', href="https://www1.president.go.kr/c/blue-house-stories"),
                            dbc.Button('정부인사', color='dark', href="https://namu.wiki/w/%EB%AC%B8%EC%9E%AC%EC%9D%B8%20%EC%A0%95%EB%B6%80/%EC%9D%B8%EC%82%AC"),
                            dbc.Button('법제처', color='dark', href="https://www.moleg.go.kr/"),
                            dbc.Button('법무부', color='dark', href="https://www.moj.go.kr/moj/index.do"),
                            dbc.Button('검찰청', color='dark', href="https://www.spo.go.kr/site/spo/main.do"),
                            dbc.Button('감사원', color='dark', href="https://www.bai.go.kr/bai/html/intro/organ/organizationchart.do;jsessionid=4rTWGWBrnjNCl3O7iF7-Xv0b.node01?mdex=bai83"),
                            dbc.Button('공정거래위원회', color='dark', href="https://www.ftc.go.kr/"),
                            dbc.Button('금융위원회', color='dark', href="http://www.fsc.go.kr/fsc040101"),
                            dbc.Button('금융감독원', color='dark', href="http://www.fss.or.kr/fss/kr/main.html"),
                            dbc.Button('기획재정부', color='dark', href="https://www.moef.go.kr/mi/orgnzt/org.do;jsessionid=9pLke3Kf4H9EZ0mVnLFi0Llt.node30?bbsId=MOSFBBS_000000000097&menuNo=9040100"),
                            dbc.Button('국세청', color='dark', href="https://nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6740&cntntsId=8140"),
                            ])
KR['T1,T2,1,0'] = html.Embed(src='https://www1.president.go.kr/about/government-organization', style={'width':'100%', 'height':'700px'})
KR['T1,T2,2,0'] = html.Div([html.Embed(src='https://www1.president.go.kr/about/organization', style={'width':'100%', 'height':'700px'}),
                            dcc.Markdown("""
                            ## Office of the President
                            - [Organization](https://www.law.go.kr/법령/대통령비서실직제)

                            """),])
KR['T1,T2,3,0'] = html.Embed(src='https://www.bai.go.kr/bai/html/intro/organ/organizationchart.do;jsessionid=4rTWGWBrnjNCl3O7iF7-Xv0b.node01?mdex=bai83', style={'width':'100%', 'height':'700px'})
KR['T1,T2,4,0'] = html.Embed(src='http://www.fsc.go.kr/fsc040101', style={'width':'100%', 'height':'700px'})
KR['T1,T2,5,0'] = html.Embed(src='https://www.moef.go.kr/mi/orgnzt/org.do;jsessionid=9pLke3Kf4H9EZ0mVnLFi0Llt.node30?bbsId=MOSFBBS_000000000097&menuNo=9040100', style={'width':'100%', 'height':'700px'})
KR['T1,T2,6,0'] = html.Embed(src='https://nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6740&cntntsId=8140', style={'width':'100%', 'height':'700px'})

# O[T1,T3] : Korea/Parties
KR['T1,T3,0,0'] = html.Div([dbc.Button('정당 목록', color="dark", href="https://namu.wiki/w/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/%EC%A0%95%EB%8B%B9/%EB%AA%A9%EB%A1%9D"), 
                            dbc.Button('정당 계보', color="dark", href="http://web.archive.org/web/20191128112759/http://museum.nec.go.kr/vote/voteKorea2.do"),
                            dbc.Button('더불어민주당', color='dark', href="https://theminjoo.kr/introduce/location"),
                            dbc.Button('더불어민주당/인사', color='dark', href="https://namu.wiki/w/%EB%8D%94%EB%B6%88%EC%96%B4%EB%AF%BC%EC%A3%BC%EB%8B%B9/%EC%A7%80%EB%8F%84%EB%B6%80"),
                            dbc.Button('국민의힘', color='dark', href="http://www.peoplepowerparty.kr/renewal/about/organization.do"),
                            dbc.Button('국민의당', color='dark', href="http://peopleparty.kr/"),
                            ])
KR['T1,T3,1,0'] = html.Embed(src='https://theminjoo.kr/introduce/location', style={'width':'100%', 'height':'700px'})
KR['T1,T3,2,0'] = html.Embed(src='http://www.peoplepowerparty.kr/renewal/about/organization.do', style={'width':'100%', 'height':'700px'})

# O[T1,T4] : Korea/Assembly
KR['T1,T4,0,0'] = html.Div([dbc.Button('Assembly', color='dark', href="https://www.assembly.go.kr/assm/userMain/main.do"),
                            dbc.Button('입법예고', color='dark', href="http://pal.assembly.go.kr/main/mainView.do"),
                            dbc.Button('위원회', color='dark', href="https://www.assembly.go.kr/assm/assemact/committee/committee01/assmCommittee/committeeUserList.do"),
                            dbc.Button('국정감사', color='dark', href="https://www.assembly.go.kr/assm/assemact/inspection/inspection01/assmInspection/inspectionUserList.do"),
                            dbc.Button('계류의안', color='dark', href="http://likms.assembly.go.kr/bill/MooringBill.do"),
                            dbc.Button('처리의안', color='dark', href="http://likms.assembly.go.kr/bill/FinishBill.do"),
                            ])
KR['T1,T4,1,0'] = html.Embed(src='https://finance.na.go.kr:444/finance/statute/statute01.do', style={'width':'100%', 'height':'700px'})

# O[T1,T5] : Korea/Judiciary
KR['T1,T5,0,0'] = html.Div([dbc.Button('법령센터', color='dark', href="https://www.law.go.kr/LSW/main.html"),
                            dbc.Button('Supreme Court of Korea', color='dark', href="https://www.scourt.go.kr/supreme/supreme.jsp"),
                            ])
KR['T1,T5,1,0'] = html.Div([dbc.Button("Kim & Chang", color='dark', href="https://www.kimchang.com/ko/main.kc"),
                            dbc.Button("Lee & Ko", color='dark', href="http://www.leeko.com/newmain/index.do?lang=KR"),
                            dbc.Button("YULCHON LLC", color='dark', href="https://www.yulchon.com/ko/main/main.do"),
                            dbc.Button("YOON & YANG", color='dark', href="http://www.hwawoo.com/kor/main.do"),
                            dbc.Button("Bae, Kim & Lee LLC", color='dark', href="http://www.bkl.co.kr/main/ko/main.jsp#law/main.jsp"),
                            dbc.Button("SHIN & KIM", color='dark', href="https://www.shinkim.com/kor"),
                            dbc.Button("BARUNLAW", color='dark', href="https://www.barunlaw.com/"),
                            dbc.Button("DONGIN", color='dark', href="http://www.donginlaw.co.kr/"),
                            dbc.Button("JIPYONG", color='dark', href="http://www.jipyong.com/kr/main/main.php"),
                            dbc.Button("HMP", color='dark', href="http://hmplaw.com/html/"),
                            dbc.Button("KCL", color='dark', href="http://www.kcllaw.com/"),
                            dcc.Markdown("""
                            ## Kim & Chang
                            ## Lee & Ko
                            ## YULCHON LLC
                            ## YOON & YANG
                            ## Bae, Kim & Lee LLC
                            ## SHIN & KIM
                            ## BARUNLAW
                            ## DONGIN
                            ## JIPYONG
                            ## HMP
                            ## KCL
                            """),
                            ])

# O[T1,T6] : Korea/Elections
KR['T1,T6,0,0'] = html.Div([dbc.Button('중앙선거관리위원회', color='dark', href="https://nec.go.kr/site/nec/main.do"),
                            dbc.Button('22/대선', color='dark', href="https://namu.wiki/w/%EC%A0%9C20%EB%8C%80%20%EB%8C%80%ED%86%B5%EB%A0%B9%20%EC%84%A0%EA%B1%B0"),
                            dbc.Button('24/총선', color='dark', href="https://namu.wiki/w/%EC%A0%9C22%EB%8C%80%20%EA%B5%AD%ED%9A%8C%EC%9D%98%EC%9B%90%20%EC%84%A0%EA%B1%B0"),
                            dbc.Button('22/지선', color='dark', href="https://namu.wiki/w/%EC%A0%9C8%ED%9A%8C%20%EC%A0%84%EA%B5%AD%EB%8F%99%EC%8B%9C%EC%A7%80%EB%B0%A9%EC%84%A0%EA%B1%B0"),
                            dbc.Button('21/재보선', color='dark', href="https://namu.wiki/w/2021%EB%85%84%20%EC%9E%AC%EB%B3%B4%EA%B6%90%EC%84%A0%EA%B1%B0"),
                            ])

# O[T1,T7] : Korea/Local Goverment
KR['T1,T7,0,0'] = html.Div([dbc.Button('Seoul', color='dark', href="https://www.seoul.go.kr/main/index.jsp"),
                            dbc.Button('Busan', color='dark', href="https://www.busan.go.kr/open/index.jsp"),
                            dbc.Button('Daegu', color='dark', href="http://www.daegu.go.kr/intro.jsp"),
                            dbc.Button('Incheon', color='dark', href="https://www.incheon.go.kr/index"),
                            dbc.Button('Gwangju', color='dark', href="https://www.gwangju.go.kr/intro/index.html"),
                            dbc.Button('Daejeon', color='dark', href="https://www.daejeon.go.kr/index.do"),
                            dbc.Button('Ulsan', color='dark', href="https://www.ulsan.go.kr/u/rep/main.ulsan"),
                            dbc.Button('Sejong', color='dark', href="https://www.sejong.go.kr/index.jsp"),
                            dbc.Button('Gyeonggi', color='dark', href="https://www.gg.go.kr/"),
                            dbc.Button('Gangwon', color='dark', href="http://www.provin.gangwon.kr/gw/portal"),
                            dbc.Button('Chungcheonbuk', color='dark', href="https://www.chungbuk.go.kr/intro/index.html"),
                            dbc.Button('Chungcheonnam', color='dark', href="http://www.chungnam.go.kr/main.do"),
                            dbc.Button('Jeollabuk', color='dark', href="https://www.jeonbuk.go.kr/index.jeonbuk"),
                            dbc.Button('Jeollanam', color='dark', href="https://www.jeonnam.go.kr/main.do"),
                            dbc.Button('Gyeongsangbuk', color='dark', href="https://www.gb.go.kr/Main/index.html"),
                            dbc.Button('Gyeongsangnam', color='dark', href="https://www.gyeongnam.go.kr/index.gyeong"),
                            dbc.Button('Jeju', color='dark', href="https://www.jeju.go.kr/index.htm"),
                            ])
KR['T1,T7,1,0'] = html.Div([])
KR['T1,T7,2,0'] = html.Div([])
KR['T1,T7,3,0'] = html.Div([])
KR['T1,T7,4,0'] = html.Div([])
KR['T1,T7,5,0'] = html.Div([])
KR['T1,T7,6,0'] = html.Div([])
KR['T1,T7,7,0'] = html.Div([])
KR['T1,T7,8,0'] = html.Div([])
KR['T1,T7,9,0'] = html.Div([])
KR['T1,T7,10,0'] = html.Div([])
KR['T1,T7,11,0'] = html.Div([])
KR['T1,T7,12,0'] = html.Div([])
KR['T1,T7,13,0'] = html.Div([])
KR['T1,T7,14,0'] = html.Div([])
KR['T1,T7,15,0'] = html.Div([])
KR['T1,T7,16,0'] = html.Div([])
KR['T1,T7,17,0'] = html.Div([])

# O[T1,T8] : Korea/Figures
KR['T1,T8,0,0'] = dcc.Markdown("""
- 노무현(46), 정세균(50), 이낙연(52), 문재인(53), 이재명(64), 박주민(74),   
  - 정성호, 김영진, 김병욱, 이규민, 김경수, 김태년, 윤호중, 전해철, 
  추미애, 임종석, 우상호, 이인영, 김민석, 홍익표, 노웅래, 김부겸, 
  김두관, 송영길, 설훈, 우원식, 인재근, 소병훈, 진성준, 양향자, 최재성, 
  이개호, 오영훈, 최인호, 정춘숙, 김영주, 김성주, 이원욱, 노웅래, 김부겸, 김두관, 송영길
- 김종인(40), 이명박(41), 박근혜(52), 홍준표(53), 황교안(57), 유승민(58), 정진석(60), 원희룡(64), 
  - 유의동, 류성걸, 김희국, 김웅, 주호영, 박진, 장제원, 김기현, 
  김성태, 박성중, 홍문표, 황보승희, 윤한홍, 윤재옥, 송언석, 배현진, 
  곽상도, 추경호, 정점식, 김도읍, 서병수, 김태흠, 박대출, 이헌승, 하태경, 조경태, 조해진,
- 안철수(62), 정동영, 박지원, 천정배, 박주선, 주승용, 손학규
""")
KR['T1,T8,1,0'] = html.Embed(src='https://news.naver.com/', style={'width':'100%', 'height':'700px'})


# O[T2,0,0] : United States
US = Component()
US['T2,T1,0,0'] = html.Div([dbc.Button('Cable News Network(CNN)', color='dark', href="https://edition.cnn.com/"),
                            ])
US['T2,T1,1,0'] = html.Embed(src='https://edition.cnn.com/', style={'width':'100%', 'height':'700px'})
US['T2,T2,0,0'] = html.Div([dbc.Button('Order of Precedence', color='dark', href="https://en.wikipedia.org/wiki/United_States_order_of_precedence"),
                            dbc.Button('The United States Government', color='dark', href="https://www.usa.gov/"),
                            dbc.Button('The white house', color='dark', href="https://www.whitehouse.gov/"),
                            dbc.Button('Organization', color='dark', href="https://www.whitehouse.gov/about-the-white-house/our-government/"),
                            dbc.Button('United States Department of Treasury', color='dark', href="https://home.treasury.gov/"),
                            ])
US['T2,T3,0,0'] = html.Div([])
US['T2,T4,0,0'] = html.Div([])
US['T2,T5,0,0'] = html.Div([])
US['T2,T5,1,0'] = dcc.Markdown("""
- [List of largest law firms by revenue](https://en.wikipedia.org/wiki/List_of_largest_law_firms_by_revenue)
- [List of largest law firms by profits per partner](https://en.wikipedia.org/wiki/List_of_largest_law_firms_by_profits_per_partner)
""")
US['T2,T6,0,0'] = html.Div([])
US['T2,T7,0,0'] = html.Div([])
US['T2,T8,0,0'] = dcc.Markdown("""

""")


# O[T3,T1,0,0] : International
IO = Component()
IO['T3,T1,0,0'] = html.Div([])

################################## CODEBLOCK ##################################
#%%
################################## DASHBOARD ##################################
T = {}
# KOREA Titles 
T['T1,T1,0,0'] = 'Press'
T['T1,T1,1,0'] = 'Naver'
T['T1,T1,2,0'] = '서울신문'
T['T1,T1,3,0'] = '조선일보'
T['T1,T1,4,0'] = '동아일보'
T['T1,T1,5,0'] = '한국일보'
T['T1,T1,6,0'] = '중앙일보'
T['T1,T1,7,0'] = '한겨례'
T['T1,T1,8,0'] = '국민일보'
T['T1,T1,9,0'] = '세계일보'
T['T1,T1,10,0'] = '문화일보'
T['T1,T2,0,0'] = 'Administration'
T['T1,T2,1,0'] = 'Korea'
T['T1,T2,2,0'] = '청와대'
T['T1,T2,3,0'] = '감사원'
T['T1,T2,4,0'] = '금융위원회'
T['T1,T2,5,0'] = '기획재정부'
T['T1,T2,6,0'] = '국세청'
T['T1,T3,0,0'] = 'Parties'
T['T1,T3,1,0'] = '더불어민주당'
T['T1,T3,2,0'] = '국민의힘'
T['T1,T4,0,0'] = 'Assembly'
T['T1,T4,1,0'] = '기획재정위원회'
T['T1,T5,0,0'] = 'Judiciary'
T['T1,T5,1,0'] = 'Law Firms'
T['T1,T6,0,0'] = 'Elections'
T['T1,T7,0,0'] = 'Local Governments'
T['T1,T7,1,0'] = 'Seoul Metropolitan Government'
T['T1,T7,2,0'] = 'Busan Metropolitan City'
T['T1,T7,3,0'] = 'Daegu Metropolitan City'
T['T1,T7,4,0'] = 'Incheon Metropolitan City'
T['T1,T7,5,0'] = 'Gwangju Metropolitan City'
T['T1,T7,6,0'] = 'Daejeon Metropolitan City'
T['T1,T7,7,0'] = 'Ulsan Metropolitan City'
T['T1,T7,8,0'] = 'Sejong Special Self-Governing City'
T['T1,T7,9,0'] = 'Gyeonggi-do'
T['T1,T7,10,0'] = 'Gangwon-do'
T['T1,T7,11,0'] = 'Chungcheongbuk-do'
T['T1,T7,12,0'] = 'Chungcheongnam-do'
T['T1,T7,13,0'] = 'Jeollabuk-do'
T['T1,T7,14,0'] = 'Jeollanam-do'
T['T1,T7,15,0'] = 'Gyeongsangbuk-do'
T['T1,T7,16,0'] = 'Gyeongsangnam-do'
T['T1,T7,17,0'] = 'Jeju Special Self-Governing Province'
T['T1,T8,0,0'] = 'Figures'
T['T1,T8,1,0'] = 'News'
# USA Titles
T['T2,T1,0,0'] = 'Press'
T['T2,T1,1,0'] = 'Cable News Network(CNN)'
T['T2,T2,0,0'] = 'Administration'
T['T2,T3,0,0'] = 'Parties'
T['T2,T4,0,0'] = 'Assembly'
T['T2,T5,0,0'] = 'Judiciary'
T['T2,T5,1,0'] = 'Law Firms'
T['T2,T6,0,0'] = 'Elections'
T['T2,T7,0,0'] = 'Local Governments'
T['T2,T8,0,0'] = 'Figures'
T['T2,T8,1,0'] = 'News'
# International Titles
T['T3,T1,0,0'] = 'Organization'

O = {}
O['T,_,_'] = None
# KOREA Objects
O['T1,T1,0,0'] = KR['T1,T1,0,0']
O['T1,T1,1,0'] = KR['T1,T1,1,0']
O['T1,T1,2,0'] = KR['T1,T1,2,0']
O['T1,T1,3,0'] = KR['T1,T1,3,0']
O['T1,T1,4,0'] = KR['T1,T1,4,0']
O['T1,T1,5,0'] = KR['T1,T1,5,0']
O['T1,T1,6,0'] = KR['T1,T1,6,0']
O['T1,T1,7,0'] = KR['T1,T1,7,0']
O['T1,T1,8,0'] = KR['T1,T1,8,0']
O['T1,T1,9,0'] = KR['T1,T1,9,0']
O['T1,T1,10,0'] = KR['T1,T1,10,0']
O['T1,T2,0,0'] = KR['T1,T2,0,0']
O['T1,T2,1,0'] = KR['T1,T2,1,0']
O['T1,T2,2,0'] = KR['T1,T2,2,0']
O['T1,T2,3,0'] = KR['T1,T2,3,0']
O['T1,T2,4,0'] = KR['T1,T2,4,0']
O['T1,T2,5,0'] = KR['T1,T2,5,0']
O['T1,T2,6,0'] = KR['T1,T2,6,0']
O['T1,T3,0,0'] = KR['T1,T3,0,0']
O['T1,T3,1,0'] = KR['T1,T3,1,0']
O['T1,T3,2,0'] = KR['T1,T3,2,0']
O['T1,T4,0,0'] = KR['T1,T4,0,0']
O['T1,T4,1,0'] = KR['T1,T4,1,0']
O['T1,T5,0,0'] = KR['T1,T5,0,0']
O['T1,T5,1,0'] = KR['T1,T5,1,0']
O['T1,T6,0,0'] = KR['T1,T6,0,0']
O['T1,T7,0,0'] = KR['T1,T7,0,0']
O['T1,T7,1,0'] = KR['T1,T7,1,0']
O['T1,T7,2,0'] = KR['T1,T7,2,0']
O['T1,T7,3,0'] = KR['T1,T7,3,0']
O['T1,T7,4,0'] = KR['T1,T7,4,0']
O['T1,T7,5,0'] = KR['T1,T7,5,0']
O['T1,T7,6,0'] = KR['T1,T7,6,0']
O['T1,T7,7,0'] = KR['T1,T7,7,0']
O['T1,T7,8,0'] = KR['T1,T7,8,0']
O['T1,T7,9,0'] = KR['T1,T7,9,0']
O['T1,T7,10,0'] = KR['T1,T7,10,0']
O['T1,T7,11,0'] = KR['T1,T7,11,0']
O['T1,T7,12,0'] = KR['T1,T7,12,0']
O['T1,T7,13,0'] = KR['T1,T7,13,0']
O['T1,T7,14,0'] = KR['T1,T7,14,0']
O['T1,T7,15,0'] = KR['T1,T7,15,0']
O['T1,T7,16,0'] = KR['T1,T7,16,0']
O['T1,T7,17,0'] = KR['T1,T7,17,0']
O['T1,T8,0,0'] = KR['T1,T8,0,0']
O['T1,T8,1,0'] = KR['T1,T8,1,0']
# USA Objects
O['T2,T1,0,0'] = US['T2,T1,0,0']
O['T2,T1,1,0'] = US['T2,T1,1,0']
O['T2,T2,0,0'] = US['T2,T2,0,0']
O['T2,T3,0,0'] = US['T2,T3,0,0']
O['T2,T4,0,0'] = US['T2,T4,0,0']
O['T2,T5,0,0'] = US['T2,T5,0,0']
O['T2,T5,1,0'] = US['T2,T5,1,0']
O['T2,T6,0,0'] = US['T2,T6,0,0']
O['T2,T7,0,0'] = US['T2,T7,0,0']
O['T2,T8,0,0'] = US['T2,T8,0,0']
# International Objects
O['T3,T1,0,0'] = IO['T3,T1,0,0']

C = {} # color code : primary, secondary, info, success, warning, danger, light, dark
# KOREA
C['T1,T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,0,0']), dbc.CardBody(O['T1,T1,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,1,0']), dbc.CardBody(O['T1,T1,1,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,2,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,2,0']), dbc.CardBody(O['T1,T1,2,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,3,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,3,0']), dbc.CardBody(O['T1,T1,3,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,4,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,4,0']), dbc.CardBody(O['T1,T1,4,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,5,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,5,0']), dbc.CardBody(O['T1,T1,5,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,6,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,6,0']), dbc.CardBody(O['T1,T1,6,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,7,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,7,0']), dbc.CardBody(O['T1,T1,7,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,8,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,8,0']), dbc.CardBody(O['T1,T1,8,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,9,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,9,0']), dbc.CardBody(O['T1,T1,9,0'])], color='light', inverse=False, outline=True)]
C['T1,T1,10,0'] = [dbc.Card([dbc.CardHeader(T['T1,T1,10,0']), dbc.CardBody(O['T1,T1,10,0'])], color='light', inverse=False, outline=True)]
C['T1,T2,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T2,0,0']), dbc.CardBody(O['T1,T2,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T2,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T2,1,0']), dbc.CardBody(O['T1,T2,1,0'])], color='light', inverse=False, outline=True)]
C['T1,T2,2,0'] = [dbc.Card([dbc.CardHeader(T['T1,T2,2,0']), dbc.CardBody(O['T1,T2,2,0'])], color='light', inverse=False, outline=True)]
C['T1,T2,3,0'] = [dbc.Card([dbc.CardHeader(T['T1,T2,3,0']), dbc.CardBody(O['T1,T2,3,0'])], color='light', inverse=False, outline=True)]
C['T1,T2,4,0'] = [dbc.Card([dbc.CardHeader(T['T1,T2,4,0']), dbc.CardBody(O['T1,T2,4,0'])], color='light', inverse=False, outline=True)]
C['T1,T2,5,0'] = [dbc.Card([dbc.CardHeader(T['T1,T2,5,0']), dbc.CardBody(O['T1,T2,5,0'])], color='light', inverse=False, outline=True)]
C['T1,T2,6,0'] = [dbc.Card([dbc.CardHeader(T['T1,T2,6,0']), dbc.CardBody(O['T1,T2,6,0'])], color='light', inverse=False, outline=True)]
C['T1,T3,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T3,0,0']), dbc.CardBody(O['T1,T3,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T3,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T3,1,0']), dbc.CardBody(O['T1,T3,1,0'])], color='light', inverse=False, outline=True)]
C['T1,T3,2,0'] = [dbc.Card([dbc.CardHeader(T['T1,T3,2,0']), dbc.CardBody(O['T1,T3,2,0'])], color='light', inverse=False, outline=True)]
C['T1,T4,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T4,0,0']), dbc.CardBody(O['T1,T4,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T4,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T4,1,0']), dbc.CardBody(O['T1,T4,1,0'])], color='light', inverse=False, outline=True)]
C['T1,T5,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T5,0,0']), dbc.CardBody(O['T1,T5,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T5,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T5,1,0']), dbc.CardBody(O['T1,T5,1,0'])], color='light', inverse=False, outline=True)]
C['T1,T6,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T6,0,0']), dbc.CardBody(O['T1,T6,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,0,0']), dbc.CardBody(O['T1,T7,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,1,0']), dbc.CardBody(O['T1,T7,1,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,2,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,2,0']), dbc.CardBody(O['T1,T7,2,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,3,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,3,0']), dbc.CardBody(O['T1,T7,3,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,4,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,4,0']), dbc.CardBody(O['T1,T7,4,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,5,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,5,0']), dbc.CardBody(O['T1,T7,5,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,6,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,6,0']), dbc.CardBody(O['T1,T7,6,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,7,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,7,0']), dbc.CardBody(O['T1,T7,7,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,8,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,8,0']), dbc.CardBody(O['T1,T7,8,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,9,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,9,0']), dbc.CardBody(O['T1,T7,9,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,10,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,10,0']), dbc.CardBody(O['T1,T7,10,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,11,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,11,0']), dbc.CardBody(O['T1,T7,11,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,12,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,12,0']), dbc.CardBody(O['T1,T7,12,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,13,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,13,0']), dbc.CardBody(O['T1,T7,13,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,14,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,14,0']), dbc.CardBody(O['T1,T7,14,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,15,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,15,0']), dbc.CardBody(O['T1,T7,15,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,16,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,16,0']), dbc.CardBody(O['T1,T7,16,0'])], color='light', inverse=False, outline=True)]
C['T1,T7,17,0'] = [dbc.Card([dbc.CardHeader(T['T1,T7,17,0']), dbc.CardBody(O['T1,T7,17,0'])], color='light', inverse=False, outline=True)]
C['T1,T8,0,0'] = [dbc.Card([dbc.CardHeader(T['T1,T8,0,0']), dbc.CardBody(O['T1,T8,0,0'])], color='light', inverse=False, outline=True)]
C['T1,T8,1,0'] = [dbc.Card([dbc.CardHeader(T['T1,T8,1,0']), dbc.CardBody(O['T1,T8,1,0'])], color='light', inverse=False, outline=True)]
# USA
C['T2,T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T1,0,0']), dbc.CardBody(O['T2,T1,0,0'])], color='light', inverse=False, outline=True)]
C['T2,T1,1,0'] = [dbc.Card([dbc.CardHeader(T['T2,T1,1,0']), dbc.CardBody(O['T2,T1,1,0'])], color='light', inverse=False, outline=True)]
C['T2,T2,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T2,0,0']), dbc.CardBody(O['T2,T2,0,0'])], color='light', inverse=False, outline=True)]
C['T2,T3,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T3,0,0']), dbc.CardBody(O['T2,T3,0,0'])], color='light', inverse=False, outline=True)]
C['T2,T4,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T4,0,0']), dbc.CardBody(O['T2,T4,0,0'])], color='light', inverse=False, outline=True)]
C['T2,T5,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T5,0,0']), dbc.CardBody(O['T2,T5,0,0'])], color='light', inverse=False, outline=True)]
C['T2,T5,1,0'] = [dbc.Card([dbc.CardHeader(T['T2,T5,1,0']), dbc.CardBody(O['T2,T5,1,0'])], color='light', inverse=False, outline=True)]
C['T2,T6,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T6,0,0']), dbc.CardBody(O['T2,T6,0,0'])], color='light', inverse=False, outline=True)]
C['T2,T7,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T7,0,0']), dbc.CardBody(O['T2,T7,0,0'])], color='light', inverse=False, outline=True)]
C['T2,T8,0,0'] = [dbc.Card([dbc.CardHeader(T['T2,T8,0,0']), dbc.CardBody(O['T2,T8,0,0'])], color='light', inverse=False, outline=True)]
# International 
C['T3,T1,0,0'] = [dbc.Card([dbc.CardHeader(T['T3,T1,0,0']), dbc.CardBody(O['T3,T1,0,0'])], color='light', inverse=False, outline=True)]
################################## DASHBOARD ##################################
contents = {}; contents['page'] = {}; page_layouts = {}
# KOREA Tabs
contents['page']['tab1'] = {}
contents['page']['tab1']['tab1'] = [dbc.Row([dbc.Col(C['T1,T1,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,1,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,2,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,3,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,4,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,5,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,6,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,7,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,8,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,9,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T1,10,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab1']['tab2'] = [dbc.Row([dbc.Col(C['T1,T2,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T2,1,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T2,2,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T2,3,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T2,4,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T2,5,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T2,6,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab1']['tab3'] = [dbc.Row([dbc.Col(C['T1,T3,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T3,1,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T3,2,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab1']['tab4'] = [dbc.Row([dbc.Col(C['T1,T4,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T4,1,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab1']['tab5'] = [dbc.Row([dbc.Col(C['T1,T5,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T5,1,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab1']['tab6'] = [dbc.Row([dbc.Col(C['T1,T6,0,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab1']['tab7'] = [dbc.Row([dbc.Col(C['T1,T7,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,1,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,2,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,3,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,4,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,5,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,6,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,7,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,8,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,9,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,10,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,11,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,12,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,13,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,14,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,15,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,16,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T7,17,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab1']['tab8'] = [dbc.Row([dbc.Col(C['T1,T8,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T1,T8,1,0'], width=12)]), html.Br(),
                                    html.Br()]
# USA Tabs                                   
contents['page']['tab2'] = {}
contents['page']['tab2']['tab1'] = [dbc.Row([dbc.Col(C['T2,T1,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T2,T1,1,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab2']['tab2'] = [dbc.Row([dbc.Col(C['T2,T2,0,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab2']['tab3'] = [dbc.Row([dbc.Col(C['T2,T3,0,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab2']['tab4'] = [dbc.Row([dbc.Col(C['T2,T4,0,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab2']['tab5'] = [dbc.Row([dbc.Col(C['T2,T5,0,0'], width=12)]), html.Br(),
                                    dbc.Row([dbc.Col(C['T2,T5,1,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab2']['tab6'] = [dbc.Row([dbc.Col(C['T2,T6,0,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab2']['tab7'] = [dbc.Row([dbc.Col(C['T2,T7,0,0'], width=12)]), html.Br(),
                                    html.Br()]
contents['page']['tab2']['tab8'] = [dbc.Row([dbc.Col(C['T2,T8,0,0'], width=12)]), html.Br(),
                                    html.Br()]
# International Tabs                                   
contents['page']['tab3'] = {}
contents['page']['tab3']['tab1'] = [dbc.Row([dbc.Col(C['T3,T1,0,0'], width=12)]), html.Br(),
                                    html.Br()]

# TAB1 : KOREA
contents['page']['tab1']['tabs'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab1'])), label="Press", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab2'])), label="Administration", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab3'])), label="Parties", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab4'])), label="Assembly", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab5'])), label="Judiciary", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab6'])), label="Elections", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab7'])), label="Local Governments", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tab8'])), label="Figures", disabled=False),
                                             ])
# TAB2 : USA
contents['page']['tab2']['tabs'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab1'])), label="Press", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab2'])), label="Administration", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab3'])), label="Parties", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab4'])), label="Assembly", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab5'])), label="Judiciary", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab6'])), label="Elections", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab7'])), label="Local Governments", disabled=False),
                                             dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tab8'])), label="Figures", disabled=False),
                                             ])
# TAB3 : International                                    
contents['page']['tab3']['tabs'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab3']['tab1'])), label="Organization", disabled=False),
                                             ])
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab1']['tabs'])), label="Korea", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab2']['tabs'])), label="United States", disabled=False),
                                 dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab3']['tabs'])), label="International", disabled=False),
                                 ])
main = dbc.Jumbotron([html.H2('analysis/Politics'),
                      html.H6('Ailever : Promulgate values for a better tomorrow'), html.Hr(),
                      html.Div([dbc.Button("Home", color="secondary", href='https://ailever.github.io/'),
                                dbc.Button("Source", color="secondary", href='https://github.com/ailever/openapi/blob/master/analysis/Politics.py'),
                                dbc.Button("Naver", color="secondary", href="https://news.naver.com/"),
                                dbc.Button("Google Trend", color="secondary", href="https://trends.google.com/trends/explore"),
                                dbc.Button("DataLab", color="secondary", href="https://datalab.naver.com/"),
                                dbc.Button('Kakao Map', color='secondary', href="https://map.kakao.com/"),
                                dbc.Button('Google Map', color='secondary', href="https://www.google.co.kr/maps/"),
                                dbc.Button("Plotly", color="secondary", href="https://plotly.com/python/"),
                                dbc.Button("Rstudio", color="secondary", href=config['R-server']+':'+config['R-port']),
                                dbc.Button("Real-Time Analysis", id='real-time', color="secondary", href=config['visdom-server']+':'+config['visdom-port'])]),
                      html.Div([dbc.Button("National Indices", color="dark", href="https://www.index.go.kr/main.do"),
                                dbc.Button("BOK Indices", color="dark", href="http://ecos.bok.or.kr/"),
                                dbc.Button("Dart", color="dark", href="http://dart.fss.or.kr/"),
                                dbc.Button("Alio", color="dark", href="http://www.alio.go.kr/home.do"),
                                dbc.Button("eGroup", color="dark", href="https://www.egroup.go.kr/egps/wi/mainPage.do"),
                                dbc.Button('Time Line 1', color='dark', href="https://en.wikipedia.org/wiki/2021"),
                                dbc.Button('Time Line 2', color='dark', href="https://ko.wikipedia.org/wiki/2021%EB%85%84"),
                                dbc.Button('Time Line 3', color='dark', href="https://namu.wiki/w/2021%EB%85%84"),
                                ]),
                      html.P(id='visdom-server')])
app.layout = html.Div([main, page_layouts['page']])
if __name__ == '__main__':
    app.run_server(host=config['dash-server'], port=config['dash-port'], debug=True) 
################################## DASHBOARD ##################################
