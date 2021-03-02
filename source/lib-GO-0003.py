#%%
import plotly.graph_objects as go

labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    parents = parents,
    marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue"]))

fig.show()
