import re


def clean_transcript(segments: list[dict]) -> str:
    """Return one clean string built from transcript segments."""
    pieces = []
    for segment in segments:
        text = segment["text"]
        text = re.sub(r"\[[^\]]*\]", "", text)
        text = " ".join(text.split())
        if text:
            pieces.append(text)
    return " ".join(pieces)