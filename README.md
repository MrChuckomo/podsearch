# podsearch

Search for Podcasts (like in the iTunes store)

```bash
podsearch-cli.py -t freakshow 
podsearch-cli.py -t freakshow -m podcast
podsearch-cli.py -t freakshow -m music
podsearch-cli.py -t freakshow -m ebook
```

## Help

```bash
Usage: podsearch-cli.py [OPTIONS]

Options:
  -t, --term TEXT                 Enter your search term!  [required]
  -m, --media [movie|podcast|music|musicVideo|audiobook|shortFilm|tvShow|software|ebook|all]
                                  Media category  [default: podcast]
  --help                          Show this message and exit.
```