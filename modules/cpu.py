import os
import sys 
import psutil
import colorama 
import time
from colorama import Fore, Back, Style

os.system(' clear ')
print(":::::::::::::::::::::::::::::::::::::")
time.sleep(0.1)
print(": Created and designed by Ark Angel :")
time.sleep(0.1)
print(":::::::::::::::::::::::::::::::::::::")
time.sleep(0.1)
print(":::::::::::::::::::::::::::::::::::::")
os.system(' date ')
print(":::::::::::::::::::::::::::::::::::::")
time.sleep(4)
os.system(' clear ')
print(Fore.MAGENTA+"================CORE===============")
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
print(Fore.YELLOW+"=================FREQ================")
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"CUrrent Frequency: {cpufreq.current:.2f}Mhz")
print(Fore.MAGENTA+"================USAGE==============")
print("CPU Usage:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(Fore.YELLOW+"==============TOTAL================")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")