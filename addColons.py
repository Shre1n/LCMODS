import json

# Name der Datei, die die Mod-Liste enthält
datei_pfad = "Overview_Names.txt"
manifest_json = "manifest.json"

# Liste von Mod-Namen aus der Datei einlesen
with open(datei_pfad, 'r') as file:
    mod_list = [line.strip() for line in file]

# Formatieren der Mod-Namen, falls noch nicht im gewünschten Format
formatierte_mod_liste = ['"{0}",'.format(mod) if not mod.startswith('"') else mod for mod in mod_list]

# Verbinde die formatierten Mod-Namen mit neuen Zeilenzeichen
mod_names_as_text = ",\n".join(formatierte_mod_liste)

with open(datei_pfad, 'w') as file:
    for mod in formatierte_mod_liste:
        file.write(mod + "\n")

mod_json = {
    "name": "random",
    "version_number": "1.0.0",
    "website_url": "https://github.com/Shre1n/LCMODS",
    "description": "Mods for playing Company on demand.",
    "dependencies": formatierte_mod_liste
}

# Laden der JSON-Datei oder Erstellen eines leeren Manifests, wenn die Datei nicht vorhanden ist
try:
    with open(manifest_json, 'r') as file:
        manifest_data = json.load(file)
except FileNotFoundError:
    manifest_data = {"dependencies": []}

# Extrahieren der Dependencies-Liste aus dem JSON
dependencies_list = manifest_data.get("dependencies", [])

# Formatieren der Dependencies
formatted_dependencies = [dep.strip('",') for dep in dependencies_list]

# Aktualisieren des manifest_data mit den neu formatierten Dependencies
manifest_data["dependencies"] = formatted_dependencies

# Speichern des aktualisierten JSON in der Datei
with open(manifest_json, 'w') as json_file:
    json.dump(manifest_data, json_file, indent=2)
