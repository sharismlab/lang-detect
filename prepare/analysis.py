#!/usr/bin/env python
# -*- coding: utf-8 -*-#

# Analyze corpus to generate freqence lists of ngram, and the n of ngram can be
# vary in the text stream according to corresponding the alphabet system, and
# is determined in the alphabet.json.

import os
import re
import codecs
import json

class Alphabet():
    def __init__(self, json):
        self.data = json
        self.keys = sorted(json.keys(), key=lambda name: json[name]['interval'][0])
    def which(self, c):
        lo=0
        hi=None
        if hi is None:
            hi = len(self.keys)
        while lo < hi:
            mid = (lo+hi)//2
            midval_lower = self.data[self.keys[mid]]['interval'][0]
            midval_upper = self.data[self.keys[mid]]['interval'][1]
            if midval_upper < x:
                lo = mid+1
            elif midval_lower > x:
                hi = mid
            else:
                return self.data[self.keys[mid]]
        return None
    def n(self, c):
        return self.which(c)['n']

class GramGenerator():
    def __init__(self, alphabet, text):
        self.alphabet = alphabet
        self.text = text
        self.iterator = next_gram(self)
    def __iter__(self):
        return self.iterator()

def next_gram(gg):
    length   = len(gg.text)
    position = 0
    def gram:
        c = gg.text[position]
        n = gg.alphabet.n(c)
        end = position + n
        if end >= length:
            raise StopIteration
        else:
            position = position + 1
            yield gg.text[position:end]
    return gram

f = codecs.open('meta/alphabet.json', 'r', 'utf-8'):
alphabet = Alphabet(json.loads(unicode(f.readlines().join(''))))

langs = ['de', 'en', 'es', 'fr', 'it', 'ja', 'nl', 'pl', 'ru',
         'zh-hans', 'zh-hant', 'zh-yue']

for lang in langs:
    for f in os.listdir(lang):
        fpath = os.path.join('.', lang, f)
        try:
            if os.path.isfile(fpath):
                f = codecs.open(fpath, 'r', 'utf-8')
                generator = GramGenerator(alphabet, unicode(f.readlines().join('')))
        except Exception, e:
            print e

