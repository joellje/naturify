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
            return getLyricsOnly(lyrics)
        else:
            return f"Couldn't find song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't find lyrics. Error: {error_message}"
    
def get_song_lyrics_by_song_name_genius(song: str):
    try:
        song = genius.search_song(song)
        if song: 
            lyrics = song.lyrics
            return getLyricsOnly(lyrics)
        else:
            return f"Couldn't find song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't find lyrics. Error: {error_message}"


def get_song_name_by_lyrics_and_artist_genius(lyrics: str, artist: str):
    try:
        artist = genius.search_artist(artist, max_songs=1) # returns Artist object
        if not artist:
            return "Couldn't find artist."
        
        for i in range(1, 10):
            res = genius.search_lyrics(lyrics, per_page = 50, page = i)
            for song in res["sections"][0]["hits"]:
                if artist.name in song["result"]["artist_names"]:
                    print(song["result"]["title"])
                    return song["result"]["title"]
                    
        return "Couldn't find song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't find song. Error: {error_message}"

def get_song_name_by_lyrics_genius(lyrics: str):
    try:
        res = genius.search_lyrics(lyrics)
        if res:
            song = res["sections"][0]["hits"][0]["result"]
            return song["title"]
        else:
            return f"Couldn't find song."
    except Exception as e:
        error_message = traceback.format_exc()
        return f"Couldn't find song. Error: {error_message}"
