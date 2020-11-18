"""
File         : podsearch-cli.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 12-Nov-2020
"""

import click

from podsearch import Media
from podsearch.podsearch import PodSearch

# ---------------------------------------------------------------------------------------------------------------------

def get_media_choices():
    return [media.value for media in Media]

def get_media(value):
    for media in Media:
        if value == media.value:
            return media

    return None


# ---------------------------------------------------------------------------------------------------------------------

@click.command()
@click.option("--term", "-t", type=click.STRING, required=True, help="Enter your search term!")
@click.option("--media", "-m", type=click.Choice(get_media_choices()), default=Media.PODCAST.value, help="Media category", show_default=True)
def search(term, media):
    PodSearch(term, media=get_media(media)).search()

if __name__ == "__main__":
    search()
    # PodSearch('Tim').search()
    # PodSearch('Tim', media=Media.PODCAST).search()
    # PodSearch.podcast_author('Tim').search()
    # PodSearch.podcast('Freakshow').search()

