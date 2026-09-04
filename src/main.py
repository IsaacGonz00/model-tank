import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

print("Model Tank initializing...")

if openai_api_key is None:
    print("OPENAI_API_KEY was not found.")