"""
File         : podsearch-cli.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 12-Nov-2020
"""

from podsearch import Media
from podsearch.podsearch import PodSearch

# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    PodSearch('Tim').search()
    PodSearch('Tim', media=Media.PODCAST).search()
    PodSearch.podcast_author('Tim').search()
    PodSearch.podcast('Freakshow').search()

