# Suno prompt variants: orchestral beautify

Style-field prompts, written in the same short, era-tagged, instrument-explicit shape as the May 2026 jazz prompts (Suno V5 style). Suggested settings are starting points: Suno's controls change, so match them to the current screen.

## Universal add-on (paste at the end of any prompt)

> instrumental only, no vocals, no electric guitar, no distortion, no rock drums

## Variants

| ID | Style prompt | Suggested settings | Goal |
|---|---|---|---|
| O1 | Cinematic orchestral ballad, 66 BPM, warm string section carrying the melody, french horns and woodwinds, soft timpani, concert hall reverb, emotional slow build, film score | Audio input = playback MP3. High audio influence (keep the melody). Low weirdness. Instrumental on | Closest to the arrangement: same notes, real-orchestra sound |
| O2 | Symphonic metal ballad in an acoustic orchestra, 66 BPM, lush strings and brass swells, cello lead in the verses, full brass climax, big timpani and cymbal crescendo, no electric guitar | Audio influence high, weirdness low to medium | Keep Metallica's dynamic arc (clean intro, slow burn, anthem finale) |
| O3 | San Francisco Symphony style concert orchestra, live recording, 66 BPM, expressive violins and violas, rich cellos and basses, clear woodwind solos, dark romantic, 19th century romantic orchestration | Audio influence medium to high, weirdness medium | The "professional SF orchestra" sound |
| O4 | Intimate chamber orchestra, 60 BPM, solo cello and piano with sparse strings, oboe countermelody, delicate, tender, studio recording | Audio influence high, weirdness low | Quiet, gentle version of the verses |
| O5 | Epic trailer orchestra, 72 BPM, powerful low strings ostinato, soaring brass, huge percussion, choir-free, dramatic and heroic, film trailer score | Audio influence medium, weirdness medium | Bold finale, more drama than the original |
| O6 | Neo-classical string quartet, 66 BPM, two violins, viola and cello, expressive vibrato, clean close-mic recording, melancholic | Audio influence high, weirdness low | Fallback if full orchestra sounds muddy |

Add-on for muddy or synthetic results: "acoustic instruments only, real orchestra recording, natural dynamics, no synthesizers".

## Lyrics field structure tags (instrumental; paste for any variant)

```
[Intro - clean strings, sparse]
[Theme - melody on strings]
[Theme - melody continues, brass joins]
[Build - dynamic growth, timpani]
[Theme - full orchestra]
[Solo - lead instrument takes the anthemic melody]
[Bridge - tension, dynamic dip]
[Final Theme - full orchestra peak]
[Outro - strings fade]
```

## Evaluation checklist (per take)

Musical:
- [ ] Melody and structure still match the score (play the take against the PDF)
- [ ] Sounds like an acoustic orchestra, not a synth or a band
- [ ] Dynamics: clear quiet intro, a real build, a big finale
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
