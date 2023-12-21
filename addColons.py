import json

# Name der Datei, die die Mod-Liste enthält
datei_pfad = "Overview_Names.txt"

# Liste von Mod-Namen aus der Datei einlesen
with open(datei_pfad, 'r') as file:
    mod_list = [line.strip() for line in file]

# Jeden Mod-Namen formatieren
formatierte_mod_liste = ['"{0}",'.format(mod) for mod in mod_list]

with open(datei_pfad, 'w') as file:
    for mod in formatierte_mod_liste:
        if not mod.startswith('"'):
            # Wenn der Mod-Name nicht mit Anführungszeichen beginnt, formatiere ihn entsprechend
            mod = '"{0}",'.format(mod.strip())
        file.write(mod + '\n')

# JSON-Objekt erstellen
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
