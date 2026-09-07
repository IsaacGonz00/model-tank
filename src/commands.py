import os
from datetime import datetime
from typing import Type

# Functions for handling various other commands in the program.
def exitProgram():
    print("Model Tank Shutting Down...")
    exit()

def showTime():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    print("The Current Time is:", current_time) 

def showDate():
    current_date = datetime.now().strftime("%m/%d/%y")
    print("The Current Date is:", current_date)

def clearScreen():
    os.system("clear")

def displayHelp():
    print("Available Commands:")
    print("1. time - Displays the current time.")
    print("2. date - Displays the current date.")
    print("3. take note - Allows you to save a note.")
    print("4. show notes - Displays all saved notes.")
    print("5. help - Displays this help message.")
    print("6. clear - Clears the terminal screen.")
    print("7. exit - Exits the program.")