#%% ################################## CODEBLOCK ##################################
class N:
    def __init__(self, tab_info=(None, None), title=None, contents=None):
        self.layout = tab_info[0]
        self.label = tab_info[1]
        self.title = title
        self.contents = contents

note = N()
note.N00 = N(('T01,0,0', 'Work & School'), 'Main Board', """
## Work & School
work on | do a good job | work hard | have a lot of work | get started on | give it a try | keep ~ing | 
do one's best | be devoted to | be tied up | take one's time | be tired out | get over | on one's own | 
be good at | take care of | be finished with | keep up with | meet the deadline | make it | win the game | 
make a mistake | have a job interview | get a job | work for | go to work | get paid | get promoted | 
go out of town | run a business | be on a night shift | give a task | have a meeting | write a report | deal with | go on sale | 
buy sth for ~ | be sold out | exchange A for B | invest in | save money | make money | spend moeny | get a loan |
make ends meet | make a deposit | go to college | quit school | graduage from | take a course | sign up for | do one's homework | take the test | 
get a good grad | 
""")
note.N00_01 = N(('T01,1,0', 'Work & School'), 'work on', """
- A: I'm so **stressed out** these days.
- B: Oh? Do you have to **work on a big project**?
- _: I'm going to **work on this stuff** at home tonight.
- _: Did you **hand in the report** you were working on?
---
- A: Hey Nick, How about we **get some beer**?
- B: I'd like to, but I have to **get back to work**.
- _: I've gotta **get to work**. So can I **call you back later**?
- _: How long does it take for you to **get to work**?
---
- A: This needs to **be done** quickly.
- B: Don't worry, I'll **get right on it**.
- _: If it's urgent, I'll **get right on it**.
- _: I understand. I'll **get right on it**.
---
- A: **Have you finished** cleaning up?
- B: **I'm on it**. I'll **be done in an hour**.
- _: **Don't mention it**. I'm just **doing my job**.
- _: Please, **get out of** my way **so I can** do my job.
""")
note.N00_02 = N(('T01,2,0', 'Work & School'), 'do a good job', """
- A: I thought you always **did a great job** on exams.
- B: Yeah, but actually I **cheated** all the time.
- _: You **did a good job**! It was **very impressive**.
- _: You **did a great job** organizing the fundraiser.
---
- A: 
- B: 
- _: My mechanic does good work on car.
- _: 
---
- A: I have to **work late tonight**, honey.
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N00_03 = N(('T01,3,0', 'Work & School'), 'work hard', """
- A: You have to **work hard**. Don't let me down.
- B: I'll **do my best**, boss. Believe me. 
- _: 
- _: 
---
- A: This wedding cake **looks great**.
- B: I **worked all night** baking it.
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N00_04 = N(('T01,4,0', 'Work & School'), 'have a lot of work', """
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N00_05 = N(('T01,5,0', 'Work & School'), 'get started on', """
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N00_06 = N(('T01,6,0', 'Work & School'), 'give it a try', """
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N00_07 = N(('T01,7,0', 'Work & School'), 'keep ~ing', """
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N00_08 = N(('T01,8,0', 'Work & School'), "do one's best", """
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N00_09 = N(('T01,9,0', 'Work & School'), 'be devoted to', """
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N00_10 = N(('T01,10,0', 'Work & School'), 'be tied up', """
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N01 = N(('T02,0,0', 'Computer & Networking'), 'Main Board', """
## Computer & Networking
fix the computer | load the file | have a virus | have access to | post one's opinion | play computer games | meet online | find sb on Facebook | have an email account | 
check one's email | attach the file | answer one's email | drop a line | give a call | take the call | be available | be on the phone | put A through B | 
be cut off | wait for one's call | text sb | own a Smart 3D TV | get held up | have a car accident | take a texi | run out of gas | give a ride | 
get a ticket | park one's car | take a bus | miss the flight | get lost | go this way | be next to |  
""")
note.N02 = N(('T03,0,0', 'Social Life with Others'), 'Main Board', """
## Social Life with Others
get a minute | make time | spend time | take time | It has been | have a plan | be going to | have a schedule | be late for | 
mean to | get together | invite sb to | would like sb to meet | come over | wait for | say hi to | have an appointment | get in touch | 
make a reservation | make friends with | talk to | consult with | leave for | come here to | go downtown | get to | go together | 
go back to | go home | take ~ to | move to | stay for | call A B | behave oneself | have a date | have a feeling for | 
give a hug | break up with | get married to | get involved in | stay out of | take part in | 
""")
note.N02_01 = N(('T03,1,0', 'Social Life with Others'), 'get a minute', """
- A: Do you **get|have a minute**?
- B: Well yeah, sure, what's up?
- _: I need to **talk to you** if you have a minute.
- _: **Hold on a second|minute**. I have a question.
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: Do you **need to visit** a dentist? 
- B: Yeah, **Who is available** now?
- _: I am not sure **if I am available** Friday.
- _: I'd like to speak with Mark, **if he is available**.
---
- A: The movie **starts at eight**.
- B: We have **time to eat before** it begins.
- _: We have **a couple of hours before** school ends.
- _: I have **a few hours before** I need to go home.
""")
note.N02_02 = N(('T03,2,0', 'Social Life with Others'), 'make time', """
- A: I'**m going to see** my grandmother this weekend.
- B: It's good you **make time to** visit her.
- _: **Make time to** pack up your suitcase.
- _: I'll **make time to** come down and see you.
---
- A: I'm going to **take time out to** do some shopping.
- B: Oh, good. Let's **go shopping** together.
- _: She **took time out to** plant a flower garden.
- _: We will **take time out to** visit some old friends.
---
- A: How long have you **been working** here?
- B: We **put in seven hours** so far.
- _: Workers must **put in thirty years** before retiring.
- _: The baseball players **put a lot of energy into** playing.
---
- A: I can **spare some time for** hiking.
- B: Well, Let's **go to the mountain** weekend.
- _: He **spared some time for** helping the old woman.
- _: You should **spare some time for** relaxing.
---
- A: I **would like to interview** that musician.
- B: We can **arrange a time for** you to meet him.
- _: The farmers **arranged time for** harvesting red peppers.
- _: I need to **arrange time for** our Christmas party.
""")
note.N02_06 = N(('T03,6,0', 'Social Life with Others'), 'have a plan', """
- A: 
- B: 
- _: 
- _: 
--- 
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: **Did you have a good time** on your date?
- B: No, it really **didn't go as planned**.
- _: The English class **didn't go as planned**.
- _: **If everything goes as planned**, we're going to make a killing.
---
- A: You look like you'**re up to something**.
- B: I **feel like selling my stocks**.
- _: I think those teenagers **are up to something**.
- _: Angelina Jolie is always **up to something**.
---
- A: Maybe we **shouldn't go** on a vacation.
- B: Let's **keep to our plan** and just go.
- _: Bart can never **keep to a plan**.
- _: It was hard, but I **kept to my plan**.
---
- A: Will your father **allow you to go** on the trip?
- B: He said that it **is under consideration**.
- _: The plans for the new building **are under consideration**.
- _: A new menu for the cafe **is under consideration**.
""")
note.N02_09 = N(('T03,9,0', 'Social Life with Others'), 'be late for', """
- A: 
- B: 
- _: 
- _: 
--- 
- A: 
- B: 
- _: 
- _: 
--- 
- A: 
- B: 
- _: 
- _: 
---
- A: It **has been dark** for a few hours.
- B: I guess it **is getting late**.
- _: It'**s getting late** in the day.
- _: I'd love to, but it'**s really getting late**.
---
- A: 
- B: 
- _: 
- _: 
""")
note.N03 = N(('T04,0,0', 'Everyday Life Activies'), 'Main Board', """
## Everyday Life Activies
get to bed | get out of bed | wash up | get one's hair cut | wear one's makeup | use the bathroom | get dressed | take a seat | blow one's nose | 
burst into tears | smile at | shout to | take a breath | live in | rent a house | do the dishes | break down | fix the car | 
be sunny | fall heavily | have dinner | grab a bite | take a drink | get drunk | have the same | pay for dinner | For here or to go | 
be full | cook dinner | boil the stew | give up smoking | go on a vacation | take a break | take a trip | hang out | watch a moive | 
have a party | keep in shape | get hurt | break one's leg | catch a cold | have a headache | have a breakdown | have a sore throat | have an upset stomach | 
get diabets | take one's medicine | cure a disease | have a checkup | work out | go on a diet | 
""")
note.N04 = N(('T05,0,0', 'Information & Understanding'), 'Main Board', """
## Information & Understanding
hear sb ~ing | look at | get to know | have no idea | ask about | check out | hear a rumor | find out | get sb wrong | 
have doubts about | tell the truth | keep a secret | tell a lie | give an excuse | have a reason | make clear | get it | stand for | 
put A before B | leave sth in ~ | insist on | Why don't you | remind A of B | forget to | 
""")
note.N05 = N(('T06,0,0', 'Thoughts & Attitude'), 'Main Board', """
## Thoughts & Attitude
think of | consider ~ing | think over | take A for B | hit on | take a guess | ~ than I thought | believe in | hope to | 
take charge of | have a duty to | be in need of | be sure of | have the courage | be famous for | be popular with | use one's head | complain about | 
think less of | play dirty | do a stupid thing | put up with | go against | agree with | be careful of | be likely to | be worth ~ing | 
get interested in | would like to | be one's favorite | have a habit of | seem to | The point is that | come up with | no longer | 
""")
note.N05_19 = N(('T06,19,0', 'Thoughts & Attitude'), 'think less of', """
- A: 
- B: 
- _: 
- _: 
--- 
- A: I **think less of** Tim **since** he got his third divorce. 
- B: Yeah, I wonder why his marriages failed.
- _: Antonio **thinks nothing of** lending his friends money.
- _: I am glad to do it. **Think nothing of it**.
--- 
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N06 = N(('T07,0,0', 'Emotions & Situations'), 'Main Board', """
## Emotions & Situations
be happy with | feel sad about | get upset | worry about | regret ~ing | say thank you | be sorry for | be embarrassed | be nervous | 
like to | be surprised at | let ~ down | take pity on | be afriad of | be sick of | be ashamed of | think highly of | be proud of | 
be impressed by | be out of one's mind | have a lot of stress | take it easy | feel the same way | be all right | have to | can't help ~ing | get worse | 
get caught in | get in trouble | have a problem | have luck | have a bad day | get a chance | take the chance | be different from | be similar to | 
get used to | be hard to | be doing okay | 
""")
note.N06_17 = N(('T07,17,0', 'Emotions & Situations'), "think highly of", """
- A: 
- B: 
- _: 
- _: 
--- 
- A: 
- B: 
- _: 
- _: 
--- 
- A: 
- B: 
- _: 
- _: 
---
- A: Richard **seems to be very popular** here.
- B: Everyone **thinks highly of** him.
- _: The chef **thinks highly of** chocolate cake.
- _: I **think highly of** BMW motocylcles.
---
- A: 
- B: 
- _: 
- _: 
""")
note.N06_26 = N(('T07,26,0', 'Emotions & Situations'), "can't help ~ing", """
- A: Just **forget about** your ex-girlfriend.
- B: I try, but I **can't help thinking** about her.
- _: She **can't help drinking** so much alcohol.
- _: I **can't help being** cautious.
--- 
- A: I **can't help but** watch TV when I'm bored.
- B: Maybe you need to **find a hobby**.
- _: I **can't help but think** that he's a loser.
- _: I **can't help but think** about Jessica.
--- 
- A: We **have no choice but to** buy her a fur coat.
- B: It's going to be really expensive.
- _: I **had no choice but to** get divorced.
- _: I **have no choice but to** do that.
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N06_29 = N(('T07,29,0', 'Emotions & Situations'), 'get in trouble', """
- A: 
- B: 
- _: 
- _: 
--- 
- A: I **have trouble with** studing here.  
- B: **It's noisy**. Let's go to the library.
- _: She **had trouble with** making a living.
- _: They **have trouble with** playing their instruments.
--- 
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N06_39 = N(('T07,39,0', 'Emotions & Situations'), 'be doing okay', """
- A: **I haven't seen your parents** in a while.
- B: My dad and mom **are doing okay|good|great**.
- _: I glad to see you'**re doing okay|good|great**.
- _: You'**re doing great**.
--- 
- A:  
- B: 
- _: 
- _: 
--- 
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
""")
note.N07 = N(('T08,0,0', 'Various Actions'), 'Main Board', """
## Various Actions
choose to | chage one's mind | make a decision | get one's own way | hold on to | cause trouble | back sb up | allow sb to | credit A with B | 
talk sb into ~ing | give some advice | warm sb about | tell sb to | ask sb to | help sb do | teach sb to | excuse sb for | wait on | 
keep one's word | prepare for | date back | get sth from | want sth back | hand sth down | make a donation | sort out | go through | 
report sth to | make use of | solve a problem | find fault with | make fun of | be hard on | cheat sb out of | rob A of B | have words with | 
beat up | get even with | make up | turn against | teach a lesson | give up | keep sb from | keep away from | set ~ free | 
take action | take a chance | register for | 
""")
note.N07_12 = N(('T08,12,0', 'Various Actions'), 'warn sb about', """
- A: 
- B: 
- _: 
- _: 
--- 
- A:  
- B: 
- _: 
- _: 
--- 
- A: 
- B: 
- _: 
- _: 
---
- A: 
- B: 
- _: 
- _: 
---
- A: **Did you hear that** Brady had an accident?
- B: I **cautioned** him **against** driving home.
- _: The teacher **cautioned** the students **against** drug abuse.
- _: The policeman **cautioned** her **to** slow down.
""")
note.N08 = N(('T09,0,0', 'Time, Place & etc.'), 'Main Board', """
## Time, Place & etc.
be in the service | break the law | buy insurance | do damage to | make up for | belong to | deserve to | go digital | whatever you want to | 
let alone | in the way that | be the first to | have the right to | come close to | such as | never happened | enough to | in no time | 
to begin with | at the same time | at the moment | to date | for a while | on a daily basis | from time to time | as soon as | later this week | 
on such short notice | in the end | in addition to | on the other hand | in other words | by the way | a bit of | as far as | over there | 
If you like | when it comes to | 
""")
note.N09 = N(('T10,0,0', 'Additionals'), 'Main Board', """
## Additionals
 |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  | 
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
