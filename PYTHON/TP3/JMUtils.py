import time

# import only system from os
from os import system, name
import sys
import random

# 1 optional arg (double delay 'number of second before shutdowning program')
# default value delay = 0
# shutdown a program, with an optional delay
def closeProgram(delay=0):
    time.sleep(delay)
    sys.exit()


# 1 optional arg (double t 'number of seconds')
# default value t = 0.5;
# make the prog
def wait(t=0.5):
    time.sleep(t)

# 2 optional args (int min 'minimum' ; int max 'maximum')
# defaults values min = 0 ; max = 1;
# make an rng
def rng(min=0, max=1):
    return random.randint(min, max)


# 1 optional arg (bool c 'announce you need to press enter')
# default value = False
# if arg1 = True, announce that an entry is needed
def waitInput(c=False):
    if c:
        print("\nPress enter to continue ...\n")
    input("")

# usual typing error
def retype():
    print("\ntyping error, please type enter to retry ...\n")
    waitInput()

# just a stupid thing
def clearConsole():
    for i in range(10):
        print("\n")

# really nice console cleaning, working for (I think) all OS
def cleanClearConsole():
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')