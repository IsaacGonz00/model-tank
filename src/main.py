import os
import notes # Importing the "notes.py" module
import commands # Importing the "commands.py" module

from dotenv import load_dotenv
from openai import OpenAI

# Indicating that Model Tank is initializing
print("Model Tank initializing...")

####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################
# AI Model Initialization Template for now, this is a placeholder for future AI model initialization code.
load_dotenv()

# Loading environment variables from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Checking to see if the OPENAI_API_KEY environment variable is set 
if openai_api_key is None:
    print("OPENAI_API_KEY was not found.")

# Initializing the OpenAI client with the API key
client = OpenAI(api_key = openai_api_key)
####################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################

# Starting a loop to continuously receive user input and adhere to the commands provided by the user
while True:

    print("--------------------------------")
    print("Model Tank ready.")
    print('Type "help" for commands.')
    user_message = input("User: ")
    command = " ".join(user_message.lower().split())

    command_dict = {
        "exit": commands.exitProgram,
        "time": commands.showTime,
        "date": commands.showDate,
        "clear": commands.clearScreen,
        "help": commands.displayHelp,

        "take note": notes.takeNote,
        "take notes": notes.takeNote,
        "make a note": notes.takeNote,

        "show notes": notes.showNotes,
        "show my notes": notes.showNotes,
        "show notes": notes.showNotes,

    }
   
    # Handling user commands
    if command in command_dict:
        command_dict[command]()

    else:
        print("Model Tank Received:", user_message)