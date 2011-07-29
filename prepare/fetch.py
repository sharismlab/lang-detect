#!/usr/bin/env python
# -*- coding: utf-8 -*-#

# Fetch the feature articles in a language version of Wikipedia as the corpus
# for analysis.

import os
import re
import codecs
import httplib
import urllib
import random

from pyquery import PyQuery as pq

langs = ['de', 'en', 'es', 'fr', 'it', 'ja', 'nl', 'pl', 'ru',
         'zh-hans', 'zh-hant', 'zh-yue']

host = {}
host['zh-hans'] = 'http://zh.wikipedia.org'
host['zh-hant'] = 'http://zh.wikipedia.org'

path = {}
path['zh-hans'] = '/zh-cn/'
path['zh-hant'] = '/zh-tw/'

fa = {}
fa['de'] = unicode(codecs.decode('Wikipedia:Exzellente_Artikel', 'utf-8'))
fa['en'] = unicode(codecs.decode('Wikipedia:Featured_articles', 'utf-8'))
fa['es'] = unicode(codecs.decode('Wikipedia:Artículos_destacados', 'utf-8'))
fa['fr'] = unicode(codecs.decode('Catégorie:Article_de_qualité', 'utf-8'))
fa['it'] = unicode(codecs.decode('Wikipedia:Vetrina', 'utf-8'))
fa['ja'] = unicode(codecs.decode('Wikipedia:秀逸な記事', 'utf-8'))
fa['nl'] = unicode(codecs.decode('Wikipedia:Etalage', 'utf-8'))
fa['pl'] = unicode(codecs.decode('Wikipedia:Artykuły_na_medal', 'utf-8'))
fa['ru'] = unicode(codecs.decode('Википедия:Избранные_статьи', 'utf-8'))
fa['zh-hans'] = unicode(codecs.decode('维基百科:特色条目', 'utf-8'))
fa['zh-hant'] = unicode(codecs.decode('維基百科:特色條目', 'utf-8'))
fa['zh-yue'] = unicode(codecs.decode('Wikipedia:正文', 'utf-8'))

class MyOpener(urllib.URLopener):
      version = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.99 Safari/535.1'
      def read(self, url):
          try:
              handle = self.open(url)
              return handle.read()
          except IOError, e:
              if e.args[1] == 301:
                  url = e.args[3]['Location']
                  print 'redirect: ' + url
                  return self.read(url)
              return '<html><body id="bodyContent"> </body></html>'

print 'remove old corpus...'
for lang in langs:
    for f in os.listdir(lang):
        fpath = os.path.join('.', lang, f)
        try:
            if os.path.isfile(fpath):
                os.unlink(fpath)
        except Exception, e:
            print e

print 'downloading...'
for lang in langs:
    if lang in host.keys():
        h = host[lang]
    else:
        h = 'http://' + lang + '.wikipedia.org'
    if lang in path.keys():
        p = path[lang]
    else:
        p = '/wiki/'
    fetch_url = h + urllib.pathname2url((p + fa[lang]).encode('utf-8'))
    print fetch_url

    def isArticle(o):
        return o.attr('href') != None and o.attr('title') != None and re.match('^/wiki/(.+)$', o.attr('href')) and not re.match('^(.+):(.+)$', o.attr('title'))

    d = pq(url=fetch_url, opener=lambda url: MyOpener().open(url).read())
    d = pq(d.html())
    links = d.find('a').filter(lambda i: isArticle(pq(this))).map(lambda i, e: pq(e).attr('title'))

    def out(lang, link, text):
        f = open(lang + '/' + link, 'w')
        f.write(text.encode('utf-8'))
        f.close()

    for ind in range(15):
        link = random.choice(links)
        link = re.sub('\[\w+\]', '', link)
        url = h + urllib.pathname2url((p + link).encode('utf-8'))
        try:
            d = pq(url=url, opener=lambda url: MyOpener().read(url))
            text = d('#bodyContent').text()
            if text != None:
                text = re.sub('$.*jumpto bodytext', '', text)
                out(lang, link, text)
        except httplib.HTTPException, e:
            print e

