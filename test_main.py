# import tests.test_lastfm as test_lastfm
# test_lastfm.test()


import lib.auth as auth
import lib.lastfm as lastfm
import pandas as pd

config = auth.initialize()

lastfm.initCache()

# response = lastfm.getReq(key=config.getKey(), useragent=config.useragent, user=config.username, method='artist.getInfo', load={'artist':'Hardwell'})
# response = lastfm.getPages(key=config.getKey(), useragent=config.useragent, user=config.username, method='user.getRecentTracks')
response = lastfm.getPages(config)

print(response)
# print(type)
print(pd.DataFrame(response))
# print(lastfm.session)