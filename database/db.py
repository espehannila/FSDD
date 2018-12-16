# -*- coding: utf-8 -*-
import pymongo

def connect(url='mongodb://localhost:27017'):
    print('Connecting to the mongodb database')
    
    client          = pymongo.MongoClient(url)
    conn            = client.FSDD

    return conn

# Adds document to database
def addDocument(doc, conn = None):
    if conn is None: conn = connect()
    collection      = conn.documents

    collection.insert_one(doc)

    return

# Removes document from database
def removeDocument(doc, conn = None):
    if conn is None: conn = connect()
    collection      = conn.documents

    collection.remove(doc)

# Add word to database
def addWord(word, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    return collection.insert_one(word)

# Update word in database
#def updateWord(word, conn = None):
    #if conn is None: conn = connect()
    #collection      = conn.words

    #collection.update_one({ 'text': word['text'] }, { '$inc': { docsword)

def replaceWord(word, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    collection.replace_one({ 'text': word['text'] }, word)

# Find word from database
def findWord(word, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    return collection.find_one({ 'text': word['text'] })
    
# Remove word from database
def removeWord(word, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    collection.remove({ 'text': word })
    
# Returns true if word exists, otherwise false
def wordExist(word, conn = None):
    found           = findWord(word, conn)

    if found is not None:
        return True
    else:
        return False



