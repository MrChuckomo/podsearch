"""
File         : podsearch.py
Description  :

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 12-Nov-2020
"""

import json
import requests

from podsearch import Media
from podsearch import Entity
from podsearch import SEARCH_URL
from podsearch.pretty_print import Stdout
from podsearch.pretty_print import AnsiColor as c
from podsearch.pretty_print import ColorPrint


# ---------------------------------------------------------------------------------------------------------------------

class PodSearch():

    def __init__(self, term: str, limit: int=10, media: Media=None, entity: Entity=None):
        self._term_ = term
        self._limit_ = limit
        self._media_ = media
        self._entity_ = entity

    @classmethod
    def podcast(cls, term: str):
        return cls(term, media=Media.PODCAST, entity=None)

    @classmethod
    def podcast_author(cls, term: str):
        return cls(term, media=Media.PODCAST, entity=Entity.Podcast.PODCASTAUTHOR)

    def search(self):
        url = self._build_uri_()

        payload = {}
        headers = {
            'Cookie': 'geo=DE'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)

        self._print_output_(data)        

        return data


    # ---------------------------------------------------------------------------------------------------------------------
    # NOTE: Private

    def _print_output_(self, data):
        res_count = self._get_value_(data, "resultCount")
        ColorPrint.cyan(f'\nPodcasts ({res_count}): ')

        if self._get_value_(data, 'results'):
            for idx, result in enumerate(self._get_value_(data, 'results')):

                rating = self._get_value_(result, 'contentAdvisoryRating').upper()

                Stdout.heading(f'Item {idx + 1}/{res_count}:', end=' ')
                Stdout.indent(self._get_value_(result, 'collectionName'), pre='', end=' ')
                if rating.lower() == 'clean':
                    Stdout.flag(rating)
                else: 
                    Stdout.flag(rating, color=c.REDBOLD)
                Stdout.indent('{} - {} - {} - {}'.format(
                    self._get_value_(result, 'kind'),
                    self._get_value_(result, 'artistName'),
                    self._get_value_(result, 'primaryGenreName'),
                    self._get_value_(result, 'country'),
                ))

    def _build_uri_(self):
        uri = f'{SEARCH_URL}term={self._term_}'

        if self._media_:
            uri += f'&media={self._media_.value}'

        if self._entity_:
            uri += f'&entity={self._entity_.value}'

        if self._limit_:
            uri += f'&limit={self._limit_}'

        # uri += f'&sort=kind'

        return uri


    @staticmethod
    def _get_value_(data, key):
        try:
            return data[key]
        except KeyError:
            return None
