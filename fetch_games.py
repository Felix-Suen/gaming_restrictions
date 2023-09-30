# this script only runs once a day
import os

game_dir = 'D:\SteamLibrary\steamapps\common'
exceptions = ['UnityCrashHandler64.exe', 'Social-Club-Setup.exe', 'Rockstar-Games-Launcher.exe']
blocked_apps_file = './blocked_apps.txt'

# find the correct game exe launcher
def find_exe_files(directory):
    exe = ''
    biggest_size = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file not in exceptions and file.endswith('.exe'):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if biggest_size < file_size:
                    biggest_size = file_size
                    exe = file
    return exe

# find the exe in each gaming folder, and write them into the txt file
def fetch_games():
    txt_file = open(blocked_apps_file, 'w')

    for game_folder in os.listdir(game_dir):
        game_path = os.path.join(game_dir, game_folder)
        if os.path.isdir(game_path):
            exe_file = find_exe_files(game_path)
            if exe_file:
                txt_file.write('%s, ' % exe_file)
    
    txt_file.close()

fetch_games()