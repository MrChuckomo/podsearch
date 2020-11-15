"""
File         : podsearch.py
Description  :

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 12-Nov-2020
"""

import json
import requests

from podsearch import SEARCH_URL


# ---------------------------------------------------------------------------------------------------------------------

class PodSearch():

    def __init__(self, term):
        self._term_ = term

    def search(self):

        # url = "https://itunes.apple.com/search?term=freakshow&media=podcast"
        # url = f'{SEARCH_URL}term={self._term_}&media=podcast&country=de'
        url = f'{SEARCH_URL}term={self._term_}&media=podcast'

        payload = {}
        headers = {
            'Cookie': 'geo=DE'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data = json.loads(response.text)

        # NOTE: Output

        # print(response.text.encode('utf8'))
        print(f'\nPodcasts ({data["resultCount"]}): ')
        for idx, result in enumerate(data['results']):
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

    def author(self):

        # url = "https://itunes.apple.com/search?term=freakshow&media=podcast"
        url = f'{SEARCH_URL}term={self._term_}&media=podcast&entity=podcastAuthor'

        payload = {}
        headers = {
            'Cookie': 'geo=DE'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data = json.loads(response.text)

        # NOTE: Output

        print(f'\nArtists ({data["resultCount"]}): ')
        for idx, result in enumerate(data['results']):
            print(idx + 1, '- 🧑‍🎨', result['artistName'])


    # ---------------------------------------------------------------------------------------------------------------------
    # NOTE: Private

    @staticmethod
    def _get_value_(data, key):
        try:
            return data[key]
        except KeyError:
            return None
