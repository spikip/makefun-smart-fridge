"""Entry for the make.fun bounty "Roast the Smart Fridge: One Line, Best Laugh Wins".

The program writes a single line roasting a smart fridge to
/output/entry.txt. The line is built on one specific behaviour: the
fridge scans expiry dates and nags about them in notifications, so it
behaves like a live-in nutritionist. That gives the roast a real
gadget to bite — not a generic smart-home joke and not the stock
line about a fridge ordering too much milk. The sting lands at the
end: the nutritionist lives in my kitchen and pays no rent. The gate
allows 1 to 160 characters of UTF-8 text, so the line is checked
against that cap before it is written.

Why this line: the judge weighs whether the line really roasts a
smart home gadget, whether it earns a real laugh, whether the angle
is fresh, whether it sets up fast and lands in one line, and whether
it names a real behaviour of the thing. The expiry-date scan is a
real behaviour, the nutritionist image is a fresh angle, and the
"pays no rent" ending turns the nagging into a joke about a bad
roommate, which is quotable enough to repeat to someone else.
"""

import os

ENTRY = (
    "My smart fridge scans expiry dates and sighs at me in "
    "notifications, like a nutritionist who lives in my kitchen "
    "and pays no rent."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One line, one sentence, no trailing newline: the gate counts
    # characters, so the entry is written exactly as judged.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
