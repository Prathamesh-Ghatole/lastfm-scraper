import lib.auth as auth
import lib.lastfm as lastfm
import pandas as pd

def test():
    #authenticating & Loading ConfigClass object in variable config
    config = auth.initialize()

    #initialize cache
    lastfm.init()

    # check if requests is working
    resp = lastfm.getReq(key=config.getKey(), user = config.username, useragent = config.useragent, method = 'library.getArtists')
    print(resp.status_code)

    # Check if cache is working
    for i in range(20):
        resp = lastfm.getReq(key=config.getKey(), user = config.username, useragent = config.useragent, method = 'library.getArtists')
        print(i, resp.status_code)

    # Flush Cache and Retry
    lastfm.flushCache()

    # Test again after flushing
    resp = lastfm.getReq(key=config.getKey(), user = config.username, useragent = config.useragent, method = 'library.getArtists')
    print(resp.status_code)

    for i in range(10):
        resp = lastfm.getReq(key=config.getKey(), user = config.username, useragent = config.useragent, method = 'library.getArtists')
        print(i, resp.status_code)

    lastfm.flushCache()

test()