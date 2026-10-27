# First release candidate: "The Day That Never Comes" (bebop jazz recast), 2026-10-27

Brando's "jazz Metallica": his 2010 school-orchestra arrangement of Metallica's *The Day That Never Comes*, recast as bebop jazz by Suno. This folder holds the audio, the cover art and the facts a release needs. The Codex prompt that uses it is `prompts/codex-spotify.md`.

## Files

| File | What it is |
|---|---|
| `the-day-that-never-comes-bebop-44k-16bit.wav` | **The upload candidate.** WAV, 44.1 kHz, 16-bit, stereo, 3:01.92, 32 MB |
| `cover_3000.jpg` | Cover art, 3000 x 3000 JPG, upscaled from Suno's 1024 x 1024 image |

SHA-256 of the WAV: `a62cdf9b01bbda212341d869ff8ee26c211a6a8f4cfa4eb4220a74b2cb3e3f8a`

## Source and why it is the best available

- **Source:** the Suno take from Brando's blog post "Metallica Goes Jazz: A 2010 High School Arrangement, Reanimated by AI" (May 7, 2026): https://brando90.github.io/brandomiranda/2026/05/07/metallica-goes-jazz.html . Suno page: https://suno.com/s/1RTl4ch6L6LlbIFP . The other link in `tracks/the-day-that-never-comes-bebop.md` (https://suno.com/s/hoKp4qmYVfWsQsog) resolves to the same song id, `f991d6df-ade7-4c1a-9561-2dedaa4179c7`.
- **Original file:** `The Day That Never Comes MP3.wav` in https://github.com/brando90/brandomiranda under `experiments/00_metallica_goes_jazz/`. It is a lossless WAV, 48 kHz, 16-bit, stereo, 181.92 s, 34.9 MB, SHA-256 `a05f2cb091f6069b29fb37aa0c0a36237bc212dd059e1faec985d30eb9b66ee6`. Its length matches the 3:01 on the Suno page. The file name says "MP3" because that is the Suno title; the file itself is a WAV.
- **Why it is the best:** it is the only jazz audio that exists as a lossless WAV. The other audio is the Sibelius playback of the school-orchestra score (`tracks/metallica-orchestra/`, an MP3 mock-up and not jazz). Suno's own MP3 could not be fetched without signing in (HTTP 403), so the WAV is the highest-quality copy found.

## What was done to it

Two steps with ffmpeg 7.0.2, nothing else (no EQ, no compression, no edits):

1. Resample 48 kHz to 44.1 kHz, with triangular dither to 16-bit.
2. Raise the level by +0.7 dB, from -14.7 to -14.0 LUFS.

| Measure (ebur128) | Original WAV | Upload candidate |
|---|---|---|
| Sample rate / bit depth | 48 kHz / 16-bit | 44.1 kHz / 16-bit |
| Integrated loudness | -14.7 LUFS | -14.0 LUFS |
| True peak | -3.2 dBFS | -2.5 dBFS |
| Loudness range | 4.4 LU | 4.4 LU |

It meets `docs/release-checklist.md` section 1 on format, peaks (under 0 dB, true peak under -1 dB) and loudness (-14 LUFS). **Not yet done:** nobody has listened to the file in full, and the start and the ending have not been checked for silence or a cut-off tail. Brando does that listen before upload.

## Quality limits

- This is Suno's generated audio, not a studio recording. Suno's original files are lossy-compressed internally (unverified; not confirmed on Suno's pages), so the WAV may hold no more detail than a high-quality MP3. Good enough for streaming, not studio master quality.
- The cover art is a simple Lanczos upscale of a 1024 x 1024 image, so it looks soft at 3000 px. A sharper original would be better.
- Resampling 48 to 44.1 kHz is a small, standard loss.

## Open items before any upload

1. **Suno plan.** Songs made on the free plan are for personal, non-commercial use only. Which plan made this song is not recorded. See `docs/for-profit-vs-nonprofit.md` section 5.
2. **Cover license.** It is a Metallica cover. Brando said about $12 for the mechanical license is fine; nothing has been bought. See section 4 of the same doc.
3. **Release and artist name.** Release title chosen by Brando on Oct 27: *Ultimate Metallica: A Jazz Orchestra Suite* (he may change it); the track title stays exactly *The Day That Never Comes* because RouteNote requires covers to carry the original title. The title says "orchestra" while this recording is a Suno bebop quintet. Artist name not set; suggested default: Brando Miranda.
4. **Rights note on this repo.** The repo is public and holds an arrangement of a copyrighted song plus this recording; the open question in `experiments/2026-10-27_suno-beautify/README.md` still stands.
5. **AI disclosure.** The recording is Suno AI output made from Brando's own arrangement; if a distributor or Spotify asks, say so.
