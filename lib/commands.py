import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit():
    print("Goodbye")
    sys.exit()