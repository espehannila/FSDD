# -*- coding: utf-8 -*-
import dash
import dash_html_components as html


authors  = html.Div(className='row small-caps', children=[
    html.P(className='light-gray bold', children='authors:'),
    html.Div(className='divider'),
    html.P('Esa Hannila'),
    html.P('Tuomas Tuokkola'), 
    html.P('Tuomas Koivuaho'),
    html.P('Santeri Matero'),
    html.P('Mauri Miettinen'),
    html.P('Oona Kivelä')
])