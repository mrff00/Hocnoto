from google import genai
import os
from dotenv import load_dotenv
import json



load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("tests/prompts/prompt1_Test.json", encoding="utf-8") as f:
    prompt = json.load(f)

response = client.models.generate_content_stream(
    model="gemini-3.1-flash-lite",
    contents=prompt
)

for stream in response:
    print(stream.text)


