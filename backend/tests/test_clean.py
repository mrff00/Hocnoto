from app.services.cleaning import clean_transcript


def test_noise_tags_are_removed():
    segments = [
        {"text": "[Music]", "start": 0.0, "duration": 2.0},
        {"text": "hello there", "start": 2.0, "duration": 1.0},
        {"text": "world", "start": 3.0, "duration": 1.0},
    ]

    assert clean_transcript(segments) == "hello there world"