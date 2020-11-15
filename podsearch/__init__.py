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

# movie	movieArtist, movie
# podcast	podcastAuthor, podcast
# music	musicArtist, musicTrack, album, musicVideo, mix, song
# Please note that “musicTrack” can include both songs and music videos in the results
# musicVideo	musicArtist, musicVideo
# audiobook	audiobookAuthor, audiobook
# shortFilm	shortFilmArtist, shortFilm
# tvShow	tvEpisode, tvSeason
# software	software, iPadSoftware, macSoftware
# ebook	ebook
# all	movie, album, allArtist, podcast, musicVideo, mix, audiobook, tvSeason, allTrack
