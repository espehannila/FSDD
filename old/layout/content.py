# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from .graph import graph
    
content = html.Div([

    html.Div([
        html.Div([
            html.H6(children='Gíve word to search'),
            html.Div(children=[
                dcc.Input(id='search-input',value='magee',placeholder='Search for the word', type='text'),
                html.Button(id='search-button',children='Search',type='submit'),
                html.Div(id='search-div')
            ])
        ]),


        html.Div([
            html.H6('Select corpus'),
            dcc.Checklist(
                id='search-select',
                options=[
                    { 'label': 'Suomi24', 'value': 'S24' },
                    { 'label': 'KLK', 'value': 'KLK' },
                    { 'label': 'Ylilauta', 'value': 'YLILAUTA' },
                    { 'label': 'Kotus', 'value': 'KOTUS' },
                    { 'label': 'Lam', 'value': 'LAM' },
                    { 'label': 'Agricola', 'value': 'AGRICOLA' },
                    { 'label': 'Eduskunta', 'value': 'EDUSKUNTA' },
                    { 'label': 'Lehdet', 'value': 'LEHDET' },
                    { 'label': 'Tiedelehdet', 'value': 'TIEDELEHDET' },
                    { 'label': 'Europa', 'value': 'EUROPA' },
                    { 'label': 'Thesis', 'value': 'ETHESIS' },
                    { 'label': 'Murre', 'value': 'LA_MURRE' },
                    { 'label': 'Skk', 'value': 'SKK' },
                    { 'label': 'Vns', 'value': 'VNS' },
                    { 'label': 'Sinerbrychoff', 'value': 'SINEBRYCHOFF' },
                    { 'label': 'Opensubtitles', 'value': 'OPUS_OPENSUBTITLES' }
                ],
                values=['S24'],
                className='row'
            )
        ])
    ], className='query-form'),

    html.Div([
        graph
    ], className='results', id='results-div', style={ 'display': 'none' }),
    html.Div([
        html.H5(id='loading-text', children='Loading, please wait...')
    ], className='loader', id='loading-div', style={ 'display': 'block' })
])
    