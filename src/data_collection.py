import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv


# Initialize Spotify client
def spotify_client():
    """
    Initialize the Spotify API client with client credentials.
    Returns an authenticated Spotify client.
    """
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="c4536e618eac4bde8a40fb861828b092",
        client_secret="56deb037e3c54cc88e6071b30f6e5f18"
    ))

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

    for track in tracks:
        track_id = track['id']
        audio_features = spotify_client().audio_features([track_id])[0]
        if audio_features:  # Ensure audio features are available
            artist_name = ", ".join([artist['name'] for artist in track['artists']])
            dict_track={"Track Name": track['name'],
                "Artists": artist_name,
                "Track ID": track_id,
                "Popularity": track['popularity'],
                "Duration (ms)": track['duration_ms'],
                "Explicit": track['explicit']}
            for key in audio_features.keys():
                dict_track[key]=audio_features[key]
            track_data.append(dict_track)
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
