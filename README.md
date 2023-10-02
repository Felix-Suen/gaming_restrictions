# gaming_restrictions
Addicted to gaming, and it must stop

* `fetch_games.py` scans the steam folder for game executables and write them to `blocked_app.txt`.
* `restrict.py` scans the list of programs currently running and block them if its on the list
* Set up task scheduler on windows to run them periodically
