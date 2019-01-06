import nltk
from bson.objectid import ObjectId
from .word import Word
from . import db
from .db_object import DbObject
from korp.finnpos import finnpos
#from finnpos.bin import omorfi2finnpos as finnpos
#import finnpos

# cp data/ftb/freq_words share/finnpos/ftb_omorfi_model


def f(word, text, doc):
    if word.text == text:
        for wDoc in word.docs:
            if wDoc['_id'] == doc._id:
                wDoc['count']  += 1
    return word


class Sentence:

    text        = ''
    year        = None

    def __init__(self, text, year=None, conn=None):
        self._id            = ObjectId()
        self.text           = text
        self.conn           = conn
        self.year           = year


    def tags(self):
        return finnpos.partOfSpeech(self.text)



class Document:
    
    text        = ''
    year        = None

    def __init__(self, text, year=None, conn=None):
        self._id            = ObjectId()
        self.text           = text
        self.conn           = conn
        self.year           = year

        

    
    # Stores word to the database
    def save(self):
        print('Saving document "%s"' % self.text)
        
        if Document.exist(self.text):
            self.replace()
        else:
            self.insert()
        

    # Replaces document in the database
    def replace(self):
        coll            = Document.collection(self.conn)
        coll.replace_one({ 'text': self.text }, self.toBSON())


    # Inserts document to the database
    def insert(self):
        coll            = Document.collection(self.conn)
        coll.insert_one(self.toBSON())



    # Convert object to BSON format
    def toBSON(self):
        return { 'text': self.text, 'year': self.year }


    # Return tokenized words
    def tokenize(self):
        return nltk.word_tokenize(self.text, language='finnish')


    # Returns unique words
    def words(self):
        words       = []

        for text in self.tokenize():
            word    = Word(text=text, doc=self)
            words   = Word.concat(words, word)
            
        words.sort(key=lambda x: x.text)
        return words

    # Returns reference dict for the word
    def reference(self):
        return { '_id': self._id, 'count': 1 }


    # Returns document lemmas
    def tags(self):
        return finnpos.partOfSpeech(self.text)

    # Returns document sentences with lemmas
    def sentences(self):
        sents       = nltk.sent_tokenize(self.text)
        return [Sentence(sent, year=self.year) for sent in sents]
        
    @staticmethod
    def collection(conn=None):
        if conn is None: conn = db.connect()
        return conn.documents


    @staticmethod
    def findOne(query, conn=None):
        coll            = Document.collection(conn)
        bsonWord        = coll.find_one({ 'text': { '$regex': query['text'] } })
        if bsonWord is None:
            return None

        return Document.fromBSON(bsonWord)

    @staticmethod
    def exist(text='', conn=None):
        doc            = Document.findOne({ 'text': text })
        if doc is None:
            return False
        else:
            return True


    @staticmethod
    def find(query={}, conn=None):
        coll            = Document.collection(conn)
        docs            = []

        for w in coll.find(query):
            doc         = Document.fromBSON(w)
            docs.append( doc )

        return docs

    @staticmethod
    def fromBSON(bsonDoc):
        doc             = Document('')
        if 'year' in bsonDoc:
            doc.year        = bsonDoc['year']
        if 'text' in bsonDoc:
            doc.text        = bsonDoc['text']
        if '_id' in bsonDoc:
            doc._id         = bsonDoc['_id']

        return doc


    @staticmethod
    def removeOne(query, conn=None):
        coll                = Document.collection(conn)
        return coll.remove({ 'text': { '$regex': query['text'] } })