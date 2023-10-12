from pydantic.v1 import BaseModel, Field
from spotify import start_play_song_by_name
from lyrics import get_song_lyrics_genius, get_song_name_genius
from langchain.tools import tool

class SongNameInput(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    song: str = Field(
        description="song name in the user's request")
    
# class SongLyricsInput(BaseModel):
#     access_token: str = Field(
#         description="user's access_token")
#     lyrics: str = Field(
#         description="lyrics in the user's request")
#     artist: str = Field(
#         description="artist in the user's request")
    
class SongInputGenius(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    song: str = Field(
        description="song name in the user's request")
    artist: str = Field(
        description="artist in the user's request")
    
class SongLyricsGenius(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    lyrics: str = Field(
        description="song name in the user's request")
    artist: str = Field(
        description="artist in the user's request")
    
@tool("play_song_by_name", return_direct=True, args_schema=SongNameInput)
def play_song_by_name(access_token: str, song: str) -> str:
    """Extract the song name from user's request and play the song."""
    return start_play_song_by_name(access_token, song)

@tool("get_song_lyrics", return_direct=True, args_schema=SongInputGenius)
def get_song_lyrics(access_token: str, artist: str, song: str) -> str:
    """Extract the song name and artist from user's request and get the lyrics."""
    return get_song_lyrics_genius(song, artist)

@tool("get_song_name", return_direct=True, args_schema=SongLyricsGenius)
def get_song_name(access_token: str, artist: str, lyrics: str) -> str:
    """Extract the lyrics and artist from user's request and get the song name."""
    return get_song_name_genius(lyrics, artist)

# @tool("play_song_by_lyrics", return_direct=True, args_schema=SongLyricsInput)
# def play_song_by_lyrics(access_token: str, artist: str, lyrics: str) -> str:
#     """Extract the song lyrics and artist from user's request and play the song."""
#     return start_play_song_by_lyrics(access_token, artist, lyrics)


music_player_tools = [
    play_song_by_name,
    get_song_lyrics,
    get_song_name
]