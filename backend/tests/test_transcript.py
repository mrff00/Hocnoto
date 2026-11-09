from types import SimpleNamespace

import pytest
from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

from app.services.transcript import TranscriptUnavailable, fetch_transcript


def make_fake_api(result=None, error=None):
    class FakeApi:
        def fetch(self, video_id, languages=None):
            if error is not None:
                raise error
            return result

    return FakeApi


def make_exception(cls):
    """Create a library exception without calling its constructor."""
    return cls.__new__(cls)


def test_returns_segments_as_dicts(monkeypatch):
    fake_snippets = [
        SimpleNamespace(text="hello", start=0.0, duration=1.5),
        SimpleNamespace(text="world", start=1.5, duration=2.0),
    ]
    monkeypatch.setattr(
        "app.services.transcript.YouTubeTranscriptApi",
        make_fake_api(result=fake_snippets),
    )

    assert fetch_transcript("abcdefghijk") == [
        {"text": "hello", "start": 0.0, "duration": 1.5},
        {"text": "world", "start": 1.5, "duration": 2.0},
    ]


@pytest.mark.parametrize(
    "library_error",
    [VideoUnavailable, TranscriptsDisabled, NoTranscriptFound],
)
def test_library_errors_become_transcript_unavailable(monkeypatch, library_error):
    monkeypatch.setattr(
        "app.services.transcript.YouTubeTranscriptApi",
        make_fake_api(error=make_exception(library_error)),
    )

    with pytest.raises(TranscriptUnavailable):
        fetch_transcript("abcdefghijk")


def test_original_error_is_kept_as_cause(monkeypatch):
    original = make_exception(TranscriptsDisabled)
    monkeypatch.setattr(
        "app.services.transcript.YouTubeTranscriptApi",
        make_fake_api(error=original),
    )

    with pytest.raises(TranscriptUnavailable) as excinfo:
        fetch_transcript("abcdefghijk")

    assert excinfo.value.__cause__ is original