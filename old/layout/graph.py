# -*- coding: utf-8 -*-
import dash
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
    
graph = html.Div([
    #html.Label('Word birth to death chart'),
    html.Div([
        html.Label(id='graph-title'),
        dcc.Graph(id='birth-death-graph', style={'margin-top': '20'})
    ]),
    
    html.Div(id='intermediate-value', style={ 'display': 'none' }),

    html.Div([
        html.Label(id='table-title',children=''),
        dt.DataTable(
            id='query-table',
            columns=[
                { 'name': 'Year', 'id': 'year' },
                { 'name': 'Frequency', 'id': 'count' }
            ],
            style_cell={
                'padding': '5px',
                'textAlign': 'left'
            },
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold',
                'fontSize': '16px',
                'textAlign': 'left'
            },
        )
    ])
], className='row')