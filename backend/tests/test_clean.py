import pytest
import json

from app.services.cleaning import clean_transcript, InvalidTranscript

with open("tests/fixtures/tedTalk_Advice_Transcript.json", encoding="utf-8") as f:
    segments = json.load(f)

with open("tests/fixtures/git_Tutorial_Transcript.json", encoding="utf-8") as f2:
    segments2 = json.load(f2)


@pytest.mark.parametrize(
    "transcript", 
    [
        segments,
        segments2
    ]

)

def test_valid_transcript(transcript):
    assert clean_transcript(transcript) == segments2 or segments

@pytest.mark.parametrize(
    "bad_transcript", 
    [
        [],
        None,
        ""
        
    ]

)


def test_invalid_transcript(bad_transcript):
    with pytest.raises(InvalidTranscript):
        clean_transcript(bad_transcript)
print(segments2)