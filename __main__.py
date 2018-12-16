# -*- coding: utf-8 -*-
import nltk
from gensim.models import Word2Vec
from stopwords import stopwords
import datetime

print('Loading Application')

doc1        = "Jokin meni nyt vikaan"
doc2        = "Ei tämä toiminut ollenkaan oikein"
doc3        = "Toivottavasti tämä toimisi nyt oikein"



def doc2db(doc):

    # Remove stopwords
    doc                 = stopwords.remove(doc)

    # Stem document
    

    # Tokenize document
    doc_tokens          = nltk.word_tokenize(doc, language='finnish')

    

    print(doc_tokens)


# Tokenize the documents
doc2db(doc1)
doc2db(doc2)
doc2db(doc3)