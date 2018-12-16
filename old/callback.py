# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
import plotly.graph_objs as go
from corpus import trend
import calendar
import time
import json


def to_figure(my_data):
    res             = dict(
        x=[],
        y=[],
        type=my_data['type'],
        name=my_data['query']
    )

    rows                = my_data['data']

    for row in rows:
        label           = row
        value           = rows[row]
        if value is None:
            value = 0

        if label is not '':
            res['x'].append(label)
            res['y'].append(value)

    return [res]


def to_table(my_data):

    res             = []

    rows                = my_data['data']

    for row in rows:
        label           = row
        value           = rows[row]
        if value is None:
            value = 0

        if label is not '':
            res.append({ 'year': label, 'count': value })

    return res

        



def createFigure(data, query, xaxis_type='Linear', yaxis_type='Linear'):


    return dict(
        data=data,
        layout=go.Layout(
            #title= 'Word "{}" birth-death process vs. time'.format(query),
            xaxis={
                'title': 'Time',
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': 'Word occurence',
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest',
        )
        
    )




def init(app):


    @app.callback(
        Output('intermediate-value', 'children'),
        [],
        [State('search-input', 'value'),
        State('search-select','values')],
        [Event('search-button', 'click')]
    )
    def clear_data(query, select_values):
        if len(query) > 3:
            print('Loading data for word {}'.format(query))
            
            data                    = trend.trendData(query, select_values)
            data['query']            = query

            print('Load done')

            return str(data)
        
    @app.callback(
        Output('graph-title','children'),
        [Input('intermediate-value', 'children')]
    )
    def update_title(data_str):
        if data_str == None:
            return []

        data                = eval(data_str)
        if data['sum'] == 0:
            return 'No data for word "{}"'.format(data['query'])
        
        return 'Found {} hit(s) for word "{}"'.format(data['sum'], data['query'])


        
    @app.callback(
        Output('results-div','style'),
        [Input('intermediate-value', 'children')]
    )
    def show_results(data_str):
        if data_str == None:
            return { 'display': 'none' }

        return { 'display': 'block' }




    @app.callback(
        Output('loading-text','children'),
        [],
        [],
        [Event('search-button', 'click')]
    )
    def manipulate_loading():

        return 'Querying from corpus, please wait...'


        
    @app.callback(
        Output('loading-text','style'),
        [Input('intermediate-value', 'children')]
    )
    def show_loading(data_str):
        if data_str == None:
            return { 'display': 'block' }

        return { 'display': 'none' }
        





    @app.callback(
        Output('table-title','children'),
        [Input('intermediate-value', 'children')]
    )
    def update_table_title(data_str):
        if data_str == None:
            return []

        data                = eval(data_str)

        if data['sum'] == 0:
            return 'No data for word "{}"'.format(data['query'])
        
        return 'Word "{}" frequency listed into the table view'.format(data['query'])



    @app.callback(
        Output('query-table', 'data'),
        [Input('intermediate-value', 'children')]
    )
    def update_table(data_str):
        if data_str == None:
            return []

        data                = eval(data_str)

        return to_table(data)


    @app.callback(
        Output('birth-death-graph', 'figure'),
        [Input('intermediate-value', 'children')]
    )
    def update_graph(data_str):
        if data_str == None:
            return {}
        
        data                = eval(data_str)

        data['type']        = 'line'

        return createFigure(to_figure(data), data['query'])

