# SPDX-License-Identifier: MIT
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one fixed, original monologue to /output/entry.txt.
Deterministic: the text is a constant; no randomness, no time,
no network, no environment input. Pure Python 3.13 stdlib.
"""

MONOLOGUE = (
    "Right. The crown. I, Lord Veylan, took it\u2014 Aldermere, the Ember Throne\u2014 "
    "and here you stand, sword out, like the bards promised. "
    "Sit down, hero. No\u2014 you stand. I'll sit. "
    "I've been standing since the siege of Thornwick, and my knees have filed a complaint. "
    "Where was I? The list. Burn the granaries, hang the banners, promote... "
    "whatshisname. The tall one. "
    "I have the relic, the kingdom, your rebellion's names, spelled correctly, mostly. "
    "So kneel, or don't. The dungeon's full, the executioner retired, "
    "and the worst thing I could do to you... is let you win, and hand you the paperwork."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
