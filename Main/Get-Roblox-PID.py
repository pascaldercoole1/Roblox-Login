import psutil
import time


while True:
    # Den Roblox-Prozess suchen
    prozesse = [p for p in psutil.process_iter(['name']) if p.info['name'] == "RobloxPlayerBeta.exe"]
    if len(prozesse) > 0:
        print("RobloxPlayerBeta.exe got found! PID:", prozesse[0].pid)
        print("Hello!")
        psutil.wait_procs(prozesse, timeout=None)
        print("RobloxPlayerBeta.exe got Closed!")
    else:
        print("RobloxPlayerBeta.exe was not found!")
    time.sleep(1)
