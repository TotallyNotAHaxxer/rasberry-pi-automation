#simple and easy system(' automation bot')
import os
import sys 
import time
import platform
from sys import platform 

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
   
   
def screen_clear():
   if name == 'nt':
      _ = system('cls')

def load_animation(): 
  
    load_str = "Loading AI."
    ls_len = len(load_str) 
  
    animation = "|/-\\|/-\|/-/"
    anicount = 0
      
    counttime = 0        
       
    i = 0                     
  
    while (counttime != 30): 
          

        time.sleep(0.075)  
                              
        load_str_list = list(load_str)  
 
        x = ord(load_str_list[i]) 
          
        y = 0                             

        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1

import colorama 
from colorama import Fore
print(Fore.CYAN+" if you are new type : install -r : in the commit")

N = str(input(" ==>> "))

if 'clear' in N:
           os.system(' clear ')
           restart_program()

elif 'install -r' in N:
                  os.system(' clear ')
                  os.system(' mpg123 install.mp3 ')
                  os.system(' clear ')
                  os.system(' pip install requests ')
                  os.system(' pip install colorama ')
                  os.system(' pip install python_weather')
                  os.system(' pip install asyncio ')
                  os.system(' pip install json ')
                  os.system(' pip install dill ')
                  os.system(' pip install requests-html ')
                  os.system(' pip install calendar ')
                  restart_program

import os
import time
from os import system, name
from time import sleep
from requests_html import HTMLSession
from sys import platform
import sys 
import colorama
import python_weather
import platform 
import asyncio
import requests 
from requests import * 
import json
import calendar
from colorama import *
from colorama import init
from colorama import * 
from colorama import init
from termcolor import colored


def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
   
   
def screen_clear():
   if name == 'nt':
      _ = system('cls')              


if 'ello' in N:
          print(" hello ")
          restart_program()

elif 'monkey' in N:
              print(" ")

elif 'flow' in N:
            os.system(' clear ')
            os.system(' open https://stackoverflow.com/ ')
            restart_program()

elif 'overflow' in N:
                os.system(' clear ')
                os.system(' open https://stackoverflow.com/ ')
                restart_program()

elif 'pypi' in N:
            os.system(' clear ')
            os.system(' open https://pypi.org/ ')
            restart_program()

elif 'py' in N:
          time.sleep(0.1)
          os.system(' clear ')
          os.system(' open https://pypi.org/ ')
          restart_program()

elif 'who am i' in N:
                os.system(' clear ')
                os.system(' mpg123 you.mp3 ')
                os.system(' clear ')
                import socket 
                import getpass
                import os.path
                username = getpass.getuser()
                homedir = os.path.expanduser("~")
                hostname = socket.gethostname()
                print(username)
                print(hostname)
                print(homedir)
                time.sleep(2)
                restart_program()


elif 'what is love' in N:
                    os.system(' clear ')
                    os.system(' mpg123 whatislove.mp3 ')
                    os.system(' clear ')
                    restart_program()


elif 'lets vibe' in N:
                 time.sleep(0.1)
                 os.system(' clear ')
                 os.system(' mpg123 vibe.mp3 ')
                 os.system(' clear ')
                 os.system(' open https://www.youtube.com/watch?v=6uddGul0oAc ')
                 restart_program()
 
elif 'i love you' in N:
                  os.system(' clear ')
                  os.system(' mpg123 love.mp3 ')
                  restart_program()

elif 'goodnight' in N:
                 os.system(' clear ')
                 os.system(' mpg123 night.mp3 ')
                 os.system(' clear ')
                 shutdown = str(input(" Y/n ==>> "))

                 if 'Y' in shutdown:
                        print(" shutting down within the next minute ")
                        print(" exiting script...... ")
                        os.system(' shutdown ')
                        os.system(' exit ')
                        sys.exit()

                 if 'n' in shutdown: 
                        os.system(' clear ')
                        os.system(' exit ')
                        sys.exit() 

                 elif 'y' in shutdown:
                          print(" shutting down within the next minute ")
                          print(" exiting script...... ")
                          os.system(' shutdown ')
                          os.system(' exit ')
                          sys.exit()                               



elif 'spotify' in N:
               os.system(' clear ')
               os.system(' mpg123 understood.mp3')
               os.system(' clear ')
               os.system(' open https://spotify.com')
               restart_program()

elif 'upgrade' in N:
               os.system(' clear ')
               os.system(' sudo apt-get update && sudo apt-get upgrade --full ')
               os.system(' clear ')
               os.system(' sudo networkmanager restart ')
               os.system(' neofetch ')
               restart_program()

elif 'update' in N:
              time.sleep(0.1)
              os.system(' sudo apt-get update ')
              restart_program()

elif 'tube' in N:
            os.system(' clear ')
            os.system(' open https://youtube.com ')
            restart_program()

elif 'start youtube' in N:
                     os.system(' clear ')
                     os.system(' mpg123 undertood.mp3 ')
                     os.system(' clear ')
                     os.system(' open https://youtube.com ')

elif 'youtube' in N:
               os.system(' clear ')
               os.system(' open https://youtube.com ')
               restart_program()


elif 'launch minecraft' in N:
                        os.system(' clear ')
                        os.system(' mpg123 havefun.mp3 ')
                        os.system(' clear ')
                        os.system(' cd ~ && cd Downloads && java -jar TLauncher-2.8.jar ')
                        restart_program()


elif 'craft' in N:
             os.system(' clear ')
             os.system(' mpg123 havefun.mp3 ')
             os.system(' clear ')
             os.system(' cd ~ && cd Downloads && java -jar TLauncher-2.8.jar ')
             restart_program()

elif 'mine' in N:
            os.system(' clear ')
            os.system(' mpg123 havefun.mp3 ')
            os.system(' clear ')
            os.system(' cd ~ && cd Downloads && java -jar TLauncher-2.8.jar ')
            restart_program()

elif 'shutoff' in N:
               os.system(' shutdown -P ')

elif 'shutdown' in N:
                os.system(' shutdown ')

elif 'reboot' in N:
              os.system(' reboot ')

elif 'minecraft' in N:
                 os.system(' clear ')
                 os.system(' mpg123 havefun.mp3 ')
                 os.system(' clear ')
                 os.system(' cd ~ && cd Downloads && java -jar TLauncher-2.8.jar ')
                 restart_program()




elif 'start minecraft' in N:
                        os.system(' clear ')
                        os.system(' mpg123 havefun.mp3 ')
                        os.system(' clear ')
                        os.system(' cd ~ && cd Downloads && java -jar TLauncher-2.8.jar ')
                        restart_program()

elif 'trace' in N:
             time.sleep(0.1)
             os.system(' clear ')
             os.system(' mpg123 IP.mp3')
             os.system(' clear ')
             print(Fore.MAGENTA+"|-------------|")
             time.sleep(0.1)
             print(Fore.BLUE+" input the IP |")
             time.sleep(0.1)
             print(Fore.MAGENTA+"|-------------|")
             def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
             def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
             def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
             def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
             from requests import get
             ip = input("enter your ip here:")
             track = get(f'https://ipapi.co/{ip}/json/')
             prYellow(track.json())
             restart_program()

elif 'traceIP' in N:
             time.sleep(0.1)
             os.system(' clear ')
             os.system(' mpg123 IP.mp3')
             os.system(' clear ')
             print(Fore.MAGENTA+"|-------------|")
             time.sleep(0.1)
             print(Fore.BLUE+" input the IP |")
             time.sleep(0.1)
             print(Fore.MAGENTA+"|-------------|")
             def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
             def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
             def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
             def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
             from requests import get
             ip = input("enter your ip here:")
             track = get(f'https://ipapi.co/{ip}/json/')
             prYellow(track.json())
             restart_program()

elif 'trace' in N:
             time.sleep(0.1)
             os.system(' clear ')
             os.system(' mpg123 IP.mp3')
             os.system(' clear ')
             print(Fore.MAGENTA+"|-------------|")
             time.sleep(0.1)
             print(Fore.BLUE+" input the IP |")
             time.sleep(0.1)
             print(Fore.MAGENTA+"|-------------|")
             def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
             def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
             def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
             def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
             from requests import get
             ip = input("enter your ip here:")
             track = get(f'https://ipapi.co/{ip}/json/')
             prYellow(track.json())
             restart_program()

elif 'open dark web magazine' in N:
                              os.system(' clear ')
                              os.system(' open https://darkwebmagazine.com/ ')
                              restart_program()


elif 'open google' in N:
                   os.system(' clear ')
                   os.system(' open https://google.com ')
                   restart_program()

elif 'dark web magazine' in N:
                         os.system(' clear ')
                         os.system(' open https://darkwebmagazine.com/ ')
                         restart_program()

elif 'DWB' in N:
           os.system(' clear ')
           os.system(' open https://darkwebmagazine.com/ ')
           restart_program()

elif 'dark' in N:
            os.system(' clear ')
            os.system(' open https://darkwebmagazine.com/ ')
            restart_program()

elif 'sf' in N:
          os.system(' clear ')
          os.system(' open https://open.spotify.com/ ')
          restart_program()

elif 'andrax' in N:
              os.system(' andrax ')
              restart_program()

elif 'AD' in N:
          os.system(' andrax ')
          restart_program()

elif 'tracePH' in N:
               os.system(' clear ')
               os.system(' mpg123 phone.mp3 ')
               os.system(' clear ')
               ph = str(input(" U S phone number ==>>> "))
               os.system(f' sudo ph33rNoNum.sh --num {num} --csv ')

elif 'pain1' in N:
                   time.sleep(0.1)
                   os.system(' clear ')
                   os.system(' mpg123 trust.mp3 ')
                   H = str(input(" yes or no ==>> "))

                   if 'no' in H:
                           time.sleep(0.1)
                           os.system(' exit ')
                           restart_program()
                   
                   if 'yes' in H:
                            time.sleep(0.1)
                            os.system(' open https://discord.com/channels/@me/847698056198488114 ')


elif 'DoS' in N:
           time.sleep(0.1)
           os.system(' sudo python3 MAL.py ')
           restart_program()

elif 'ape' in N:
           os.system(' clear ')
           os.system(' sudo etherape ')
           restart_program()

elif 'ether' in N:
             os.system(' clear ')
             os.system(' sudo etherape ')
             restart_program()

elif 'monke' in N:
             os.system(' clear ')
             os.system(' sudo etherape ')
             restart_program()

elif 'wireshark' in N:
                 os.system(' clear ')
                 os.system(' sudo wireshark ')
                 restart_program()

elif 'shark' in N:
             os.system(' clear ')
             os.system(' sudo wireshark ')
             restart_program()

elif 'wire' in N:
            os.system(' clear ')
            os.system(' sudo wireshark ')
            restart_program()

elif 'news' in N:
            os.system(' clear ')
            os.system(' mpg123 fetching.mp3 ')
            os.system(' clear ')
            os.system(' python3 scrape.py ')
            restart_program()

elif 'specs' in N:
             time.sleep(0.1)
             os.system(' clear ')
             os.system(' neofetch ')
             restart_program()

elif 'system' in N:
              os.system(' clear ')
              os.system(' neofetch ')
              restart_program()

elif '-w' in N:
          os.system(' clear ')
          WE = str(input(" location/city ==>> "))
          os.system(f' weather {WE} ')
          restart_program()

elif 'weather' in N:
               os.system(' clear ')
               os.system(' mpg123 understood.mp3')
               os.system(' clear ')
               WE = str(input(" location/city ==>> "))
               os.system(f' weather {WE} ')
               restart_program()


elif 'cls' in N:
           os.system(' clear ')
           restart_program()

elif 'h' in N:
         time.sleep(0.1)
         F = open('help.json','r+',encoding='utf-8')
         data = json.load(F)
         for x in data['prints']:
             print(x)
             time.sleep(0.1)
         restart_program()

elif 'vpn' in N:
           os.system(' clear ')
           os.system(' mpg123 gotit.mp3 ')
           os.system(' clear ')
           os.system(' sudo anonsurf start ')
           restart_program

elif 'VPN' in N:
           os.system(' clear ')
           os.system(' mpg123 gotit.mp3 ')
           os.system(' clear ')
           os.syste(' sudo anonsurf start ')
           restart_program()

elif 'dis' in N:
           os.system(' mpg123 gotit.mp3 ')
           os.system(' clear ')
           os.system(' open https://discord.com ')
           restart_program()

elif 'discord' in N:
               time.sleep(0.1)
               os.system(' clear ')
               os.system(' mpg123 gotit.mp3 ')
               os.system(' clear ')
               os.system(' open https://discord.com ')
               restart_program()

elif 'wiki' in N:
            os.system(' mpg123 understood.mp3 ')
            os.system(' open https://en.wikipedia.org/wiki/Main_Page ')
            restart_program()

elif 'im new' in N:
              time.sleep(0.1)
              time.slee(0.1)
              F = open('help.json','r+',encoding='utf-8')
              data = json.load(F)
              for x in data['prints']:
                  print(x)
                  time.sleep(0.1)
              restart_program() 

elif 'help' in N:
            time.sleep(0.1)
            time.slee(0.1)
            F = open('help.json','r+',encoding='utf-8')
            data = json.load(F)
            for x in data['prints']:
                print(x)
                time.sleep(0.1)
            restart_program()            


elif 'date' in N:
            os.system(' clear ')
            os.system(' date ')
            time.sleep(2)
            restart_program()
            

elif 'gl' in N:
          os.system(' clear ')
          time.sleep(0.1)
          os.system(' mpg123 heard.mp3 ')
          os.system(' open https://google.com ')
          restart_program()

elif 'g' in N:
         os.system(' clear ')
         os.system(' mpg123 heard.mp3 ')
         os.system(' clear ')
         os.system(' open https://google.com ')
         restart_program()

elif 'google' in N:
              os.system(' clear ')
              os.system(' mpg123 heard.mp3 ')
              os.system(' clear ')
              os.system(' open https://google.com ')
              restart_program()           