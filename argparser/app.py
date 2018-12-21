# -*- coding: utf-8 -*-
import sys

def command():
    if len( sys.argv ) == 1:
        return None
    
    return sys.argv[1]