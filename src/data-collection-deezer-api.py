import requests
import pandas as pd
import time

# API KEYS (remplacez par vos clés API si nécessaire)
LASTFM_API_KEY = 3d08e00c985d4d4f2497254924de0085
Shared_secret = d3aa88fd5684b881a8270eda9f24e88f

# Fonctions de requête API

def fetch_from_deezer(track_name, artist_name):
    url = f"https://api.deezer.com/search?q=track:\"{track_name}\" artist:\"{artist_name}\""
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {}

def fetch_from_lastfm(track_name, artist_name):
    url = (f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&track={track_name}" 
           f"&artist={artist_name}&api_key={LASTFM_API_KEY}&format=json")
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {}

def fetch_from_musicbrainz(track_name):
    url = f"https://musicbrainz.org/ws/2/recording?query=track:\"{track_name}\"&fmt=json"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {}

# Fonction principale

def fetch_music_metadata(tracks):
    data = []

    for track_name, artist_name in tracks:
        record = {"track_name": track_name, "artist_name": artist_name}

        # Récupération des données depuis Deezer
        deezer_data = fetch_from_deezer(track_name, artist_name)
        if deezer_data.get("data"):
            deezer_info = deezer_data["data"][0]
            record.update({
                "deezer_title": deezer_info.get("title"),
                "deezer_artist": deezer_info.get("artist", {}).get("name"),
                "deezer_album": deezer_info.get("album", {}).get("title"),
                "deezer_genre": deezer_info.get("genre_id"),
                "deezer_popularity": deezer_info.get("rank"),
            })

        # Récupération des données depuis Last.fm
        lastfm_data = fetch_from_lastfm(track_name, artist_name)
        if lastfm_data.get("track"):
            track_info = lastfm_data["track"]
            record.update({
                "lastfm_listeners": track_info.get("listeners"),
                "lastfm_playcount": track_info.get("playcount"),
                "lastfm_tags": [tag["name"] for tag in track_info.get("toptags", {}).get("tag", [])],
            })

        # Récupération des données depuis MusicBrainz
        musicbrainz_data = fetch_from_musicbrainz(track_name)
        if musicbrainz_data.get("recordings"):
            mb_info = musicbrainz_data["recordings"][0]
            record.update({
                "musicbrainz_title": mb_info.get("title"),
                "musicbrainz_artist": ", ".join([artist["name"] for artist in mb_info.get("artist-credit", [])]),
                "musicbrainz_date": mb_info.get("first-release-date"),
            })

        data.append(record)
        time.sleep(1)  # Respect du taux limite des API

    return pd.DataFrame(data)

# Exemple d'utilisation
if __name__ == "__main__":
    tracks = [("Shape of You", "Ed Sheeran"), ("Blinding Lights", "The Weeknd")]
    df = fetch_music_metadata(tracks)
    print(df.head())
