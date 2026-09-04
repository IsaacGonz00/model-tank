import os
from datetime import datetime

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Loading environment variables from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Indicating that Model Tank is initializing
print("Model Tank initializing...")

# Checking to see if the OPENAI_API_KEY environment variable is set 
if openai_api_key is None:
    print("OPENAI_API_KEY was not found.")

# Initializing the OpenAI client with the API key
client = OpenAI(api_key = openai_api_key)

# Starting a loop to continuously receive user input and adhere to the commands provided by the user, until the user types "exit"
while True:
    user_message = input("User: ")
    command = user_message.lower()

    if command == "exit":
        print("Model Tank Shutting Down...")
        break
    elif command == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("The Current Time is:", current_time)
    elif command == "date":
        current_date = datetime.now().strftime("%m/%d/%y")
        print("The Current Date is:", current_date)
    elif command == "take note":
        note = input("Please enter your note: ")
        with open("data/notes.txt", "a") as file:
            file.write(note + "\n")
        print("Note saved.")
    elif command == "help":
        print("Available Commands:")
        print("1. time - Displays the current time.")
        print("2. date - Displays the current date.")
        print("3. take note - Allows you to save a note.")
        print("4. help - Displays this help message.")
        print("5. exit - Exits the program.")
    else:
        print("Model Tank Received:", user_message)