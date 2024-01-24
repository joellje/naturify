from pydantic.v1 import BaseModel, Field
from spotify import start_play_song_by_name, start_play_song_by_lyrics, start_play_song_by_name_and_artist, start_play_song_by_lyrics_and_artist, start_playback, pause_playback, play_next_track, play_previous_track, add_to_queue_song_by_name, add_to_queue_song_by_name_and_artist, add_to_queue_song_by_lyrics_and_artist, add_to_queue_song_by_lyrics, recommend_tracks_by_user_top_tracks, recommend_tracks_by_user_prompt, recommend_tracks_by_genre, recommend_tracks_by_artist
from lyrics import get_song_lyrics_by_artist_and_song_name_genius, get_song_lyrics_by_song_name_genius, get_song_name_by_lyrics_and_artist_genius, get_song_name_by_lyrics_genius
from langchain.tools import tool

class AccessToken(BaseModel):
    access_token: str = Field(
        description="user's access_token")

class UserPrompt(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    prompt: str = Field(
        description="prompt in the user's request to recommend songs")
    
class GenrePrompt(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    genre: str = Field(
        description="genre in the user's request to recommend songs")
    
class Artist(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    artist: str = Field(
        description="artist in the user's request, usually found after the word 'by'")

class Song(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    song: str = Field(
        description="song name in the user's request")
    
class SongArtist(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    song: str = Field(
        description="song name in the user's request")
    artist: str = Field(
        description="artist in the user's request, usually found after the word 'by'")
    
class Lyrics(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    lyrics: str = Field(
        description="lyrics in the user's request")
    
class LyricsArtist(BaseModel):
    access_token: str = Field(
        description="user's access_token")
    lyrics: str = Field(
        description="lyrics in the user's request")
    artist: str = Field(
        description="artist in the user's request, usually found after the word 'by'")
    
@tool("play_song_by_name", return_direct=True, args_schema=Song)
def play_song_by_name_tool(access_token: str, song: str) -> str:
    """Extract the song name from user's request and play the song."""
    return start_play_song_by_name(access_token, song)

@tool("add_to_queue_song_by_name", return_direct=True, args_schema=Song)
def add_to_queue_song_by_name_tool(access_token: str, song: str) -> str:
    """Extract the song name from user's request and add the song to queue."""
    return add_to_queue_song_by_name(access_token, song)

@tool("play_song_by_lyrics", return_direct=True, args_schema=Lyrics)
def play_song_by_lyrics_tool(access_token: str, lyrics: str) -> str:
    """Extract the song lyrics from user's request and play the song."""
    return start_play_song_by_lyrics(access_token, lyrics)

@tool("add_to_queue_song_by_lyrics", return_direct=True, args_schema=Lyrics)
def add_to_queue_song_by_lyrics_tool(access_token: str, lyrics: str) -> str:
    """Extract the song lyrics from user's request and add the song to queue."""
    return add_to_queue_song_by_lyrics(access_token, lyrics)

@tool("play_song_by_name_and_artist", return_direct=True, args_schema=SongArtist)
def play_song_by_name_and_artist_tool(access_token: str, song: str, artist: str) -> str:
    """Extract the song name and artist from user's request and play the song."""
    return start_play_song_by_name_and_artist(access_token, song, artist)

@tool("add_to_queue_song_by_name_and_artist", return_direct=True, args_schema=SongArtist)
def add_to_queue_song_by_name_and_artist_tool(access_token: str, song: str, artist: str) -> str:
    """Extract the song name and artist from user's request and add the song to queue."""
    return add_to_queue_song_by_name_and_artist(access_token, song, artist)

@tool("play_song_by_lyrics_and_artist", return_direct=True, args_schema=LyricsArtist)
def play_song_by_lyrics_and_artist_tool(access_token: str, lyrics: str, artist: str) -> str:
    """Extract the lyrics and artist from user's request and play the song."""
    return start_play_song_by_lyrics_and_artist(access_token, lyrics, artist)

@tool("add_to_queue_song_by_lyrics_and_artist", return_direct=True, args_schema=LyricsArtist)
def add_to_queue_song_by_lyrics_and_artist_tool(access_token: str, lyrics: str, artist: str) -> str:
    """Extract the lyrics and artist from user's request and add the song to queue."""
    return add_to_queue_song_by_lyrics_and_artist(access_token, lyrics, artist)

@tool("get_song_lyrics_by_artist_and_song_name", return_direct=True, args_schema=SongArtist)
def get_song_lyrics_by_artist_and_song_name_tool(access_token: str, artist: str, song: str) -> str:
    """Extract the song name and artist from user's request and get the lyrics."""
    return get_song_lyrics_by_artist_and_song_name_genius(song, artist)

@tool("get_song_lyrics_by_song_name", return_direct=True, args_schema=Song)
def get_song_lyrics_by_song_name_tool(access_token: str, song: str) -> str:
    """Extract the song name from user's request and get the lyrics."""
    return get_song_lyrics_by_song_name_genius(song)

@tool("get_song_name_by_lyrics_and_artist", return_direct=True, args_schema=LyricsArtist)
def get_song_name_by_lyrics_and_artist_tool(access_token: str, artist: str, lyrics: str) -> str:
    """Extract the lyrics and artist from user's request and get the song name."""
    return get_song_name_by_lyrics_and_artist_genius(lyrics, artist)

@tool("get_song_name_by_lyrics", return_direct=True, args_schema=Lyrics)
def get_song_name_by_lyrics_tool(access_token: str, lyrics: str) -> str:
    """Extract the lyrics from user's request and get the song name."""
    return get_song_name_by_lyrics_genius(lyrics)

@tool("start_playback", return_direct=True, args_schema=AccessToken)
def start_playback_tool(access_token: str) -> str:
    """Starts or resumes user's playback."""
    return start_playback(access_token)

@tool("pause_playback", return_direct=True, args_schema=AccessToken)
def pause_playback_tool(access_token: str) -> str:
    """Pauses user's playback."""
    return pause_playback(access_token)

@tool("play_next_track", return_direct=True, args_schema=AccessToken)
def play_next_track_tool(access_token: str) -> str:
    """Skips the current track and plays the next track."""
    return play_next_track(access_token)

@tool("play_previous_track", return_direct=True, args_schema=AccessToken)
def play_previous_track_tool(access_token: str, lyrics: str) -> str:
    """Plays the previous track."""
    return play_previous_track(access_token)

@tool("recommend_tracks_by_user_top_tracks", return_direct=True, args_schema=AccessToken)
def recommend_tracks_by_user_top_tracks_tool(access_token: str) -> str:
    """Recommends tracks to the user based on their current top tracks."""
    return recommend_tracks_by_user_top_tracks(access_token)

@tool("recommend_tracks_by_user_prompt", return_direct=True, args_schema=UserPrompt)
def recommend_tracks_by_user_prompt_tool(access_token: str, prompt: str) -> str:
    """Recommends tracks to the user based on their prompt."""
    return recommend_tracks_by_user_prompt(access_token, prompt)

@tool("recommend_tracks_by_genre", return_direct=True, args_schema=GenrePrompt)
def recommend_tracks_by_genre_tool(access_token: str, genre: str) -> str:
    """Recommends tracks to the user based on genre."""
    return recommend_tracks_by_genre(access_token, genre)

@tool("recommend_tracks_by_artist", return_direct=True, args_schema=Artist)
def recommend_tracks_by_artist_tool(access_token: str, artist: str) -> str:
    """Recommends tracks to the user based on artist."""
    return recommend_tracks_by_artist(access_token, artist)

music_player_tools = [
    play_song_by_name_tool,
    add_to_queue_song_by_name_tool,
    play_song_by_lyrics_tool,
    add_to_queue_song_by_lyrics_tool,
    play_song_by_name_and_artist_tool,
    add_to_queue_song_by_name_and_artist_tool,
    play_song_by_lyrics_and_artist_tool,
    add_to_queue_song_by_lyrics_and_artist_tool,
    get_song_lyrics_by_artist_and_song_name_tool,
    get_song_name_by_lyrics_and_artist_tool,
    get_song_lyrics_by_song_name_tool,
    get_song_name_by_lyrics_tool,
    start_playback_tool,
    pause_playback_tool,
    play_next_track_tool,
    play_previous_track_tool,
    recommend_tracks_by_user_top_tracks_tool,
    # recommend_tracks_by_user_prompt_tool
    recommend_tracks_by_genre_tool,
    recommend_tracks_by_artist_tool

]