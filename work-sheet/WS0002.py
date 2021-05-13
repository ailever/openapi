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
note.N04_19 = N(('T05,19,0', 'Information & Understanding'), 'put A before B', """
- A: 
- B: 
- _: 
- _: 
--- 
- A: Larry **looks so handsome** today.
- B: People are **making less|much of** his new haircut.
- _: My boss **made less|much of the fact** that I left early.
- _: The teacher **made less|much of the fact** that he cheated.
--- 
- A: When you work at this company, punctuality **comes first**.
- B: That'**s pretty much the same** for all companies.
- _: Work **comes first** for the older generation.
- _: I stayed home because my children **come first**.
---
- A: What is the philosophy of your company?
- B: I always tell my employees to **put** honesty **before** benifit.
- _: Lisa **puts** others **before** herself most of the time.
- _: I **had to put** studying **before** relaxing.
---
- A: We have to **get** this homework **done**.
- B: You're right. We should **give it top priority**.
- _: I'd like you to **give this top priority**.
- _: I'd like to **make it my top priority**.
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

note.N05 = N(('T06,0,0', 'Thoughts & Attitude'), 'Main Board', """
## Thoughts & Attitude
think of | consider ~ing | think over | take A for B | hit on | take a guess | ~ than I thought | believe in | hope to | 
take charge of | have a duty to | be in need of | be sure of | have the courage | be famous for | be popular with | use one's head | complain about | 
think less of | play dirty | do a stupid thing | put up with | go against | agree with | be careful of | be likely to | be worth ~ing | 
get interested in | would like to | be one's favorite | have a habit of | seem to | The point is that | come up with | no longer | 
""")
note.N05_03 = N(('T06,03,0', 'Thoughts & Attitude'), 'think over', """
- A: I need to **think over** my choices.
- B: You'll have to decide soon.
- _: You **think it over**. Call me back.
- _: You need **think carefully before** starting your own business.
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
note.N05_09 = N(('T06,09,0', 'Thoughts & Attitude'), 'hope to', """
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
- A: Stanley and Jennifer **are dating now**.
- B: She is dating him **in hopes of** getting married.
- _: We came **in the hopes that** we'd meet your parents.
- _: **Hopefully**, Lindy will be home soon.
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
note.N05_10 = N(('T06,10,0', 'Thoughts & Attitude'), 'take charge of', """
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
- A: I'm going to take over as class president.
- B: Did you win a student election?
- _: Who is going to take over the company?
- _: You can take over the meeting.
---
- A: 
- B: 
- _: 
- _: 
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
note.N06_01 = N(('T07,01,0', 'Emotions & Situations'), "be happy with", """
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
- A: **Why did you give** the homeless man money?
- B: I **feel good about** helping poor people.
- _: Kendra **felt good about** completing the marathon.
- _: Did Sam **feel good about** finishing his work.
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
- A: I wonder if the boss **is still angry with** me.
- B: He seems to **be in a good mood** today.
- _: Gina **was in a good mood after** eating lunch.
- _: They **are in a good mood because** they are together.
---
- A: 
- B: 
- _: 
- _: 
""")
note.N06_02 = N(('T07,02,0', 'Emotions & Situations'), "feel sad about", """
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
note.N06_05 = N(('T07,05,0', 'Emotions & Situations'), "regret ~ing", """
- A: Don't you **regret anything about your past**?
- B: No, If I had the chance, **I'd do it all over again**.
- _: I **regret the day I met you**.
- _: I'm sure he dosen't **regret it that much**.
--- 
- A: Do you like the new clothes you bought?
- B: I **regret spending** so much money on them.
- _: I **regret asking** Suzie out the other day. 
- _: I **regret spending** last night playing computer games.
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
note.N06_12 = N(('T07,12,0', 'Emotions & Situations'), "let ~ down", """
- A: **How would you like it if** I decided to quit?
- B: Well, I'd **be disappointed**.
- _: I **was disappointed in** the movie's ending.
- _: They **were disappointed in** their honeymoon.
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
- A: You'**re in trouble**. The boss wants to see you.  
- B: Really? **What did I do**?
- _: You **will get in trouble if** you do that. 
- _: I'm not here to **get you in trouble**.
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
note.N06_37 = N(('T07,37,0', 'Emotions & Situations'), 'get used to', """
- A: **Did you get used to the weather** in Canada?
- B: Yes, but it **is awfully cold** in the winter.
- _: You need to **get used to eating** different foods.
- _: You'd better **get used to it**.
- _: Did you **get used to driving** in the rain?
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
- A: **Have you learned how to** salsa dance yet?
- B: Well, I am starting **to get the hang of** it.
- _: Sam couldn't **get the hang of** using chopsticks.
- _: You'll **get the hang of** using your new cell phone.
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

note.N09 = N(('T10,0,0', 'Opic'), 'Main Board', """
## Opic
""")
note.N09_01 = N(('T10,1,0', 'Opic'), 'Key Sentences', """
- I **like watching** movies.
- **I was busy working on** the project very important.
- **It was such a** tiring process.
- **It was supposed to be done under** limited time, but it didn't.
- It cost more but **it was worth it**.
- **I shold have brought** my work **to a halt**.
- **I am seldom getting used to getting up** early in the morning.
- **I was looking forward to** culminating in success.
- **I used to** keep studing my reserach-area **whenever I can all the time**.
- **I was used to** continuing to studing my reserach-area whenever I can all the time.
- **I got used to** keeping studing my reserach-area whenever I can all the time.
- **Tough times** made me grow.
- I tried not to **be a bad influence on** myself. 
- When I was in my 20s, **I was almost active in** study and research.
- **It forced me to make** an impulsive decision.
- **I should have stayed away from** my favorite things.
- **I had a hard time** learning how to ride a bike. 
- **I ran into** an unsolved problem.
- **I first became interested in** quantitatively analysis method when I was in my 10s.
- **I first became interested in** singing **about 10 years ago**.
- **On the contrary, I had a skeptical impression of** enjoying something for pleasure for self-improvement at one time.
- **I tend to try not to** be negative too much.
- **The best part about that** is that it allows us to access esaily.
- **The best part of the hotel** is the inside.
- It taught me how to learn.
- We **should try to avoid** focusing on a **collateral issue**.
- He saves money **so that** he may buy a house. 
- I save money **so as to** buy a house.
- It's **a perfect opportunity to thrive into** new business.
- Spring is **the time of year that** people start spring cleaning. 
- **I just didn't want to waste** my time doing nothing. 
- **I didn't fully intend to** protest the decision.
- **I didn't fully mean to** oppose to the plan.
- **I couldn't decide whether to take** the risk or not.
- I can't find time to work out during the week.
- **The most important thing I consider** is price.
- **I've seen many people** talking about it.
- **I've heard nothing** from him yet.
- **It was my first time** seeing a celebrity.
- **I’ve really gotten into** playing tennis these days. 
- **I’ve always been interested in** cooking because my mom is a great cook. 
- Whenever I get stressed out, I usually go home and sleep.
- My favorite childhood memory was joining the soccer club at school.
- I take public transportation when I go to school.
- It’s usually my wife who decides what to do
- **I had got to** go to the dental clinic recently.
- **I like researching something to be related to studies, so it’s always great to** have him as fellow worker.
- **It was great to** have him as fellow worker.
- **I tend to favor watching** movies **rather than** reading books.
- **I prefer watching** movies **to** reading books.
- There are **few things that I dislike** about this bank.
- You do not need to spend much money on it.
- There are **some simple tips** for staying in shape. 
- He gave me excellent advices.
- The bank I usually go to is located in Jamsil.
- **I have no preference for any particular** food.
- This is how I got into listening to music.
- I am not too crazy about him.
- I took an English class.
- It’s always great to ride a bike along the Han River.
- I decided to buy it because it looked good. 
- **By the time I got home**, I realized I left my wallet at home.
- **The main reason I like it** is that I can just relax and enjoy my vacation at my own home.
- **I know it sounds a little weird.**
- **There’s nothing better than** relaxing at home.
- It’s famous for its beautiful scenery, coastline, and beaches.
- I’ve been there more than 3 times since I watched it on TV. 
- I usually go to the movies on the weekend.
- Using online services has **many benefits as well as many drawbacks**.
- I have a friend who is a huge fan of action movies.
- I **highly recommend that** you watch this movie.
- **I am going to briefly talk about** my apartment.
- **The most recent|significant|noticeable change** was this new Starbucks, which **was opened about** 2 weeks ago.
- **I think it all depends on what kind of** the direction you are going on.
- **At the end of every** month, our community opens a flea market.
- It was very tiring because the castle was huge and it was very hot.
- **It’s kind of hard to** describe.
- **We ended up walking** all the way down to the hotel.
- **I don’t remember anything unusual happening while** we were there.
- There are many books throughout the hotel.
- I can’t remember any other scenes. 
- **I don’t think** the park **has changed much enormously since then**. 
- I don’t play online games **that often**. 
- In my childhood memories, waking up early in the morning was not easy.
- **Are there probably** any books you would like to recommend?
- We also make sure to go to the restroom before the concert.
- I remember taking papers and newspapers to school once every month. 
- **In terms of** unemployment rate, **there have been some increases since** 2013.
- **I am not familiar with** this topic. 
- **I guess that was the start of my career**.
""")

note.N10 = N(('T11,0,0', 'Verb and Preposition'), 'Main Board', """
## Verb and Preposition


### A
/a * 
/abandon 
/able 
/aboard 
/abort ** 
/about * 
/above * 
/abroad 
/absent 
/absolute 
/absorb 
/abstract 
/absurd ** 
/abundant 
/abuse 
/academy * 
/accelerate 
/accent * 
/accept 
/access 
/accident * 
/accommodate 
/accompany 
/accomplish 
/accord ** 
/account 
/accumulate ** 
/accurate 
/accuse 
/achieve 
/acid 
/acknowledge 
/acquaint ** 
/acquire 
/acquisition ** 
/across * 
/act * 
/activate 
/actual 
/acute 
/adapt 
/add * 
/addict 
/address * 
/adequate 
/adjust 
/administer 
/admire 
/admission 
/admit 
/adolescent 
/adopt 
/adult * 
/advance 
/advantage 
/adventure * 
/adverse ** 
/advertize / advertise 
/advise * 
/advocate 
/aesthetic ** 
/affair 
/affect 
/affection 
/affiliate ** 
/afford 
/afraid * 
/after * 
/afternoon * 
/again * 
/against * 
/age * 
/agency 
/agenda 
/agent 
/aggressive 
/ago * 
/agree * 
/agriculture 
/ahead * 
/aid 
/aim 
/air * 
/airplane * / plane / aeroplane 
/aircraft 
/airline * 
/airport * 
/aisle 
/alert 
/alien 
/alike 
/alive 
/all * 
/allocate ** 
/allow 
/ally 
/almost * 
/alone * 
/along * 
/alongside 
/aloud * 
/already * 
/alright * 
/also * 
/alter 
/alternative 
/although 
/altogether 
/always * 
/A.M. / a.m. * 
/amaze 
/ambassador 
/ambition 
/among 
/amount 
/amplify ** 
/amuse 
/analyze / analyse 
/anchor 
/ancient 
/and * 
/angel * 
/anger * 
/angle 
/animal * 
/anniversary 
/announce 
/annoy 
/annual 
/another * 
/answer * 
/ant * 
/anticipate 
/anxiety 
/anxious 
/any * 
/apart 
/apology 
/apparent 
/appeal 
/appear 
/apple * 
/applicant 
/apply 
/appoint 
/appreciate 
/approach 
/appropriate 
/approve 
/approximate 
/architect 
/architecture 
/archive ** 
/area * 
/argue 
/arise 
/arm * 
/army 
/around * 
/arrange 
/arrest 
/arrive * 
/arrow 
/art * 
/article 
/artificial 
/as * 
/ash 
/aside 
/ask * 
/asleep 
/aspect 
/aspire 
/assault ** 
/assemble 
/assert 
/assess 
/asset 
/assign 
/assist 
/associate 
/assume 
/assure 
/astonish 
/at * 
/athlete 
/atmosphere 
/atom 
/attach 
/attack 
/attain 
/attempt 
/attend 
/attention 
/attitude 
/attorney ** 
/attract 
/attribute 
/auction 
/audience 
/aunt * 
/authentic ** 
/author 
/autobiography 
/automatic 
/automobile 
/available 
/avenue 
/average 
/avoid 
/await 
/awake 
/award 
/aware 
/away * 
/awesome 
/awful 
/awkward


### B
/baby * 
/back * 
/background * 
/bad * 
/bake * 
/balance 
/ball * 
/balloon * 
/ban 
/band * 
/bang 
/bank * 
/bankrupt ** 
/bar 
/bare 
/bargain 
/bark 
/barn 
/barrier 
/base * 
/baseball * 
/basic * 
/basis 
/basket * 
/basketball * 
/bat * 
/bath * 
/bathroom * 
/battery * 
/battle * 
/bay 
/be * 
/beach * 
/beam 
/bean * 
/bear *
/beard 
/beast 
/beat 
/beauty * 
/because * 
/become * 
/bed * 
/bedroom * 
/bee * 
/beef * 
/beer 
/before * 
/beg 
/begin * 
/behalf 
/behave 
/behavior / behaviour 
/behind * 
/believe * 
/bell * 
/belong 
/below * 
/bend 
/beneath 
/benefit 
/berry 
/beside * 
/bet 
/betray 
/between * 
/beyond 
/bias 
/bible 
/bicycle * 
/big * 
/bill * 
/billion 
/bin 
/bind 
/biography 
/biology 
/bird * 
/birth * 
/birthday * 
/bishop ** 
/bit 
/bite * 
/bitter 
/black * 
/blame 
/blank 
/blanket 
/blast ** 
/blend 
/bless 
/blind 
/blink 
/block * 
/blonde 
/blood * 
/bloom 
/blossom 
/blow 
/blue * 
/board * 
/boat * 
/body * 
/boil 
/bold 
/bomb * 
/bond 
/bone * 
/book * 
/boom 
/boost 
/boot * 
/border 
/bore 
/borrow * 
/boss * 
/both * 
/bother 
/bottle * 
/bottom * 
/bounce 
/boundary 
/bow 
/bowl * 
/boy * 
/brain * 
/brake * 
/branch * 
/brand * 
/brave * 
/bread * 
/break * 
/breakfast * 
/breast 
/breathe 
/breed ** 
/breeze 
/brew ** 
/brick 
/bride 
/bridge * 
/brief 
/bright * 
/brilliant 
/bring * 
/broad 
/broadcast 
/brother * 
/brown * 
/brush * 
/brute ** 
/bubble * 
/budget 
/bug * 
/build * 
/bulk ** 
/bull 
/bullet 
/bully 
/bump 
/bunch 
/bundle 
/burden 
/burn * 
/burst 
/bury 
/bush 
/business * 
/busy * 
/but * 
/butcher 
/button * 
/buy * 
/buzz 
/by *



### C
/cab 
/cabin 
/cable 
/cage * 
/calculate 
/calendar * 
/call * 
/calm *
/can * 
/cancel 
/cancer 
/candidate 
/candy * 
/canvas 
/cap * 
/capable 
/cape 
/capital 
/captain * 
/caption ** 
/capture 
/car * 
/care * 
/career 
/carrot * 
/carry * 
/cart * 
/carve 
/case * 
/cash * 
/cast 
/castle * 
/casual 
/cat * 
/catch * 
/category 
/cater ** 
/cathedral ** 
/cattle 
/causal 
/cause 
/caution 
/cave 
/cease 
/ceiling 
/celebrate 
/celebrity 
/cell 
/censor 
/century 
/certain * 
/certificate 
/chain * 
/chair * 
/chairman 
/challenge 
/chamber ** 
/chance * 
/change *
/chaos 
/character 
/characteristic 
/charge 
/charity 
/charm 
/chase 
/chat 
/cheap * 
/check / cheque * 
/cheek 
/cheer 
/chef 
/chemical 
/chemistry 
/chest 
/chew 
/chief 
/child * 
/chill 
/chin 
/chip 
/choir 
/choose * 
/chop 
/chorus 
/chronic ** 
/church * 
/cigarette 
/cinema * 
/circle * 
/circulate 
/circumstance 
/cite 
/citizen 
/city * 
/civil 
/claim 
/clap 
/clarify 
/clash 
/class * 
/classic 
/classify 
/classroom * 
/clause 
/clay 
/clean * 
/clear * 
/clerk * 
/clever * 
/client 
/cliff 
/climate 
/climb * 
/cling 
/clinic 
/clip * 
/clock * 
/close *
/cloth * 
/cloud * 
/club * 
/clue 
/cluster 
/coach 
/coal 
/coast 
/code 
/coin * 
/coincide 
/cold * 
/collaborate 
/collapse 
/collar 
/colleague 
/collect * 
/college * 
/colony 
/color / colour * 
/column 
/combat 
/combine 
/come * 
/comedy * 
/comfort 
/command 
/commence ** 
/comment 
/commerce 
/commission 
/commit 
/committee 
/commodity ** 
/communicate 
/communist 
/community 
/companion 
/company * 
/compare 
/compatible ** 
/compel ** 
/compensate ** 
/compete 
/competent 
/compile ** 
/complain 
/complement 
/complete 
/complex 
/complicate 
/component ** 
/compose 
/compound ** 
/comprehensive 
/comprise ** 
/compromise ** 
/compulsory **
/conceal 
/conceive ** 
/concentrate 
/concept 
/concern 
/concert * 
/conclude 
/concrete 
/condemn ** 
/condition * 
/conduct 
/confer ** 
/confess 
/confident 
/confine 
/confirm 
/conflict 
/conform 
/confront 
/confuse 
/congratulate * 
/congress 
/connect 
/conscience 
/conscious 
/consensus ** 
/consent ** 
/conserve ** 
/consider 
/consist 
/consistent 
/constant 
/constitute ** 
/constrain ** 
/construct 
/consult 
/consume 
/contact 
/contain 
/contemporary ** 
/contend ** 
/content 
/contest * 
/context 
/continent 
/continue 
/contract 
/contradict ** 
/contrary 
/contrast 
/contribute 
/control * 
/controversy 
/convenient 
/convention ** 
/conversation 
/convert ** 
/convey 
/convict 
/convince 
/cook *
/cookie / cooky * 
/cool * 
/cooperate 
/coordinate ** 
/cop 
/cope 
/copy *
/copyright 
/cord 
/core 
/corn 
/corner * 
/corporate 
/correct 
/correspond 
/corridor ** 
/corrupt 
/cost * 
/costume 
/cottage 
/cotton * 
/couch 
/cough 
/could * 
/council 
/counsel 
/count 
/counter 
/counterpart ** 
/country * 
/countryside * 
/county ** 
/couple * 
/courage 
/cousin * 
/cover *
/cow * 
/cowboy 
/crack 
/craft 
/crash 
/crawl 
/crazy * 
/create 
/creature 
/credible 
/credit 
/creek ** 
/creep ** 
/crew 
/cricket 
/crime 
/criminal 
/crisis 
/crisp 
/criteria ** 
/critic 
/criticize / criticise
/criticism 
/crop 
/cross * 
/crowd * 
/crown * 
/crucial 
/cruel 
/cruise 
/crush 
/cry * 
/crystal 
/cultivate 
/culture * 
/cupboard 
/cure 
/curious * 
/curl 
/currency ** 
/current 
/curriculum ** 
/curry 
/curse ** 
/curtain * 
/curve 
/custody ** 
/custom 
/customer * 
/cut *
/cute * 
/cycle * 
/cynical **



### D
/dad * 
/dairy 
/dam 
/damage 
/damp 
/dance * 
/danger * 
/dare 
/dark * 
/darling 
/dash 
/database 
/date * 
/daughter * 
/dawn 
/day * 
/dead * 
/deal 
/death * 
/debate 
/debt 
/decade 
/decay 
/decent ** 
/decide * 
/decision 
/deck 
/declare 
/decline 
/decorate 
/decrease 
/dedicate ** 
/deep * 
/defeat 
/defense / defence 
/defend 
/defendant 
/deficiency ** 
/deficit ** 
/define 
/definite 
/degrade ** 
/degree 
/delay 
/delegate ** 
/delete 
/deliberate ** 
/delicate 
/delicious * 
/delight 
/deliver 
/demand 
/democracy 
/democrat 
/demon 
/demonstrate 
/dense 
/dentist * 
/deny 
/department 
/departure 
/depend 
/dependence 
/depict ** 
/deposit ** 
/depress 
/deprive ** 
/derive 
/descend 
/describe 
/description 
/desert 
/deserve 
/design * 
/designate ** 
/desire 
/desk * 
/despair 
/desperate 
/despite 
/destination 
/destiny 
/destroy 
/destruction 
/detach 
/detail 
/detect 
/determine 
/develop 
/device 
/devil 
/devise 
/devote 
/diabetes ** 
/dialogue / dialog * 
/diary * 
/dictate ** 
/dictionary 
/die * 
/different * 
/difficult * 
/dig 
/dignity ** 
/dimension ** 
/diminish 
/dine ** 
/dinner * 
/dip 
/diplomat 
/direct 
/dirty * 
/disabled 
/disadvantage 
/disagree 
/disappear 
/disappoint 
/disaster 
/discharge ** 
/discipline 
/disclose 
/discount 
/discourse ** 
/discover 
/discriminate ** 
/discuss * 
/disease 
/disgust 
/dish * 
/dismiss 
/disorder 
/displace ** 
/display 
/dispose 
/dispute ** 
/disrupt ** 
/distant 
/distort ** 
/distract 
/distribute 
/district 
/disturb 
/dive 
/diverse 
/divide * 
/divine ** 
/divorce 
/do * 
/doctor * 
/document 
/dog * 
/doll * 
/dolphin * 
/domain 
/domestic 
/dominant ** 
/donate 
/door * 
/dose ** 
/dot 
/double * 
/doubt 
/down * 
/dozen 
/draft ** 
/drag 
/drain ** 
/draw * 
/drawer 
/dread ** 
/dream * 
/drink * 
/drive * 
/drop * 
/drown 
/drug 
/dry * 
/dual ** 
/duck * 
/due 
/dull 
/dump 
/during * 
/dust 
/duty 
/dwell 
/dynamic


### E
/each 
/eager 
/ear * 
/early * 
/earn 
/earth * 
/ease 
/east * 
/easy * 
/eat * 
/economy 
/edge 
/edit 
/educate 
/effect 
/effective 
/efficient 
/effort 
/egg * 
/either 
/elaborate ** 
/elect 
/electric 
/electronic 
/elegant 
/element 
/elementary * 
/elephant * 
/eliminate 
/else 
/embarrass 
/embassy 
/embrace ** 
/emerge 
/emergency 
/emit ** 
/emotion 
/emphasis 
/empire 
/employ 
/empty 
/enclose 
/encounter 
/encourage 
/end *
/endure 
/enemy 
/enforce ** 
/engage 
/engine * 
/engineer * 
/enhance 
/enjoy * 
/enormous 
/enough * 
/enroll / enrol ** 
/ensure 
/enter * 
/enterprise 
/entertain 
/enthusiastic 
/entire 
/entitle ** 
/entry 
/envelope 
/environment 
/envy 
/episode 
/equal 
/equate ** 
/equipment 
/era 
/eraser * 
/erect ** 
/error * 
/escape 
/escort 
/especially 
/essential 
/establish 
/estate ** 
/estimate 
/etc / et cetera 
/ethical ** 
/ethnic ** 
/evacuate ** 
/evaluate 
/eve 
/even 
/evening * 
/eventually 
/ever 
/every * 
/evident 
/evil 
/evolution 
/evolve 
/exact 
/exaggerate 
/exam * / examination 
/examine 
/example * 
/exceed 
/excellent 
/except 
/excess 
/exchange 
/excite 
/exclude 
/exclusive ** 
/excuse 
/executive ** 
/exercise * 
/exhaust
/exhibit 
/exist 
/exit * 
/exotic 
/expand 
/expect 
/expense 
/expensive 
/experience 
/experiment 
/expert 
/expertise ** 
/explain 
/explicit ** 
/explode 
/explore 
/export 
/expose 
/express 
/extend 
/extent 
/external 
/extinct 
/extra 
/extract ** 
/extraordinary ** 
/extreme 
/eye * 
/eyebrow 



### F
/fabric 
/face *
/facilitate ** 
/facility 
/fact * 
/factor 
/factory * 
/faculty ** 
/fade 
/fail * 
/faint 
/fair 
/faith 
/fall * 
/false 
/fame 
/familiar 
/family * 
/famous * 
/fan * 
/fancy 
/fantastic * 
/far * 
/fare 
/farm * 
/fascinate 
/fast * 
/fasten 
/fat * 
/fatal ** 
/fate 
/father * 
/fault 
/favor / favour 
/favorite / favourite * 
/fear 
/feature 
/federal ** 
/fee 
/feed 
/feel * 
/fellow 
/female 
/ferry 
/fertile ** 
/fever * 
/few 
/fiber / fibre 
/field * 
/fierce 
/fight * 
/figure 
/file * 
/fill * 
/filter 
/final 
/finance 
/find * 
/fine *
/finger * 
/finish * 
/finite 
/fire *
/firm 
/fish *
/fist 
/fit 
/fix * 
/flag * 
/flame 
/flash 
/flat 
/flavor / flavour 
/flaw 
/flee ** 
/flesh 
/flexible 
/flight 
/flip ** 
/float 
/flock 
/flood 
/floor * 
/flourish 
/flow 
/flower * 
/fluid ** 
/flush ** 
/fly *
/focus * 
/fog * 
/fold 
/folk 
/follow 
/fond ** 
/food * 
/fool *
/foot * 
/football * 
/for * 
/forbid 
/force 
/forecast 
/forehead 
/foreign 
/forest * 
/forever * 
/forget * 
/forgive 
/form *
/formal 
/format 
/formation 
/former 
/formula ** 
/forth 
/fortunate 
/fortune 
/forum 
/forward 
/foster ** 
/foundation 
/fountain 
/fox * 
/fraction ** 
/frame 
/framework 
/frankly 
/free * 
/freeze 
/frequent 
/fresh * 
/friend * 
/fright 
/frog * 
/from * 
/front * 
/frost ** 
/frown 
/fruit * 
/frustrate 
/fry * 
/fuel 
/fulfil 
/full * 
/fun * 
/function 
/fund 
/fundamental 
/funeral 
/fur 
/furious ** 
/furnish ** 
/furniture 
/furthermore 
/fuse ** 
/future *



### G
/gain 
/gamble 
/gang 
/gap 
/garage 
/garden * 
/gasoline / petrol ** 
/gate * 
/gather 
/gaze ** 
/gear 
/gender 
/gene 
/general 
/generate ** 
/generation 
/generous 
/genius 
/genre 
/gentle 
/gentleman * 
/genuine 
/geography 
/geology 
/gesture * 
/get * 
/ghost * 
/giant * 
/gift * 
/giraffe * 
/girl * 
/give * 
/glad * 
/glance 
/glare ** 
/glass * 
/glimpse ** 
/global 
/glory 
/glove * 
/glow 
/glue * 
/go * 
/goal * 
/goat 
/god * 
/gold * 
/good * 
/goodbye * 
/goods 
/gorgeous 
/govern 
/grab 
/grace 
/grade 
/gradual 
/graduate 
/grain 
/grand 
/grandfather * 
/grant 
/grape * 
/graphic 
/grasp ** 
/grass * 
/grateful 
/grave 
/great * 
/greed 
/green * 
/greet 
/grey / gray * 
/grief 
/grip
/grocery 
/gross ** 
/ground * 
/group * 
/grow * 
/guarantee 
/guardian ** 
/guess * 
/guest 
/guide * 
/guideline 
/guilty 
/gulf ** 
/gun 
/guy * 
/gymnasium / gym



### H
/habit * 
/habitat ** 
/hair * 
/half 
/hall 
/halt ** 
/hammer 
/hand * 
/handicap 
/handle 
/handsome * 
/hang * 
/happen 
/happy * 
/harbor / harbour 
/hard * 
/hardly 
/harm 
/harsh 
/harvest 
/haste 
/hat * 
/hate * 
/haunt ** 
/have * 
/hazard 
/he * 
/head * 
/headache * 
/headquarters ** 
/heal 
/health 
/hear 
/heart * 
/heat * 
/heaven * 
/heavy * 
/heel 
/height 
/heir ** 
/helicopter * 
/hell 
/hello / hey / hi * 
/help *
/hence ** 
/here * 
/heritage ** 
/hero * 
/hesitate 
/hide 
/high * 
/highway 
/hill * 
/hip 
/hire 
/history * 
/hit *
/hobby * 
/hold * 
/hole 
/holiday * 
/holy 
/home * 
/homework * 
/honest * 
/honey * 
/honor / honour 
/hook ** 
/hope *
/horizon 
/horn ** 
/horror 
/horse * 
/hospital * 
/host 
/hostage ** 
/hostile ** 
/hot * 
/hour * 
/house * 
/household 
/how * 
/however * 
/hug 
/huge 
/human * 
/humor / humour * 
/hundred * 
/hungry * 
/hunt * 
/hurry * 
/hurt 
/husband * 
/hut 
/hypothesis **



### I
/I * 
/ice * 
/idea * 
/ideal 
/identical 
/identify 
/ideology ** 
/if * 
/ignore 
/ill 
/illusion ** 
/illustrate 
/imagine 
/imitate 
/immediate 
/immense ** 
/immigrate ** 
/immune 
/impact 
/imperial 
/implement ** 
/imply ** 
/import 
/important * 
/impose ** 
/impress 
/improve 
/in * 
/incentive 
/incident 
/incline ** 
/include 
/income 
/incorporate ** 
/increase 
/incredible 
/indeed 
/independent 
/index ** 
/indicate 
/individual 
/induce ** 
/industry 
/inevitable ** 
/infant 
/infect ** 
/infer ** 
/inflate ** 
/influence 
/inform 
/informal 
/ingredient 
/inhabit 
/inherent ** 
/inhibit ** 
/initial 
/initiate 
/inject 
/injure 
/inn 
/innocent 
/innovate 
/input 
/inquire / enquire ** 
/insect 
/insert 
/inside * 
/insight 
/insist 
/inspect 
/inspire 
/install 
/instance 
/instant 
/instead 
/instinct 
/institute 
/instruct 
/instrument 
/insult 
/insure 
/integrate ** 
/intellectual 
/intelligent 
/intend 
/intense 
/intent 
/interact 
/interest 
/interfere 
/intermediate 
/internal 
/international 
/interpret 
/interrupt 
/interval 
/intervene ** 
/intimate 
/into * 
/intrigue ** 
/introduce * 
/invade 
/invent 
/invest 
/investigate 
/invite * 
/involve 
/iron 
/irony 
/irritate 
/island 
/isolate 
/it * 
/item


### J
/jail 
/jar 
/jaw 
/jeans * 
/jet 
/job * 
/jog 
/join * 
/joint 
/joke 
/journal 
/journey 
/joy * 
/judge 
/judicial ** 
/junior 
/jury 
/just * 
/justice 
/justify 


### K
/keen ** 
/keep * 
/key * 
/kick * 
/kid * 
/kill * 
/kind *
/king * 
/kit 
/kitchen * 
/knee 
/knife * 
/knight 
/knock 
/knot ** 
/know * 



### L
/label 
/labor / labour 
/laboratory / lab 
/lack 
/ladder 
/lady * 
/lake * 
/lamb 
/lamp 
/land * 
/landscape 
/lane 
/language 
/lap 
/large * 
/last *
/late * 
/latter 
/laugh 
/launch 
/laundry 
/law 
/lawn 
/lawyer 
/lay 
/layer 
/lazy * 
/lead 
/leaf * 
/leak 
/lean 
/leap 
/learn * 
/lease ** 
/leather 
/leave 
/lecture 
/left *
/leg * 
/legal 
/legend 
/legislate ** 
/legitimate ** 
/leisure 
/lend 
/lesson * 
/let 
/letter * 
/level 
/liberal 
/liberty 
/library * 
/license/licence
/lid 
/lie * 
/lift 
/light * 
/like *
/likely 
/likewise 
/limit 
/line * 
/linguistic 
/link 
/lion * 
/lip * 
/liquid 
/list 
/listen * 
/literal ** 
/literature 
/little * 
/live * 
/livingroom * 
/load 
/loan 
/local 
/locate 
/lock 
/log 
/logic 
/lone ** 
/long * 
/look *
/loose 
/lose 
/loss 
/lot 
/loud 
/lounge 
/love * 
/low * 
/loyal 
/luck * 
/lump ** 
/lunch * 
/luxury 



### M
/machine 
/mad * 
/magazine 
/magnet 
/magnificent ** 
/mail *
/main 
/maintain 
/major 
/majority 
/make * 
/male 
/man * 
/manage 
/manifest ** 
/manipulate ** 
/manner 
/manufacture 
/many * 
/map * 
/margin 
/marine 
/mark 
/marry * 
/marvel 
/mass 
/master 
/match 
/mate 
/material 
/mathematics / maths / math * 
/matter 
/mature 
/maximum 
/may * 
/maybe 
/mayor 
/meal 
/mean 
/meantime 
/meanwhile ** 
/measure 
/meat * 
/mechanic 
/mechanism 
/mediate 
/medical 
/medicine 
/medieval ** 
/medium 
/meet * 
/melt 
/memory * 
/mental 
/mention 
/merchant 
/mere ** 
/merge ** 
/merit 
/mess 
/metal 
/method 
/metropolitan ** 
/microphone 
/microwave 
/middle * 
/might * 
/migrate ** 
/mild 
/military 
/milk * 
/mill 
/million 
/mind * 
/miner 
/mineral 
/minimal 
/minimum 
/ministry 
/minor 
/minute 
/miracle 
/mirror * 
/miss * 
/missile 
/mission 
/mistake 
/mix 
/mobile 
/mock ** 
/mode 
/moderate ** 
/modern 
/modest ** 
/modify ** 
/moisture 
/molecule ** 
/moment 
/money * 
/monitor 
/monkey * 
/monster 
/month * 
/monument ** 
/mood 
/moon * 
/moral 
/moreover 
/morning * 
/mortal ** 
/mother * 
/motion 
/motive 
/mount 
/mountain * 
/mouse * 
/mouth * 
/move * 
/movie * 
/much * 
/mud 
/multiple 
/multiply 
/murder 
/muscle 
/museum * 
/mushroom 
/music * 
/must * 
/mutual ** 
/myth



### N
/nail 
/naive ** 
/naked 
/name * 
/nanny ** 
/narrate 
/narrow 
/nasty ** 
/nation * 
/native 
/nature * 
/navy 
/near * 
/neat 
/necessary 
/neck * 
/need *
/needle 
/negative 
/neglect 
/negotiate 
/neighbor / neighbour 
/neither 
/nephew 
/nervous 
/nest 
/net 
/network 
/neutral 
/never * 
/nevertheless 
/new * 
/newspaper * 
/next * 
/nice * 
/night * 
/nightmare 
/no / nope / nay * 
/noble 
/nobody 
/nod 
/noise 
/nominate ** 
/none 
/nonetheless ** 
/nonsense 
/noon * 
/nor 
/norm ** 
/normal 
/north * 
/nose * 
/not * 
/note *
/nothing * 
/notice 
/notion ** 
/novel 
/now * 
/nowadays 
/nowhere 
/nuclear 
/number * 
/numerous ** 
/nun ** 
/nurse * 
/nut 



### O
/oak 
/obey 
/object 
/objective 
/oblige ** 
/observe 
/obsess ** 
/obtain 
/obvious 
/occasion 
/occupation 
/occupy 
/occur 
/ocean * 
/odd 
/of * 
/off * 
/offend 
/offer 
/office * 
/officer 
/official 
/often * 
/oil * 
/old * 
/olive 
/on * 
/once 
/one * 
/only * 
/open * 
/operate 
/opinion 
/opportunity 
/oppose 
/optimist 
/option 
/or * 
/oral 
/orbit ** 
/orchestra 
/order 
/ordinary 
/organ 
/organic 
/organize / organise 
/orient 
/origin 
/other 
/otherwise 
/ought 
/ounce ** 
/out * 
/outcome 
/outline 
/output 
/outrage ** 
/outstanding 
/over * 
/overall 
/overcome 
/overhead 
/overlap 
/overlook
/overnight 
/oversea / overseas 
/overwhelm ** 
/owe 
/own 



### P
/pace 
/pack 
/packet 
/pad 
/pain 
/paint * 
/pair 
/palace * 
/pale 
/palm 
/pan 
/panel ** 
/panic 
/pants * 
/paper * 
/paragraph 
/parallel ** 
/pardon 
/parent * 
/park *
/parliament ** 
/part * 
/participate 
/particle ** 
/particular 
/pass *
/passage 
/passenger 
/passion 
/passport 
/past 
/pat ** 
/patch ** 
/patent ** 
/path 
/patient 
/patrol ** 
/pattern 
/pause 
/pave ** 
/pay * 
/peace * 
/peak 
/pear * 
/peasant ** 
/peel 
/peer 
/penalty 
/pencil * 
/people * 
/pepper 
/per 
/perceive 
/perfect 
/perform 
/perhaps 
/period 
/permanent 
/permit 
/persist ** 
/person 
/personality 
/perspective ** 
/persuade 
/pet 
/phase ** 
/phenomenon 
/philosophy 
/photograph 
/phrase 
/physical 
/physics 
/pick * 
/picnic * 
/picture * 
/piece 
/pig * 
/pile 
/pill 
/pin 
/pinch ** 
/pine 
/pink * 
/pioneer 
/pitch ** 
/pity 
/place * 
/plain 
/plan * 
/planet 
/plant 
/plate 
/platform 
/play * 
/pleasant 
/please * 
/pleasure 
/plenty 
/plot 
/plus 
/P.M. / p.m. *
/pocket * 
/poem 
/poet 
/point *
/poison 
/polar 
/pole 
/police * 
/policy 
/polish ** 
/polite 
/politics 
/poll 
/pollute 
/pond 
/pool 
/poor * 
/pop 
/pope ** 
/popular 
/population 
/pork 
/port 
/portion ** 
/portrait 
/pose 
/position 
/positive 
/possess 
/possible 
/post 
/poster 
/pot 
/potato * 
/potential 
/pour 
/powder 
/power * 
/practical 
/practice / practise 
/praise 
/pray 
/preach ** 
/precede ** 
/precious 
/precise 
/predator ** 
/predict 
/prefer 
/pregnant 
/prejudice ** 
/premier ** 
/premium ** 
/prepare 
/prescribe 
/presence 
/present * 
/preserve 
/president 
/press 
/presume ** 
/pretend 
/pretty * 
/prevail ** 
/prevent 
/previous 
/prey 
/price 
/pride 
/priest 
/primary 
/prime 
/primitive 
/prince * 
/principal 
/principle 
/print *
/prior ** 
/prison 
/privacy 
/private 
/privilege ** 
/prize * 
/probably 
/problem * 
/procedure ** 
/proceed 
/process 
/produce 
/profession 
/professor 
/profile ** 
/profit 
/profound ** 
/progress 
/prohibit ** 
/prominent ** 
/promise 
/promote 
/prompt ** 
/pronounce 
/proof 
/proper 
/property 
/proportion ** 
/propose 
/prospect 
/prosper ** 
/protect 
/protein 
/protest 
/proud 
/prove 
/provide 
/province 
/provoke ** 
/psychology 
/pub 
/public 
/publish 
/pull 
/pump 
/punch 
/punish 
/pupil 
/puppy * 
/purchase 
/pure 
/purple 
/purpose 
/pursue 
/push * 
/put * 
/puzzle * 


### Q
/qualify 
/quality 
/quantity 
/quarter 
/queen * 
/question * 
/questionnaire ** 
/quick * 
/quiet * 
/quit 
/quite 
/quote **


### R
/rabbit * 
/race * 
/racial 
/rage ** 
/rail 
/rain * 
/rainbow * 
/raise 
/rally ** 
/random 
/range 
/rank 
/rapid 
/rare 
/rat 
/rate 
/rather 
/rational ** 
/raw 
/reach 
/react 
/read * 
/ready * 
/real 
/realize / realise 
/rear ** 
/reason 
/rebel ** 
/recall 
/receipt 
/receive 
/recent 
/reception 
/recipe 
/recognize 
/recommend 
/record 
/recover 
/recruit ** 
/recycle 
/red * 
/reduce 
/refer 
/refine ** 
/reflect 
/reform 
/refrigerator / fridge 
/refuse 
/regard 
/region 
/register 
/regret 
/regular 
/regulate ** 
/reinforce ** 
/reject 
/relate 
/relative 
/relax 
/release 
/relevant ** 
/relieve 
/religion 
/reluctant ** 
/rely 
/remain 
/remark 
/remedy 
/remember * 
/remind 
/remote 
/remove 
/rent 
/repair 
/repeat 
/replace 
/reply 
/report 
/represent 
/republic 
/reputation ** 
/request 
/require 
/rescue 
/research 
/resemble 
/reserve 
/reside ** 
/resign ** 
/resist 
/resolve 
/resort 
/resource 
/respect 
/respective ** 
/respond 
/responsible 
/rest 
/restaurant * 
/restore 
/restrain ** 
/restrict ** 
/restroom * 
/result 
/resume ** 
/retail ** 
/retain ** 
/retire 
/retreat ** 
/return * 
/reveal 
/revenge ** 
/reverse ** 
/review 
/revise 
/revive 
/revolution 
/reward 
/rhythm 
/rice 
/rich * 
/rid ** 
/ride 
/ridiculous ** 
/right *
/ring *
/riot ** 
/rise 
/risk 
/rival 
/river * 
/road * 
/roar ** 
/roast 
/rob 
/rock *
/rod ** 
/role 
/roll 
/romantic 
/roof * 
/room * 
/root 
/rope 
/rot ** 
/rough 
/round 
/route 
/routine 
/row 
/royal 
/rub 
/rubber 
/rude 
/ruin 
/rule 
/rumor / rumour 
/run * 
/rural 
/rush 


### S
/sack ** 
/sacred 
/sacrifice 
/sad * 
/safe * 
/sail 
/salary 
/sale * 
/salon ** 
/salt * 
/same * 
/sand * 
/satellite 
/satisfy
/save * 
/say * 
/scale 
/scan 
/scandal 
/scarce ** 
/scare 
/scatter ** 
/scene 
/scheme 
/scholar 
/school * 
/science * 
/scissors * 
/scold
/scope ** 
/score * 
/scramble 
/scratch 
/scream 
/screen 
/screw ** 
/scrub ** 
/sculpture / sculpt ** 
/sea * 
/seal 
/search 
/season * 
/seat 
/secret 
/secretary 
/sector 
/secure 
/see * 
/seed 
/seek 
/seem 
/seize ** 
/select 
/self 
/sell * 
/send * 
/senior 
/sensation 
/sense 
/sensible 
/sentence 
/sentiment ** 
/separate 
/sequence ** 
/series 
/serious 
/serve 
/session 
/settle 
/several 
/severe 
/sew 
/sex 
/shade 
/shadow 
/shake 
/shall 
/shallow 
/shame 
/shape 
/share 
/sharp 
/shave 
/she * 
/sheep 
/sheet 
/shelf 
/shell 
/shelter ** 
/shield ** 
/shift 
/shine 
/ship * 
/shock * 
/shoe * 
/shoot 
/shop * 
/shore 
/short * 
/should * 
/shoulder 
/shout 
/show *
/shower 
/shrink ** 
/shut 
/shy * 
/sick * 
/side * 
/sigh 
/sight 
/sign 
/significant 
/silent 
/silk 
/silly 
/silver 
/similar 
/simple 
/simulate ** 
/simultaneous ** 
/sin 
/since 
/sing * 
/single 
/sink 
/sister * 
/sit * 
/site 
/situation 
/size * 
/skill 
/skin * 
/skip 
/skirt * 
/sky * 
/slaughter ** 
/slave 
/sleep * 
/slice 
/slide 
/slight ** 
/slim 
/slip 
/slope ** 
/slow * 
/small * 
/smart * 
/smash 
/smell * 
/smile * 
/smoke 
/smooth 
/snake 
/snap 
/sneak ** 
/sniff ** 
/snow * 
/so * 
/soak 
/soap 
/soccer * 
/social 
/society 
/sociology 
/sock * 
/soft * 
/software 
/soil 
/soldier 
/sole ** 
/solid 
/solo 
/solve 
/some * 
/somewhat 
/son * 
/song * 
/soon 
/sophisticated ** 
/sore 
/sorry * 
/sort 
/soul 
/sound *
/sour * 
/source 
/south * 
/space * 
/span ** 
/spare
/spark 
/speak * 
/special 
/species 
/specific 
/spectacle ** 
/spectrum ** 
/speech 
/speed * 
/spell 
/spend 
/sphere ** 
/spill ** 
/spin 
/spirit 
/spit ** 
/spite ** 
/splash ** 
/split ** 
/spoil 
/spoon * 
/spot 
/spouse ** 
/spread 
/square 
/squeeze 
/stable 
/stack ** 
/stage 
/stain 
/stairs 
/stamp 
/stand *
/standard 
/stare 
/start * 
/starve ** 
/state 
/station 
/statistic ** 
/statue 
/status 
/stay * 
/steady 
/steal 
/steam 
/steel 
/steep ** 
/stem 
/step 
/stick 
/stiff ** 
/still 
/stimulate ** 
/stir ** 
/stitch ** 
/stock 
/stomach 
/stone * 
/stop *
/store *
/storm 
/story * 
/stove 
/straight 
/strain ** 
/strange 
/strategy 
/straw 
/strawberry * 
/stream 
/street * 
/stress *
/stretch 
/strict 
/strike 
/string 
/strip ** 
/stripe 
/stroke ** 
/strong * 
/structure 
/struggle 
/student * 
/study * 
/stuff 
/subject 
/subjective ** 
/submarine
/submit ** 
/subscribe ** 
/substance ** 
/substantial ** 
/substitute ** 
/subtle ** 
/suburb 
/subway * 
/succeed 
/such 
/suck ** 
/sudden 
/suffer 
/sufficient 
/sugar * 
/suggest 
/suicide 
/suit 
/suite ** 
/sum 
/summary 
/summit 
/sun * 
/super 
/superb 
/superior 
/supervise ** 
/supper * 
/supplement ** 
/supply 
/support 
/suppose 
/sure 
/surface 
/surgery 
/surprise 
/surrender ** 
/surround 
/survey 
/survive 
/suspect 
/suspend ** 
/sustain ** 
/swallow 
/swear ** 
/sweat 
/sweep ** 
/sweet 
/swell ** 
/swift ** 
/swim * 
/swing 
/switch 
/symbol 
/sympathy 
/symphony 
/symptom 
/system



### T
/table * 
/tackle 
/tag 
/tail * 
/take * 
/tale 
/talent 
/talk *
/tall * 
/tap 
/tape *
/target 
/task 
/taste *
/tattoo 
/tax 
/tea 
/teach * 
/tear 
/tease ** 
/teen * 
/teenage 
/telegraph ** 
/telephone * 
/tell * 
/temperature 
/temple 
/temporary ** 
/tempt ** 
/tenant ** 
/tend 
/tender 
/tense 
/term 
/terminal 
/terminate ** 
/terrace ** 
/terrible 
/terrific 
/territory 
/test *
/testify ** 
/text 
/textbook * 
/than * 
/thank * 
/that * 
/the * 
/theater / theatre 
/theme 
/then 
/theory 
/therapy ** 
/there * 
/therefore 
/they * 
/thick 
/thief 
/thin 
/thing * 
/think * 
/thirst *
/this * 
/thorough 
/though 
/thousand 
/thread ** 
/threat 
/thrill 
/throat 
/through 
/throw 
/thumb 
/thus 
/tick ** 
/tide 
/tidy 
/tie 
/tiger * 
/tight 
/till 
/timber ** 
/time * 
/tin 
/tiny 
/tip 
/tire / tyre 
/tissue 
/title 
/to * 
/tobacco
/today * 
/toe 
/together * 
/toilet 
/tomorrow * 
/tone 
/tongue 
/tonight * 
/too * 
/tool 
/tooth * 
/top * 
/torture ** 
/toss 
/total 
/touch *
/tough 
/tour * 
/toward / towards 
/tower * 
/town * 
/toxic 
/toy * 
/trace 
/trade 
/tradition 
/traffic 
/tragic 
/trail ** 
/train *
/transact ** 
/transfer 
/transform 
/transition ** 
/translate 
/transmit ** 
/transport 
/trap 
/travel * 
/tray 
/treasure 
/treat 
/treaty ** 
/tree * 
/tremendous ** 
/trend 
/trial 
/triangle * 
/tribe 
/trick 
/trigger ** 
/trim ** 
/trip * 
/triumph 
/troop 
/trophy 
/trouble 
/trouser 
/true * 
/trunk 
/trust 
/truth 
/try * 
/tube 
/tune 
/tunnel 
/turn *
/turnover ** 
/tutor 
/twice * 
/twin 
/twist 
/type *
/typical



### U
/ugly * 
/ultimate 
/umbrella * 
/uncle * 
/under * 
/undergo ** 
/underlie ** 
/undermine ** 
/understand * 
/undertake ** 
/uniform 
/unify 
/union 
/unique 
/unit 
/unite 
/universe 
/university 
/unless 
/until 
/up * 
/update 
/upon 
/upper 
/upset 
/upward / upwards 
/urban 
/urge 
/urgent
/use *
/usual 
/utilize / utilise ** 
/utter ** 



### V
/vacation 
/vacuum 
/vague ** 
/valid ** 
/valley 
/value 
/van 
/vanish ** 
/various 
/vary 
/vast 
/vegetable * 
/vehicle 
/venture 
/verbal ** 
/verse ** 
/version 
/versus 
/vertical ** 
/very * 
/vessel ** 
/veteran ** 
/veterinarian ** 
/via 
/vice ** 
/victim 
/victory 
/view 
/vigorous ** 
/village 
/violent 
/virgin ** 
/virtual ** 
/virtue ** 
/visible 
/visit *
/visual 
/vital ** 
/vivid ** 
/vocabulary 
/vocation ** 
/voice * 
/volume 
/voluntary 
/vote 
/voyage 



### W
/wage 
/wagon ** 
/wait * 
/wake * 
/walk *
/wall * 
/wander ** 
/want * 
/war * 
/warehouse ** 
/warm * 
/warn 
/warrant ** 
/warrior ** 
/wash * 
/waste 
/watch * 
/water *
/watermelon * 
/wave 
/way * 
/we * 
/weak 
/wealth 
/weapon 
/wear * 
/weather * 
/weave ** 
/wedding * 
/weed ** 
/week * 
/weekend * 
/weigh 
/weight * 
/weird 
/welcome * 
/welfare 
/well * 
/west * 
/wet * 
/whale 
/what * 
/wheat 
/wheel 
/when * 
/where * 
/whereas ** 
/whether 
/which 
/while 
/whip ** 
/whisper 
/whistle 
/white * 
/who * 
/whole 
/why * 
/wicked ** 
/wide 
/widespread 
/widow ** 
/wife * 
/wild 
/will * 
/win * 
/wind *
/window * 
/wing 
/wipe 
/wire 
/wise 
/wish *
/wit 
/with * 
/withdraw ** 
/within 
/without 
/witness 
/woman * 
/wonder 
/wood * 
/wool 
/word * 
/work *
/world * 
/worry * 
/worship 
/worth 
/would 
/wound 
/wrap 
/wreck ** 
/write * 
/wrong *


### Y
/year * 
/yell 
/yellow * 
/yes / yeah / yep * 
/yesterday * 
/yet 
/yield ** 
/you * 
/young * 


### Z
/zebra * 
/zone 
/zoo *

""")
note.N10_01 = N(('T11,1,0', 'Verb and Preposition'), 'up', """
""")
note.N10_02 = N(('T11,2,0', 'Verb and Preposition'), 'down', """
""")
note.N10_03 = N(('T11,3,0', 'Verb and Preposition'), 'on', """
""")
note.N10_04 = N(('T11,4,0', 'Verb and Preposition'), 'off', """
""")
note.N10_05 = N(('T11,5,0', 'Verb and Preposition'), 'in/into', """
""")
note.N10_06 = N(('T11,6,0', 'Verb and Preposition'), 'out', """
""")
note.N10_07 = N(('T11,7,0', 'Verb and Preposition'), 'away/after/over', """
""")
note.N10_08 = N(('T11,8,0', 'Verb and Preposition'), 'for/to/at', """
""")
note.N10_09 = N(('T11,9,0', 'Verb and Preposition'), 'about/with/through/across', """
""")

note.N11 = N(('T12,0,0', 'Additionals'), 'Main Board', """
## Additionals
""")
note.N11_01 = N(('T12,1,0', 'Additionals'), 'script 1', """
- For thinking over about this intuitively, it is necessary to understand ~. 
- I applied myself to the job.
- I can apply in my research and for industry applications.
- I am going to talk about what this is about.
- **It's just for your information in case you need more** background knowledge.
- These are not necessary, absolutely.
- **Familiarity with** one, two options** is strongly recommend**.
""")
note.N11_02 = N(('T12,2,0', 'Additionals'), 'script 2', """
- You're being a little bit too loud
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
- They only use organic ingredients.
- They **are known for** healthy, pretty, delicious food.
- This is **truly number one**.
- **Let's continue with** the story. 
- It was amazing.
- It has **exceptional cocktails**.
- This is **one place you can't afford to miss**.
- You'll experience a **culinary adventure**.
- The place **is rated in the top ten** on a site
- **That doesn't matter** because ~
- It's the **ultimate experience**.
- I mean I am **speechless with that**.
- It's currently **the beginning of November**.
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
                                dbc.Button("Notion", color="secondary", href="https://www.notion.so/WorkSheet-d64a1a09956d4318ac38b3d7f0131cfb"),                                
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
################################## SETUP INFO ##################################
"""
[name] : -
[version] : 0.0
[description] : -
[author] : anonym
[keywords] : -
"""    
