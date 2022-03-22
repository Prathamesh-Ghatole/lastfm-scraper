# import tests.test_lastfm as test_lastfm
# test_lastfm.test()


import lib.auth as auth
import lib.lastfm as lastfm

config = auth.init()

lastfm.initCache()

print("Fetching Scrobbles:")
scrobbles = lastfm.grab(config)
print("Done!\n")

format = input("Enter format to export in:\n(JSON / CSV / [ALL]): ")
if format != 'JSON' or format != 'CSV':
    format = 'ALL'

lastfm.export(scrobbles, format)