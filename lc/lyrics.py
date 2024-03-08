import os
from dotenv import load_dotenv
from lyricsgenius import Genius
import traceback

load_dotenv()
genius_api_key = os.getenv("GENIUS_API_KEY")
genius = Genius(genius_api_key, verbose = True)

def getLyricsOnly(geniusLyrics: str):
    start_index = geniusLyrics.find('[')
    res = geniusLyrics[start_index:].split('Embed')[0]
    return res

def get_song_lyrics_by_artist_and_song_name_genius(song: str, artist: str):
    try:
        song = genius.search_song(title=song, artist=artist, get_full_info=True)
        if song:
            lyrics = song.lyrics
            message = getLyricsOnly(lyrics)
            res = {"message": message, "function": "get_song_lyrics_by_artist_and_song_name_genius", "status": 200}
            return res
        else:
            message = f"Couldn't find song."
            res = {"message": message, "function": "get_song_lyrics_by_artist_and_song_name_genius", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't find lyrics. Error: {error_message}"
        res = {"message": message, "function": "get_song_lyrics_by_artist_and_song_name_genius", "status": 500}
        return res
    
def get_song_lyrics_by_song_name_genius(song: str):
    try:
        song = genius.search_song(song)
        if song: 
            lyrics = song.lyrics
            message = getLyricsOnly(lyrics)
            res = {"message": message, "function": "get_song_lyrics_by_song_name_genius", "status": 200}
            return res
        else:
            message = f"Couldn't find song."
            res = {"message": message, "function": "get_song_lyrics_by_song_name_genius", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't find lyrics. Error: {error_message}"
        res = {"message": message, "function": "get_song_lyrics_by_song_name_genius", "status": 500}
        return res


def get_song_name_by_lyrics_and_artist_genius(lyrics: str, artist: str):
    try:
        artist = genius.search_artist(artist, max_songs=1) # returns Artist object
        if not artist:
            message = f"Couldn't find artist."
            res = {"message": message, "function": "get_song_name_by_lyrics_and_artist_genius", "status": 500}
            return res
        artist_id = artist.id
        res = genius.search_artist_songs(artist_id, lyrics, per_page = 50, page = 1, sort="popularity")
        if res:
            song = res["songs"][0]
            message = f"Song found: {song['title']}"
            res = {"message": message, "function": "get_song_name_by_lyrics_and_artist_genius", "status": 200}
            return res
        else:
            message = f"Couldn't find song."
            res = {"message": message, "function": "get_song_name_by_lyrics_and_artist_genius", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't find song. Error: {error_message}"
        res = {"message": message, "function": "get_song_name_by_lyrics_and_artist_genius", "status": 500}
        return res

def get_song_name_by_lyrics_genius(lyrics: str):
    try:
        res = genius.search_lyrics(lyrics)
        if res:
            song = res["sections"][0]["hits"][0]["result"]
            message = song["title"]
            res = {"message": message, "function": "get_song_name_by_lyrics_genius", "status": 200}
            return res
        else:
            message = f"Couldn't find song."
            res = {"message": message, "function": "get_song_name_by_lyrics_genius", "status": 500}
            return res
    except Exception as e:
        error_message = traceback.format_exc()
        message = f"Couldn't find song. Error: {error_message}"
        res = {"message": message, "function": "get_song_name_by_lyrics_genius", "status": 500}
        return res
