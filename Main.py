""" LenvxShell Remake"""

#Important
import colorama, ujson, random, platform, os, time, getpass, readline
from colorama import Fore
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("Welcome to DEV release...")

def reg():
    print("Seems Something is missing, Register.")
    username = input("username:")
    print(f"Hello {username}!")
    password = input("pass:")
    jsons = open("data/logindata.json", "w")
    dict1 = {"user": username, "pass": password, "prefix": f"{username}$~ ", "welcome": f"Wellcome {username}!"}
    ujson.dump(dict1, jsons, indent=6)
    print("Saved credentials..")

if os.path.isfile("data/logindata.json"):
    print(f"data/logindata.json Exist.")
if not os.path.isfile("data/logindata.json"):
    reg()
with open("data/logindata.json", "r") as cfg:
    console: dict = ujson.load(cfg)
def login():
    with open("data/logindata.json", "r") as cfg:
        console: dict = ujson.load(cfg)
    print(f"Welcome {console['user']}!")
    loginpass =input("password:")
    if loginpass == console["pass"]:
       pass
    else:
        print("Incorrect password.")
        time.sleep(3)
        exit()
login()
def shell():
    os.system('clear')
    print(console['welcome'])
    while True:
        sytax=input(console["prefix"]).strip()
        if sytax == "":
            pass
        elif sytax == "hear":
            print("Usage of hear:")
            print("hear Hello world!")
            print("Hello world!")
        elif f"{sytax} ".startswith("hear"):
            print(sytax[4:])
        elif sytax == "help":
            print("""
                     hear - Echo command.
                     help - this command
                     cl - clears out text
                     clst - same as cl but with welcome text
                     src - source link
                     ver - version
                     """)
        elif sytax == "cl":
            os.system('clear')
        elif sytax == "src":
            print("https://github.com/lenvxcodes/lenvxshell2")
        elif sytax == "ver":
            print("Version 0.1")
        elif sytax == "clst":
            os.system('clear')
            print(console['welcome'])
        else:
            print("Response Invalid.")
            
shell()


