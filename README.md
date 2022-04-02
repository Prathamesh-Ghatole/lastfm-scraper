<img src="https://raw.githubusercontent.com/Prathamesh-Ghatole/lastfm-scraper/main/webserver/static/assets/lastfm_scraper_logo_white.png" width="400" height="101">

### This Project is Under Construction! ⚠
A simple platform to scrape & Analyze last.fm scrobbles.
> **Update**: Web-server is ready! Update flask to forward downloads to the user.
## Done:
- 🔐 Added authentication features
- 🔍 Added Module for last.fm requests
- 📥 Scrape all streaming history from last.fm

## Upcoming Feature Set:
- 📜 Metadata Enhancement (Extended _Artist-Info_, _Genre-Tags_, _Composer-info_, _producers_, etc.) with [_MusicBrainz_](https://musicbrainz.org/doc/MusicBrainz_API) & [_Spotify_](https://developer.spotify.com/documentation/web-api/) APIs.
- ➕ Update Scrobbles/Listens on Last.fm & Listenbrainz
- 📊 Chart and Visualization Generation with Plotly
  - Word Clouds
- 🎶 Playlist Generator
- 🧠 Machine Learning based recommendations for the next song
- 🧹 Clean-up Metadata
  - Resolve artist-name fields with commas to first artist in the list.
  - Resolve artist aliases to single common name. (e.g. Reslove ```TK from Ling tosite sigure``` & ```TK from 凛として時雨``` to the prior.)

## To-Do:
- Add Interesting Progress bars (refer listenbrainz.org imports)
- Add links to git, developer contacts and info.
- Rename Exports for better concurrency
- setup db for exports
- add params for username in lastfm module
- clean up format selection / export-algo
- Setup flask for actually sending files to the user.
