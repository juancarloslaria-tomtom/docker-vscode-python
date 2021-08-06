import sys
from datetime import datetime

def print_welcome_msg(yourname):
    print(f"Welcome {yourname}!")
    print(f"You are running python {sys.version} and your executable is on {sys.executable}")
    print(datetime.today())

def welcome():
    yourname = input('Plase, tell me your name: ')
    print_welcome_msg(yourname)

