from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
    IpBlocked,
    RequestBlocked
)


class TranscriptUnavailable(Exception):
   """Raised when a transcript cannot be retrieved for a video."""


def fetch_transcript(video_id: str) -> list[dict]:
    """Return transcript segments as dicts with text, start and duration."""
    api = YouTubeTranscriptApi()
    try:
        transcript = api.fetch(video_id, languages=["en"])
    except VideoUnavailable as e:
        raise TranscriptUnavailable("This video does not exist or is unavailable.") from e
    except TranscriptsDisabled as e:
        raise TranscriptUnavailable("Captions are disabled for this video.") from e
    except NoTranscriptFound as e:
        raise TranscriptUnavailable("No English transcript exists for this video.") from e
    except (IpBlocked, RequestBlocked) as e:
        raise TranscriptUnavailable("You had made a lot of petitions to Youtube, temporarily blocking transcript requests. Please try again later.")

    return [
        {"text": s.text, "start": s.start, "duration": s.duration}
        for s in transcript
    ]