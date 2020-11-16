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


# ---------------------------------------------------------------------------------------------------------------------

class PodSearch():

    def __init__(self, term: str, media: Media=None, entity: Entity=None):
        self._term_ = term
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

        # NOTE: Output
        print(f'\nPodcasts ({self._get_value_(data, "resultCount")}): ')
        if self._get_value_(data, 'results'):
            for idx, result in enumerate(self._get_value_(data, 'results')):
                print(
                    idx + 1,
                    '- 🧑‍🎨',
                    self._get_value_(result, 'artistName'),
                    '- 📚',
                    self._get_value_(result, 'collectionName'),
                    '- 🔞',
                    self._get_value_(result, 'contentAdvisoryRating'),
                    '- 🌍',
                    self._get_value_(result, 'country'),
                    '- 🎦',
                    self._get_value_(result, 'primaryGenreName')
                )

        return data


    # ---------------------------------------------------------------------------------------------------------------------
    # NOTE: Private

    def _build_uri_(self):
        uri = f'{SEARCH_URL}term={self._term_}'

        if self._media_:
            uri += f'&media={self._media_.value}'

        if self._entity_:
            uri += f'&entity={self._entity_.value}'

        return uri


    @staticmethod
    def _get_value_(data, key):
        try:
            return data[key]
        except KeyError:
            return None
