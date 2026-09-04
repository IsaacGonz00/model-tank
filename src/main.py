import os
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

# Checking to see if Model Tank is echoing user input
user_message = input("User: ")
print("Model Tank Received:", user_message)