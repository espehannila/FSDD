# -*- coding: utf-8 -*-
import pymongo
#from word import Word

def connect(url='mongodb://localhost:27017'):
    print('Connecting to the mongodb database')
    
    client          = pymongo.MongoClient(url)
    conn            = client.FSDD

    return conn
'''
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

# Lists all documents
def documentList(conn = None):
    if conn is None: conn = connect()
    collection      = conn.documents

    return collection.find()


'''




'''
# Add word to database
def addWord(word, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    print('Adding word "%s" into database' % word.text)

    return collection.insert_one({ 'text': word.text, 'docs': word.docs })
    
# Remove word from database
def removeWord(word, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    collection.remove({ 'text': word.text })

# Lists all words
def wordList(query, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    words           = []

    for w in collection.find(query):
        print(w)
        word = Word(w['text'])
        if 'docs' in w:
            word.docs       = w['docs']

        words.append(word)

    return words

# Update word in database
#def updateWord(word, conn = None):
    #if conn is None: conn = connect()
    #collection      = conn.words

    #collection.update_one({ 'text': word['text'] }, { '$inc': { docsword)

# Replaces word in database
def replaceWord(word, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    collection.replace_one({ 'text': word.text }, word.toBSON())

# Find word from database
def findWord(word, conn = None):
    if conn is None: conn = connect()
    collection      = conn.words

    bsonWord        = collection.find_one({ 'text': word.text })

    print('Found word', bsonWord['text'])

    return Word.fromBSON(bsonWord)
    
# Returns true if word exists, otherwise false
def wordExist(word, conn = None):
    found           = findWord(word, conn)

    if found is not None:
        return True
    else:
        return False
'''










# Add sentence to database
def addSentence(sent, conn = None):
    if conn is None: conn = connect()
    collection      = conn.sentences

    return collection.insert_one(sent)

# Remove sentence from database
def removeSentence(sent, conn = None):
    if conn is None: conn = connect()
    collection      = conn.sentences

    collection.remove({ 'text': sent })
