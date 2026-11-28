from app.services.youtube import parse_video_id
from app.services.transcript import fetch_transcript
from app.services.cleaning import clean_transcript
from app.services.prompt_generator import generate_prompt
from app.services.llm.gemini import GeminiClient




def process_video(url):

    gemini = GeminiClient()

    video_id = parse_video_id(url)
    transcript = fetch_transcript(video_id)
    cleaned = clean_transcript(transcript)
    prompt = generate_prompt(cleaned)
    notes = gemini.generate_notes(prompt)


    return notes

print(process_video("https://www.youtube.com/watch?v=ERI_2wwX0jg"))