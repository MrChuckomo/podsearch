"""
File         : podsearch-cli.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 12-Nov-2020
"""

from podsearch.podsearch import PodSearch

# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    PodSearch.author('Tim')
    PodSearch.search('freakshow')

