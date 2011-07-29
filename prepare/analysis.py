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
    """A simple example class"""
    def __init__(self):
        self.data = []
    def f(self):
        return 'hello world'

class Analyzor():
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

f = codecs.open('meta/alphabet.json', 'r', 'utf-8'):
alphabet = json.loads(unicode(f.readlines().join('')))


langs = ['de', 'en', 'es', 'fr', 'it', 'ja', 'nl', 'pl', 'ru',
         'zh-hans', 'zh-hant', 'zh-yue']

for lang in langs:
    for f in os.listdir(lang):
        fpath = os.path.join('.', lang, f)
        try:
            if os.path.isfile(fpath):

        except Exception, e:
            print e

