# -*- coding: utf-8 -*-
from .config import *
import requests
import json
from .corpora import Corpora
from .query import KorpQuery

'''
# Returns available corporas as an array
def corporas(query=None):
    content             = requests.get(INFO_URL).content

    jsonContent         = json.loads(content)

    if 'corpora' in jsonContent:
        if query is not None:
            return [corp for corp in jsonContent['corpora'] if [c for c in query if c in corp] ]
        else:
            return [corp for corp in jsonContent['corpora']]
    else:
        return []


def count_time(query):

    corpora             = Corpora(['S24'])

    return corpora.count_time(query.toURL())

def co_occurence_words(query):

    corpora             = Corpora(['S24'])

    corpora.sentences(query.toURL())
'''