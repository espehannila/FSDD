# -*- coding: utf-8 -*-
import nltk
from gensim.models import Word2Vec
from stopwords import stopwords

print('Loading Application')

doc1        = "Jokin meni nyt vikaan"
doc2        = "Ei tämä toiminut ollenkaan oikein"
doc3        = "Toivottavasti tämä toimisi nyt oikein"


# Text Processing
# Text processing chain
# 1. tokenization
# 2. filtering
# 3. stopwords handling
# 4. tokenization
# 5. lemmatization
# 6. building dictionary

# Parsing
# Information retrieval (building model, scoring function)
# Sentiment Analysis
# Summarization
# Comparison, discussions with alternatives
# GUI interface


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