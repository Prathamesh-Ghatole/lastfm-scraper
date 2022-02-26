# import tests.test_lastfm as test_lastfm
# test_lastfm.test()


import lib.auth as auth
import lib.lastfm as lastfm

config = auth.initialize()

lastfm.initCache()

response = lastfm.getReq(key=config.getKey(), useragent=config.useragent, user=config.username, method='artist.getInfo', load={'artist':'Hardwell'})


print(response.json()['artist'])

# print(lastfm.session)