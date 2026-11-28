import json
import re

from pydantic import ValidationError

from app.schemas.notes import Notes
from app.services.llm.base import LLMClient
from app.services.prompt_generator import build_prompt


class NotesGenerationError(Exception):
    """Raised when the model's answer cannot be turned into valid notes."""


def extract_json(answer: str) -> str:
    """Strip code fences and any text around the JSON object."""
    text = answer.strip()
    fenced = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if fenced:
        text = fenced.group(1).strip()
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        text = text[start : end + 1]
    return text


def parse_notes(answer: str) -> Notes:
    data = json.loads(extract_json(answer))
    return Notes.model_validate(data)


def generate_notes(
    transcript: str, client: LLMClient, prompt_version: str = "v2"
) -> Notes:
    prompt = build_prompt(transcript, prompt_version)
    answer = client.generate(prompt)

    try:
        return parse_notes(answer)
    except (json.JSONDecodeError, ValidationError) as first_error:
        repair_prompt = (
            f"{prompt}\n\n"
            "Your previous answer could not be used.\n"
            f"Problem: {str(first_error)[:500]}\n"
            f"Previous answer:\n{answer}\n\n"
            "Return the corrected JSON only."
        )
        answer = client.generate(repair_prompt)
        try:
            return parse_notes(answer)
        except (json.JSONDecodeError, ValidationError) as second_error:
            raise NotesGenerationError(
                "The AI returned notes in an unusable format. Please try again."
            ) from second_error