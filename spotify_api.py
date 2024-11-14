# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# import config

# # Initialize Spotify client
# def init_spotify_client():
#     """
#     Initialize the Spotify API client with client credentials.
#     Returns an authenticated Spotify client.
#     """
#     return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
#         client_id=config.CLIENT_ID,
#         client_secret=config.CLIENT_SECRET
#     ))

# # Search for a song
# def search_song(sp, query, limit=1):
#     """
#     Search for a song by name.
#     :param sp: Initialized Spotipy client.
#     :param query: The song title or artist to search for.
#     :param limit: Maximum number of results to return.
#     :return: A list of track dictionaries.
#     """
#     results = sp.search(query, limit=limit, type='track')
#     return results['tracks']['items']

# # Retrieve song details and audio features
# def get_song_details(sp, track_id):
#     """
#     Fetch audio features and metadata for a specific track ID.
#     :param sp: Initialized Spotipy client.
#     :param track_id: The Spotify ID of the track.
#     :return: A dictionary containing track details and audio features.
#     """
#     # Get audio features
#     audio_features = sp.audio_features([track_id])[0]

#     # Get track metadata
#     track = sp.track(track_id)

#     # Get the genre using artist info (approximation)
#     artist_id = track['artists'][0]['id']
#     artist_info = sp.artist(artist_id)
#     genres = artist_info.get('genres', [])
#     track_genre = genres[0] if genres else "Unknown"

#     # Combine details
#     details = {
#         "Track ID": track_id,
#         "Track Name": track['name'],
#         "Artists": [artist['name'] for artist in track['artists']],
#         "Popularity": track['popularity'],
#         "Duration (ms)": track['duration_ms'],
#         "Explicit": track['explicit'],
#         "Danceability": audio_features['danceability'],
#         "Energy": audio_features['energy'],
#         "Key": audio_features['key'],
#         "Loudness": audio_features['loudness'],
#         "Mode": "Major" if audio_features['mode'] == 1 else "Minor",
#         "Speechiness": audio_features['speechiness'],
#         "Acousticness": audio_features['acousticness'],
#         "Instrumentalness": audio_features['instrumentalness'],
#         "Liveness": audio_features['liveness'],
#         "Valence": audio_features['valence'],
#         "Tempo (BPM)": audio_features['tempo'],
#         "Time Signature": audio_features['time_signature'],
#         "Genre": track_genre
#     }
#     return details

# # Main function
# if __name__ == "__main__":
#     # Initialize Spotify client
#     sp = init_spotify_client()

#     # Search for a song
#     song_query = "Blinding Lights"
#     print(f"Searching for: {song_query}")
#     songs = search_song(sp, song_query)

#     if songs:
#         # Get details for the first song
#         song = songs[0]
#         track_id = song['id']
#         song_details = get_song_details(sp, track_id)

#         # Display song details
#         print("\nSong Details:")
#         for key, value in song_details.items():
#             print(f"{key}: {value}")
#     else:
#         print("No song found.")


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
def fetch_playlist_tracks(sp, playlist_id):
    """
    Fetch all tracks from a Spotify playlist.
    :param sp: Initialized Spotipy client.
    :param playlist_id: Spotify playlist ID.
    :return: A list of dictionaries containing track details.
    """
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    while results:
        for item in results['items']:
            track = item['track']
            if track:  # Ensure the track is not None
                tracks.append(track)
        results = sp.next(results) if results['next'] else None
    return tracks

# Fetch detailed track information
def fetch_track_data(sp, tracks):
    """
    Fetch metadata and audio features for each track in the playlist.
    :param sp: Initialized Spotipy client.
    :param tracks: List of tracks from the playlist.
    :return: A list of dictionaries containing track metadata and audio features.
    """
    track_data = []

    for track in tracks:
        track_id = track['id']
        audio_features = sp.audio_features([track_id])[0]
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
    :param data: List of dictionaries containing track details.
    :param filename: Output CSV file name.
    """
    keys = data[0].keys() if data else []
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to {filename}")

# Main function
if __name__ == "__main__":
    # Initialize Spotify client
    sp = spotify_client()

    # Replace with your playlist ID (from the Spotify playlist link)
    playlist_id = "37i9dQZF1DXcBWIGoYBM5M"  # Example: Replace with your playlist's ID

    # Fetch playlist tracks
    print("Fetching playlist tracks...")
    tracks = fetch_playlist_tracks(sp, playlist_id)

    # Fetch track data
    print("Fetching track data...")
    track_data = fetch_track_data(sp, tracks)

    # Save to CSV
    if track_data:
        save_to_csv(track_data, "playlist_database.csv")
    else:
        print("No data to save.")
