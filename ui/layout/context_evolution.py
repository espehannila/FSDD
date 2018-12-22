# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

contextGraph        = html.Div(children=[
    html.H6('Context evolution'),
    dcc.Graph(id='context-evolution')
])