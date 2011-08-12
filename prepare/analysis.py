#!/usr/bin/env python
# -*- coding: utf-8 -*-#

# Analyze corpus to generate freqence lists of ngram, and the n of ngram can be
# vary in the text stream according to corresponding the alphabet system, and
# is determined in the alphabet.json.

import os
import re
import codecs
import math
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
            if int(midval_upper, 16) < ord(c):
                lo = mid+1
            elif int(midval_lower, 16) > ord(c):
                hi = mid
            else:
                return self.data[self.keys[mid]]
        return None
    def n(self, c):
        seg = self.which(c)
        if seg is None:
            return 1
        else:
            return seg['n']

class GramGenerator():
    def __init__(self, alphabet, text):
        self.alphabet = alphabet
        self.text = text
        self.iterator = next_gram(self)
    def __iter__(self):
        return self.iterator()

position = -1
def next_gram(gg):
    global position
    length   = len(gg.text)
    position = -1
    def gram():
        global position
        while True:
            position = position + 1
            if position >= length:
                position = -1
                raise StopIteration
            c = gg.text[position]
            n = gg.alphabet.n(c)
            if n < 1: n = 1
            end = position + n
            if end >= length - 1:
                position = -1
                raise StopIteration
            else:
                yield gg.text[position:end]
    return gram

f = codecs.open('../meta/alphabet.json', 'r', 'utf-8')
alphabet = Alphabet(json.loads(unicode(''.join(f.readlines()))))

langs = ['de', 'en', 'es', 'fr', 'it', 'ja', 'nl', 'pl', 'ru',
         'zh-hans', 'zh-hant', 'zh-yue']

for lang in langs:

    freq = {}
    for f in os.listdir(lang):
        fpath = os.path.join('.', lang, f)
        print fpath
        if os.path.isfile(fpath):
            f = codecs.open(fpath, 'r', 'utf-8')
            lines = f.readlines()
            gg = GramGenerator(alphabet, unicode(''.join(lines)))
            for gram in gg:
                if gram in freq.keys():
                    freq[gram] = freq[gram] + 1
                else:
                    freq[gram] = 1

    sq = 0
    for k in freq.keys():
        sq = sq + freq[k] * freq[k]
    l = math.sqrt(sq)

    f = open('../data/' + lang + '.txt', 'w')
    keys = sorted(freq.keys(), key=lambda ind: -freq[ind])
    for k in keys:
        freq[k] = float(freq[k]) / l
        text = k + ', ' + str(freq[k]) + '\n'
        f.write(text.encode('utf-8'))
    f.close()


