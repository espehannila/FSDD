# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, Event
import plotly.graph_objs as go
import nltk
from korp.corpora import Corpora
from korp.query import KorpQuery


class QueryParser:

    def __init__(self, input, mode, qType):
        self.input          = input
        self.tokens         = nltk.word_tokenize(input)
        self.mode           = mode
        self.qType          = qType

    def query(self):
        if self.mode == 'lemmas':
            return KorpQuery(lemmas=self.tokens, qType=self.qType)

        elif self.mode == 'words':
            return KorpQuery(words=self.tokens, qType=self.qType)





class DataParser:

    def __init__(self, data_str):
        print('Parsing data')
        self.data           = eval(data_str)

    def none2zero(self, val):
        if val is None:
            return 0
        return val

    def query(self):
        return self.data['query']

    def freqDistData(self):

        # Get data
        freqDist            = self.data['freqDist']
        absolute            = freqDist['absolute']

        # Convert dict to
        xy                  = [(key, self.none2zero(absolute[key])) for key in absolute if key != '']

        # Sort frequency data
        xy.sort(key=lambda tup: tup[0])

        # Load x and y arrays
        x                   = [tup[0] for tup in xy]
        y                   = [tup[1] for tup in xy]

        # Return chart data
        return [
            go.Scatter(
                x=x,
                y=y,
                name=self.query(),
                mode='lines+markers'
            )
        ]

    def contextEvolutionData(self):
        # Get data
        data                = self.data['sentenceLengths']
        xy= []
        for i in data:
            xy.append((i, data[i]))
        xy.sort()

        # Load x and y arrays
        x                   = [tup[0] for tup in xy]
        y                   = [tup[1] for tup in xy]

        # Return chart data
        return [
            go.Scatter(
                x=x,
                y=y,
                name="Sentence length",
                mode='lines+markers'
            )
        ]

    # Create scatter
    def Scatter(self, val):
        return go.Scatter(
            name=val['value'],
            x=[tup[0] for tup in val['absolute']],
            y=[tup[1] for tup in val['absolute']],
            #marker=dict(
            #    symbol='circle'
            #),
            mode='lines+markers'
        )

    def coWordData(self):

        # Get data
        data                = self.data['coOccurrences']
        fDist               = data['fDist']
        #prevWords           = data['words']['prev']
        p = CoWordParser()
        for word in fDist['words']['prev']:
            p.add(self.Scatter(word))


        # scatters            = [ self.Scatter(word) for word in fDist['words']['prev']]
        scatters = p.scatters
        return scatters

class CoWordParser(object):
    def __init__(self, counts=5):
        self.scatters = []
        self.appearances = []
        self.min = 0
        self.counts = counts
    def add(self,scatter):
        appearance = sum(scatter.y)
        if len(self.scatters) < self.counts:
            self.scatters.append(scatter)
            self.appearances.append(appearance)
            self.min = min(self.appearances)
            return
        if appearance > self.min:
            i = self.appearances.index(self.min)
            self.scatters.pop(i)
            self.appearances.pop(i)
            self.scatters.append(scatter)
            self.appearances.append(appearance)
            self.min = min(self.appearances)
            return
        if  len(self.scatters) > self.counts:
            print('bug')
            
def init(app):
    print('Initializing application functionalities')

    corpora                 = Corpora(['S24'])


    @app.callback(
        Output('frequency-distribution', 'figure'),
        [Input('intermediate-value', 'children')]
    )
    def updateFreqDist(data_str):

        if data_str is None:
            return go.Figure(layout=dict(title='Frequency distribution'))

        # Create data parser
        parser              = DataParser(data_str)

        return go.Figure(
            layout=dict(
                title='Frequency distribution',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            ),
            data=parser.freqDistData()
        )



    @app.callback(
        Output('context-evolution', 'figure'),
        [Input('intermediate-value', 'children')]
    )
    def updateContextEvolution(data_str):

        if data_str is None:
            return go.Figure(layout=dict(title='Context evolution'))

        # Create data parser
        parser              = DataParser(data_str)

        return go.Figure(
            layout=dict(
                title='Context evolution',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            ),
            data=parser.contextEvolutionData()
        )

    @app.callback(
        Output('co-occurring-words', 'figure'),
        [Input('intermediate-value', 'children')]
    )
    def updateCoOccurringWords(data_str):

        if data_str is None:
            return go.Figure(layout=dict(title='Co-Occurring words'))

        # Create data parser
        parser              = DataParser(data_str)

        print('Parsing co occurring data')
        data                = parser.coWordData()
        print('Parsed co occurring data')

        return go.Figure(
            layout=dict(
                title='Co-Occurring words',
                showlegend=True,
                legend=go.layout.Legend(
                    x=0,
                    y=1.0
                ),
                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
            ),
            data=data
        )







    @app.callback(
        Output('intermediate-value', 'children'),
        [],
        [
            State('search-input', 'value'),
            State('query-mode','value'),
            State('query-type','value')
        ],
        [Event('search-button', 'click')]
    )
    def clear_data(input, mode, qType):

        parser              = QueryParser(input, mode, qType)

        query               = parser.query()

        print('Query', query.toURL())

        freqRes, err        = corpora.freqDist(query)

        if err is not None:
            print('Error occurred', err)
            return str({
                'query': query.toString(),
                'freqDist': None,
                'coOccurrence': None
            })


        coRes, lengthRes, err          = corpora.coOccurrence(query)

        return str({
            'query': query.toString(),
            'freqDist': freqRes['results'],
            'coOccurrences': coRes['results'],
            'sentenceLengths': lengthRes,
        })
