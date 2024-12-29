import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import time



# Spotify client initialization
def spotify_client():
    """
    Initialize the Spotify API client with client credentials.
    Returns an authenticated Spotify client.
    """
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="d666ee3ae4c94b85945c3dba39776f4f",
        client_secret="c1973a77acbe48c0b2f105e4f57d7d46" 
    ))


# Fetch tracks from the playlist
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


# Fetch metadata from tracks
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


# Fetch the genre
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


# Save the df
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


if __name__ == "__main__":
    playlist_ids = []
    track_data = []
    for playlist in playlist_ids:
        tracks = fetch_playlist_tracks(playlist)
        track_data += fetch_track_data(tracks)

    save_to_csv(track_data, "datafram.csv")
