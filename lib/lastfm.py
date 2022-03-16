from distutils.command.config import config
from re import I, X
from tkinter.ttk import Progressbar
from urllib import response
import requests
import json
import requests_cache as rcache

# Initializing the cache for requests_cache to cache requests.
def initCache():
    rcache.install_cache(cache_name = 'request-cache/lastfm', backend='sqlite', expire_after = 180)
    global session
    session = rcache.CachedSession()

# Function for flushing / resetting cache for requests_cache
def flushCache():
    session.cache.clear()

# Function for sending a generic request to last.fm
# When using, pass in params user=config.username, key=config.getKey(), useragent=config.useragent
# Use the load parameter to add custom arguments.
def getReq(user, key, useragent, page=1, load = {}, method = 'user.getRecentTracks'):
    
    headers = {'user-agent': useragent}
    payload ={
    'user':user,
    'api_key': key,
    'method': method,
    'format': 'json',
    'page': page
    }
    for k, v in load.items():
        payload[k] = v

    api_reply = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    
    return api_reply

# Grab a single page from lastfm user.getRecentTracks
def getPage(config, page=1):
    
    key=config.getKey()
    user=config.username
    useragent=config.useragent
    
    response = getReq(user, key, useragent, page=1, load = {'limit':200}, method = 'user.getRecentTracks')
    # Raise error if status code is anything other than 200.
    if response.status_code != 200:
        raise Exception('status code: {}'.format(response.status_code))
    
    # 
    page = (response.json())['recenttracks']['track']
    current_page = int((response.json())['recenttracks']['@attr']['page'])

    if current_page==1:
        total_pages = int((response.json())['recenttracks']['@attr']['totalPages'])

    if (current_page!=1) & ('@attr' in page[0].keys()):
        if (page[0]['@attr']=={'nowplaying': 'true'}):
            del page[0]

    return page

# Display a status bar on console while fetching data.
def Progress (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
    return None

def getPages(config):
    key = config.getKey()
    user = config.username
    useragent = config.useragent
    
    # Set total number of pages as collected from blank API call for user.getRecentTracks.
    response = getReq(page=1, user=user, key=key, useragent=useragent, load={'limit':200})
    # total_pages = int((response.json())['recenttracks']['@attr']['totalPages'])
    all_scrobbles = []
    for i in range(total_pages):
        key = config.getKey()
        # print('key = {}'.format(key))
        pg = getPage(config, page=i)
        # print(pg)
        Progress(iteration = i, total=total_pages)
        all_scrobbles = [*all_scrobbles, *pg]
    
    return all_scrobbles