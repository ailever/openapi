import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2000', Finish='2009', Resource="A"),
    dict(Task="Job B", Start='2009', Finish='2011', Resource="A"),
    dict(Task="Job C", Start='2009', Finish='2020', Resource="B")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
fig.show()
