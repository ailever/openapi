# Libraries
#from dash.dependencies import Input, Output, State
#import plotly.express as px
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import sympy
#import dolfin
#from scipy import interpolate
#from scipy import integrate
#from scipy import sparse
#from scipy import linalg
#from scipy import stats
#import statsmodels.api as sm
#import statsmodels.tsa.api as smt
#import statsmodels.formula.api as smf
#from arch import arch_model
#from sklearn import datasets
#from sklearn import model_selection
#from sklearn import linear_model
#from sklearn import metrics
#from sklearn import tree
#from sklearn import neighbors
#from sklearn import svm
#from sklearn import ensemble
#from sklearn import cluster
#import torch
#import torch.nn as nn
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots
import plotly.graph_objs as go

# Project Details
project_title = 'PROJECT'
description = """
Describe your project.
- content1
- content2
- content3
"""

# Code
fig = make_subplots(rows=1, cols=1, subplot_titles=['TITLE'])
fig.add_trace(go.Scatter(x=[1,2,3], y=[3,2,1], mode='lines+markers'), row=1, col=1)











# Layout
contents = {}; contents['page'] = {}; page_layouts = {}
app = dash.Dash(suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
contents['page']['tab'] = [html.H2(project_title), dcc.Graph(figure=fig), dcc.Markdown(description)]
page_layouts['page'] = dbc.Tabs([dbc.Tab(dbc.Card(dbc.CardBody(contents['page']['tab'])), label="AILEVER", disabled=True)])
app.layout = page_layouts['page']
if __name__ == '__main__':
    app.run_server(host="127.0.0.1", port='8050', debug=True)