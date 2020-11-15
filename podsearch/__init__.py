"""
File         : __init__.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 11-Nov-2020
"""

from enum import Enum


# ---------------------------------------------------------------------------------------------------------------------

SEARCH_URL = 'https://itunes.apple.com/search?'


class Media(Enum):
    MOVIE = 'movie'
    PODCAST = 'podcast'
    MUSIC = 'music'
    MUSICVIDEO = 'musicVideo'
    AUDIOBOOK = 'audiobook'
    SHORTFILM = 'shortFilm'
    TVSHOW = 'tvShow'
    SOFTWARE = 'software'
    EBOOK = 'ebook'
    ALL = 'all'


class Entity():
    class Movie(Enum):
        MOVIEARTIST = 'movieArtist'
        MOVIE = 'movie'

    class Podcast(Enum):
        PODCASTAUTHOR = 'podcastAuthor'
        PODCAST = 'podcast'

    class Music(Enum):
        MUSICARTIST = 'musicArtist'
        MUSICTRACK = 'musicTrack'
        ALBUM = 'album'
        MUSICVIDEO = 'musicVideo'
        MIX = 'mix'
        SONG = 'song'

    class MusicVideo(Enum):
        MUSICARTIST = 'musicArtist'
        MUSICVIDEO = 'musicVideo'

    class Audiobook(Enum):
        AUDIOBOOKAUTHOR = 'audiobookAuthor'
        AUDIOBOOK = 'audiobook'

    class ShortFilm(Enum):
        SHORTFILMARTIST = 'shortFilmArtist'
        SHORTFILM = 'shortFilm'

    class TvShow(Enum):
        TVEPISODE = 'tvEpisode'
        TVSEASON = 'tvSeason'

    class Software(Enum):
        SOFTWARE = 'software'
        IPADSOFTWARE = 'iPadSoftware'
        MACSOFTWARE = 'macSoftware'

    class Ebook(Enum):
        EBOOK = 'ebook'

    class All(Enum):
        MOVIE = 'movie'
        ALBUM = 'album'
        ALLARTIST = 'allArtist'
        PODCAST = 'podcast'
        MUSICVIDEO = 'musicVideo'
        MIX = 'mix'
        AUDIOBOOK = 'audiobook'
        TVSEASON = 'tvSeason'
        ALLTRACK = 'allTrack'
