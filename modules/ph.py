import time 
import sys 
import os 
import phonenumbers 
import colorama 
from phonenumbers import carrier 
from phonenumbers import geocoder 
from tabulate import tabulate
from phonenumbers import timezone
from colorama import Fore, Back, Style

os.system(' clear ')
print(Fore.BLUE+"|===============================================|")
print(Fore.MAGENTA+"|number should be formatted like +1 XXX-XXX-XXXX|")
print(Fore.BLUE+"|===============================================|")


def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

def number_scanner(phone_number):
    number = phonenumbers.parse(phone_number)
    description = geocoder.description_for_number(number, "en" )
    supplier = carrier.name_for_number(number, "en")
    info = [["State or Country", "Supplier",],
            [description, supplier,]]
    data = str(tabulate(info, headers="firstrow", tablefmt="github"))
    return data 

if __name__ == "__main__":
    number = input(" Enter Number ==>> ")
    os.system(' clear ')
    print(number_scanner(number))
    time.sleep(3)
    restart_program()          