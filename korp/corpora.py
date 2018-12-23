# -*- coding: utf-8 -*-
from .config import *
from .query import KorpQuery
import requests
import json
import nltk

class Sentence:

    def __init__(self, json, queryWord):
        self.name           = json['corpus']
        self.sentence_id    = json['structs']['sentence_id']
        self.date           = json['structs']['text_date']
        self.time           = json['structs']['text_time']
        self.title          = json['structs']['text_title']
        self.urlBoard       = json['structs']['text_urlboard']
        self.urlMsg         = json['structs']['text_urlmsg']
        self.tokens         = json['tokens']
        self.queryWord      = queryWord

    def toString(self):
        return ' '.join([word['word'] for word in self.tokens if word['word'] is not None])

    def getWords(self):
        return [token['word'] for token in self.tokens]

    def getLemmas(self):
        return [token['lemma'] for token in self.tokens]

    def getPosTags(self):
        return [token['pos'] for token in self.tokens]



    # Return bigrams
    def bigrams(self):
        return nltk.bigrams(self.getWords())

    # Returns index array of query word(s)
    def queryIndexes(self, words):
        return [index for index, item in enumerate(self.getWords()) if item in words]

    # Returns pos by words
    def getTokensByWords(self, words):
        return [self.tokens[index] for index in self.queryIndexes(words)]

    def getPosByWords(self, words):
        return [self.getPosTags()[index] for index in self.queryIndexes(words)]

    def prevBigrams(self):
        return [bigram for bigram in self.bigrams() if self.queryWord == bigram[1]]

    def nextBigrams(self):
        return [bigram for bigram in self.bigrams() if self.queryWord == bigram[0]]

    def prevOccurrenceWords(self):
        return [bigram[0] for bigram in self.prevBigrams()]

    def mextOccurrenceWords(self):
        return [bigram[1] for bigram in self.nextBigrams()]

    def year(self):
        dateArr         = self.date.split('.')
        if len(dateArr) == 1:
            return dateArr[0]
        elif len(dateArr) == 2:
            return dateArr[1]
        elif len(dateArr) == 3:
            return dateArr[2]
        
    # Returns nearby words
    def nearbyData(self):

        # Find next and prev words from query word
        prevWords           = self.prevOccurrenceWords()
        nextWords           = self.mextOccurrenceWords()
        
        prevTokens          = self.getTokensByWords(prevWords)
        nextTokens          = self.getTokensByWords(nextWords)

        prevPos             = self.getPosByWords(prevWords)
        nextPos             = self.getPosByWords(nextWords)        

        nearby              = { 
            'year': self.year(), 
            'date': self.date, 
            'time': self.time, 
            'words': { 
                'prev': prevWords, 
                'next': nextWords 
            }, 
            'tokens': { 
                'prev': prevTokens, 
                'next': nextTokens 
            },
            'pos': {
                'prev': prevPos,
                'next': nextPos
            }
        }

        return nearby




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
    def freqDist(self, query):

        if type(query) is not KorpQuery:
            print('Invalid query type, use korp.query.KorpQuery')
            exit(1)
    
        url                 = self.cqpUrl('count_time', query.toURL())
        print('Loading from %s' % url)
        content             = self.load(url)

        jsonContent         = json.loads(content)

        return { 'query': query, 'results': jsonContent['combined'] }, None

    # Loads nearby words for queried word from korp.csc.fi
    def partOfSpeech(self, query):

        if type(query) is not KorpQuery:
            print('Invalid query type, use korp.query.KorpQuery')
            exit(1)

        url                 = self.cqpUrl('query', query.toURL())
        url                 += '&defaultWithin=sentence&show=sentence,pos,lemma&start=0&end=10&indent=2'
        url                 += '&show_struct=text_title,text_date,text_time,text_sect,text_sub,text_user,sentence_id,text_urlmsg,text_urlboard'
        print('Loading from %s' % url)
        content             = self.load(url)

        jsonContent         = json.loads(content)

        corpArr             = [Sentence(corp, query.getWord()) for corp in jsonContent['kwic']]

        return { 'query': query, 'results': corpArr }, None
    
    # Convert tuple array to frequency distribution array
    def tuple2freqDist(self, arr):
        fDist           = nltk.FreqDist(arr)

        # convert to { value, yearsArr, countsArr }

        # TODO: Fix this code to properly concat values

        '''print(fDist.items())

        seen            = []
        res             = []

        for tup, count in fDist.items():
            val         = tup[1]
            year        = tup[0]
            indexArr    = [index for index in enumerate(seen) if seen[index] == val]
            if len(indexArr) > 0:
                for index in indexArr:
                    res[index]['years'].append(year)
                    res[index]['values'].append(val)
            else:
                res.append({ 'years': [year], 'value': val, 'counts': [count] })
                seen.append(val)

        print(res)'''


        return [{ 'year': tup[0], 'value': tup[1], 'count': count} for tup, count in nltk.FreqDist(arr).items()]


    # Loads co-occurring words from korp.csc.fi
    def coOccurrence(self, query):

        if type(query) is not KorpQuery:
            print('Invalid query type, use korp.query.KorpQuery')
            exit(1)

        res, err            = self.partOfSpeech(query)

        if err is not None:
            return None, err

        sents               = res['results']

        print('Number of sentences', len(sents))

        prevWords           = []
        nextWords           = []
        prevTags            = []
        nextTags            = []

        prevOcc             = []
        nextOcc             = []
        prevPos             = []
        nextPos             = []


        # Concat sentences nearby datas
        for sent in sents:

            nearbyData      = sent.nearbyData()
            year            = nearbyData['year']

            # Get words
            words           = nearbyData['words']
            prevWords       += words['prev']
            nextWords       += words['next']

            # Get pos tags
            pos             = nearbyData['pos']
            prevTags        += pos['prev']
            nextTags        += pos['next']


            # Generate array of word(s) with year
            prevOcc         += [(year, word) for word in prevWords]
            nextOcc         += [(year, word) for word in nextWords]

            # Generate array of tag(s) with year
            prevPos         += [(year, tag) for tag in prevTags]
            nextPos         += [(year, tag) for tag in nextTags]

        # Sum similar co-occurrences together
        res                 = { 
            'results': {
                'fDist': {
                    'words': {
                        'prev': self.tuple2freqDist(prevOcc),
                        'next': self.tuple2freqDist(nextOcc),
                    },
                    'pos': {
                        'prev': self.tuple2freqDist(prevPos),
                        'next': self.tuple2freqDist(nextPos)
                    }
                },
                'words': {
                    'prev': prevWords,
                    'next': nextWords
                },
                'tags': {
                    'prev': prevTags,
                    'next': nextTags
                }
            }
        }
        return res, None


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

    @staticmethod
    def sentArr2sent(arr):
        return ' '.join([word['word'] for word in arr])