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

# Starting a loop to continuously receive user input and print it back until the user types "exit"
while True:
    user_message = input("User: ")
    command = user_message.lower()

    if command == "exit":
        print("Model Tank Shutting Down...")
        break
    elif command == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print("The Current Time is:", current_time)
    else:
        print("Model Tank Received:", user_message)