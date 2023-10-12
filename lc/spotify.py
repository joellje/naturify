import os
import traceback
import spotipy

def get_song_by_name(access_token: str, name: str):
    sp = spotipy.Spotify(auth = access_token)
    results = sp.search(q=name, type='track')
    if (results):
        song_uri = results['tracks']['items'][0]['uri']
        return song_uri

def start_play_song_by_name(access_token: str, song_name: str):
    sp = spotipy.Spotify(auth = access_token)
    song_uri = get_song_by_name(access_token, song_name)
    try:
        if (song_uri):
            sp.start_playback(uris=[song_uri])
            return f"Started playing song {song_name}"
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't play song. Error: {error_message}"
   
# def start_play_song_by_lyrics(access_token: str, artist: str, lyrics: str):
