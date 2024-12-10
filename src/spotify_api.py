import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import time


# Initialize Spotify client
def spotify_client():
    """
    Initialize the Spotify API client with client credentials.
    Returns an authenticated Spotify client.
    """
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="d9b0f1004f1e4cf1b4fe2b34ad6878c9",
    client_secret="7753034ebadf42fcac3de6e4b64f2846"
    ))
    
def fetch_artist_genre(track):
    """This function fetches the genre of an artist with a track from this artist, it will be 
    considerated as the genre of the song later

    Args:
        track a dict the countains infos about the track

    Returns: genre a string that is the genre of an artist
        
    """
    artist=track['artists'][0]['id']
    if spotify_client().artist(artist)['genres'] != []:
        return spotify_client().artist(artist)['genres'][0]
    else:
        return 'N/A'

# Fetch playlist tracks
def fetch_playlist_tracks(playlist_id):
    """
    Fetch all tracks from a Spotify playlist. 
    Params:
        -playlist_id: Spotify playlist ID.
    Returns a list of dictionaries containing track details.
    """
    tracks = []
    results = spotify_client().playlist_tracks(playlist_id)
    while results:
        for item in results['items']:
            track = item['track']
            if track:  # Ensure the track is not None
                tracks.append(track)
        results = spotify_client().next(results) if results['next'] else None
    return tracks

# Fetch detailed track information
def fetch_track_data(tracks):
    """
    Fetch metadata and audio features for each track in the playlist.
    Params:
        -tracks: List of tracks from the playlist.
    Returns a list of dictionaries containing track metadata and audio features.
    """
    track_data = []
    i=0
    j=0
    for track in tracks:
        track_id = track['id']
        i+=1
        print(i)
        audio_features = spotify_client().audio_features([track_id])[0]
        genre=fetch_artist_genre(track)
        if audio_features:  # Ensure audio features are available
            artist_name = ", ".join([artist['name'] for artist in track['artists']])
            dict_track={"track Name": track['name'],
                "artists": artist_name,
                "track_id": track_id,
                "popularity": track['popularity'],
                "duration_ms": track['duration_ms'],
                "explicit": track['explicit'], 'genre': genre}
            for key in audio_features.keys():
                dict_track[key]=audio_features[key]
            track_data.append(dict_track)
        if i==100:
            j+=1
            save_to_csv(track_data, f"intermédiaire{j}")
            i=0
            time.sleep(60)
    return track_data

# Save data to a CSV file
def save_to_csv(data, filename):
    """
    Save the list of track data to a CSV file.
    Params:
    :param data: List of dictionaries containing track details.
    :param filename: Output CSV file name.
    """
    keys = data[0].keys() if data else []
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")


def get_playlists_data_to_csv(playlist_ids):
    """This function allows to fetch the data from different playlists into a csv 
    Params:
        - playlist_ids: a list of playlists we want to fetch our data from
    """
    names=[]
    track_data=[]
    file_name=''
    for playlist in playlist_ids: 
        print(f"Fetching playlist {playlist} tracks...")
        tracks = fetch_playlist_tracks(playlist)
        print("Fetching track data...")
        track_data+=(fetch_track_data(tracks))
    for id in playlist_ids:
        names.append(spotify_client().playlist(id)['name'])
    for name in names:
        file_name+=name+'+'
    file_name=file_name[:-1]
    print(file_name)
    if track_data:
        save_to_csv(track_data, f"playlists_{file_name}_data.csv")
    else:
        print("No data to save.")


def fetch_track_data_without_genre(tracks,genre):
    """
    Fetch metadata and audio features for each track in the playlist knowing the genre of the playlist
    Params:
        -tracks: List of tracks from the playlist.
    Returns a list of dictionaries containing track metadata and audio features.
    """
    track_data = []
    i=0
    for track in tracks:
        track_id = track['id']
        i+=1
        audio_features = spotify_client().audio_features([track_id])[0]
        if audio_features:  # Ensure audio features are available
            artist_name = ", ".join([artist['name'] for artist in track['artists']])
            dict_track={"track Name": track['name'],
                "artists": artist_name,
                "track_id": track_id,
                "popularity": track['popularity'],
                "duration_ms": track['duration_ms'],
                "explicit": track['explicit'], 'genre': genre}
            for key in audio_features.keys():
                dict_track[key]=audio_features[key]
            track_data.append(dict_track)
        if i==100:
            j+=1
            save_to_csv(track_data, f"intermédiaire_realdb{j}")
            i=0
            time.sleep(60)
    return track_data

def get_playlists_data_to_csv_with_genre(playlist_ids):
    """This function allows to fetch the data from different playlists into a csv 
    Params:
        - playlist_ids: a dict whose keys are genres and values are playlists (strings)
    """
    names=[]
    track_data=[]
    file_name=''
    for key in playlist_ids.keys(): 
        print(f"Fetching playlist {playlist_ids[key]} tracks...")
        tracks = fetch_playlist_tracks(playlist_ids[key])
        print("Fetching track data...")
        track_data+=(fetch_track_data_without_genre(tracks, key))
    for key1 in playlist_ids.keys():
        names.append(spotify_client().playlist(playlist_ids[key1])['name'])
    for name in names:
        file_name+=name+'+'
    file_name=file_name[:-1]
    print(file_name)
    if track_data:
        save_to_csv(track_data, f"playlists_{file_name}_data.csv")
    else:
        print("No data to save.")

get_playlists_data_to_csv_with_genre({'rap' : '4KsrGBWG6gzBwGe9dx16OE', 
                                      'country' : '33mU9g6y8nKFAOyiISor0G',
                                      'blues' : '7BDUphylF8dfPKFo9Tvdr9',
                                      'metal' : '1yYEy4MtNLVScj74wcPR7w',
                                      'r_and_b' : '7CI3NR7rvCkgiLhch1qprf',
                                      'classical_music' : '5n9btvMZ52rxwozhQdKU7v',
                                      'jazz' : '79Bcltku1dcD08JcAM29kL',
                                      'pop' : '7gqtGYFoCR3tAqTtEUQZTw'})
