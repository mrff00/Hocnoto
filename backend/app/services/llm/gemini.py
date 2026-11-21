from google import genai
import os
from dotenv import load_dotenv



load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content_stream(
    model="gemini-3.1-flash-lite",
    contents="Why is the sky blue?"
)

for stream in response:
    print(stream.text)


