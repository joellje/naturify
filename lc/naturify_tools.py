from pydantic.v1 import BaseModel, Field
from spotify import start_play_song_by_name
from lyrics import get_song_lyrics_genius
from langchain.tools import tool

class SongNameInput(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    song: str = Field(
        description="song name in the user's request")
    
class SongInputGenius(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    song: str = Field(
        description="song name in the user's request")
    artist: str = Field(
        description="artist in the user's request")
    
@tool("play_song_by_name", return_direct=True, args_schema=SongNameInput)
def play_song_by_name(access_token: str, song: str) -> str:
    """Extract the song name from user's request and play the song."""
    return start_play_song_by_name(access_token, song)

@tool("get_song_lyrics", return_direct=True, args_schema=SongInputGenius)
def get_song_lyrics(access_token: str, artist: str, song: str) -> str:
    """Extract the song name from user's request and get the lyrics."""
    return get_song_lyrics_genius(song, artist)

music_player_tools = [
    play_song_by_name,
    get_song_lyrics
]