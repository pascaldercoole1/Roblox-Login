import os
import webbrowser
import time
import json
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Function to clear the terminal window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Starting")
time.sleep(0.3)
clear()
print("Starting.")
time.sleep(0.3)
clear()
print("Starting..")
time.sleep(0.3)
clear()
print("Starting...")
time.sleep(0.3)
clear()

print("Made by bossisback (https://github.com/pascaldercoole1/Roblox-Login)")

time.sleep(2)

clear()

# Path to the cookie file in the user's home directory
COOKIE_FILE_PATH = os.path.join(str(Path.home()), 'cookies.json')

def start_cookie(cookie_value, cookie_name, browser=None):
    # Path to the Chrome Webdriver
    webdriver_path = '/path/to/chromedriver'

    # Open the browser if not already opened
    if browser is None:
        options = Options()
        options.add_argument("--start-maximized")  # Maximize the browser window
        browser = webdriver.Chrome(options=options)

    # Go to the Roblox website
    browser.get('https://www.roblox.com/Home')

    # Create the cookie
    cookie = {
        'name': '.ROBLOSECURITY',
        'value': cookie_value,
        'domain': '.roblox.com',
        'path': '/',
    }

    browser.add_cookie(cookie)

    # Refresh the page
    browser.refresh()

    # Print the cookie name
    print(f"Cookie Name: {cookie_name}")

    return browser

def save_cookies(cookies):
    # Save the cookies to the file
    with open(COOKIE_FILE_PATH, 'w') as file:
        json.dump(cookies, file)

    print("Cookies saved successfully.")

def load_cookies():
    # Check if the cookie file exists
    if not os.path.exists(COOKIE_FILE_PATH):
        print("No cookies have been saved.")
        return []

    # Load cookies from the file
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

# Main program
browsers = []

while True:
    clear()  # Clear the terminal window

    print("Warning:")
    print("- Never Click Logout or your Cookie will be unusable")
    print("- Dont Close the Python App while having a Browser open (it will Crash)")

    print("----------------------------------------------------------------------------------------------")

    print("Cookie Management:")
    print("1. Start a Cookie")
    print("2. Save a Cookie")
    print("3. Show All Cookies")
    print("4. Delete Cookie by Name")
    print("5. Delete all Cookies")
    print("6. Update All Cookies")
    print("7. Quit Program")

    choice = input("Select an option (1-7): ")

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
        cookie_name = input("Enter the name of the cookie: ")
        cookie_value = input("Enter the cookie value: ")
        loaded_cookies = load_cookies()
        loaded_cookies.append({'name': cookie_name, 'value': cookie_value})
        save_cookies(loaded_cookies)
    elif choice == '3':
        clear()  # Clear the terminal window
        loaded_cookies = load_cookies()
        if len(loaded_cookies) == 0:
            print("No cookies have been loaded.")
        else:
            print("Saved Cookies:")
            for i, cookie in enumerate(loaded_cookies):
                print(f"{i + 1}. Cookie Name: {cookie['name']}")
            input("Press Enter to continue...")
    elif choice == '4':
        clear()  # Clear the terminal window
        cookie_name = input("Enter the name of the cookie to delete: ")
        delete_cookie_by_name(cookie_name)
        input("Press Enter to continue...")
    elif choice == '5':
        clear()  # Clear the terminal window
        delete_cookies()
        input("Press Enter to continue...")
    elif choice == '6':
        clear()  # Clear the terminal window
        browsers = update_all_cookies()
        input("Press Enter to continue...")
    elif choice == '7':
        clear()  # Clear the terminal window
        for browser in browsers:
            browser.quit()
        print("Goodbye!")
        time.sleep(1)
        break
    else:
        clear()  # Clear the terminal window
        print("Invalid selection. Please try again. (3)")
        time.sleep(1)
        clear()  # Clear the terminal window
        print("Invalid selection. Please try again. (2)")
        time.sleep(1)
        clear()  # Clear the terminal window
        print("Invalid selection. Please try again. (1)")
        time.sleep(1)
        clear()  # Clear the terminal window
