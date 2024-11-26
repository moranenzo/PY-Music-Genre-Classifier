import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time

# Liste des genres et leurs playlists associées
genres = {
    "Pop": '0ZwUMU8Kt8e141i5aqhDfD',
    "Rock": '0ZwUMU8Kt8e141i5aqhDfD',
    "Rap": '0ZwUMU8Kt8e141i5aqhDfD',
    "Country": '33mU9g6y8nKFAOyiISor0G',
    "Blues": '7BDUphylF8dfPKFo9Tvdr9',
    "Metal": '1yYEy4MtNLVScj74wcPR7w',
    "R_and_B": '7CI3NR7rvCkgiLhch1qprf',
    "Classical_music": '5n9btvMZ52rxwozhQdKU7v',
    "Jazz": '79Bcltku1dcD08JcAM29kL'
}

# Authentification avec le Client ID et le Client Secret
client_id = "d666ee3ae4c94b85945c3dba39776f4f"
client_secret = "c1973a77acbe48c0b2f105e4f57d7d46"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Fonction pour extraire les données d'une playlist
def get_playlist_data(playlist_id, genre_name):
    all_tracks = []
    offset = 0

    while True:
        # Récupération par lot (max 100 morceaux par requête)
        response = sp.playlist_items(
            playlist_id,
            offset=offset,
            fields="items(track(id,name,artists,duration_ms,explicit,popularity)),next",
            additional_types=["track"]
        )
        
        # Parcours des morceaux
        for item in response['items']:
            track = item['track']
            if track:  # Filtrer les morceaux valides
                features = sp.audio_features(track['id'])[0]
                if features:  # Vérifier que les caractéristiques existent
                    track_info = {
                        "Track Name": track['name'],
                        "Artists": ", ".join([artist['name'] for artist in track['artists']]),
                        "Track ID": track['id'],
                        "Popularity": track['popularity'],
                        "Duration (ms)": track['duration_ms'],
                        "Explicit": track['explicit'],
                        "Danceability": features['danceability'],
                        "Energy": features['energy'],
                        "Key": features['key'],
                        "Loudness": features['loudness'],
                        "Mode": features['mode'],
                        "Speechiness": features['speechiness'],
                        "Acousticness": features['acousticness'],
                        "Instrumentalness": features['instrumentalness'],
                        "Liveness": features['liveness'],
                        "Valence": features['valence'],
                        "Tempo": features['tempo'],
                        "Time Signature": features['time_signature'],
                        "Genre": genre_name  # Ajout de la colonne personnalisée
                    }
                    all_tracks.append(track_info)

        # Pagination : vérifier s'il y a plus de morceaux
        offset += len(response['items'])
        if not response['next']:
            break
        time.sleep(0.1)  # Respecter les limites de l'API

    return all_tracks

# Collecte des données dans une boucle
while True:
    # Saisie des informations dans le terminal
    playlist_id = input("\nEntrez l'ID de la playlist Spotify (ou 'q' pour quitter) : ")
    if playlist_id.lower() == 'q':
        print("Fin du programme.")
        break
    genre_name = input("Entrez le nom du genre correspondant à cette playlist : ")

    print(f"Collecte des données pour la playlist {playlist_id} ({genre_name})...")
    data = get_playlist_data(playlist_id, genre_name)

    # Conversion en DataFrame pandas
    df = pd.DataFrame(data)

    # Sauvegarde du tableau dans un fichier CSV
    output_file = f"{genre_name}_playlist_data.csv"
    df.to_csv(output_file, index=False)
    print(f"Données sauvegardées dans {output_file}")
