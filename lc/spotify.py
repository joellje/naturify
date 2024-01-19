import os
import traceback
import spotipy
from lyrics import get_song_name_by_lyrics_genius, get_song_name_by_lyrics_and_artist_genius

def get_song_by_name(access_token: str, name: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        results = sp.search(q=name, type='track')
        if (results):
            song_uri = results['tracks']['items'][0]['uri']
            return song_uri
        else:
            return f"Couldn't play song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't play song. Error: {error_message}"
    
def start_play_song_by_name(access_token: str, song_name: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_uri = get_song_by_name(access_token, song_name)
        if (song_uri):
            sp.start_playback(uris=[song_uri])
            track = sp.track(song_uri)
            return f"Started playing song {track['name']}"
        else:
            return f"Couldn't play song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't play song. Error: {error_message}"
    
def add_to_queue_song_by_name(access_token: str, song_name: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_uri = get_song_by_name(access_token, song_name)
        print(song_uri)
        if (song_uri):
            sp.add_to_queue(song_uri)
            track = sp.track(song_uri)
            return f"Added to queue {track['name']}"
        else:
            return f"Couldn't add to queue."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't add to queue. Error: {error_message}"
    
def start_play_song_by_name_and_artist(access_token: str, song_name: str, artist: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_uri = get_song_by_name(access_token, song_name+artist)
        if (song_uri):
            sp.start_playback(uris=[song_uri])
            track = sp.track(song_uri)
            return f"Started playing song {track['name']}"
        else:
            return f"Couldn't play song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't play song. Error: {error_message}"
    
def add_to_queue_song_by_name_and_artist(access_token: str, song_name: str, artist: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_uri = get_song_by_name(access_token, song_name+artist)
        if (song_uri):
            sp.add_to_queue(uri=song_uri)
            track = sp.track(song_uri)
            return f"Added to queue {track['name']}"
        else:
            return f"Couldn't add to queue."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't add to queue. Error: {error_message}"
   
def start_play_song_by_lyrics(access_token: str, lyrics: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_name = get_song_name_by_lyrics_genius(lyrics)
        song_uri = get_song_by_name(access_token, song_name)
        if (song_uri):
            sp.start_playback(uris=[song_uri])
            return f"Started playing song {song_name}"
        else:
            return f"Couldn't play song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't play song. Error: {error_message}"
    
def add_to_queue_song_by_lyrics(access_token: str, lyrics: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_name = get_song_name_by_lyrics_genius(lyrics)
        song_uri = get_song_by_name(access_token, song_name)
        if (song_uri):
            sp.add_to_queue(uri=song_uri)
            track = sp.track(song_uri)
            return f"Added to queue {track['name']}"
        else:
            return f"Couldn't add to queue."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't add to queue. Error: {error_message}"
    
def start_play_song_by_lyrics_and_artist(access_token: str, lyrics: str, artist: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_name = get_song_name_by_lyrics_and_artist_genius(lyrics, artist)
        print(song_name)
        if song_name[:13] != "Couldn't find":
            song_uri = get_song_by_name(access_token, song_name)
            if (song_uri):
                sp.start_playback(uris=[song_uri])
                return f"Started playing song {song_name}"
            else:
                return f"Couldn't play song."
        else:
            return f"Couldn't play song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't play song. Error: {error_message}"
    
def add_to_queue_song_by_lyrics_and_artist(access_token: str, lyrics: str, artist: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_name = get_song_name_by_lyrics_and_artist_genius(lyrics, artist)
        print(song_name)
        if song_name[:13] != "Couldn't find":
            song_uri = get_song_by_name(access_token, song_name)
            if (song_uri):
                sp.add_to_queue(uri=song_uri)
                track = sp.track(song_uri)
                return f"Added to queue {track['name']}"
            else:
                return f"Couldn't add to queue."
        else:
            return f"Couldn't add to queue."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't add to queue. Error: {error_message}"
    
def start_playback(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        sp.start_playback()
        return f"Playback Started."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't start playback. Error: {error_message}"

def pause_playback(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        sp.pause_playback()
        return f"Playback Paused."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't stop playback. Error: {error_message}"
    
def play_next_track(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        sp.next_track()
        return f"Skipped to next track."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't skip track. Error: {error_message}"
    
def play_previous_track(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        sp.previous_track()
        return f"Playing previous track."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't play previous track. Error: {error_message}"