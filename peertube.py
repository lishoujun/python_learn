#!/usr/bin/python3.7
import json
import sys
import urllib.request
url = "https://instances.joinpeertube.org/api/v1/instances?start=0&count=400"
response = urllib.request.urlopen(url)
res = response.read()
jsonobj = json.loads(res)
for i in jsonobj.get('data'):
    if(i['totalVideos']>10000):
        print(i.get('host'))