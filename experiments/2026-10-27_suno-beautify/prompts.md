# Suno prompt variants: orchestral beautify

Style-field prompts, written in the same short, era-tagged, instrument-explicit shape as the May 2026 jazz prompts (Suno V5 style). Suggested settings are starting points: Suno's controls change, so match them to the current screen.

## Universal add-on (paste at the end of any prompt)

> instrumental only, no vocals, no electric guitar, no distortion

## What the score says (checked with pdftotext on the PDF)

- Tempo: **q=124**, marked "Gently". Two "rit." marks near the end.
- Rehearsal markings: "Intro" at the start and "Bridge" twice. Nothing else is labeled, so the structure tags below are guesses.
- Key areas: Am and Em chords appear throughout.
- Dynamics: mp, mf, f and ff all appear (f and mf most often).
- Instruments: flute, clarinet, bassoon, soprano/alto/tenor/baritone saxophone, two horns in F, trumpet, trombone, euphonium, glockenspiel, vibraphone, piano, two harps, violins, viola, cello, contrabass and drum kit. There is **no timpani and no choir** in the score.

All variants below use the score's tempo, 124 BPM, so the style field does not fight the audio input. If a take feels rushed, a half-time reading (62 BPM) is an alternative to try; that is a guess, not something in the score.

## Variants

| ID | Style prompt | Suggested settings | Goal |
|---|---|---|---|
| O1 | Cinematic orchestral ballad, 124 BPM, warm string section carrying the melody, french horns and woodwinds, harp and glockenspiel colors, concert hall reverb, emotional slow build, film score | Audio input = playback MP3. High audio influence (keep the melody). Low weirdness. Instrumental on | Closest to the arrangement: same notes, real-orchestra sound |
| O2 | Symphonic ballad for acoustic orchestra, 124 BPM, lush strings and brass swells, cello lead in the quiet parts, full brass and woodwind climax, soft drum kit and cymbal crescendo, no electric guitar | Audio influence high, weirdness low to medium | Keep the dynamic arc from the score (mp up to ff) |
| O3 | Concert orchestra live recording, 124 BPM, expressive violins and violas, rich cellos and basses, clear woodwind and saxophone solos, dark romantic, professional symphony hall sound | Audio influence medium to high, weirdness medium | The "professional SF orchestra" sound |
| O4 | Intimate chamber orchestra, 124 BPM, gentle, solo cello and piano with sparse strings, clarinet and flute countermelody, delicate, tender, studio recording | Audio influence high, weirdness low | Quiet, gentle version (the score is marked "Gently") |
| O5 | Epic cinematic orchestra, 124 BPM, powerful low strings, soaring horns and trumpet, big percussion, dramatic and heroic, film trailer score, no choir | Audio influence medium, weirdness medium | Bold finale, more drama than the original |
| O6 | Neo-classical string ensemble, 124 BPM, violins, viola and cello, expressive vibrato, clean close-mic recording, melancholic | Audio influence high, weirdness low | Fallback if the full orchestra sounds muddy |

Add-on for muddy or synthetic results: "acoustic instruments only, real orchestra recording, natural dynamics, no synthesizers".

## Lyrics field structure tags (guess, not from the score)

The score labels only "Intro" and "Bridge", so this order is a starting guess. Check it against a take and adjust.

```
[Intro - gentle, sparse]
[Theme - melody on strings and woodwinds]
[Theme - melody continues, brass joins]
[Build - dynamic growth]
[Theme - full orchestra]
[Bridge - tension, dynamic dip]
[Final Theme - full orchestra peak]
[Outro - ritardando, fade]
```

## Evaluation checklist (per take)

Musical:
- [ ] Melody and structure still match the score (play the take against the PDF)
- [ ] Sounds like an acoustic orchestra, not a synth or a band
- [ ] Dynamics follow the score: gentle start (mp), builds through mf and f, loudest sections ff, ritardando at the end
- [ ] No artifacts, glitches, vocals or cut-off ending

Technical (before release):
- [ ] Final master is a WAV, 44.1 kHz, 16-bit, stereo
- [ ] Peaks under 0 dB (true peak about -1 dB is safer)
- [ ] Loudness about -14 LUFS integrated
- [ ] Cover art 3000 x 3000 px, no store logos or URLs
- [ ] Cover-song license handled (see README), original songwriters credited
- [ ] Suno plan and terms allow release

## Take log

Newest first. Add a row for every take, including the bad ones.

| Date | Take | Variant | Suno link or file | Audio input | Settings used | Melody OK? | Sound (1 to 10) | Keep? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| (next take goes here) | | | | | | | | | |
| 2026-05 (before this experiment) | J1 | Charlie Parker bebop prompt from the blog post | https://suno.com/s/1RTl4ch6L6LlbIFP | Playback MP3 | Not recorded | n/a | n/a | n/a | Jazz recast, not orchestral |
