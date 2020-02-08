#!/usr/bin/python3.7
# get ed2k link of The Good Doctor
import json
import sys
import urllib.request
import lxml.html
from lxml import etree


url = 'http://www.hao6v.com/mj/2017-09-27/29897.html'
response = urllib.request.urlopen(url)
html = response.read()
html = str(html, "GB18030")
#print(html)
doc = lxml.html.fromstring(html)
nodes = doc.xpath('//tr/td/a')
for i in nodes:
    if 'S02' in i.text:
        print(i.text)
        print(i.get('href'))
        print('')
        #print(etree.tostring(i,pretty_print=True))
        #print(i.keys())



