import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

from app.services.llm.base import LLMClient, LLMConfigError, LLMUnavailable

load_dotenv()

DEFAULT_MODEL = "gemini-3.1-flash-lite"
RETRYABLE_CODES = {429, 500, 503}


class GeminiClient(LLMClient):
    def __init__(self, model: str = DEFAULT_MODEL, max_attempts: int = 4):
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise LLMConfigError("GEMINI_API_KEY is missing. Add it to backend/.env.")
        self.client = genai.Client(api_key=key)
        self.model = model
        self.max_attempts = max_attempts

    def generate(self, prompt: str) -> str:
        delay = 2
        for attempt in range(1, self.max_attempts + 1):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                    config=types.GenerateContentConfig(temperature=0.2),
                )
            except errors.APIError as e:
                if e.code not in RETRYABLE_CODES:
                    raise LLMConfigError(
                        f"Gemini rejected the request (HTTP {e.code}): {e.message}"
                    ) from e
                if attempt == self.max_attempts:
                    raise LLMUnavailable(
                        "The AI service is busy. Please try again in a minute."
                    ) from e
                time.sleep(delay)
                delay *= 2
                continue

            text = response.text
            if not text:
                raise LLMUnavailable("The AI service returned an empty answer.")
            return text

        raise LLMUnavailable("The AI service did not answer.")