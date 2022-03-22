import pandas as pd
import requests
# import json
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
def getPage(config, page_num):
    
    key=config.getKey()
    user=config.username
    useragent=config.useragent
    response = getReq(user, key, useragent, page=int(page_num), load = {'limit':200}, method = 'user.getRecentTracks')
    # Raise error if status code is anything other than 200.

    if response.status_code != 200:
        raise Exception('status code: {}'.format(response.url))
    
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
    total_pages = int((response.json())['recenttracks']['@attr']['totalPages'])
    
    # Loop and fetch scrobbles
    all_scrobbles = []
    
    for x in range(1,total_pages+1):
        pg = getPage(config, page_num=x)
        # print(pg)
        all_scrobbles = [*all_scrobbles, *pg]
        Progress(iteration = x, total=total_pages)
    
    return all_scrobbles

def cleanup(all_scrobbles):
    # Convert list of pages to dataframe
    df = pd.DataFrame(all_scrobbles)

    # Split dictionary columns into separate columns
    def split_column(dataframe, column_name, name1, name2, del_column=False):
        def splt(entry):
            if entry==None or entry=='None':
                return (None, None)
            d = (entry)
            return (d[tuple(d.keys())[0]],d[tuple(d.keys())[1]])

        dataframe[str(name1)] = dataframe[column_name].map(lambda x: splt(x)[0])
        dataframe[str(name2)] = dataframe[column_name].map(lambda x: splt(x)[1])
        
        if del_column==True:
            dataframe.drop([column_name], axis=1, inplace=True)
    # Use function split_column to split columns and place them into the dataframe
    split_column(df, 'artist', 'artist_mbid', 'artist_name', del_column=True)
    split_column(df, 'album', 'album_mbid', 'album_name', del_column=True)
    split_column(df, 'date', 'date_uts', 'date_text', del_column=True)
    
    #Drop useless columns
    df.drop(['image', 'streamable', 'date_uts'], axis=1, inplace=True)
    if '@attr' in df.columns:
        df.drop(['@attr'], axis=1, inplace=True)

    #Convert date column to pandas datetime format.
    df.date_text = pd.to_datetime(df.date_text)

    #Rename the date column
    df.rename({'date_text':'date'}, inplace=True, axis=1)

    #Reorder the columns
    df = df[['artist_name', 'name', 'album_name', 'date', 'mbid', 'artist_mbid', 'album_mbid', 'url']]

    return df

# Driver function to grab and clean all scrobbles
def grab(config):
    
    # Get list of scrobbles
    scrobble_list = getPages(config)
    
    # Clean the list of scrobbles, and return it.
    # return cleanup(scrobble_list)
    return pd.DataFrame(scrobble_list)

#Export it in desired format.
def export(clean_df,format='ALL'):

        pth = 'exports/export.json'
        clean_df.to_json(pth)
        print("Exported data to '{}'\n".format('exports/export.json'))

        pth = 'exports/export.csv'
        clean_df.to_json(pth)
        clean_df.to_csv(pth, encoding='utf-8-sig')
        print("Exported data to '{}'\n".format('exports/export.csv'))