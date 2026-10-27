# Suno prompt template

A reusable way to write the style field and the lyrics (structure) field in Suno, built from the song Brando likes most so far: `tracks/the-day-that-never-comes-bebop.md`. Copy the blocks, fill in the brackets, and log the take in the song's notes file.

Suno's screens and limits change. When a menu name here is not on the screen, use the nearest match and fix this file afterwards.

## 1. Style field: formula

```
[Genre and era], [recording-era tag], [lead instrument + adjective], [rhythm section: bass, drums, comping], [tempo in BPM], [recording character], [ensemble size], [no X, no Y exclusions]
```

Rules that worked for the liked song:

- 8 to 14 comma-separated descriptors, concrete instruments instead of artist names.
- One era or label tag ("1947 Dial Records era") steers the sound more than adjectives do.
- Give an exact BPM.
- End with exclusions for what Suno tends to add by itself ("no orchestra, no strings, no rock, no metal").
- If a take drifts to smooth jazz or rock, append: `acoustic instruments only, no synthesizers, vintage analog recording, instrumental only, no vocals`.

**Worked example (the liked song, verbatim):**

```
Bebop jazz, 1947 Dial Records era, virtuosic alto sax, walking upright bass, fast jazz ride cymbal swing, snare bombs, jazz piano comping with rootless voicings, 220 BPM, mono recording warmth, vintage jazz quintet, no orchestra, no strings, no rock, no metal
```

## 2. Lyrics field: structure tags for an instrumental

One line per section, with the section name, who plays and what they do. No sung words.

```
[Intro: <instrument>, <length>]
[Theme: <who states the melody and how>]
[Verse 1: <solo instrument> over <rhythm section detail>]
[Verse 2: <next solo instrument>, <comping change>]
[Chorus: <return of the theme>]
[Bridge: <contrast section>]
[Outro: <how it ends>]
```

**Worked example (the liked song, verbatim):**

```
[Intro: solo alto sax, 4 bars unaccompanied]
[Theme: alto sax states melody, fast unison with trumpet]
[Verse 1: alto sax solo over walking bass, drum bombs]
[Verse 2: trumpet solo, busier piano comping]
[Chorus: alto sax returns to theme]
[Bridge: piano solo, sparse]
[Outro: alto sax restates head, sudden ending]
```

## 3. Variants to try (same formula)

| Goal | Change |
|---|---|
| Calmer take | Lower BPM (160 instead of 220), "brushed drums", "ballad" |
| Cleaner ending | Outro line: `[Outro: fade with piano and bass]` |
| Orchestral recast of a score | Use the prompts in `experiments/2026-10-27_suno-beautify/prompts.md` |
| Other jazz styles | Six ready prompts in `experiments/2026-10-27_suno-beautify/source-jazz-prompts-from-website.md` |

## 4. Generation habits

- Make 2 to 3 takes per prompt. The second or third is often the best.
- Keep every take that is worth a second listen. Never delete takes.
- Log each take (link, prompt version, what was good or bad) in the song's `tracks/<slug>.md` table.
- Pick the keeper by listening to the whole song once on headphones, not by the first 30 seconds.

## 5. Copy-paste prompt for an agent (Codex or Claude Code)

Suggested model and effort: Claude Opus 5.5 at xhigh, or Codex GPT-5.6 Sol at high.

```
In the repo brando90/ultimate-music, read AGENTS.md and docs/suno-to-spotify-workflow.md. For the song "<title>" with Suno link <url>: create tracks/<slug>.md from tracks/TEMPLATE.md, copy the title, style tags and lyrics from the Suno page exactly, mark the song type (original or cover), run the rights checks in the workflow, and stop before any upload. Commit straight to main, no branches. Do not upload to any distributor and do not spend money. List every step that needs Brando as "BRANDO MUST DO".
```
