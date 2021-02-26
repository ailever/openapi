#%%
# https://plotly.com/python-api-reference/
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Bar.html
# https://github.com/ailever/openapi/blob/master/source/lib-GO-0000.py

import plotly.graph_objects as go

fig = go.Figure(go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation='h'))

fig.show()
