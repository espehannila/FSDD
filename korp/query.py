class KorpQuery:

    def __init__(self, word=None, lemma=None, co_occurring=None, words=None, lemmas=None, lemmacomp=None, pos=None, msd=None, ref=None, dephead=None, deprel=None, qType='and'):
        self.word           = word
        self.lemma          = lemma
        self.lemmacomp      = lemmacomp
        self.pos            = pos
        self.msd            = msd
        self.ref            = ref
        self.dephead        = dephead
        self.deprel         = deprel
        self.co_occurring   = co_occurring
        self.words          = words
        self.lemmas         = lemmas
        self.qType          = qType


    def getWords(self):
        if self.words is not None:
            return self.words
        elif self.lemmas is not None:
            return self.lemmas
        else:
            return []

    def getWord(self):
        if self.words is not None:
            return self.words[0]
        elif self.lemmas is not None:
            return self.lemmas[0]
        else:
            return self.word


    # Convert query to string
    def toString(self):

        joinStr             = ' %s ' % self.qType
        
        if self.words:
            return '[%s]' % joinStr.join(self.words)

        elif self.lemmas:
            return '[%s]' % joinStr.join(self.lemmas)

        elif self.word:
            return '[%s]' % self.word

        elif self.lemma:
            return '[%s]' % self.lemma

        

    # Convert query object to url query
    def toURL(self):
        
        # Parse word query
        if self.word is not None:
            query           = "[word='%s']" % self.word

        # Parse lemma query
        if self.lemma is not None:
            query           = "[lemma='%s']" % self.lemma

        # Parse co occurring cqp query
        if self.co_occurring is not None:
            query           = "[lemma='{0}'] []* [lemma='{1}']".format( self.co_occurring[0], self.co_occurring[1] )

        # Parse lemma array cqp query
        if self.lemmas is not None:
            queryStr        = ["[lemma='%s']" % lemma for lemma in self.lemmas]
            if self.qType == 'and':
                query           = ' '.join(queryStr)
            elif self.qType == 'or':
                query           = ' | '.join(queryStr)
            elif self.qType == 'both':
                query           = ' []* '.join(queryStr)


        # Parse word array cqp query
        if self.words is not None:
            queryStr        = ["[word='%s']" % word for word in self.words]
            if self.qType == 'and':
                query           = ' '.join(queryStr)
            elif self.qType == 'or':
                query           = ' | '.join(queryStr)
            elif self.qType == 'both':
                query           = ' []* '.join(queryStr)

        return query