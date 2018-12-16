# -*- coding: utf-8 -*-
import requests
import json
from .korplib import parse


command                 = 'count_time'
default_within          = 'sentence'


def load(url):
    return requests.get(url).content

def byWord(word, corpusArr):
    corpus              = parse(corpusArr)

    cqp                 = "[lemma='{}']".format(word)#"%5Blemma+%3D+%22{}%22%5D".format(word)
    url                 = 'https://korp.csc.fi/cgi-bin/korp.cgi?command={}&cqp={}&corpus={}&indent=2'.format(command, cqp, corpus)
    content             = load(url)
    jsondata            = json.loads(content)
    return jsondata

def trendData(word, corpusArr=['S24']):
    jsondata            = byWord(word, corpusArr)
    if 'ERROR' in jsondata:

        print(jsondata)
        return { 'data': [] }

    data                = jsondata['combined']['absolute']
    sums                = jsondata['combined']['sums']['absolute']

    #data.pop(1)
    #data.shift(1)

    return { 'data': data, 'sum': sums }

if __name__ == "__main__":
    word                = 'suomi'
    jsondata            = trendData(word)
    print('Requesting data from korp.csc.fi\nWord:{}'.format(word))