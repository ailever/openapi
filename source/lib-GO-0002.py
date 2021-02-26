#%%
# https://plotly.com/python-api-reference/
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Sankey.html
# https://github.com/ailever/openapi/blob/master/source/lib-GO-0002.py

import plotly.graph_objects as go
import numpy as np

obj = np.zeros((10,10))
obj[0,1] = 1
obj[1,9] = 1
obj[5,7] = 1
obj[3,7] = 1
obj[5,5] = 1
obj[9,9] = 1
x, y = np.where(obj==1)
x = np.cumsum(x/x.sum())
y = np.cumsum(y/y.sum())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
fig = go.Figure(go.Sankey(
    arrangement = "snap",
    node = {
        "label": [alphabet[i] for i in range(x.shape[0])],
        "x": x,
        "y": y,
        'pad':10},
    link = {
        "source": [0, 0, 1, 2, 5, 4, 3, 5],
        "target": [5, 3, 4, 3, 0, 2, 2, 3],
        "value": [1, 1, 1, 1, 1, 1, 1, 2]}))

fig.show()
