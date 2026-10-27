#!/usr/bin/env python3
"""
Gemini Music Integration — The "Originality" Layer.

This module will eventually use the Google Gemini API (Lyria RealTime) to
re-style or re-interpret downloaded MIDI files. The goal is to maintain the
original mood and musical structure while producing a sufficiently
transformed version that avoids copyright claims.

Planned workflow (Gemini API integration — NOT YET IMPLEMENTED):
  1. Load the raw MIDI from midis/raw/.
  2. Send it to the Gemini Lyria RealTime endpoint for re-interpretation.
  3. Receive the transformed MIDI back.
  4. Save the result to midis/processed/.

For now, this module simply copies files from midis/raw/ to midis/processed/
as a pass-through placeholder.
"""

import shutil
from pathlib import Path

RAW_DIR = Path("midis/raw")
PROCESSED_DIR = Path("midis/processed")


def remix_with_gemini(input_midi_path: str | Path) -> Path:
    """
    Placeholder for Gemini API MIDI re-styling.

    Eventually this function will:
      - Call the Gemini API (Lyria RealTime) with the input MIDI
      - Apply a re-interpretation / re-styling pass
      - Return the path to the transformed MIDI

    For now it copies the file from midis/raw/ to midis/processed/ unchanged.

    Args:
        input_midi_path: Path to a .mid file (typically in midis/raw/).

    Returns:
        Path to the processed file in midis/processed/.
    """
    src = Path(input_midi_path)
    if not src.exists():
        raise FileNotFoundError(f"Input MIDI not found: {src}")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PROCESSED_DIR / src.name
    shutil.copy2(src, dest)
    print(f"  [pass-through] {src.name} -> {dest}")
    return dest


def process_all() -> list[Path]:
    """Run remix_with_gemini on every .mid file in midis/raw/."""
    raw_files = sorted(RAW_DIR.glob("*.mid"))
    if not raw_files:
        print("No .mid files found in midis/raw/. Run the scraper first.")
        return []

    print(f"Processing {len(raw_files)} file(s) through Gemini layer...\n")
    results: list[Path] = []
    for midi_file in raw_files:
        results.append(remix_with_gemini(midi_file))

    print(f"\nDone — {len(results)} file(s) in {PROCESSED_DIR}/")
    return results


if __name__ == "__main__":
    process_all()
