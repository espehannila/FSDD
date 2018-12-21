class KorpQuery:

    def __init__(self, word=None, lemma=None, co_occurring=None, lemmacomp=None, pos=None, msd=None, ref=None, dephead=None, deprel=None):
        self.word           = word
        self.lemma          = lemma
        self.lemmacomp      = lemmacomp
        self.pos            = pos
        self.msd            = msd
        self.ref            = ref
        self.dephead        = dephead
        self.deprel         = deprel
        self.co_occurring   = co_occurring

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
            

        return query