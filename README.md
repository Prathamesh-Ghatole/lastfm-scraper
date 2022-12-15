<!-- <img src="https://raw.githubusercontent.com/Prathamesh-Ghatole/lastfm-scraper/main/static/assets/lastfm_scraper_logo_white.png" width="400" height="101"> -->

<img src="https://github.com/Prathamesh-Ghatole/lastfm-scraper/raw/main/static/assets/lastfm-scraper-preview.gif">
<!-- <img src="https://raw.githubusercontent.com/Prathamesh-Ghatole/lastfm-scraper/main/static/assets/lastfm-scraper-preview.gif"> -->



### Lastfm-scraper is a simple platform to scrape, clean & analyze your last.fm scrobbles.
> **Update**: This project is currently hosted on: http://lastfm-scraper.azurewebsites.net/ (Takes a while to load!)

## Done:
- 🔐 Added authentication features
- 🔍 Added Module for last.fm requests
- 📥 Scrape & Download all streaming history from last.fm

## Upcoming Feature Set:
- 📜 Metadata Enhancement (Extended _Artist-Info_, _Genre-Tags_, _Composer-info_, _producers_, etc.) with [_MusicBrainz_](https://musicbrainz.org/doc/MusicBrainz_API) & [_Spotify_](https://developer.spotify.com/documentation/web-api/) APIs.
- ➕ Update Scrobbles/Listens on Last.fm & Listenbrainz
- 📊 Chart and Visualization Generation with Plotly
- 🎶 Playlist Generator
- 🧠 Machine Learning based recommendations for the next song
- 🧹 Clean-up Metadata
  - Resolve artist-name fields with commas to first artist in the list.
  - Resolve artist aliases to single common name. (e.g. Reslove ```TK from Ling tosite sigure``` & ```TK from 凛として時雨``` to the prior.)

## To-Do:
- Add parallel processing features with concurrent futures.
- Implement a cleanup algorithm for the exports.
- Add Interesting Progress bars (refer listenbrainz.org imports)
- Clean up format selection / export-algo
- Update config system to work with simpler config.py files instead.
- Auto delete old exports from system.
