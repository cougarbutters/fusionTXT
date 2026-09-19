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
        os.makedirs("system/usr", exist_ok=True)
        print("Creating configuration...")
        data = {
            "install_finished": True,
            "version_identifier": "0.1 BETA",
            "hostname": "fusion"
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
        "desktop": True,
        "gchrome": False,
        "chromium": False,
        "mozillafirefox": False,
        "gnugimp": False,
        "spotify": False,
        "vlc": False,
        "libreoffice": False,
        "secret app!": False
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
if os.path.exists("system/whois.json"):
    print("[OK] system/whois.json")
else:
    print("fusion > Creating whois data...")
    whois = {
        "gchrome": {
            "name": "Google Chrome",
            "version": "139.0",
            "description": "An internet browser developed by Google."
        },
        "chromium": {
            "name": "Chromium",
            "version": "181.0",
            "description": "An open-source internet browser developed by Google."
        },
        "mozillafirefox": {
            "name": "Mozilla Firefox",
            "version": "118.0",
            "description": "An internet browser developed by Mozilla."
        },
        "gnugimp": {
            "name": "GNU Image Manipulation Program",
            "version": "3.0",
            "description": "A free and open-source raster graphics editor."
        },
        "spotify": {
            "name": "Spotify",
            "version": "1.0",
            "description": "A digital music service that gives you access to millions of songs."
        },
        "vlc": {
            "name": "VLC Media Player",
            "version": "4.0",
            "description": "A free and open-source, portable, cross-platform media player software."
        },
        "libreoffice": {
            "name": "LibreOffice",
            "version": "8.0",
            "description": "A free and open-source office suite."
        }
    }
    with open("system/whois.json", "w") as file:
        json.dump(whois, file, indent=4)
if os.path.exists("dbs/packages.json"):
    print("[OK] dbs/packages.json")
else:
    print("fusion > Creating packages data...")
    packages = [
        "gchrome",
        "chromium",
        "mozillafirefox",
        "gnugimp",
        "spotify",
        "vlc",
        "libreoffice",
        "secret app!"
    ]
    with open("dbs/packages.json", "w") as file:
        json.dump(packages, file, indent=4)
os.makedirs("system/usr", exist_ok=True)
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
    print("[OK] system/config.json")
else:
    print("fusion > Installation has failed, or it cannot find system/config.json")
if os.path.isdir("system/usr"):
    print("[OK] system/usr/")
else:
    print("fusion > Installation has failed, or it cannot find 'system/usr/'")
os.system("cls" if os.name == "nt" else "clear")
print(copyright)
print(post_cr)
time.sleep(2)
with open("system/users.json", "r") as file:
    users = json.load(file)
with open("system/config.json", "r") as file:
    data = json.load(file)
hostname = data.get("hostname") or "fusion"
while True:
    username = input("fusion > Enter the root user: ")
    password = input("fusion > Enter the root password: ")

    if username == users["username"] and password == users["password"]:
        os.system("cls" if os.name == "nt" else "clear")
        print(copyright)
        print(post_cr)
        print(f"fusion > Logging into {username}@{hostname}...")
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
    cmdline = input(f"{username}@{hostname}> ")
    if cmdline == "help":
            print("Available commands:")
            print("neofetch (Fetches OS Information.)")
            # print("osad conf (Configures system as OS Administrator.)")
            print("time (Shows current time on a 12h clock.)")
            print("osad rm sys (Removes system/)")
            print("osad rm sys /y (Instantly removes system, no confirmation.)")
            print("osad rm fusion (Completely removes Fusion)")
            print("clean (Clears the terminal)")
            print("reboot (Restarts FusionTXT)")
            print("ls (Lists all files in the 'usr/' directory.)")
            print("rm file (Removes a file in the 'usr/' directory.)")
            print("mk file (Creates a new file in the 'usr/' directory.)")
            print("ap file (Appends content to a file in the 'usr/' directory.)")
            print("read file (Reads the contents of a file in the 'system/usr/' directory.)")
            print("pkmg (Installs packages.)")
            print("pkmg rm (Removes a package.)")
            print("pkmg list (Lists all installed packages.)")
    if cmdline == "neofetch":
            print(neofetch_art)
            print(f"OS: FusionTXT")
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
    if cmdline == "shutdown":
        print("Shutting down FusionTXT...")
        time.sleep(2)
        sys.exit()
    if cmdline == "ls":
        print("Files in 'system/usr/':")
        lsres = os.listdir("system/usr")
        for item in lsres:
            print(item)
    if cmdline == "rm file":
        rmfile = os.listdir("system/usr")
        print("Files in 'system/usr/':")
        print(rmfile)
        filename = input("Enter the filename to remove: ")
        filepath = os.path.join("system/usr", filename)
        if os.path.isfile(filepath):
            os.remove(filepath)
            print(f"{filename} has been removed.")
        else:
            print(f"{filename} does not exist in system/usr/.")
    if cmdline == "mk file":
        newfile = input("Type in a name for the new file: ")
        open(f"system/usr/{newfile}", "w").close()
        print(f"File created at system/usr/{newfile}")
    if cmdline == "ap file":
        apfile = os.listdir("system/usr")
        print("Files in 'system/usr/':")
        print(apfile)
        appendfile = input("Type in a name for the file to append to: ")
        with open(f"system/usr/{appendfile}", "a") as file:
            appendcontent = input("Type in the content to append: ")
            file.write(appendcontent + "\n")
            print(f"Content appended to system/usr/{appendfile}")
    if cmdline == "read file":
        readfile = os.listdir("system/usr")
        print("Files in 'system/usr/':")
        print(readfile)
        showdir = input("Enter a file to read its contents: ")
        with open(f"system/usr/{showdir}", "r") as file:
            content = file.read()
            print(f"Contents of system/usr/{showdir}:")
            print(content)
    if cmdline == "pkmg":
        while True:
            with open("dbs/packages.json", "r") as file:
                packages = json.load(file)
            print(packages)
            pkmg = input("fusion > Enter the name of the package to install: ")
            if pkmg in packages:
                with open("dbs/installed.json", "r") as file:
                    installed = json.load(file)
                if installed.get(pkmg) == True:
                    print(f"{pkmg} is already installed.")
                    break
                else:
                    installed[pkmg] = True
                    with open("dbs/installed.json", "w") as file:
                        json.dump(installed, file, indent=4)
                    print(f"{pkmg} has been installed.")
                    break
    if cmdline == "pkmg rm":
        while True:
            with open("dbs/installed.json", "r") as file:
                installed = json.load(file)
            print(installed)
            pkmg_rm = input("fusion > Enter the name of the package to remove: ")
            if pkmg_rm in installed:
                if installed.get(pkmg_rm) == False:
                    print(f"{pkmg_rm} is not installed.")
                    break
                else:
                    installed[pkmg_rm] = False
                    with open("dbs/installed.json", "w") as file:
                        json.dump(installed, file, indent=4)
                    print(f"{pkmg_rm} has been removed.")
                    break
    if cmdline == "pkmg list":
        with open("dbs/installed.json", "r") as file:
            installed = json.load(file)
        print("Installed packages:")
        for package, status in installed.items():
            if status == True:
                print(f"{package} (installed)")
            else:
                print(f"{package} (not installed)")
    if cmdline == "uptime":
        boot_time = time.monotonic()
        print(f"System uptime: {boot_time:.2f} seconds")