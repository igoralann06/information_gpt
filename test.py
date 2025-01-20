import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

try:
    # Use the correct API method for GPT-4
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Use "gpt-4" or "gpt-4-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello!"}
        ],
        max_tokens=5
    )
    print(response.choices[0].message['content'].strip())
except Exception as e:
    print(f"Error: {e}")