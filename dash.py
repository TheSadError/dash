from colorama import *
import optparse
import datetime
from scanlib import socialmedia
import requests
import socket 
import os
def banner():
    print(Fore.BLACK+f"""
     ____    _    ____  _   _
    |  _ \  / \  / ___|| | | |
    | | | |/ _ \ \___ \| |_| |
    | |_| / ___ \ ___) |  _  |
    |____/_/   \_\____/|_| |_| 1.3

    """)

def start(username,time):
    banner()
    ip = requests.get("https://api.my-ip.io/ip").text
    hostname = socket.gethostname()
    print(Fore.BLUE+f"\nStarting DASH OSINT scanner... ( https://github.com/TheSadError/DASH ) Time : {time}")
    print(Fore.RED+f"""
    Your INFO :
    
    IP       : {ip}
    HOSTNAME : {hostname}
    """)
    socialmedia.scan(username)

def main():
    time= datetime.datetime.now()
    parser = optparse.OptionParser(f" sudo python3 dash.py --u username")

    parser.add_option("-u","--u",dest = "username",type="string") # username parameter
    (options,args) = parser.parse_args()
    username = options.username
    if(username == None ):
        banner()
        print(parser.usage)
        exit(0)
    start(username,time)


if __name__ == "__main__":
    main()
