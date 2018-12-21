
def strArr2Tuple(val):
    valArr = val.replace('[','').replace(']','').split('=')
    return (valArr[0],valArr[1])

class Tag:

    def __init__(self, text, lemma='', pos='', num='', case='', subcat='', mood='', pers='', voice='', conj='', proper='', pcp='', tense='', inf='', neg='', poss='', position='', clit='', cmp=''):
        self.text       = text
        self.lemma      = lemma
        self.pos        = pos
        self.num        = num
        self.case       = case
        self.subcat     = subcat
        self.mood       = mood
        self.pers       = pers
        self.voice      = voice
        self.conj       = conj
        self.proper     = proper
        self.pcp        = pcp
        self.tense      = tense
        self.inf        = inf
        self.neg        = neg
        self.poss       = poss
        self.position   = position
        self.clit       = clit
        self.cmp        = cmp

    def toString(self):
        return '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}'.format(
            self.text,
            self.lemma,
            self.pos,
            self.num,
            self.case,
            self.subcat,
            self.mood,
            self.voice,
            self.pers,
            self.conj,
            self.proper,
            self.pcp,
            self.tense,
            self.inf,
            self.neg,
            self.poss,
            self.position,
            self.clit,
            self.cmp
        )

    def setTag(self, key, value):
        if key == 'POS':
            self.pos         = value
        elif key == 'NUM':
            self.num         = value
        elif key == 'CASE':
            self.case        = value
        elif key == 'SUBCAT':
            self.subcat      = value
        elif key == 'MOOD':
            self.mood        = value
        elif key == 'VOICE':
            self.voice       = value
        elif key == 'PERS':
            self.pers        = value
        elif key == 'CONJ':
            self.conj        = value
        elif key == 'PROPER':
            self.proper        = value
        elif key == 'PCP':
            self.pcp         = value
        elif key == 'TENSE':
            self.tense       = value
        elif key == 'INF':
            self.inf         = value
        elif key == 'NEG':
            self.neg         = value
        elif key == 'POSS':
            self.poss        = value
        elif key == 'POSITION':
            self.position    = value
        elif key == 'CLIT':
            self.clit        = value
        elif key == 'CMP':
            self.cmp         = value
        else:
            print('Unknown key', key)

    @staticmethod
    def fromString(str):
        arr         = str.split('\t')
        return Tag(*arr)

    #print('Word\tLemma\tPos\tNum\tCase\tSubcat\tMood\tVoice\tPers\tConj\tProper\tPcp\tTense\tInf')

    @staticmethod
    def Convert(stdin):
        arr                             = []
        for line in stdin:

            lineArr                     = line.replace('\n','').split('\t')


            if lineArr[0] is not '':

                tag                     = Tag(lineArr[0])
                if len( lineArr ) >= 3:
                    tag.lemma           = lineArr[2]

                if len( lineArr ) >= 4:
                    for (key, value) in [strArr2Tuple(val) for val in lineArr[3].split('|')]:
                        tag.setTag(key, value)

                arr.append(tag)

        return arr
    