from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()
transcript = api.fetch("dQw4w9WgXcQ", languages=["en"])

print(type(transcript))
print(transcript.language, transcript.is_generated)
for snippet in list(transcript)[:5]:
    print(snippet)