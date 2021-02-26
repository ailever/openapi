#%%
# https://plotly.com/python-api-reference/generated/plotly.express.timeline.html
# https://github.com/ailever/openapi/blob/master/source/lib-PX-0000.py

import plotly.express as px
import pandas as pd


text = ['Job A',
        'Job B',
        'Job C',
        'Job 4']

df = pd.DataFrame([
    dict(Details=text[0], Start='2000', Finish='2009', Level="L1"),
    dict(Details=text[1], Start='2009', Finish='2011', Level="L1"),
    dict(Details=text[2], Start='2009', Finish='2017', Level="L2"),
    dict(Details=text[3], Start='2017', Finish='2023', Level="L2"),
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Level", color="Details", text=text)
fig.show()
