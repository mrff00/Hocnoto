import re
import json

class InvalidTranscript(ValueError):
    """Raised when a transcript is empty or invalid."""


def clean_transcript(segments: list[dict]) -> str:
    """Return one clean string built from transcript segments."""

    if not isinstance(segments, list) or not segments:
        raise InvalidTranscript("Transcript must be a non-empty list")

    transcript = []

    for s in segments:
        if not isinstance(s, dict) or not isinstance(s.get("text"), str):
            raise InvalidTranscript("Invalid transcript segment")

        text = s["text"].strip()
        text = re.sub(r"\s+", " ", text)
        text = text.replace("\u2019", "'")
        text = text.replace('"', "'")
        text = text.replace("\u201c", "")
        text = text.replace("\u201d", "")

        if text:
            transcript.append(text)

    cleaned = " ".join(transcript)

    if not cleaned:
        raise InvalidTranscript("Transcript contains no usable text")

    return cleaned

    
    
with open("tests/fixtures/tedTalk_Advice_Transcript.json", encoding="utf-8") as f:
    segments = json.load(f)

print(clean_transcript(segments))