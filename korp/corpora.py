# -*- coding: utf-8 -*-
from .config import *
from .query import KorpQuery
import requests
import json

class Corpora:

    # Default constructor
    def __init__(self, selection):
        self.corps              = Corpora.corporas(selection)

    # Generates corpus url
    def getUrl(self):
        return '{0}?corpus={1}'.format(URL, ','.join(self.corps))

    # Generates command url
    def commandUrl(self, cmd):
        return '{0}&command={1}'.format(self.getUrl(), cmd)

    # Generates cqp url
    def cqpUrl(self, cmd, query):

        print('Querying from %a' % self.corps)

        url      = '{0}&cqp={1}'.format( self.commandUrl( cmd ), query )
        return url

    # Loads content from requested url
    def load(self, url):
        return requests.get(url).content
        
    # Loads trend data from korp.csc.fi
    def count_time(self, query):

        if type(query) is not KorpQuery:
            print('Invalid query type, use korp.query.KorpQuery')
            exit(1)
    
        url                 = self.cqpUrl('count_time', query.toURL())
        print('Loading from %s' % url)
        content             = self.load(url)

        jsonContent         = json.loads(content)

        return { 'query': query, 'res': jsonContent['combined'] }, None

    # Loads nearby words for queried word from korp.csc.fi
    def partOfSpeech(self, query):

        if type(query) is not KorpQuery:
            print('Invalid query type, use korp.query.KorpQuery')
            exit(1)

        url                 = self.cqpUrl('query', query.toURL())
        url                 += '&defaultWithin=sentence&show=sentence,pos&start=0&end=24'
        print('Loading from %s' % url)
        content             = self.load(url)

        jsonContent         = json.loads(content)
        
        sentArr             = [sent['tokens'] for sent in jsonContent['kwic']]
        sents               = [sentArr2sent(sent) for sent in sentArr]

        return { 'query': query, 'res': sentArr }, None


    # Loads co-occurring words from korp.csc.fi
    def coOccurrence(self, query):

        if type(query) is not KorpQuery:
            print('Invalid query type, use korp.query.KorpQuery')
            exit(1)

        res, err            = self.partOfSpeech(query)

        wordArr             = []

        # Iterate each sentences
        for sent in res['res']:

            # Iterate each word in sentence
            for i in range(0, len(sent) ):
                word            = sent[i]

                # TODO: IMPROVE THIS PART WITH GENSIM????

                if word['word'] in query.toURL():
                    print(i, word)

                    if i == 0 and i < len(sent):
                        wordArr.append({
                            'center': sent[i],
                            'right': sent[i+1]
                        })

                    elif i > 0 and i == len(sent):
                        wordArr.append({
                            'left': sent[i-1],
                            'center': sent[i]
                        })

                    elif i > 0 and i < len(sent):
                        wordArr.append({
                            'left': sent[i-1],
                            'center': sent[i],
                            'right': sent[i+1]
                        })

        return wordArr, err


    @staticmethod
    def corporas(query):
        content             = requests.get(INFO_URL).content

        jsonContent         = json.loads(content)

        if 'corpora' in jsonContent:
            if query is not None:
                return [corp for corp in jsonContent['corpora'] if [c for c in query if c in corp] ]
            else:
                return [corp for corp in jsonContent['corpora']]
        else:
            return []


def sentArr2sent(arr):
    return ' '.join([word['word'] for word in arr])