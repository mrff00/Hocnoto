from urllib.parse import urlparse, parse_qs


class InvalidYouTubeURL(ValueError):
    """Raised when a string is not a valid YouTube video URL."""


YOUTUBE_HOSTS = {"www.youtube.com", "youtube.com", "m.youtube.com"}
SHORT_HOST = "youtu.be"


def parse_video_id(url: str) -> str:
    """Return the 11-character video ID from a YouTube URL."""
    url = url.strip()
    parts = urlparse(url)

    if parts.netloc == SHORT_HOST:
        video_id = parts.path.lstrip("/")
    elif parts.netloc in YOUTUBE_HOSTS:
        if parts.path != "/watch":
            raise InvalidYouTubeURL("The link is not a watch link")
        ids = parse_qs(parts.query).get("v")
        if not ids:
            raise InvalidYouTubeURL("The link has no video ID")
        video_id = ids[0]
    else:
        raise InvalidYouTubeURL("The link is not from YouTube")

    if not video_id:
        raise InvalidYouTubeURL("The link has no video ID")
    return video_id