"""Write the GPS's one-line excuse to /output/entry.txt."""

from pathlib import Path

ENTRY_TEXT = "In 200 meters, turn right at the stranger's wedding. Wrong address, I know — but your destination had no cake."


def main():
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
