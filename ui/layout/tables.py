# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_table as dt

summary = html.Div(children=[
    html.H6('Word appearance sorted by count'),
    dt.DataTable(
        id='word-appearance-table',
        columns=[
            { 'name': 'Year', 'id': 'year' },
            { 'name': 'Count', 'id': 'count' }
        ],
        style_cell={
            'padding': '5px',
            'text-align': 'left'
        },
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold',
            'fontSize': '16px',
            'textAlign': 'left'
        }
    )
])


totalCoOccurrence = html.Div(children=[
    html.H6('Co-Occurring Word appearance sorted by count'),
    dt.DataTable(
        id='co-occurring-word-appearance-table',
        columns=[
            { 'name': 'Word', 'id': 'word' },
            { 'name': 'Count', 'id': 'count' }
        ],
        style_cell={
            'padding': '5px',
            'text-align': 'left'
        },
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold',
            'fontSize': '16px',
            'textAlign': 'left'
        }
    )
])