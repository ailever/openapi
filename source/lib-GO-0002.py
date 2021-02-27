#%%
# https://plotly.com/python-api-reference/
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Sankey.html
# https://github.com/ailever/openapi/blob/master/source/lib-GO-0002.py

import plotly.graph_objects as go

Labels = ['A', 'B', 'C']
labels = {}
for idx, label in enumerate(Labels):
    labels[label] = idx
L = labels
source = [L['A'], L['C']]
target = [L['B'], L['B']]

fig = go.Figure(go.Sankey(
    arrangement = "snap",
    node=dict(label=Labels),
    link = {
        "source": source,
        "target": target,
        "value":  [ 1 ]*len(source)}))
fig.show()
