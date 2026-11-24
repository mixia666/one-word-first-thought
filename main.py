"""One Word, First Thought.

Writes exactly one word to /output/entry.txt: the first word that came
to mind. Apricity (noun, obsolete): the warmth of the sun on a cold
winter's day. Rare enough to surprise, specific enough to feel.
"""

import os

WORD = "Apricity"

OUTPUT_PATH = "/output/entry.txt"


def check_word(word: str) -> None:
    """Guard the gate: UTF-8 text of 1 to 24 characters, one word only."""
    if not word or len(word) > 24 or word.split() != [word]:
        raise ValueError(f"not a valid single-word entry: {word!r}")


def main() -> None:
    check_word(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: tied entries go to the smaller text, byte for
    # byte, so the file carries the word and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
