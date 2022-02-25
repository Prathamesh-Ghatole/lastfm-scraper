import requests
import json
import requests_cache as rcache

def init():
    rcache.install_cache(cache_name = 'request-cache/lastfm', backend='sqlite', expire_after = 180)
    global session
    session = rcache.CachedSession()

def flushCache():
    session.cache.clear()

def getReq(user, key, useragent, page=1, load = {}, method = 'user.getRecentTracks'):
    
    headers = {'user-agent': useragent}
    
    payload ={
    'user':user,
    'api_key': key,
    'method': method,
    'format': 'json',
    'page': page
    }

    # payload = payload.update(load)
    # print(payload)
    
    api_reply = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    
    return api_reply