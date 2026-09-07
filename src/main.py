import os
from datetime import datetime
from typing import Type

from dotenv import load_dotenv
from openai import OpenAI

# Indicating that Model Tank is initializing
print("Model Tank initializing...")

##################################################################################################################
# AI Model Initialization Template for now, this is a placeholder for future AI model initialization code.
load_dotenv()

# Loading environment variables from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Checking to see if the OPENAI_API_KEY environment variable is set 
if openai_api_key is None:
    print("OPENAI_API_KEY was not found.")

# Initializing the OpenAI client with the API key
client = OpenAI(api_key = openai_api_key)
##################################################################################################################

# Functions
def exitProgram():
    print("Model Tank Shutting Down...")
    exit()

def showTime():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    print("The Current Time is:", current_time) 

def showDate():
    current_date = datetime.now().strftime("%m/%d/%y")
    print("The Current Date is:", current_date)

def takeNote():
    note = input("Please enter your note: ")
    if note.strip() == "":
        print("Empty note not saved.")
    else:
        with open("data/notes.txt", "a") as file:
            file.write(note + "\n")

def showNotes():
    try:
        with open("data/notes.txt", "r") as file:
            notes = file.readlines()
    except FileNotFoundError:
        print("File has not been created yet. Please take a note first.")
        return
    if notes:
        print("Your Notes:")
        for idx, note in enumerate(notes, start=1):
            print(f"{idx}. {note.strip()}")
    else:
        print("No notes found.")

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




# Starting a loop to continuously receive user input and adhere to the commands provided by the user
while True:

    print("--------------------------------")
    print("Model Tank ready.")
    print('Type "help" for commands.')
    user_message = input("User: ")
    command = user_message.lower()

    # Handling user commands
    if command == "exit":
        exitProgram()

    elif command == "time":
        showTime()

    elif command == "date":
        showDate()

    elif command == "take note":
        takeNote()

    elif command == "show notes":
        showNotes()

    elif command == "clear":
        clearScreen()

    elif command == "help":
        displayHelp()
      
    else:
        print("Model Tank Received:", user_message)