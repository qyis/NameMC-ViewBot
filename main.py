#imports all the modules that we will need
import math
from subprocess import call
import sys
from sys import platform
import asyncio
import requests
import asyncio
from termcolor import colored
from colorama import init
from proxyscrape import create_collector
from fake_useragent import UserAgent

#gets useragent that we could use
ua = UserAgent()

#makes proxies collector
collector = create_collector('my-collector', 'https')

#Makes this work for windows
init()

#Sets console title
sys.stdout.write("\x1b]2;NameMC ViewBot by Aldas\x07")

#clears terminal by using command in the shell
def clear():
    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    else:
        command = 'cls'
    try:
        call(command, shell=True)
    except OSError as e:
        pass

#function to view profiles
async def view(username, number=None, proxies=None, headers=None, timeout=None):
    if number == None:
        r = requests.get(f"https://namemc.com/profile/{username}", headers=headers, proxies=proxies, timeout=timeout)
        return r.status_code
    else:
        r = requests.get(f"https://namemc.com/profile/{username}.{number}", headers=headers, proxies=proxies, timeout=timeout)
        return r.status_code

#prints the banner
print(colored('''
_  _                __  __     __   ___              ___      _   
| \| |__ _ _ __  ___|  \/  |__  \ \ / (_)_____ __ __ | _ ) ___| |_ 
| .` / _` | '  \/ -_) |\/| / _|  \ V /| / -_) V  V / | _ \/ _ \  _|
|_|\_\__,_|_|_|_\___|_|  |_\__|   \_/ |_\___|\_/\_/  |___/\___/\__|
                        By Aldas | Version 1.0
''', "magenta"))

#makes an loop
name_input = True
while name_input:
    #tries to execute this username input code
    try:
        #username input
        username = input(f"[{colored('*', 'red')}] Username: ")
        #if user presses enter
        if username == "":
            continue
        #if user enters anything else
        else:
            pass
        
        #prints text to let users know that its not really needed
        print(colored("Press enter for 1 (default) as user number", "magenta"))
        #user number input
        usernumber = input(f"[{colored('+', 'green')}] User number incase needed: ")
        #if user presses enter (skips)
        if usernumber == "":
            usernameid = None
        #if user enters anything else
        else:
            pass
        
        #defines proxy
        proxy = collector.get_proxy()
        port = proxy[1]
        proxy = proxy[0]
        proxy = f"{proxy}:{port}"
        #sends a reuqest
        r_status_code = asyncio.run(view(username=username, number=usernumber, proxies={"https":proxy}, headers={'user-agent': ua.random}, timeout=10))
        #if we get 200 as a status code (success)
        if r_status_code == 200:
            sviews += 1
            print(colored(f"[{sviews} sent]", "magenta") + " " + colored('Successfully sent a view', 'green'))
        #if 404 error occurs (page not found error)
        elif r_status_code == 404:
            print(colored("No such a profile", "red"))
            exit()
        #if request status code is something else
        else:
            print(colored(f"Sent a request and got status code of {r_status_code}", "magenta"))
                
    #if you press ctrl + c
    except KeyboardInterrupt:
        print(colored("Bye!", "green"))
        exit()
    
    #if any other error occurs
    except Exception as e:
        print(f"{e}\n{colored('Error has occured! ^')}")
