import pytest  # pants: no-infer-dep

from lib import normalize_date


@pytest.mark.parametrize(
    "s",
    [
        "",
        "  ",
        "some text",
        "132",
        # A date is expected to have exactly 3 `/`s
        "132/1 41/2",
        "132/1/41/2",
    ],
)
def test_ignore_non_dates(s: str) -> None:
    assert normalize_date(s) == s.strip()


@pytest.mark.parametrize(
    "date,expected",
    [
        ("24/4/63", "4/24/20"),
        ("6/1/64", "1/6/21"),
        ("22/5/63", "5/22/20"),
        ("22/5/70", "5/22/27"),
    ],
)
def test_single_thai_date(date: str, expected: str) -> None:
    assert normalize_date(date) == expected


@pytest.mark.parametrize(
    "date,expected",
    [
        ("10/3/2022", "3/10/2022"),
        ("28/1/24", "1/28/24"),
    ],
)
def test_european_style_date(date: str, expected: str) -> None:
    assert normalize_date(date) == expected


@pytest.mark.parametrize(
    "date,expected",
    [
        ("Thursday 23/7/63", "Thursday 7/23/20"),
        ("S. 27/3/64", "S. 3/27/21"),
        ("Thu. 8/4/64", "Thu. 4/8/21"),
        ("Thursday 23/7/63 more words", "Thursday 7/23/20 more words"),
    ],
)
def test_date_with_surrounding_words(date: str, expected: str) -> None:
    assert normalize_date(date) == expected


def test_multiple_dates() -> None:
    assert normalize_date("24/4/63,27/4/63, 28/4/63") == "4/24/20 4/27/20 4/28/20"


@pytest.mark.parametrize(
    "date,expected",
    [
        ("24/4/U 63", "4/24/U 63"),
        ("6/1/", "1/6/"),
    ],
)
def test_invalid_year(date: str, expected: str) -> None:
    assert normalize_date(date) == expected
