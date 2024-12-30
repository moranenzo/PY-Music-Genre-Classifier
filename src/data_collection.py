# Importation des librairies
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import time


# Initialisation du client Spotify
def spotify_client():
    """
    Initialise le client de l'API Spotify avec les identifiants du client.
    Retourne un client Spotify authentifié.
    """
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id="d666ee3ae4c94b85945c3dba39776f4f",
        client_secret="c1973a77acbe48c0b2f105e4f57d7d46"
    ))


# Récupérer les morceaux d'une playlist
def fetch_playlist_tracks(playlist_id):
    """
    Récupère tous les morceaux d'une playlist Spotify.
    Paramètres :
        - playlist_id : ID de la playlist Spotify.
    Retourne une liste de dictionnaires contenant les détails des morceaux.
    """
    tracks = []
    results = spotify_client().playlist_tracks(playlist_id)
    while results:
        for item in results['items']:
            track = item['track']
            if track:  # S'assurer que le morceau n'est pas None
                tracks.append(track)
        results = spotify_client().next(results) if results['next'] else None
    return tracks


# Récupérer les métadonnées des morceaux
def fetch_track_data(tracks):
    """
    Récupère les métadonnées et les caractéristiques audio pour chaque morceau de la playlist.
    Paramètres :
        - tracks : Liste des morceaux de la playlist.
    Retourne une liste de dictionnaires contenant les métadonnées des morceaux et leurs caractéristiques audio.
    """
    track_data = []
    i = 0
    j = 0
    for track in tracks:
        track_id = track['id']
        i += 1
        print(i)
        audio_features = spotify_client().audio_features([track_id])[0]
        genre = fetch_artist_genre(track)
        if audio_features:  # S'assurer que les caractéristiques audio sont disponibles
            artist_name = ", ".join([artist['name'] for artist in track['artists']])
            dict_track = {"track Name": track['name'],
                          "artists": artist_name,
                          "track_id": track_id,
                          "popularity": track['popularity'],
                          "duration_ms": track['duration_ms'],
                          "explicit": track['explicit'], 'genre': genre}
            for key in audio_features.keys():
                dict_track[key] = audio_features[key]
            track_data.append(dict_track)
        if i == 100:
            j += 1
            save_to_csv(track_data, f"intermédiaire{j}")
            i = 0
            time.sleep(60)
    return track_data


# Récupérer le genre de l'artiste
def fetch_artist_genre(track):
    """Cette fonction récupère le genre d'un artiste à partir d'un morceau de cet artiste,
    il sera ensuite considéré comme le genre de la chanson.

    Arguments :
        track un dict contenant des informations sur le morceau

    Retourne : genre un string représentant le genre de l'artiste
    """
    artist = track['artists'][0]['id']
    if spotify_client().artist(artist)['genres'] != []:
        return spotify_client().artist(artist)['genres'][0]
    else:
        return 'N/A'


# Sauvegarder dans un fichier CSV
def save_to_csv(data, filename):
    """
    Sauvegarde la liste des données des morceaux dans un fichier CSV.
    Paramètres :
    :param data : Liste de dictionnaires contenant les détails des morceaux.
    :param filename : Nom du fichier CSV de sortie.
    """
    keys = data[0].keys() if data else []
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Données sauvegardées dans {filename}")


if __name__ == "__main__":
    playlist_ids = ['1G8IpkZKobrIlXcVPoSIuf', '7gqtGYFoCR3tAqTtEUQZTw']
    track_data = []
    for playlist in playlist_ids:
        tracks = fetch_playlist_tracks(playlist)
        track_data += fetch_track_data(tracks)

    save_to_csv(track_data, "datafram.csv")
