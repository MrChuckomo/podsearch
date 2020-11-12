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

    def __init__(self):
        pass

    @staticmethod
    def search(term):

        # url = "https://itunes.apple.com/search?term=freakshow&media=podcast"
        # url = f'{SEARCH_URL}term={term}&media=podcast&country=de'
        url = f'{SEARCH_URL}term={term}&media=podcast'

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
                result['artistName'],
                '- 📚',
                result['collectionName'],
                '- 🔞',
                result['contentAdvisoryRating'],
                '- 🌍',
                result['country'],
                '- 🎦',
                result['primaryGenreName']
            )


    @staticmethod
    def author(term):

        # url = "https://itunes.apple.com/search?term=freakshow&media=podcast"
        url = f'{SEARCH_URL}term={term}&media=podcast&entity=podcastAuthor'

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
