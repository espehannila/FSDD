# -*- coding: utf-8 -*-
import dash_html_components as html

from .header import header
from .freq_dist import freqGraph
from .context_evolution import contextGraph
from .co_occurring_words import coOccurringWordsGraph, nextCoOccurringWordsGraph
from .co_occurring_evolution import coOccurringEvolutionGraph
from .tables import summary, totalCoOccurrence

layout  = html.Div(className='grid',children=[
    html.Div(className='row',children=[
        header,
        freqGraph
    ]),
    
    html.Div(className='row',children=[
        contextGraph,
        coOccurringWordsGraph,
        nextCoOccurringWordsGraph,
        coOccurringEvolutionGraph
    ]),
    
    html.Div(className='row',children=[
        summary,
        totalCoOccurrence
    ]),
    html.Div(id='intermediate-value')
    #footer
    
   
])