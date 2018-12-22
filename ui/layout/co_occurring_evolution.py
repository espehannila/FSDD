# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

coOccurringEvolutionGraph        = html.Div(children=[
    html.H6('Co-Occurring evolution'),
    dcc.Graph(id='co-occurring-evolution')
])