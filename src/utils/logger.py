from colorama import Fore, init
from src.utils.args import *

init(autoreset=True)

def log_setup(msg):
    print(Fore.MAGENTA+msg)
    return 0

def log_msg(msg):
    if verbose == True:
        print(msg)
    return 0

def log_success(msg):
    print(Fore.GREEN+msg)
    return 0

def log_warning(msg):
    print(Fore.YELLOW+msg)
    return 0

def log_error(msg):
    print(Fore.RED+msg)
    input("Press enter to continue")
    return 0 

def log_fatal_error(msg):
    print(Fore.RED+msg)
    return 0 
