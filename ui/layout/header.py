# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from .authors import authors


queryRadios = html.Div(children=[
    html.Div(className='row',children=[
        html.P(className='light-gray bold small-caps', children='mode'),
        dcc.RadioItems(
            id='query-mode',
            className='row',
            options=[
                { 'label': 'Words', 'value': 'words' },
                { 'label': 'Lemmas', 'value': 'lemmas' }
            ],
            value='words'
        ),
    ]),
    html.Div(className='row',children=[        
        html.P(className='light-gray bold small-caps', children='type'),
        dcc.RadioItems(
            id='query-type',
            className='row',
            options=[
                { 'label': 'AND', 'value': 'and' },
                { 'label': 'OR', 'value': 'or' },
                { 'label': 'BOTH', 'value': 'both' }
            ],
            value='and'
        ),
    ])
])



header  = html.Header([
    html.Div(className='row',children=[
        html.H3('NLP Project 21.'),
        html.H6(className='light-gray',children='Finnish Slang. Dynamic Distribution')
    ]),
    html.Div(className='divider'),
    html.Div(className='row',children=[
        html.H5(className='light-gray small-caps', children='search word(s):'),
        dcc.Input(id='search-input',value='magee',placeholder='Find...', type='text'),
        html.Button(id='search-button',children='Search',type='submit')
    ]),
    html.Div(className='divider'),
    queryRadios,
    html.Div(className='divider'),
    authors,
    html.Div(className='divider'),
    html.Div(className='row',children=[
        html.P(className='light-gray bold small-caps', children='Powered by:'),
        html.A(className='blue',children='korp.csc.fi',href='http://korp.csc.fi',target='_blank'),
        html.A(className='blue',children='nltk.org',href='http://nltk.org',target='_blank'),
    ])
    
    # Finnish Slang. Dynamic Distribution')
])
