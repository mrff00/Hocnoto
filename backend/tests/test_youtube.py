import pytest

from app.services.youtube import InvalidYouTubeURL, parse_video_id 


VALID_ID = "dQw4w9WgXcQ"

@pytest.mark.parametrize(
    "url",
    [
        f"https://www.youtube.com/watch?v={VALID_ID}",
        f"https://youtu.be/{VALID_ID}"
    ]

)

def test_valid_urls_return_the_id(url):
    assert parse_video_id(url) == VALID_ID

@pytest.mark.parametrize(
    "bad_url",
    [
        "",
        "not a url",
        "https://www.youtube.com/shorts/dQw4w9WgXcQ",
        "https://www.youtube.com/embed/dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=abc",           # too short
        "https://www.youtube.com/watch?v=dQw4w9WgXcQx",  # too long
        "https://www.youtube.com/watch?v=!!!!!!!!!!!",   # bad characters
        "https://youtu.be/",                              # empty ID

    ]
)


def test_invalid_urls_raise(bad_url):
    with pytest.raises(InvalidYouTubeURL):
        parse_video_id(bad_url)