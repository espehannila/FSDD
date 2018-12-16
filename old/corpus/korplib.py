# -*- coding: utf-8 -*-
from korp.korp import Korp
from operator import is_not
from functools import partial

korppi      = Korp(service_name='kielipankki')

def parse(corpuses):
    parsed      = ''
    for name in corpuses:
        corpus_list         = filter(partial(is_not, None), korppi.list_corpora(name))
        
        if parsed == '':
            parsed          = parsed + ','.join(corpus_list)
        else:
            parsed          = parsed + ',' + ','.join(corpus_list)

    parsed          = parsed.replace('LEHDET_KS,','')
    

    return parsed