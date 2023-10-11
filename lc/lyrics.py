import os
from dotenv import load_dotenv
from lyricsgenius import Genius
import traceback

load_dotenv()
genius_api_key = os.getenv("GENIUS_API_KEY")

def get_song_lyrics_genius(song: str, artist: str):
    genius = Genius(genius_api_key)
    print(genius_api_key)
    artist = genius.search_artist(artist, max_songs=3, sort="title")
    try:
        if (artist):
            songFound = artist.song(song)
            if (songFound):
                print(songFound.lyrics)
                return songFound.lyrics
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't find lyrics. Error: {error_message}"
    