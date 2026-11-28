from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


def build_prompt(transcript: str, version: str = "v2") -> str:
    template = (PROMPTS_DIR / f"{version}_notes.md").read_text(encoding="utf-8")
    return template.replace("{{TRANSCRIPT}}", transcript)
