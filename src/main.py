import os
import notes # Importing the "notes.py" module
import commands # Importing the "commands.py" module

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

# Starting a loop to continuously receive user input and adhere to the commands provided by the user
while True:

    print("--------------------------------")
    print("Model Tank ready.")
    print('Type "help" for commands.')
    user_message = input("User: ")
    command = user_message.lower()

    # Handling user commands
    if command == "exit":
        commands.exitProgram()

    elif command == "time":
        commands.showTime()

    elif command == "date":
        commands.showDate()

    elif command == "take note":
        notes.takeNote()

    elif command == "show notes":
        notes.showNotes()

    elif command == "clear":
        commands.clearScreen()

    elif command == "help":
        commands.displayHelp()

    else:
        print("Model Tank Received:", user_message)