# AGENTS.md: ultimate-music

Instructions for AI agents (Claude Code, Codex, Cursor and others) working in this repo for Brando Miranda. Shared rules live in https://github.com/brando90/agents-config; this file adds what is specific to music.

## Purpose

Brando's music: song ideas, arrangements (including Metallica-style orchestral arrangements), Suno prompts and takes, mastering notes, MIDI files and release tracking. Music is for fun first. Money, maybe, comes later.

**Release path:** Spotify through [RouteNote](https://routenote.com) free tier first, then DistroKid (paid, about $25 a year as a labeled best guess) if the catalog grows. Details: `docs/release-checklist.md`.

## Repo layout

| Path | What it holds |
|---|---|
| `tracks/` | One notes file per song, copied from `tracks/TEMPLATE.md` |
| `experiments/` | One folder per experiment (for example Suno prompts and a take log), each with a short README: goal, prompt, result |
| `midi-music-library/` | The MIDI-to-score archive, ported from `brando90/midi-music-library` with its history |
| `docs/release-checklist.md` | Step by step checklist from final mix to live on Spotify |
| `agents/AGENTS.md` | Short agent notes kept from the first layout; this file is the main one |
| `exports/` | Local audio exports (WAV masters, stems, cover art). Not committed; see below |

## Where audio exports go

- Put every WAV master, stem and cover image in `exports/<track-slug>/` on the machine that made it. The folder is git-ignored so large files stay out of the repo.
- Name files `<track-slug>_<version>.wav`, for example `my-song_v2_master.wav`. New version, new file.
- In the song's `tracks/<track-slug>.md`, record the final file name, where it is stored (Drive link or machine path), the loudness and the date.
- Small files (a cover image under about 2 MB, short MIDI) may be committed beside the track notes.

## Rules

- Commit straight to `main`. No branches, no pull requests. Run `git pull --rebase` before every push, since other agents push here too.
- Never delete anything. Add new versions beside old ones; old takes stay. Archiving something needs Brando's word.
- Proofread everything you write. No typos, and spell the name Miranda correctly.
- Covers need a cover-song license from the distributor before release (RouteNote and DistroKid both offer one). A Metallica arrangement counts as a cover. Original songs do not need one. Check Suno's plan terms before releasing anything made there.
- Never upload or submit a release to any distributor, and never spend money, without Brando's explicit yes.
- Money: the only payment allowed is a ONE-TIME cover-song license of $30 or less in total (Brando, Oct 27), never yearly, recurring or renewing. Stop and tell Brando if the total is higher or any renewal appears. Checkout always stops so he sees the exact charge and enters his own card; never type or store card details. Any other spend needs his explicit yes.
- Follow `docs/release-checklist.md` for every release: 44.1 kHz, 16-bit WAV, peaks under 0 dB, about -14 LUFS, cover art 3000 x 3000.
- Every copy-paste prompt you give Brando for another agent carries a suggested model and reasoning effort.
- Reports and messages to Brando: no TLDR at the top; end with one closing line, `TLDR-end: [project: task] ...`.
- Give real results only: commit links, file names, numbers. Say plainly what did not work.

## Naming and tone (Brando, Oct 27)

- Everything is professional in tone and presentation: titles, file names, notes, cover art text, commit messages, release copy. Artistic, never sloppy or jokey.
- Titles are excellent, professional and artistic. They keep the song's own name (for the Metallica jazz cover, "The Day That Never Comes"). No word is required in a title; the word "ultimate" does not have to appear. Current release title: **The Day That Never Comes (Jazz Quintet Suite)**. Brando can change it; he may drop "Suite".
- Never put "MP3" or any other file-type suffix (WAV, MIDI, PDF) in a song or release title, for example "The Day That Never Comes", never "The Day That Never Comes MP3".
- Never delete a file without Brando's yes. Add new versions beside old ones.
