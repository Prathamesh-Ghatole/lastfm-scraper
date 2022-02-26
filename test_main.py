# import tests.test_lastfm as test_lastfm
# test_lastfm.test()


import lib.auth as auth
import lib.lastfm as lastfm

config = auth.initialize()

lastfm.initCache()
for i in range(10):
    response = lastfm.getReq(key=config.getKey(), useragent=config.useragent, user=config.username, method='user.getTopArtists')
    print(response.json().keys())

# print(lastfm.session)