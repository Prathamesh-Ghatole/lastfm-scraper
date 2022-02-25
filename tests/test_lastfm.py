import lib.auth as auth
import lib.lastfm as lastfm
import pandas as pd

def test():
    print('authenticating & Loading ConfigClass object in variable config')
    config = auth.initialize()

    print('initializing cache')
    lastfm.init()

    print('checking if requests is working')
    resp = lastfm.getReq(key=config.getKey(), user = config.username, useragent = config.useragent, method = 'library.getArtists')
    print(resp.status_code)

    print('Checking if cache is working')
    for i in range(5):
        resp = lastfm.getReq(key=config.getKey(), user = config.username, useragent = config.useragent, method = 'library.getArtists')
        print(i, resp.status_code)

    print('Flushing Cache and Retry')
    lastfm.flushCache()

    print('Testing again after flushing')
    resp = lastfm.getReq(key=config.getKey(), user = config.username, useragent = config.useragent, method = 'library.getArtists')
    print(resp.status_code)

    for i in range(5):
        resp = lastfm.getReq(key=config.getKey(), user = config.username, useragent = config.useragent, method = 'library.getArtists')
        print(i, resp.status_code)

    print('flushing cache')
    lastfm.flushCache()