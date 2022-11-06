""" LenvxShell Remake"""

#Important
import colorama, ujson, random, platform, os, time, requests, string, readline, psutil
from colorama import Fore
from datetime import date
from os import getpid
mem_usage = psutil.virtual_memory()
my_process = psutil.Process(getpid())
ver = 0.3
today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("Welcome to DEV release...")
updatechk = requests.get("https://lenvxshell2.netlify.app/response.json").json()
if updatechk["name"] > ver:
    print(f"{Fore.RED} New version came out! {Fore.RESET}")
    updatestate = True
else:
    updatestate = False
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
    print("--------------------------------------")
    print(f"{d1} -~~~~")
    print("--------------------------------------")
    while True:
        sytax=input(console['prefix']).strip()
        if sytax == "":
            pass
        elif sytax == "hear":
            print("Usage of hear:")
            print("hear Hello world!")
            print("Hello world!")
        elif f"{sytax} ".startswith("hear "):
            print(sytax[4:])
        elif f"{sytax} ".startswith("#"):
            pass
        elif sytax == "help":
            print(f"""
                     {Fore.BLUE} hear {Fore.RESET} >> {Fore.GREEN} Usage: hear Hello world!
                     {Fore.BLUE} Help {Fore.RESET} >> {Fore.GREEN} this command
                     {Fore.BLUE} cl {Fore.RESET} >> {Fore.GREEN} clears out text
                     {Fore.BLUE} clst {Fore.RESET} >> {Fore.GREEN} same as cl but with welcome text
                     {Fore.BLUE} # {Fore.RESET} >> {Fore.GREEN} Comment
                     {Fore.BLUE} src {Fore.RESET} >> {Fore.GREEN} source link
                     {Fore.BLUE} ver {Fore.RESET} >> {Fore.GREEN} version
                     {Fore.BLUE} qu! {Fore.RESET} >> {Fore.GREEN} quits the shell.
                     {Fore.BLUE} kz {Fore.RESET} >> {Fore.GREEN} Change your prefix/PS1
                     {Fore.BLUE} kx {Fore.RESET} >> {Fore.GREEN} Change your pass
                     {Fore.BLUE} kc {Fore.RESET} >> {Fore.GREEN} Change your user
                     {Fore.BLUE} feth {Fore.RESET} >> {Fore.GREEN} neofetch but lenvxshell's only
                     {Fore.BLUE} randomize {Fore.RESET} >> {Fore.GREEN} hides text with generated letters
                     {Fore.BLUE} spamermize {Fore.RESET} >> {Fore.GREEN} spams the the output with selected text
                    {Fore.RESET}
                     """)
        elif sytax == "cl":
            os.system('clear')
        elif sytax== "feth":
            print(f"""{Fore.GREEN}
                       %%%%%%%%%
                 %%%%%%%%%%%%%%%%%%%%%%%
             &%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&
           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             {Fore.RED}OS      = {Fore.BLUE}{platform.system()}{Fore.GREEN}
       %%%%%%%%%%%%%%%   %%%%%%.  %%%%%%%%%%%%%%%%            {Fore.RED}Date    = {Fore.BLUE}{d1}{Fore.GREEN}
      %%%%%%%%%%%%%%#  *%%%%%%   %%%%%%%%%%%%%%%%%%&          {Fore.RED}RP      = {Fore.BLUE}LenvxREPL{Fore.GREEN}
     %%%%%%%%%%%%%%#     *%%%,  %%%%%%%%%%%%%%%%%%%%          {Fore.RED}State   = {Fore.BLUE}DEV{Fore.GREEN}
    %%%%%%%%%%%%%%%   %%%#     %%%%%%%%%%%%%%%%%%%%%%         {Fore.RED}Version = {Fore.BLUE}0.3{Fore.GREEN}
    %%%%%%%%%%%%%%%  ,%%%%%*  #.   /%%%%%%%%%%%%%%%%%         {Fore.RED}Update needed: = {Fore.BLUE}{updatestate}{Fore.GREEN}
    %%%%%%%%%%%%%%%  *%%%%/  *    ,#%%%%%%%%%%%%%%%%%         {Fore.RED}RAM usage = {Fore.BLUE}{mem_usage.used/(1024**3):.2f}/{mem_usage.total/(1024**3):.2f}g{Fore.GREEN}
    %%%%%%%%%%%%%%%  .%(.    (%%%%%%%%%%%%%%%%%%%%%%%         {Fore.RED}CPU ={Fore.BLUE} {my_process.cpu_percent(interval=0)}%{Fore.GREEN}
     %%%%%%%%%%%%%%,   ,%  /%%%%%%%%%%%%%%%%%%%%%%%%%
     &%%%%%%%%%%%%%%   #  /%%%%%%%%%%%%%%%%%%%%%%%%%
       %%%%%%%%%%%%%%   %%%%%%%%%%%%%%%%%%%%%%%%%%%
        %%%%%%%%%%%%%%#  /%%%%%%%%%%%%%%%%%%%%%%%&
        %%%%%%%%%%%%%%#  /%%%%%%%%%%%%%%%%%%%%%%%&
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&
           &%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                &%%%%%%%%%%%%%%%%%%%%%%%%%&
                    %%%%%%%%%%%%%%%
                       %%%%%%%%%
        {Fore.RESET} """)
        elif sytax == "kz":
            print("KOS lenvxshell edition")
            for i in range(3):
                verifypass=input(f"(Password for {console['user']})")
                if verifypass == console["pass"]:
                    newps1=input("New Prefix:")
                    console["prefix"] = newps1
                    with open("data/logindata.json", "w") as cfgf:
                        ujson.dump(console, cfgf, indent=4)
                    break
                if i + 1 == 3:
                    time.sleep(2)
                    print("Failed all 3 attempts")
                    pass
                else:
                    time.sleep(2)
                    print("Try again")      
        elif sytax == "kx":
            print("KOS lenvxshell edition")
            for i in range(3):
                verifypass=input(f"(Password for {console['user']})")
                if verifypass == console["pass"]:
                    newps1=input("New password: ")
                    console["pass"] = newps1
                    with open("data/logindata.json", "w") as cfgf:
                        ujson.dump(console, cfgf, indent=4)
                    break
        elif sytax == "kc":
            print("KOS lenvxshell edition")
            for i in range(3):
                verifypass=input(f"(Password for {console['user']})")
                if verifypass == console["pass"]:
                    newps1=input("New username: ")
                    console["user"] = newps1
                    with open("data/logindata.json", "w") as cfgf:
                        ujson.dump(console, cfgf, indent=4)
                    break
                if i + 1 == 3:
                    time.sleep(2)
                    print("Failed all 3 attempts")
                    pass
                else:
                    time.sleep(2)
                    print("Try again")       
        elif sytax == "src":
            print("https://github.com/lenvxcodes/lenvxshell2")
        elif sytax == "ver":
            print("Version 0.3")
        elif sytax == "clst":
            os.system('clear')
            print(console['welcome'])
            print("--------------------------------------")
            print(f"{d1} -~~~~")
            print("--------------------------------------")
        elif sytax == "qu!":
            exit()
        elif sytax == "randomize":
            print("Usage: $~ randomize Im-somewhere-here")
        elif f"{sytax} ".startswith("randomize "):
            print(f"{randomize + Fore.YELLOW + sytax[9:] + Fore.RESET + randomize}")
        elif f"{sytax} ".startswith("spamermize "):
            for _ in range(1 + input("Times to spam:")):
                print(sytax[10:])
        elif sytax == "spamermize":
            print("Usage: randomize Spammed!")
        else:
            print("Response Invalid.")
randomize =''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.punctuation) for i in range(1000))
shell()
