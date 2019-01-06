import io
import subprocess
import nltk
import sys
from finnpos.lib.bin import finnpos_ratna_feats as ratna

FINNPOS_FOLDER          = './finnpos/lib'
BIN_FOLDER              = '{0}/bin'.format(FINNPOS_FOLDER)
MODEL_FOLDER            = '{0}/share/finnpos/ftb_omorfi_model'.format(FINNPOS_FOLDER)
FREQ_WORDS              = '{0}/freq_words'.format(MODEL_FOLDER)
OMORFI_MODEL            = '{0}/ftb.omorfi.model'.format(MODEL_FOLDER)

FINNPOS_RATNA_FEATS     = '{0}/finnpos-ratna-feats.py'.format(BIN_FOLDER)
FINNPOS_LABEL           = '{0}/finnpos-label'.format(BIN_FOLDER)

POSTAG                  = '{0}/postag.py'.format(BIN_FOLDER)


def create_command():
    return 'echo "Samoin" | bash -c "python3 {ratna} {words}"'.format(# | "{label} {model}"'.format(#) | bash -c "{label} {model}'.format(
        ratna=FINNPOS_RATNA_FEATS,
        words=FREQ_WORDS
        #label=FINNPOS_LABEL,
        #model=OMORFI_MODEL
    )
    '''return 'bash -c "py {0}/test.py"'.format(
        FINNPOS_FOLDER
    )
    return 'echo Sanoin | py {0} {1} | {2} {3} | py {4}"'.format(
        FINNPOS_RATNA_FEATS,
        FREQ_WORDS,
        FINNPOS_LABEL,
        OMORFI_MODEL,
        POSTAG
    )'''


def bash_command(cmd, stdin=None, stdout=None):
    '''if stdin is not None and stdout is not None:
        return subprocess.Popen(['bash', '-c', cmd], stdin=stdin, stdout=stdout)    
    elif stdin is not None:
        return subprocess.Popen(['bash', '-c', cmd], stdin=stdin)    
    elif stdout is not None:
        return subprocess.Popen(['bash', '-c', cmd], stdout=stdout)    
    else:'''
    return subprocess.Popen(['bash', '-c', 'bash -c "{cmd}"'.format(cmd=cmd)])#"python3 {0} {1}"'.format(FINNPOS_RATNA_FEATS, FREQ_WORDS)], shell=False)


def postag(token):

    print('Create ratnaProc')
    ratnaProc       = subprocess.Popen([
            'bash',
            '-c',
            'py {0} {1}'.format( FINNPOS_RATNA_FEATS, FREQ_WORDS ), 
        ],
        stdin=subprocess.PIPE,
        stderr=sys.stderr,
        stdout=subprocess.PIPE
    )
    
    #ratnaOut        = ratnaProc.communicate()[0].decode('latin1')
    #print('ratnaOut', ratnaOut)

    print('Create labelProc')
    labelProc       = subprocess.check_output([
            'bash',
            '-c',
            'bash -c "{0} {1}"'.format( FINNPOS_LABEL, OMORFI_MODEL ), 
        ],
        stdin=ratnaProc.stdout,
        stderr=sys.stderr
    )
    print('Write to the ratna')
    ratnaProc.stdin.write( bytes(token, 'latin1') )
    print('Wait for the ratna')
    ratnaProc.wait()
    print('Wait for the ratna done')
    #labelProc.stdin.write( bytes(ratnaOut, 'latin1'))
    #out = labelProc.communicate()
    

    print('Closing processes')
    #labelProc.stdin.close()

    #print('out', out)

    #print('ratnaComm', ratnaProc.communicate()[0].decode('latin1'))

    return 


def test(tokens):

    with open(FREQ_WORDS, encoding='utf-8') as file:
        freq_words      = file.read().split('\n')

        stdin       = io.StringIO('\n'.join(tokens))

        print('Loading labelProc')
        labelProc   = subprocess.check_output([
            'bash',
            '-c',
            'bash -c "{0} {1}"'.format( FINNPOS_LABEL, OMORFI_MODEL )
        ], shell=True, stderr=sys.stderr)
        print('labelProc', labelProc)
        
        print('Pass tokens to the ratna')
        ratna.main('finnpos', 'STDIN', stdin, 'STDOUT', labelProc, sys.stderr, freq_words)
        
        print('Wait for labelProc')
        #labelProc.wait()
        #finnpos.finnpos_ratna_feats.main('finnpos', 'STDIN', sys.stdin, 'STDOUT', sys.stdout, sys.stderr, freq_words)
        #finnpos.finnpos_ratna_feats.main('finnpos-ratna-feats', "STDIN", stdin, "STDOUT", stdout, stderr, freq_words)




    '''
    
    if len(argv) != 2:
        stderr.write("cat data | %s freq_word_list\n" % argv[0])
        exit(1)

    freq_words = set(open(argv[1]).read().split('\n'))

    exit(main(argv[0], "STDIN", stdin, "STDOUT", stdout, stderr, freq_words))
    def main(pname, iname, ifile, oname, ofile, olog, freq_words):
    '''

def lemmatize(val):

    print('Lemmatizing data')

    #test(val)

    tokens              = nltk.word_tokenize(val)

    test(tokens)

    #print(postag(tokens[0]))
    #cmd                 = create_command()
    #print('Run', cmd)
    #bash_command(cmd)

    #print(postag(tokens[0]))
    #tags                = [postag(token) for token in tokens]

    #print(tags)

    #tokenized_input     = '\n'.join(tokens)

    #cmd                 = create_command('Sanoin')

    #print(cmd)

    #ps1                 = bash_command(cmd, stdin=subprocess.PIPE)
    #ps1.stdin.buffer.write('testaus')
    #print(ps1.communicate()[0])

    #ps1.stdin.write("tokens")

    #[ps1.stdin.writelines(token) for token in tokens]
    #ps1.stdin.write()

    #bash_command('a="Apples and oranges" && echo "${a/oranges/grapes}"')
    #subprocess.Popen('bash -c "ls"')

    #cmd         = 'bash -c "echo Sanoin | python3 ./lib/bin/finn-pos-ratna-feats.py"'
    #cmd          = 'ls ./finnpos/lib/bin/'
    #cmd             = 'bash -c "echo Sanoin | python3 ./lib/bin/finn-pos-ratna-feats.py ./lib/share/finnpos/ftb_omorfi_model/freq_words"'

    #ps = subprocess.Popen(cmd, shell=True)#, '"python3 ./finnpos-ratna-feats.py"'), stdout=subprocess.PIPE)
    #output = subprocess.check_output(('grep', 'process_name'), stdin=ps.stdout)
    #ps.wait()

    #subprocess.Popen(['bash', '-c', 'python3', 'finnpos-ratna-feats.py'], stdin=tokenized_input, stdout=subprocess.PIPE)


    #bash -c "cat tokenized_input | python3 finnpos-ratna-feats.py ../share/finnpos/ftb_omorfi_model/freq_words | ./finnpos-label ../share/finnpos/ftb_omorfi_model/ftb.omorfi.model | python3 postag.py > tagged_input"

    #print(tokenized_input)

