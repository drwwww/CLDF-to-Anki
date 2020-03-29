import pandas, json, genanki, re, random

# Creates an Anki deck from a Cross-linguistic Data Formats (CLDF) dictionary

path_to_metadata = input("Path to cldf folder json and csv files (ending in slash): ")
metadata_file = path_to_metadata + "Dictionary-metadata.json"

# Anki model
model_id = random.randrange(1 << 30, 1 << 31)
my_model= genanki.Model(
	model_id,
	'Simple Model',
	fields=[
		{'name': 'Question'},
		{'name': 'Answer'},
	],
	templates=[
		{
			'name': 'Card 1',
			'qfmt': '{{Question}}',
			'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
		},
	])

# Anki deck
print()
deck_name = str(input("Name your Anki deck: "))
deck_id = random.randrange(1 << 30, 1 << 31)
my_deck = genanki.Deck(
  deck_id,
  deck_name)

# Read json to get csv's
with open(metadata_file) as json_file:
	data = json.load(json_file)
	title = data['dc:title']
	entries_num = data['tables'][0]['dc:extent']
	print()
	print("Creating deck based on: {} ({} entries)".format(title, entries_num)) # Print dictionary name
	print()

# Read csv's with pandas

## Assign csv variables
entries_csv = path_to_metadata + "entries.csv"
#examples_csv = path_to_metadata + "examples.csv"
#languages_csv = path_to_metadata + "languages.csv"
#media_csv = path_to_metadata + "media.csv"
senses_csv = path_to_metadata + "senses.csv"

## Read csvs
entries = pandas.read_csv(entries_csv)
# examples = pandas.read_csv(examples_csv)
# languages = pandas.read_csv(languages_csv)
# media = pandas.read_csv(media_csv)
senses = pandas.read_csv(senses_csv)

print("Creating notes...")
for row in senses.itertuples(): # Senses
	description_raw = getattr(row, "Description")
	alt_translation_raw = getattr(row, "alt_translation1")
	description = re.sub('\[|\]', '', str(description_raw))
	alt_translation = re.sub('\[|\]', '', str(alt_translation_raw))

	entry_id = getattr(row, "Entry_ID")
	
	headword_raw = entries.loc[entries['ID'] == entry_id, ['Headword']].values[0]
	headword = headword_raw[0]
	part_of_speech_raw = entries.loc[entries['ID'] == entry_id, ['Part_Of_Speech']].values[0]
	part_of_speech = part_of_speech_raw[0]
	#headword = entry['Headword']

	# Printing
	# if "nan" not in str(alt_translation):
	# 	print("{} ({}) - {}; {}".format(headword,part_of_speech,description,alt_translation))
	# else:
	# 	print("{} ({}) - {}".format(headword,part_of_speech,description))

	note_front = "{} ({})".format(headword,part_of_speech)

	if "nan" not in str(alt_translation):
		note_back = "{}; {}".format(description,alt_translation)
	else:
		note_back = "{}".format(description)

# Build Anki notes with genanki
	my_note = genanki.Note(
		model=my_model,
		fields=[note_front, note_back])

# Create Anki deck
	my_deck.add_note(my_note)

# Export Anki deck
print()
deck_filename = str(input("Save deck as (without extenion): "))
deck_ext = ".apkg"
deck_fullname = deck_filename + deck_ext
genanki.Package(my_deck).write_to_file(deck_fullname)
print()
print("Deck saved as {}".format(deck_fullname)) # Check user folder