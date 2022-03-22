# import tests.test_lastfm as test_lastfm
# test_lastfm.test()


import lib.auth as auth
import lib.lastfm as lastfm

config = auth.init()
lastfm.initCache()

print("Fetching Scrobbles:")
scrobbles = lastfm.grab(config)
print("Done!\n")

type = input("Enter type to export in:\n(JSON / CSV / [ALL]): ")
if type != 'JSON' or type != 'CSV':
    type = 'ALL'

lastfm.export(scrobbles, type)