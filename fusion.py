import time
import os
import json
import sys
import datetime
import shutil

copyright = "Copyright Wintercat Development Digital © 2026."
post_cr = "Made, Developed, Managed, Updated, and Secured by Wintercat Development."

neofetch_art = r"""
███████╗██╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗
██╔════╝██║   ██║██╔════╝██║██╔═══██╗████╗  ██║
█████╗  ██║   ██║███████╗██║██║   ██║██╔██╗ ██║
██╔══╝  ██║   ██║╚════██║██║██║   ██║██║╚██╗██║
██║     ╚██████╔╝███████║██║╚██████╔╝██║ ╚████║
╚═╝      ╚═════╝ ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""

os.system("cls" if os.name == "nt" else "clear")


print("Checking dir...")
time.sleep(.6)
if os.path.exists("system/config.json"):
    print("[OK] system/config.json")
else:
    print("[FAILED] system/config.json")
    answer = input("fusion > System not installed. Would you like to install it? [y/n]")
    if answer == "y":
        print("Thanks for choosing")
        print(neofetch_art)
        time.sleep(3)
        print("Starting install...")
        time.sleep(.5)
        os.makedirs("system", exist_ok=True)
        print("Creating configuration...")
        data = {
            "install_finished": True,
            "version_identifier": "0.1 BETA",
            "hostname": ""
        }
        with open("system/config.json", "w") as file:
            json.dump(data, file, indent=4)
        time.sleep(1)
        print("Dumping config...")
        with open("system/config.json", "r") as file:
            data = json.load(file)
        time.sleep(.5)
        print("Checking config...")
        time.sleep(1)
        if data["install_finished"] == True:
            print("Configuration made.")
        else:
            print("fusion > The file at system/config.json is invalid")
time.sleep(.5)
if os.path.exists("dbs/installed.json"):
    print("[OK] dbs/installed.json")
else:
    print("fusion > Creating installed data...")
    apps = {
        "desktop": False
    }
    time.sleep(.5)
    print("fusion > Creating dbs/installed.json")
    os.makedirs("dbs", exist_ok=True)
    with open("dbs/installed.json", "w") as file:
        json.dump(apps, file, indent=4)
    time.sleep(.5)
    print("Validating dbs/installed.json")
    time.sleep(.5)
    with open("dbs/installed.json", "r") as file:
        if ["desktop"] == False:
            print("fusion > Validated dbs/installed.json with a 100% success rate.")
if os.path.isfile("system/users.json"):
    print("[OK] system/users.json")
else:
    print("[FAILED] system/users.json")
    time.sleep(.5)
    print("fusion > Creating user backboard...")
    users = {
        "username": "root",
        "password": "root"
    }
    time.sleep(.5)
    print("fusion > Creating user storage...")
    with open("system/users.json", "w") as file:
        json.dump(users, file, indent=4)
    time.sleep(.5)
    print("fusion > User storage and backboard created.")
    print("fusion > Validating system/config.json, system/users.json, and dbs/installed.json")
time.sleep(.5)
if os.path.isdir("system"):
    print("[OK] system/")
else:
    print("fusion > Installation has failed, or it cannot find system/")
time.sleep(.5)
if os.path.isdir("dbs"):
    print("[OK] dbs/")
else:
    print("fusion > Installation has failed, or it cannot find dbs/")
if os.path.isfile("dbs/installed.json"):
    print("[OK] dbs/installed.json")
else:
    print("fusion > Installation has failed, or it cannot find dbs/installed.json")
if os.path.isfile("system/users.json"):
    print("[OK] system/users.json")
else:
    print("fusion > Installation has failed, or it cannot find system/users.json")
if os.path.isfile("system/config.json"):
    print("[OK] system/users.json")
else:
    print("fusion > Installation has failed, or it cannot find system/config.js")
os.system("cls" if os.name == "nt" else "clear")
print(copyright)
print(post_cr)
time.sleep(2)
with open("system/users.json", "r") as file:
    users = json.load(file)
while True:
    username = input("fusion > Enter the root user: ")
    password = input("fusion > Enter the root password: ")

    if username == users["username"] and password == users["password"]:
        os.system("cls" if os.name == "nt" else "clear")
        print(copyright)
        print(post_cr)
        print(f"fusion > Logging into {username}@fusion...")
        time.sleep(1)
        break
    else:
        print("fusion > User does not exist or was entered incorrectly.")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        print(copyright)
        print(post_cr)
os.system("cls" if os.name == "nt" else "clear")
print(copyright)
print(post_cr)
print("Type 'help' for commands.")
while True:
    cmdline = input(f"{username}@fusion> ")
    if cmdline == "help":
            print("Available commands:")
            print("neofetch (Fetches OS Information.)")
            print("osad conf (Configures system as OS Administrator.)")
            print("time (Shows current time on a 12h clock.)")
            print("osad rm sys (Removes system/)")
            print("osad rm sys /y (Instantly removes system, no confirmation.)")
            print("osad rm fusion (Completely removes Fusion)")
            print("clean (Clears the terminal)")
            print("reboot (Restarts FusionTXT)")
    if cmdline == "neofetch":
            print(neofetch_art)
            print(f"OS: Fusion")
            print(f"Version: {data['version_identifier']}")
            print(f"User: {username}")
    if cmdline == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(f"Current time: {current_time}")
    if cmdline == "osad rm sys":
        while True:
            confirm_sys = input("Are you sure you want to delete system/? [y/n]")
            if confirm_sys == "y":
                shutil.rmtree("system")
                print("system/ has been removed.")
                break
    if cmdline == "osad rm sys /y":
        shutil.rmtree("system")
        print("Removed system/")
    if cmdline == "osad rm fusion":
        while True:
            confirm_all = input("Are you sure you would like to remove everything? [y/n]")
            if confirm_all == "y":
                shutil.rmtree("system")
                shutil.rmtree("dbs")
                print("Verifying dir...")
                time.sleep(2)
                if os.path.isdir("system"):
                    print("Fusion failed to delete.")
                    break
                else:
                    print("Fusion has been deleted. System will not function as normal.")
                    break
    if cmdline == "clean":
        os.system("cls" if os.name == "nt" else "clear")
        print(copyright)
        print(post_cr)
    if cmdline == "reboot":
        print("Rebooting FusionTXT...")
        time.sleep(.7)
        os.execv(sys.executable, [sys.executable] + sys.argv)
    while True:
        if cmdline == "osad conf":
            print("Type 'help' to see available configuration commands.")
            confcmd = input(f"{username}@fusionconf>")
            if confcmd == "help":
                # print("hostname (Changes the hostname)")
                print("rootuser (Changes the root username)")
                print("rootpass (Changes the root pass)")
                print("exit (Exits osad config)")
            if confcmd == "rootuser":
                print("Please type in the new root username.")
                new_username = input(f"{username}@fusion>")
                users["username"] = new_username

            with open("system/users.json", "w") as file:
                json.dump(users, file, indent=4)
            if confcmd == "rootpass":
                print("Please type in the new root password.")
                new_pass = input(f"{username}@fusion>")
                users["password"] = new_pass
        
                with open("system/users.json", "w") as file:
                    json.dump(users, file, indent=4)
            if confcmd == "exit":
                break