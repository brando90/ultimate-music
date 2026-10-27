#!/usr/bin/env python3
"""
MuseScore Pipeline — Headless CLI automation for MIDI-to-score conversion.

Iterates through midis/processed/ and uses the MuseScore 4 CLI to:
  1. Convert each .mid file to a .mscz (MuseScore project file).
  2. Export a high-quality .pdf from the .mscz.

Requires MuseScore 4 installed and accessible from the system PATH,
or configured via the MUSESCORE_PATH environment variable.
"""

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

PROCESSED_DIR = Path("midis/processed")
SCORES_MSCZ_DIR = Path("scores/mscz")
SCORES_PDF_DIR = Path("scores/pdf")


def find_musescore() -> str | None:
    """
    Locate the MuseScore 4 executable.

    Search order:
      1. MUSESCORE_PATH environment variable
      2. Common executable names on PATH
      3. Platform-specific default install locations
    """
    # 1. Environment variable override
    env_path = os.environ.get("MUSESCORE_PATH")
    if env_path and Path(env_path).is_file():
        return env_path

    # 2. Common names on PATH
    candidates = ["musescore4", "mscore", "MuseScore4", "musescore"]
    if platform.system() == "Windows":
        candidates.extend(["MuseScore4.exe", "mscore.exe"])

    for name in candidates:
        found = shutil.which(name)
        if found:
            return found

    # 3. Platform-specific default locations
    default_paths: list[str] = []
    if platform.system() == "Darwin":
        default_paths.append("/Applications/MuseScore 4.app/Contents/MacOS/mscore")
    elif platform.system() == "Windows":
        default_paths.extend(
            [
                r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe",
                r"C:\Program Files (x86)\MuseScore 4\bin\MuseScore4.exe",
            ]
        )
    else:  # Linux
        default_paths.extend(
            [
                "/usr/bin/mscore",
                "/usr/local/bin/mscore",
                "/snap/bin/musescore",
            ]
        )

    for p in default_paths:
        if Path(p).is_file():
            return p

    return None


def convert_midi_to_mscz(musescore: str, midi_path: Path, mscz_path: Path) -> bool:
    """Convert a MIDI file to MuseScore format (.mscz)."""
    mscz_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [musescore, "-o", str(mscz_path), str(midi_path)],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        return True
    except subprocess.CalledProcessError as exc:
        print(f"  [error] MIDI->MSCZ failed for {midi_path.name}: {exc.stderr}")
        return False
    except subprocess.TimeoutExpired:
        print(f"  [error] Timed out converting {midi_path.name} to .mscz")
        return False


def convert_mscz_to_pdf(musescore: str, mscz_path: Path, pdf_path: Path) -> bool:
    """Export a MuseScore file to high-quality PDF."""
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [musescore, "-o", str(pdf_path), str(mscz_path)],
            check=True,
            capture_output=True,
            text=True,
            timeout=120,
        )
        return True
    except subprocess.CalledProcessError as exc:
        print(f"  [error] MSCZ->PDF failed for {mscz_path.name}: {exc.stderr}")
        return False
    except subprocess.TimeoutExpired:
        print(f"  [error] Timed out exporting {mscz_path.name} to PDF")
        return False


def main() -> None:
    musescore = find_musescore()
    if not musescore:
        print(
            "ERROR: MuseScore 4 not found.\n"
            "Install MuseScore 4 and ensure it is on your PATH, or set the\n"
            "MUSESCORE_PATH environment variable to the executable location.\n"
            "  e.g.  export MUSESCORE_PATH=/usr/bin/mscore"
        )
        sys.exit(1)

    print(f"Using MuseScore at: {musescore}\n")

    midi_files = sorted(PROCESSED_DIR.glob("*.mid"))
    if not midi_files:
        print(f"No .mid files found in {PROCESSED_DIR}/. Run the earlier pipeline steps first.")
        return

    print(f"Processing {len(midi_files)} MIDI file(s)...\n")

    success_count = 0
    for midi_path in midi_files:
        stem = midi_path.stem
        mscz_path = SCORES_MSCZ_DIR / f"{stem}.mscz"
        pdf_path = SCORES_PDF_DIR / f"{stem}.pdf"

        print(f"  [{stem}]")

        # Step 1: MIDI -> .mscz
        if not convert_midi_to_mscz(musescore, midi_path, mscz_path):
            continue

        # Step 2: .mscz -> .pdf
        if not convert_mscz_to_pdf(musescore, mscz_path, pdf_path):
            continue

        print(f"    -> {pdf_path}")
        success_count += 1

    print(f"\nDone — {success_count}/{len(midi_files)} score(s) generated.")


if __name__ == "__main__":
    main()
