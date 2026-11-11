class UnclearTranscript(Exception):
    """Return clean string"""
    raise NotImplementedError



def clean_transcript(segments: list[dict]) -> str:
    """Return one clean string built from transcript segments."""
        