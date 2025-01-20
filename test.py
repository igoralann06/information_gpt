import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)

try:
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt="Say hello!",
        max_tokens=5
    )
    print(response.choices[0].text.strip())
except Exception as e:
    print(f"Error: {e}")