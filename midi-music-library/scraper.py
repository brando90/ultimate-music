#!/usr/bin/env python3
"""
Nintendo MIDI Scraper — Downloads MIDI files from vgmusic.com (SNES section).

Targets: Mega Man X, Mega Man X2, Donkey Kong Country.
Saves files to midis/raw/ with naming convention: GameTitle_TrackName.mid
"""

import os
import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.vgmusic.com/music/console/nintendo/snes/"
OUTPUT_DIR = Path("midis/raw")

# Map of game title substrings to look for -> sanitized prefix for filenames
TARGET_GAMES = {
    "Mega Man X2": "MegaManX2",
    "Mega Man X": "MegaManX",       # checked after X2 to avoid false matches
    "Donkey Kong Country": "DonkeyKongCountry",
}


def sanitize_filename(name: str) -> str:
    """Remove or replace characters that are problematic in filenames."""
    name = re.sub(r"[^\w\s\-]", "", name)
    name = re.sub(r"\s+", "_", name.strip())
    return name


def match_game(text: str) -> str | None:
    """Return the sanitized game prefix if *text* matches a target game."""
    for game_name, prefix in TARGET_GAMES.items():
        if game_name.lower() in text.lower():
            return prefix
    return None


def scrape_midi_links(session: requests.Session) -> list[dict]:
    """
    Parse the SNES page on vgmusic.com and return a list of dicts:
      [{"url": "<absolute url>", "game_prefix": "...", "track_name": "..."}, ...]
    """
    print(f"Fetching index page: {BASE_URL}")
    resp = session.get(BASE_URL, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    midi_entries: list[dict] = []

    # vgmusic.com structures its SNES page as a large table.
    # Each game section has a header row followed by track rows containing .mid links.
    current_game_prefix: str | None = None

    for row in soup.find_all("tr"):
        cells = row.find_all("td")
        # Detect game header rows (typically bold or large-font cells)
        header = row.find(["b", "strong", "h3", "h4"])
        if header:
            current_game_prefix = match_game(header.get_text())

        if current_game_prefix is None:
            continue

        # Look for .mid links in this row
        for link in row.find_all("a", href=True):
            href = link["href"]
            if href.lower().endswith(".mid"):
                track_text = link.get_text(strip=True)
                track_name = sanitize_filename(track_text.removesuffix(".mid"))
                if not track_name:
                    track_name = sanitize_filename(Path(href).stem)
                midi_entries.append(
                    {
                        "url": urljoin(BASE_URL, href),
                        "game_prefix": current_game_prefix,
                        "track_name": track_name,
                    }
                )

    return midi_entries


def download_midis(
    session: requests.Session,
    entries: list[dict],
    output_dir: Path,
    delay: float = 1.0,
) -> list[Path]:
    """Download each MIDI entry to *output_dir*. Returns list of saved paths."""
    output_dir.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []

    for entry in entries:
        filename = f"{entry['game_prefix']}_{entry['track_name']}.mid"
        dest = output_dir / filename

        if dest.exists():
            print(f"  [skip] {filename} (already exists)")
            saved.append(dest)
            continue

        print(f"  [download] {filename}")
        try:
            resp = session.get(entry["url"], timeout=30)
            resp.raise_for_status()
            dest.write_bytes(resp.content)
            saved.append(dest)
        except requests.RequestException as exc:
            print(f"  [error] Failed to download {filename}: {exc}")

        # Be polite to the server
        time.sleep(delay)

    return saved


def main() -> None:
    session = requests.Session()
    session.headers.update(
        {"User-Agent": "MIDIScoreArchive/1.0 (educational project)"}
    )

    entries = scrape_midi_links(session)
    print(f"\nFound {len(entries)} MIDI file(s) for target games.\n")

    if not entries:
        print("No matching MIDI files found. The page structure may have changed.")
        return

    saved = download_midis(session, entries, OUTPUT_DIR)
    print(f"\nDone — {len(saved)} file(s) saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
