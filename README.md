# CLDF to Anki
 Python script to generate an [Anki](https://apps.ankiweb.net/) deck from a [Cross-Linguistic Data Formats](https://github.com/cldf/cldf) (CLDF) dictionary.
 
## Requirements
* Python 3
   * [genanki](https://github.com/kerrickstaley/genanki) (a Python 3 library for generating Anki decks)
   * pandas
   * json
   * re
   * random

## How-to
1. Choose a dictionary on https://dictionaria.clld.org/contributions.
2. Follow the dictionary's `DOI` link to Zenodo (e.g., [DOI: 10.5281/zenodo.3067648](https://zenodo.org/record/3258853)).
3. Download the dictionary's `.zip` file (e.g., dictionaria-hdi-b795079.zip)
4. Unzip the contents to a handy directory and copy the path to your clipboard.
5. Run the Python script `cldf_to_anki.py`.
6. Follow the prompts to:
   * Paste the path to your dictionary's `json` and `csv` files
   * Name your Anki deck
   * Save deck as...
7. Import your newly created deck (`.apkg` file) into Anki.
8. Study!
