# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html


footer  = html.Footer([
    
    html.Div(children=[
        html.H6(children='Project 21: Finnish Slang. Dynamic Distribution'),
        html.P('Esa Hannila, Tuomas Tuokkola, Tuomas Koivuaho, Santeri Matero, Mauri Miettinen, Oona Kivelä'),
        html.A(href='https://korp.csc.fi', target='blank', children='Powered by korp.csc.fi')
    ]),
    #html.A(href='https://newsapi.org',children='Powered by newsapi.org')
])