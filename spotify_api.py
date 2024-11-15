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
            track_data.append({
                "Track Name": track['name'],
                "Artists": artist_name,
                "Track ID": track_id,
                "Popularity": track['popularity'],
                "Duration (ms)": track['duration_ms'],
                "Explicit": track['explicit'],
                "Danceability": audio_features['danceability'],
                "Energy": audio_features['energy'],
                "Key": audio_features['key'],
                "Loudness": audio_features['loudness'],
                "Mode": audio_features['mode'],
                "Speechiness": audio_features['speechiness'],
                "Acousticness": audio_features['acousticness'],
                "Instrumentalness": audio_features['instrumentalness'],
                "Liveness": audio_features['liveness'],
                "Valence": audio_features['valence'],
                "Tempo": audio_features['tempo'],
                "Time Signature": audio_features['time_signature']
            })
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
    track_data=[]
    for playlist in playlist_ids: 
        print(f"Fetching playlist {playlist} tracks...")
        tracks = fetch_playlist_tracks(playlist)
        print("Fetching track data...")
        track_data+=(fetch_track_data(tracks))
    if track_data:
        save_to_csv(track_data, "playlist_database.csv")
    else:
        print("No data to save.")
