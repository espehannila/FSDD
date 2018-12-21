from . import db
from .db_object import DbObject




class Word(DbObject):

    text        = ''

    def __init__(self, text, doc=None, conn=None):
        self.text   = text
        self.docs   = []
        self.conn   = conn
        if doc is not None:
            self.inDocument(doc)

    
    # Stores word to the database
    def save(self):
        print('Saving word "%s"' % self.text)
        
        if Word.exist(self.text):
            self.replace()
        else:
            self.insert()
        

    # Replaces word in the database
    def replace(self):
        coll            = Word.collection(self.conn)
        coll.replace_one({ 'text': self.text }, self.toBSON())


    # Inserts word to the database
    def insert(self):
        coll            = Word.collection(self.conn)
        coll.insert_one(self.toBSON())

    # Convert object to BSON format
    def toBSON(self):
        return { 'text': self.text, 'docs': self.docs }

    # Add document to the word
    def inDocument(self, doc):

        exist       = False

        for dbDoc in self.docs:
            if dbDoc['_id'] is doc._id:
                dbDoc['count'] += 1
                exist       = True
                print('Matching document found')
            
        if not exist:
            DBdoc       = { '_id': doc._id, 'year': doc.year, 'count': 1 }
            self.docs.append( DBdoc )



    @staticmethod
    def collection(conn=None):
        if conn is None: conn = db.connect()
        return conn.words


    @staticmethod
    def findOne(query, conn=None):
        coll            = Word.collection(conn)
        bsonWord        = coll.find_one(query)
        if bsonWord is None:
            return None

        return Word.fromBSON(bsonWord)

    @staticmethod
    def exist(text='', conn=None):
        word            = Word.findOne({ 'text': text })
        if word is None:
            return False
        else:
            return True


    @staticmethod
    def find(query={}, conn=None):
        coll            = Word.collection(conn)
        words           = []

        for w in coll.find(query):
            word        = Word.fromBSON(w)
            words.append( word )

        return words

    @staticmethod
    def fromBSON(bsonWord):
        word        = Word('')
        if 'text' in bsonWord:
            word.text       = bsonWord['text']
        if 'docs' in bsonWord:
            word.docs       = bsonWord['docs']
        if '_id' in bsonWord:
            word._id        = bsonWord['_id']

        return word


    @staticmethod
    def removeOne(query, conn=None):
        coll                = Word.collection(conn)
        return coll.remove(query)



    @staticmethod
    def inDocumentArray(word, doc):

        return word
        

    @staticmethod
    def concat(words, word, doc):
        print('Concatting word array')

        [Word.inDocumentArray(w, word, doc) for w in words]

        return words