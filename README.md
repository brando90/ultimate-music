# ultimate-music

Brando's ultimate music repo for everything, including Spotify ;)

## Purpose

This repo holds Brando's music: ideas, arrangements, prompts, release notes and the final tracks. Music is for fun first. Making money from it, maybe, comes later.

## Release plan

1. **First releases:** upload to Spotify and the other stores through [RouteNote](https://routenote.com) (free tier).
2. **Later:** if the catalog grows and earnings matter, move to DistroKid (paid, about $25 a year as a labeled best guess; check the current price before signing up).
3. **After the first release:** claim the artist profile in Spotify for Artists.

Covers need a cover-song license from the distributor before release. Original songs do not.

## Layout

| Path | What it holds |
|---|---|
| `tracks/` | One notes file per song, copied from `tracks/TEMPLATE.md` |
| `docs/release-checklist.md` | Step by step checklist from master to live on Spotify |
| `AGENTS.md`, `CLAUDE.md` | Instructions for AI agents (CLAUDE.md points to AGENTS.md) |
| `experiments/` | One folder per experiment (Suno prompts, take logs) |
| `midi-music-library/` | MIDI-to-score archive |
| `exports/` | Local audio exports, git-ignored |

## Rules of thumb

- Work goes straight to `main`. No branches.
- Nothing is deleted. Old takes stay, new ones are added beside them.
- Large audio files (WAV, stems) stay out of git unless they are small; link to where they live in the song's notes file.
