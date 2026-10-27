# The MIDI-to-Score Archive

A pipeline that scrapes classic Nintendo SNES MIDI files, processes them through a Gemini AI re-styling layer, and converts them into high-quality PDF sheet music using MuseScore 4.

## Requirements

- **Python 3.10+**
- **MuseScore 4** — installed and accessible from PATH (or set `MUSESCORE_PATH`)
- Python packages listed in `requirements.txt`

## Setup

```bash
# Clone the repository
git clone https://github.com/brando90/midi-music-library.git
cd midi-music-library

# Install Python dependencies
pip install -r requirements.txt
```

## Directory Structure

```
midi-music-library/
├── CLAUDE.md              # Agent config (agents-config bootstrap)
├── README.md
├── requirements.txt
├── scraper.py             # Step 1: Download MIDIs from vgmusic.com
├── gemini_music.py        # Step 2: Gemini re-styling pass (placeholder)
├── process_scores.py      # Step 3: MuseScore MIDI → PDF conversion
├── midis/
│   ├── raw/               # Downloaded .mid files
│   └── processed/         # MIDIs after Gemini processing
└── scores/
    ├── mscz/              # MuseScore project files
    └── pdf/               # Final PDF sheet music
```

## Pipeline

The pipeline runs in three stages:

### Step 1 — Scrape MIDI files

Downloads `.mid` files from [vgmusic.com](https://www.vgmusic.com/music/console/nintendo/snes/) for the following SNES games:

- Mega Man X
- Mega Man X2
- Donkey Kong Country

```bash
python scraper.py
```

Files are saved to `midis/raw/` with the naming convention `GameTitle_TrackName.mid`.

### Step 2 — Gemini re-styling (placeholder)

Passes each MIDI through the Gemini "originality" layer. Currently a pass-through that copies files from `midis/raw/` to `midis/processed/`. The eventual goal is to use the Gemini API (Lyria RealTime) to re-interpret each track while maintaining the original mood.

```bash
python gemini_music.py
```

### Step 3 — MuseScore conversion

Converts each processed MIDI into a MuseScore project (`.mscz`) and exports a high-quality PDF.

```bash
python process_scores.py
```

Requires MuseScore 4. If it's not on your PATH, set the environment variable:

```bash
export MUSESCORE_PATH=/path/to/mscore
python process_scores.py
```

### Run the full pipeline

```bash
python scraper.py && python gemini_music.py && python process_scores.py
```

## Configuration

| Environment Variable | Description | Default |
|---|---|---|
| `MUSESCORE_PATH` | Path to the MuseScore 4 executable | Auto-detected from PATH |

## License

See [LICENSE](LICENSE).
