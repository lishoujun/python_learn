#!/usr/bin/python3.7
import json
import sys
import urllib.request
import time

BASEURL = "https://api.github.com/repos/"
urls = [
"antennapod/AntennaPod",
"Neamar/KISS",
"scoute-dich/browser",
"sschueller/peertube-android",
#"clemensbartz/essential-launcher",
"renyuneyun/Easer"
]

def getRepoUpdateTime(url):
    response = urllib.request.urlopen(url)
    res = response.read()
    jsonobj = json.loads(res)
    print(jsonobj.get('pushed_at') + " " + jsonobj.get('full_name'))
    
    
def main():
    for i in urls:
        getRepoUpdateTime(BASEURL+i)

    

if __name__ == '__main__':
    starttime = time.time()
    main()
    endtime = time.time()
    costtime = endtime - starttime
    print(costtime)
