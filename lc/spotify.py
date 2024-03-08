import os
import traceback
import spotipy
import requests
import json
from lyrics import get_song_name_by_lyrics_genius, get_song_name_by_lyrics_and_artist_genius
from datetime import datetime

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
            message = f"Started playing song {track['name']}"
            res = {"message": message, "function": "start_play_song_by_name", "status": 200}
            return res
        else:
            message = f"Couldn't play song."
            res = {"message": message, "function": "start_play_song_by_name", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't play song. Error: {error_message}"
        res = {"message": message, "function": "start_play_song_by_name", "status": 500}
        return res
    
def add_to_queue_song_by_name(access_token: str, song_name: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_uri = get_song_by_name(access_token, song_name)
        print(song_uri)
        if (song_uri):
            sp.add_to_queue(song_uri)
            track = sp.track(song_uri)
            message = f"Added to queue {track['name']}"
            res = {"message": message, "function": "add_to_queue_song_by_name", "status": 200}
            return res
        else:
            message = f"Couldn't add to queue."
            res = {"message": message, "function": "add_to_queue_song_by_name", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't add to queue. Error: {error_message}"
        res = {"message": message, "function": "add_to_queue_song_by_name", "status": 500}
        return res
    
def start_play_song_by_name_and_artist(access_token: str, song_name: str, artist: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_uri = get_song_by_name(access_token, song_name+artist)
        if (song_uri):
            sp.start_playback(uris=[song_uri])
            track = sp.track(song_uri)
            message = f"Started playing song {track['name']}"
            res = {"message": message, "function": "start_play_song_by_name_and_artist", "status": 200}
            return res
        else:
            message = f"Couldn't play song."
            res = {"message": message, "function": "start_play_song_by_name_and_artist", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't play song. Error: {error_message}"
        res = {"message": message, "function": "start_play_song_by_name_and_artist", "status": 500}
        return res
    
def add_to_queue_song_by_name_and_artist(access_token: str, song_name: str, artist: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_uri = get_song_by_name(access_token, song_name+artist)
        if (song_uri):
            sp.add_to_queue(uri=song_uri)
            track = sp.track(song_uri)
            message = f"Added to queue {track['name']}"
            res = {"message": message, "function": "add_to_queue_song_by_name_and_artist", "status": 200}
            return res
        else:
            message = f"Couldn't add to queue."
            res = {"message": message, "function": "add_to_queue_song_by_name_and_artist", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't add to queue. Error: {error_message}"
        res = {"message": message, "function": "add_to_queue_song_by_name_and_artist", "status": 500}
        return res
   
def start_play_song_by_lyrics(access_token: str, lyrics: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_name = get_song_name_by_lyrics_genius(lyrics)
        song_uri = get_song_by_name(access_token, song_name)
        if (song_uri):
            sp.start_playback(uris=[song_uri])
            message = f"Started playing song {song_name}"
            res = {"message": message, "function": "start_play_song_by_lyrics", "status": 200}
            return res
        else:
            message = f"Couldn't play song."
            res = {"message": message, "function": "start_play_song_by_lyrics", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't play song. Error: {error_message}"
        res = {"message": message, "function": "start_play_song_by_lyrics", "status": 500}
        return res
    
def add_to_queue_song_by_lyrics(access_token: str, lyrics: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_name = get_song_name_by_lyrics_genius(lyrics)
        song_uri = get_song_by_name(access_token, song_name)
        if (song_uri):
            sp.add_to_queue(uri=song_uri)
            track = sp.track(song_uri)
            message = f"Added to queue {track['name']}"
            res = {"message": message, "function": "add_to_queue_song_by_lyrics", "status": 200}
            return res
        else:
            message = f"Couldn't add to queue."
            res = {"message": message, "function": "add_to_queue_song_by_lyrics", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't add to queue. Error: {error_message}"
        res = {"message": message, "function": "add_to_queue_song_by_lyrics", "status": 500}
        return res
    
def start_play_song_by_lyrics_and_artist(access_token: str, lyrics: str, artist: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        song_name = get_song_name_by_lyrics_and_artist_genius(lyrics, artist)
        if song_name[:13] != "Couldn't find":
            song_uri = get_song_by_name(access_token, song_name)
            if (song_uri):
                sp.start_playback(uris=[song_uri])
                message = f"Started playing song {song_name}"
                res = {"message": message, "function": "start_play_song_by_lyrics_and_artist", "status": 200}
                return res
            else:
                message = f"Couldn't play song."
                res = {"message": message, "function": "start_play_song_by_lyrics_and_artist", "status": 500}
                return res
        else:
            message = f"Couldn't play song."
            res = {"message": message, "function": "start_play_song_by_lyrics_and_artist", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't play song. Error: {error_message}"
        res = {"message": message, "function": "pause_playback", "status": 500}
        return res
    
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
                message = f"Added to queue {track['name']}"
                res = {"message": message, "function": "add_to_queue_song_by_lyrics_and_artist", "status": 200}
                return res
            else:
                message = f"Couldn't add to queue."
                res = {"message": message, "function": "add_to_queue_song_by_lyrics_and_artist", "status": 500}
                return res
        else:
            message = f"Couldn't add to queue."
            res = {"message": message, "function": "add_to_queue_song_by_lyrics_and_artist", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't add to queue. Error: {error_message}"
        res = {"message": message, "function": "add_to_queue_song_by_lyrics_and_artist", "status": 500}
        return res
    
def start_playback(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        sp.start_playback()
        message = f"Playback Started."
        res = {"message": message, "function": "start_playback", "status": 200}
        return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't start playback. Error: {error_message}"
        res = {"message": message, "function": "start_playback", "status": 500}
        return res

def pause_playback(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        sp.pause_playback()
        res = {"message": "Playback Paused.", "function": "pause_playback", "status": 200}
        return res
    except Exception as e:
        error_message = traceback.format_exc()
        message =  f"Couldn't stop playback. Error: {error_message}"
        res = {"message": message, "function": "pause_playback", "status": 500}
        return res
    
def play_next_track(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        sp.next_track()
        message = f"Skipped to next track."
        res = {"message": message, "function": "play_next_track", "status": 200}
        return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't skip track. Error: {error_message}"
        res = {"message": message, "function": "play_next_track", "status": 500}
        return res
    
def play_previous_track(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        sp.previous_track()
        message = f"Playing previous track."
        res = {"message": message, "function": "play_previous_track", "status": 200}
        return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't play previous track. Error: {error_message}"
        res = {"message": message, "function": "play_previous_track", "status": 500}
        return res
    
def recommend_tracks_by_user_top_tracks(access_token: str):
    try: 
        sp = spotipy.Spotify(auth = access_token)
        user_top_tracks= sp.current_user_top_tracks(limit=5, offset=0, time_range='medium_term')
        user_top_tracks_uris = [item["uri"].split(":")[-1] for item in user_top_tracks["items"]]
        recommended_tracks = sp.recommendations(seed_tracks = user_top_tracks_uris, limit = 20, country = 'SG')
        recommended_tracks_uris = [track["id"] for track in recommended_tracks["tracks"]]

        playlist_name = "Recommended Tracks " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        res = create_playlist(access_token, playlist_name, "Naturify-recommended tracks, just for you!", False)
        
        sp.user_playlist_add_tracks(sp.me()["uri"].split(":")[-1], res["playlist_id"], recommended_tracks_uris, position=None)
        url = res["url"]
        message = f"To access playlist, click here: {url}"
        res = {"message": message, "function": "recommend_tracks_by_user_top_tracks", "status": 200}
        return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't recommend tracks. Error: {error_message}"
        res = {"message": message, "function": "recommend_tracks_by_user_top_tracks", "status": 500}
        return res
    
def recommend_tracks_by_user_prompt(access_token: str, prompt: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        related_playlists = sp.search(prompt, limit=10,type='playlist')['playlists']['items']
        related_playlists_ids = [playlist["id"] for playlist in related_playlists]
        related_playlists_tracks = [sp.playlist_tracks(playlist_id, limit=10, offset=0)["items"] for playlist_id in related_playlists_ids]
        track_ids = []
        for playlist in related_playlists_tracks:
            for track in playlist:
                if not track or not track["track"]: continue
                track_ids.append(track["track"]["id"])

        # Get variables from track ids
        audio_features = sp.audio_features(track_ids)
        totals = {}
        for track in audio_features:
            for key, value in track.items():
                if not isinstance(value, str):
                    if key in totals:
                        totals[key] += value
                    else:
                        totals[key] = value

        # Get averages
        averages = {}
        for key, value in totals.items():
            averages["target_" + key] = value / len(audio_features)
        averages["target_duration_ms"] = int(averages["target_duration_ms"])
        averages["target_key"] = int(averages["target_key"])
        averages["target_time_signature"] = int(averages["target_time_signature"])
        del averages["target_mode"]

        recommended_tracks_details = sp.recommendations(seed_tracks = track_ids[:5], **averages)
        recommended_tracks_uris = [track["id"] for track in recommended_tracks_details["tracks"]]

        playlist_name = "Recommended Tracks " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        res = create_playlist(access_token, playlist_name, "Naturify-recommended tracks, just for you!", False)
        print(recommended_tracks_uris)
        sp.user_playlist_add_tracks(sp.me()["uri"].split(":")[-1], res["playlist_id"], recommended_tracks_uris, position=None)
        url = res["url"]
        message = f"To access playlist, click here: {url}"
        res = {"message": message, "function": "recommend_tracks_by_user_prompt", "status": 200}
        return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't recommend tracks. Error: {error_message}"
        res = {"message": message, "function": "recommend_tracks_by_user_prompt", "status": 500}
        return res

def recommend_tracks_by_genre(access_token: str, genre: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        recommended_tracks = sp.recommendations(seed_genres = [genre.lower()], limit = 20, country = 'SG')
        recommended_tracks_uris = [track["id"] for track in recommended_tracks["tracks"]]
        if not recommended_tracks_uris: return f"No tracks found. Please input a valid genre."

        playlist_name = "Recommended Tracks " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        res = create_playlist(access_token, playlist_name, "Naturify-recommended tracks, just for you!", False)
        print(recommended_tracks_uris)
        sp.user_playlist_add_tracks(sp.me()["uri"].split(":")[-1], res["playlist_id"], recommended_tracks_uris, position=None)
        url = res["url"]
        message = f"To access playlist, click here: {url}"
        res = {"message": message, "function": "recommend_tracks_by_genre", "status": 200}
        return res
    
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't recommend tracks. Error: {error_message}"
        res = {"message": message, "function": "recommend_tracks_by_genre", "status": 500}
        return res
    
def recommend_tracks_by_artist(access_token: str, artist: str):
    try:
        sp = spotipy.Spotify(auth = access_token)
        artist = sp.search(artist, limit=1,type='artist')["artists"]["items"][0]["id"]
        if not artist: return f"No tracks found. Please input a valid artist."
        recommended_tracks = sp.recommendations(seed_artists = [artist], limit = 20, country = 'SG')
        recommended_tracks_uris = [track["id"] for track in recommended_tracks["tracks"]]

        playlist_name = "Recommended Tracks " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        res = create_playlist(access_token, playlist_name, "Naturify-recommended tracks, just for you!", False)
        sp.user_playlist_add_tracks(sp.me()["uri"].split(":")[-1], res["playlist_id"], recommended_tracks_uris, position=None)
        url = res["url"]
        message =  f"To access playlist, click here: {url}"
        res = {"message": message, "function": "recommend_tracks_by_artist", "status": 200}
        return res
    
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't recommend tracks. Error: {error_message}"
        res = {"message": message, "function": "recommend_tracks_by_artist", "status": 500}
        return res
    
def create_playlist(access_token: str, playlist_name: str, description: str, public: bool):
    try:
        sp = spotipy.Spotify(auth = access_token)
        user_id = sp.me()["uri"].split(":")[-1]

        data = {"name": playlist_name, "description": description, "public": public}
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}'}
        res = requests.post(f"https://api.spotify.com/v1/users/{user_id}/playlists", data=json_data, headers=headers)

        playlist_id = res.json()["id"]
        url = res.json()["external_urls"]["spotify"]

        res = {"playlist_id": playlist_id, "url": url}
        return res
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't create playlist. Error: {error_message}"