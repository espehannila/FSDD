# -*- coding: utf-8 -*-
import nltk
from gensim.models import Word2Vec
from korp.stopwords import stopwords
from database import db
from database.word import Word
from database.document import Document
from korp.corpora import Corpora
from korp.query import KorpQuery
from ui.app import app
bigram_measures = nltk.collocations.BigramAssocMeasures()

app.run_server(debug=True)

def wordTrend():

    query           = KorpQuery(word='magee')
    corpora         = Corpora(['S24'])
    res, err        = corpora.freqDist(query)

    if err is not None:
        print('Error occurred', err)
        exit(1)
    
    print(res)



def coOccurringTrend():

    query           = KorpQuery(co_occurring=['suuri', 'yritys'])
    corpora         = Corpora(['S24'])
    res, err        = corpora.freqDist(query)


    if err is not None:
        print('Error occurred', err)
        exit(1)

    print(res)



def partOfSpeech():

    query           = KorpQuery(word='testi')
    corpora         = Corpora(['S24'])
    res, err        = corpora.partOfSpeech(query)


    if err is not None:
        print('Error occurred', err)
        exit(1)

    [print('\nsentence', sent) for sent in res['res']]
    


def coOccurrence():

    query           = KorpQuery(word='testi')
    corpora         = Corpora(['S24'])
    res, err        = corpora.coOccurrence(query)


    if err is not None:
        print('Error occurred', err)
        exit(1)
    
    print(res)

#wordTrend()
#coOccurringTrend()
#partOfSpeech()
#coOccurrence()