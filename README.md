# projectredstoneworld.github.io

To anyone lurking, this was originally setup by my friend Lenni and now I'm trying to customize it, enjoy watching me struggle trying to understand what I'm doing

## Wiki archive

The pages in `_wiki` were imported from the former Fandom wiki and are published under `/wiki/`. They can be edited directly as normal Markdown files.

To rebuild all imported articles from another MediaWiki XML export:

```sh
python3 scripts/import_fandom.py path/to/export.xml
```

The importer replaces the generated `_wiki` directory, so commit any manual article changes before running it. MediaWiki XML exports do not contain the uploaded image files. Recovered wiki images are stored in `wiki/assets/images`, and their original Fandom filenames are mapped in the importer.
