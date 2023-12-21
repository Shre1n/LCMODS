# Name der Datei, die die Mod-Liste enthält
datei_pfad = "Overview_Names.txt"

# Liste von Mod-Namen aus der Datei einlesen
with open(datei_pfad, 'r') as file:
    mod_list = [line.strip() for line in file]

# Jeden Mod-Namen formatieren
formatierte_mod_liste = ['"{0}",'.format(mod) for mod in mod_list]

# Ergebnisse in die gleiche Datei schreiben
with open(datei_pfad, 'w') as file:
    for mod in formatierte_mod_liste:
        file.write(mod + '\n')