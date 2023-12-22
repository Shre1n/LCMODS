import json

# Name der Datei, die die Mod-Liste enthält
datei_pfad = "Overview_Names.txt"

#working

# Liste von Mod-Namen aus der Datei einlesen
with open(datei_pfad, 'r') as file:
    mod_list = [line.strip() for line in file]

mod_json = {
    "name": "random",
    "version_number": "1.0.0",
    "website_url": "https://github.com/thunderstore-io",
    "description": "Mods for playing Company on demand.",
    "dependencies": mod_list
}

# JSON-Objekt als manifest.json speichern
with open('manifest.json', 'w') as json_file:
    json.dump(mod_json, json_file, indent=2)
