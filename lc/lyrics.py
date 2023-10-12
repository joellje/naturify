import os
from dotenv import load_dotenv
from lyricsgenius import Genius
import traceback

load_dotenv()
genius_api_key = os.getenv("GENIUS_API_KEY")

def get_title(hit):
    return hit["result"]["title"]

def get_song_lyrics_genius(song: str, artist: str):
    genius = Genius(genius_api_key)
    try:
        artist = genius.search_artist(artist, max_songs=3, sort="title")
        if (artist):
            songFound = artist.song(song)
            if (songFound):
                print(songFound.lyrics)
                return songFound.lyrics
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't find lyrics. Error: {error_message}"
    
def get_song_name_genius(lyrics: str, artist: str):
    genius = Genius(genius_api_key)
    try:
        songs = genius.search_lyrics(lyrics, per_page = 10)
        if songs:
            hits = songs["sections"][0]["hits"]
            titles = [hit["result"]["title"] for hit in hits]
            return titles[0]
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't find song. Error: {error_message}"