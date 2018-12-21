import io
import sys
import subprocess
import nltk
from .tag import Tag

FINNPOS_FOLDER          = './finnpos/lib'
BIN_FOLDER              = '{0}/bin'.format(FINNPOS_FOLDER)
FTB_LABEL               = '{0}/ftb-label'.format(BIN_FOLDER)
#MODEL_FOLDER            = '{0}/share/finnpos/ftb_omorfi_model'.format(FINNPOS_FOLDER)
#FREQ_WORDS              = '{0}/freq_words'.format(MODEL_FOLDER)
#OMORFI_MODEL            = '{0}/ftb.omorfi.model'.format(MODEL_FOLDER)

#FINNPOS_RATNA_FEATS     = '{0}/finnpos-ratna-feats.py'.format(BIN_FOLDER)
#FINNPOS_LABEL           = '{0}/finnpos-label'.format(BIN_FOLDER)

#POSTAG                  = '{0}/postag.py'.format(BIN_FOLDER)


# Converts array to readable stdin stream
def arr2stdin(arr):
    return io.StringIO('\n'.join(arr))

# Executes requested command in bash shell
def process(cmd):
    return subprocess.Popen(
        ['bash', '-c', 'bash -c "{0}"'.format( cmd )],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )



def partOfSpeech(text):

    print('Lemmatizing data')

    tokens              = nltk.word_tokenize(text)

    tokenStdin          = io.StringIO('\n'.join(tokens))

    p                   = process(FTB_LABEL)
    
    output, err         = p.communicate( bytes(tokenStdin.read(), 'utf-8') )
    #print(output.decode('utf-8'), err)
    if err is not None:
        print('Error occurred while lemmatizing', err)
        sys.exit(1)

    stdin               = io.StringIO( output.decode('utf-8') )

    return Tag.Convert(stdin)

    #return [Tag.fromString(tag) for tag in io.StringIO(output.split('\n'))]
    
    
