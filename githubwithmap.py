#!/usr/bin/python3.7
"""
use map to 
https://segmentfault.com/a/1190000000414339
"""
import json
import sys
import urllib.request
import time
from multiprocessing.dummy import Pool as ThreadPool

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
    response = urllib.request.urlopen(BASEURL + url)
    res = response.read()
    jsonobj = json.loads(res)
    print(jsonobj.get('pushed_at') + " " + jsonobj.get('full_name'))
    
    
def main():
    threadnum = 10 if 10 < len(urls)  else len(urls)
    print(threadnum)
    pool = ThreadPool(threadnum) 
    pool.map(getRepoUpdateTime, urls)
    pool.close() 
    pool.join()
   

if __name__ == '__main__':
    starttime = time.time()
    main()
    endtime = time.time()
    costtime = endtime - starttime
    print(costtime)
