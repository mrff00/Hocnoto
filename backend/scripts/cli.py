import argparse
import json
import sys
from pathlib import Path

from app.schemas.notes import Notes
from app.services.cleaning import clean_transcript
from app.services.llm.base import LLMConfigError, LLMUnavailable
from app.services.llm.gemini import GeminiClient
from app.services.note_generator import NotesGenerationError, generate_notes
from app.services.transcript import TranscriptUnavailable, fetch_transcript
from app.services.youtube import InvalidYouTubeURL, parse_video_id

OUTPUT_DIR = Path("outputs")


def format_notes(notes: Notes) -> str:
    """Turn validated notes into readable text for the terminal."""
    lines = [notes.title.upper(), "", notes.overview, ""]

    lines.append("TOPICS")
    for number, topic in enumerate(notes.topics, start=1):
        lines.append(f"{number}. {topic.heading}")
        lines.append(f"   {topic.explanation}")
        for sub in topic.subtopics:
            lines.append(f"   - {sub.heading}")
            for point in sub.points:
                lines.append(f"       * {point}")
    lines.append("")

    if notes.key_concepts:
        lines.append("KEY CONCEPTS")
        for concept in notes.key_concepts:
            lines.append(f"- {concept.term}: {concept.definition}")
        lines.append("")

    if notes.examples:
        lines.append("EXAMPLES")
        for example in notes.examples:
            lines.append(f"- {example.description}")
        lines.append("")

    lines.append("SUMMARY")
    lines.extend(f"- {bullet}" for bullet in notes.summary_bullets)
    lines.append("")
    lines.append("CONCLUSION")
    lines.append(notes.conclusion)
    return "\n".join(lines)


def save_notes(notes: Notes, video_id: str, prompt_version: str) -> Path:
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / f"{video_id}_{prompt_version}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(notes.model_dump(), f, ensure_ascii=False, indent=2)
    return path


def run(url: str, prompt_version: str, save: bool) -> str:
    video_id = parse_video_id(url)
    segments = fetch_transcript(video_id)
    text = clean_transcript(segments)
    notes = generate_notes(text, GeminiClient(), prompt_version)

    output = format_notes(notes)
    if save:
        path = save_notes(notes, video_id, prompt_version)
        output += f"\n\n[saved to {path}]"
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Turn a YouTube video into study notes.")
    parser.add_argument("url", help="the YouTube video link")
    parser.add_argument("--prompt", default="v2", help="prompt version (default: v2)")
    parser.add_argument("--save", action="store_true", help="also save the notes as JSON")
    args = parser.parse_args()

    try:
        print(run(args.url, args.prompt, args.save))
    except InvalidYouTubeURL as e:
        print(f"Invalid link: {e}", file=sys.stderr)
    except TranscriptUnavailable as e:
        print(f"No transcript: {e}", file=sys.stderr)
    except LLMUnavailable as e:
        print(f"AI service problem: {e}", file=sys.stderr)
    except LLMConfigError as e:
        print(f"Setup problem: {e}", file=sys.stderr)
    except NotesGenerationError as e:
        print(f"Notes failed: {e}", file=sys.stderr)
    else:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())