#%%
# https://plotly.com/python-api-reference/
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Sankey.html
# https://github.com/ailever/openapi/blob/master/source/lib-GO-0002.py

import plotly.graph_objects as go

Labels = ['A', 'B', 'C', 'D']
labels = {}
obj = type('obj', (), {})
L = obj()
for idx, label in enumerate(Labels):
    setattr(L, label, idx)
source = [L.A, L.B]
target = [L.C, L.D]

fig = go.Figure(go.Sankey(
    arrangement = "snap",
    node=dict(label=Labels),
    link = {
        "source": source,
        "target": target,
        "value":  [ 1 ]*len(source)}))
fig.update_layout(title_text='Title')
fig.show()
