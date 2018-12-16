# -*- coding: utf-8 -*-
import sys
import stopwords

if __name__ == '__main__':
    print(stopwords.remove(sys.argv[1]))