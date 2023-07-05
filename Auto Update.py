import os
import time
import requests

def download_file(url, local_path):
    response = requests.get(url)
    with open(local_path, "wb") as file:
        file.write(response.content)

def download_repository_files(repository_url, local_path):
    response = requests.get(repository_url)
    if response.status_code == 200:
        json_response = response.json()
        for item in json_response:
            if item["type"] == "file":
                file_url = item["download_url"]
                file_name = item["name"]
                local_file_path = os.path.join(local_path, file_name)
                print("Downloading:", file_name)
                download_file(file_url, local_file_path)
    else:
        print("Cant download the latest Version!")

repository_url = "https://api.github.com/repos/pascaldercoole1/Roblox-Login/contents/Main"
local_path = os.path.expanduser("~/Roblox-Login")

if os.path.exists(local_path):

    dateien = os.listdir(local_path)

    for datei in dateien:
        datei_pfad = os.path.join(local_path, datei)
        os.remove(datei_pfad)

    os.rmdir(local_path)
    print("Clearing Old Data...")
else:
    print("Not Found! New User ;)")

print("Downloading Files...")
os.makedirs(local_path, exist_ok=True)
download_repository_files(repository_url, local_path)

print("All Files got downloaded.")


print("Staring latest Version...")

lokaler_pfad = os.path.expanduser("~/Roblox-Login")
datei_name = os.path.join(lokaler_pfad, "Main.py")

os.startfile(datei_name)
