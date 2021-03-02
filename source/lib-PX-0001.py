#%%
import numpy as np
import pandas as pd
import plotly.express as px

base = np.ones((100,1))
sectors = np.random.multinomial(1, [.4, .3, .3], size=(100,))
df = pd.DataFrame(np.c_[base, sectors])
df.columns = ['Base', 'Sector A', 'Sector B', 'Sector C']
px.sunburst(df, path=df.columns[1:], values='Base')
