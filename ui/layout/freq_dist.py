# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

freqGraph       = html.Div(children=[
    html.H6('Frequency distribution'),
    dcc.Graph(id='word-frequency')
])