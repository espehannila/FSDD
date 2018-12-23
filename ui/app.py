# -*- coding: utf-8 -*-
from dash import Dash
from .layout import layout
from . import callback

external_stylesheets        = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Create applicaton
app                         = Dash(__name__, external_stylesheets=external_stylesheets)

# Setup layout
app.layout                  = layout.layout

# Init functionalities
callback.init(app)