import os
import platform
import psutil
import time
import re
import datetime

while True:
    # Den Roblox-Prozess suchen
    prozesse = [p for p in psutil.process_iter(['name']) if p.info['name'] == "RobloxPlayerBeta.exe"]
    if len(prozesse) > 0:
        #print("RobloxPlayerBeta.exe got found! PID:", prozesse[0].pid)
        #print("Hello!")
        roblox_prozess = prozesse[0]
        pid = roblox_prozess.pid

        prozess_info = roblox_prozess.as_dict(attrs=['status', 'cpu_percent', 'memory_info', 'ppid', 'create_time', 'cmdline'])

        status = prozess_info['status']
        cpu_percent = prozess_info['cpu_percent']
        memory_info = prozess_info['memory_info']
        ppid = prozess_info['ppid']
        create_time = prozess_info['create_time']
        cmdline = prozess_info['cmdline']

        username = os.getlogin()
        print("User:", username)

        process = psutil.Process(pid)
        architecture = platform.architecture()[0]

        if architecture == '32bit':
            print("RobloxPlayerBeta.exe got found! PID:", pid, " (32bit, Byfron was not Found!)")
        elif architecture == '64bit':
            print("RobloxPlayerBeta.exe got found! PID:", pid, " (64bit, Byfron Found!)")
        else:
            print("RobloxPlayerBeta.exe got found! PID:", pid)

        

        #print("Status:", status)
        #print("CPU-utilization:", cpu_percent, "%")
        #print("StorageInfo:", memory_info)
        #print("parentprozess PID:", ppid)
        #print("acceleration time:", time.ctime(create_time))
        #print("CmdLine Aguments:", cmdline)

        cmdline_string = cmdline[5]

        GameData = cmdline_string.replace("[", "").replace("]", "")

        place_id = re.search(r"placeId=(\d+)", GameData)
        if place_id:
            place_id = place_id.group(1)
            print(f"placeId: {place_id}")
        else:
            print("Keine placeId gefunden.")


        match = re.search(r'isPlayTogetherGame=(\w+)', cmdline_string)
        if match:
            is_play_together_game = match.group(1)
            print("PlayTogetherGame:",is_play_together_game)

        cmdline_string2 = ' '.join(cmdline)  # Befehlszeile zu einem String konvertieren
        launchtime_match = re.search(r'launchtime=([^&]+)', cmdline_string2)

        cmdline_launch_timestring = ' '.join(cmdline)
        launch_time = re.search(r'--launchtime=(\w+)', cmdline_launch_timestring)

        if launch_time:
            launch_time_value = int(launch_time.group(1))

            launch_time = datetime.datetime.utcfromtimestamp(launch_time_value / 1000.0)

            formatted_time = launch_time.strftime("%Y-%m-%d %H:%M:%S")
            print("Launch Time:", formatted_time, "(", launch_time_value, ")")
        else:
            print("No Launch Time!")

        pattern = r'Versions\\version-(\w+)'
        match = re.search(pattern, cmdline[0])

        if match:
            roblox_version = match.group(1)
            print("Roblox-Version:", roblox_version)
        else:
            print("Roblox-Version nicht gefunden.")

        
        psutil.wait_procs(prozesse, timeout=None)
        print("RobloxPlayerBeta.exe got Closed!")
    else:
        print("RobloxPlayerBeta.exe was not found!")
    time.sleep(1)

