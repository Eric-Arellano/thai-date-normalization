import re


def normalize_date(s: str) -> str:
    # Split into words, separated by `,` or a space. This is meant to handle how sometimes
    # there will be multiple dates, or there will be extra words like `Saturday`.
    words = re.split(r",|\s", s)
    new_words = []
    for word in words:
        if not word.strip():
            continue
        if word.count("/") != 2:
            new_words.append(word)
            continue
        day, month, year = word.split("/")
        likely_thai_year = len(year) == 2 and "6" <= year[0] < ":"
        if likely_thai_year:
            try:
                year = str(int(year) - 43)
            except TypeError:
                pass
        new_words.append(f"{month}/{day}/{year}")

    return " ".join(new_words)
