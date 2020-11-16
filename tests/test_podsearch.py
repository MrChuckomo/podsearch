"""
File         : test_podsearch.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 16-Nov-2020
"""

import os
import sys
import json
import pytest

TEST_CTX = os.path.dirname(os.path.abspath(__file__))

sys.path.append(f'{TEST_CTX}{os.sep}..')

from podsearch import Media
from podsearch.podsearch import PodSearch


# ---------------------------------------------------------------------------------------------------------------------

def get_test_data(key):
    with open(f'{TEST_CTX}{os.sep}test_data.json', 'r') as f:
        data = json.load(f)

    return data[key]

RESULT_KEYS = get_test_data('result_keys')

# ---------------------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize('query', get_test_data('query'))
def test_all(query):
    data = PodSearch('Tim').search()
    assert isinstance(data, dict)
    assert list(data.keys()) == RESULT_KEYS

@pytest.mark.parametrize('query', get_test_data('query'))
def test_podcast(query):
    data = PodSearch('Tim', media=Media.PODCAST).search()
    assert isinstance(data, dict)
    assert list(data.keys()) == RESULT_KEYS

    data = PodSearch.podcast('Freakshow').search()
    assert isinstance(data, dict)
    assert list(data.keys()) == RESULT_KEYS

@pytest.mark.parametrize('query', get_test_data('query'))
def test_podcast_author(query):
    data = PodSearch.podcast_author('Tim').search()
    assert isinstance(data, dict)
    assert list(data.keys()) == RESULT_KEYS
