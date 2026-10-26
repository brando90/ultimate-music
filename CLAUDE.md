# CLAUDE.md — The MIDI-to-Score Archive

<!-- Layer 1 entry point — bootstraps to ~/agents-config (Layer 2 + 3) -->
<!-- See: https://github.com/brando90/agents-config -->

## Bootstrap

```bash
# Clone or update the shared agents-config repo
if [ -d "$HOME/agents-config" ]; then
  git -C "$HOME/agents-config" pull --quiet
else
  git clone https://github.com/brando90/agents-config.git "$HOME/agents-config"
fi
```

Read `~/agents-config/INDEX_RULES.md` at task start for global rules and doc routing.

## Hard Rules

1. **TLDR on every response** — Start every answer with a 1-2 sentence TLDR.
2. **QA before marking done** — Verify correctness (run tests, lint, type-check) before declaring a task complete.
3. **No secrets** — Never commit API keys, tokens, or credentials. Use environment variables.
4. **Config freshness** — Pull `~/agents-config` at each task start.
5. **LaTeX / ML writing** — When editing `.tex` files, follow `~/agents-config/writing/ml_research_writing.md`.

## Project-Specific Context

- **Project**: The MIDI-to-Score Archive
- **Language**: Python 3.10+
- **Key dependencies**: requests, beautifulsoup4, MuseScore 4 CLI
- **Directory layout**:
  - `midis/raw/` — Downloaded MIDI files from vgmusic.com
  - `midis/processed/` — MIDIs after Gemini re-styling pass
  - `scores/pdf/` — Final high-quality PDF sheet music
  - `scores/mscz/` — MuseScore project files
- **Entry points**:
  - `scraper.py` — Downloads MIDI files from vgmusic.com (SNES section)
  - `gemini_music.py` — Gemini API integration for MIDI re-styling
  - `process_scores.py` — MuseScore CLI pipeline (MIDI → .mscz → .pdf)

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the scraper
python scraper.py

# Process MIDIs through Gemini layer
python gemini_music.py

# Convert processed MIDIs to scores
python process_scores.py
```

## Testing

```bash
python -m pytest tests/ -v
```
