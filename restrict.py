import datetime
import psutil
import os

start = datetime.time(0, 0, 0)
end = datetime.time(19, 0, 0)
blocked_apps_file = './blocked_apps.txt'

# read the list of apps that are blocked from the blocked list
def read_from_txt():
    with open(blocked_apps_file) as f:
        restricted_apps = f.readline().split(', ')
    restricted_apps.pop(len(restricted_apps) - 1)
    return restricted_apps

# check if the time is within the scheduled block time
def is_within_restriction():
    current_time = datetime.datetime.now().time()
    return current_time >= start and current_time <= end

# if gaming, don't
def app_restrict():
    restricted_apps = read_from_txt()
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name']
            if process_name in restricted_apps and is_within_restriction():
                print(f"Restricting {process_name} (PID: {process.info['pid']})")
                os.system(f"taskkill /F /PID {process.info['pid']}")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print("error occurred")

app_restrict()