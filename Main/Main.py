import os
import requests
import webbrowser
import time
import json
import psutil
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Function to clear the terminal window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

print("Made by bossisback (https://github.com/pascaldercoole1/Roblox-Login)")

time.sleep(2)

clear()

with open('Version.txt', 'r') as file:
    FZ = file.readline()

if requests.get("https://raw.githubusercontent.com/pascaldercoole1/Roblox-Login/main/Main/Version.txt").text == FZ:
    ## Updated!
    print("Updated!")
    clear()
else:
    print("There is a new Version do you want to Download it?")
    newversionyorno = input("Yes (Y) / No (N): ")
    if newversionyorno == "Y" or newversionyorno == "y":
        local_path = os.path.expanduser("~\\Roblox-Login")
        print("Local path:", local_path)

        new_backup = os.path.join(local_path, "AutoUpdateBackup.py")
        os.startfile(new_backup)
        os.system("pause")


COOKIE_FILE_PATH = os.path.join(str(Path.home()), 'cookies.json')

def start_cookie(cookie_value, cookie_name, browser=None):

    if browser is None:
        options = Options()
        options.add_argument("--start-maximized")  
        browser = webdriver.Chrome(options=options)

    browser.get('https://www.roblox.com/Home')

    cookie = {
        'name': '.ROBLOSECURITY',
        'value': cookie_value,
        'domain': '.roblox.com',
        'path': '/',
    }

    browser.add_cookie(cookie)

    browser.refresh()

    print(f"Cookie Name: {cookie_name}")

    return browser

def save_Browser_Cookie(browser=None):

    if browser is None:
        options = Options()
        options.add_argument("--start-maximized")  
        browser = webdriver.Chrome(options=options)

    browser.get('https://www.roblox.com/Login')

    WebDriverWait(browser, float('inf')).until(
        lambda driver: "web.roblox.com/home" in driver.current_url or "www.roblox.com/home?nu=true" in driver.current_url
    )
    cookie_value = browser.get_cookie('.ROBLOSECURITY')['value']

    element = browser.find_element(By.XPATH, '//*[@id="right-navigation-header"]/div[2]/ul/div/a/span[2]')


    print("Name:", element.text)

    print(f"Cookie Name: {cookie_value}")

    loaded_cookies = load_cookies()

    text_without_at = element.text.replace("@", "")
    
    loaded_cookies.append({'name': text_without_at, 'value': cookie_value})
    save_cookies(loaded_cookies)

    return browser


def save_cookies(cookies):
    with open(COOKIE_FILE_PATH, 'w') as file:
        json.dump(cookies, file)

    print("Cookies saved successfully.")

def load_cookies():
    if not os.path.exists(COOKIE_FILE_PATH):
        print("No cookies have been saved.")
        return []


    with open(COOKIE_FILE_PATH, 'r') as file:
        cookies = json.load(file)

    print("Cookies loaded successfully.")
    return cookies

def delete_cookies():
    # Delete the cookie file if it exists
    if os.path.exists(COOKIE_FILE_PATH):
        confirmation = input("Are you sure you want to delete all cookies? (Y/N): ")
        if confirmation.lower() == 'y':
            os.remove(COOKIE_FILE_PATH)
            print("Cookies deleted successfully.")
        else:
            print("Deletion process canceled.")
    else:
        print("No cookies have been saved.")

def delete_cookie_by_name(cookie_name):
    loaded_cookies = load_cookies()
    filtered_cookies = [cookie for cookie in loaded_cookies if cookie['name'] != cookie_name]
    if len(loaded_cookies) == len(filtered_cookies):
        print(f"Cookie with name '{cookie_name}' was not found.")
    else:
        save_cookies(filtered_cookies)
        print(f"Cookie with name '{cookie_name}' deleted successfully.")

def update_all_cookies():
    loaded_cookies = load_cookies()
    if len(loaded_cookies) == 0:
        print("No cookies have been loaded.")
    else:
        browser = None
        for cookie in loaded_cookies:
            browser = start_cookie(cookie['value'], cookie['name'], browser)
        print("All cookies have been updated.")
        return [browser]

browsers = []

robloxProccesid = None
robloxProcces = None

while True:

    clear()  # Clear the terminal window

    print("Version: 0.4")

    print("Warning:")
    print("- Never Click Logout or your Cookie will be unusable")
    print("- Dont Close the Python App while having a Browser open (it will Crash)")

    print("----------------------------------------------------------------------------------------------")

    loaded_cookies = load_cookies()
    total_cookies = len(loaded_cookies)

    print(f"Cookies Loaded: {total_cookies}")

    print("----------------------------------------------------------------------------------------------")

    print("Cookie Management:")
    print("1. Start a Cookie")
    print("2. Login")
    print("3. Save a Cookie")
    print("4. Show All Cookies")
    print("5. Delete Cookie by Name")
    print("6. Delete all Cookies")
    print("7. Update All Cookies")
    print("8. Quit Program")
    ##print("I. Get Roblox Informations")
    print("X. Kill Roblox")

    choice = input("Select an option (1-8): ")

    if choice == '1':
        clear()  # Clear the terminal window
        loaded_cookies = load_cookies()
        if len(loaded_cookies) == 0:
            print("No cookies have been loaded.")
        else:
            print("Loaded Cookies:")
            for i, cookie in enumerate(loaded_cookies):
                print(f"{i + 1}. Cookie Name: {cookie['name']}")

            cookie_choice = input("Select a cookie to start (1-{}): ".format(len(loaded_cookies)))
            cookie_index = int(cookie_choice) - 1

            if 0 <= cookie_index < len(loaded_cookies):
                browser = start_cookie(loaded_cookies[cookie_index]['value'], loaded_cookies[cookie_index]['name'])
                browsers.append(browser)
            else:
                print("Invalid selection. Please try again.")
    elif choice == '2':
        clear()  # Clear the terminal window
        save_Browser_Cookie()
    elif choice == '3':
        clear()  # Clear the terminal window
        cookie_name = input("Enter the name of the cookie: ")
        cookie_value = input("Enter the cookie value: ")
        loaded_cookies = load_cookies()
        loaded_cookies.append({'name': cookie_name, 'value': cookie_value})
        save_cookies(loaded_cookies)
    elif choice == '4':
        clear()  # Clear the terminal window
        loaded_cookies = load_cookies()
        if len(loaded_cookies) == 0:
            print("No cookies have been loaded.")
        else:
            print("Saved Cookies:")
            for i, cookie in enumerate(loaded_cookies):
                print(f"{i + 1}. Cookie Name: {cookie['name']}")
            input("Press Enter to continue...")
    elif choice == '5':
        clear()  # Clear the terminal window
        cookie_name = input("Enter the name of the cookie to delete: ")
        delete_cookie_by_name(cookie_name)
        input("Press Enter to continue...")
    elif choice == '6':
        clear()  # Clear the terminal window
        delete_cookies()
        input("Press Enter to continue...")
    elif choice == '7':
        clear()  # Clear the terminal window
        browsers = update_all_cookies()
        input("Press Enter to continue...")
    elif choice == '8':
        clear()  # Clear the terminal window
        for browser in browsers:
            browser.quit()
        print("Goodbye!")
        time.sleep(1)
        break
    elif choice == 'X':

        prozesse = [p for p in psutil.process_iter(['name']) if p.info['name'] == "RobloxPlayerBeta.exe"]

        if len(prozesse) > 0:
            robloxProccesid = prozesse[0].pid
            robloxProcces = prozesse[0]

            clear()  # Clear the terminal window
            if robloxProcces and robloxProccesid:
                try:
                    robloxProcces.terminate()
                    print("Roblox-Prozess Terminated.")
                    robloxProcces = None
                    robloxProccesid = None
                except psutil.NoSuchProcess:
                    print("The Roblox Prozess got terminated!")
                    robloxProcces = None
                    robloxProccesid = None
                    time.sleep(2)
            else:
                print("No Roblox-Prozess Found!")
                time.sleep(2)
    elif choice == 'I':
        clear()
        prozesse = [p for p in psutil.process_iter(['name']) if p.info['name'] == "RobloxPlayerBeta.exe"]

        if len(prozesse) > 0:
            roblox_prozess = prozesse[0]
            pid = roblox_prozess.pid

            print("Roblox-Prozess Found! PID:", pid)

            prozess_info = roblox_prozess.as_dict(attrs=['status', 'cpu_percent', 'memory_info', 'ppid', 'create_time', 'cmdline'])

            status = prozess_info['status']
            cpu_percent = prozess_info['cpu_percent']
            memory_info = prozess_info['memory_info']
            ppid = prozess_info['ppid']
            create_time = prozess_info['create_time']
            cmdline = prozess_info['cmdline']

            print("Status:", status)
            print("CPU-utilization:", cpu_percent, "%")
            print("StorageInfo:", memory_info)
            print("parentprozess PID:", ppid)
            print("acceleration time:", time.ctime(create_time))
            print("CmdLine Aguments:", cmdline)

            ## psutil.wait_procs(prozesse, timeout=None)
        else:
            print("Roblox-Prozess not Found!.")

        input("Press Enter to continue...")
    elif choice == 'SRM':
        clear()        
        print("Loading...")
        lokaler_pfad = os.path.expanduser("~/Roblox-Login")
        datei_name = os.path.join(lokaler_pfad, "Get-Roblox-PID.py")
        os.startfile(datei_name)
        time.sleep(1)

    elif choice == 'SRMV2':
        clear()        
        print("Loading...")
        lokaler_pfad = os.path.expanduser("~/Roblox-Login")
        datei_name = os.path.join(lokaler_pfad, "Get-Roblox-PIDV2.py")
        os.startfile(datei_name)
        time.sleep(1)
    else:
        clear()  
