# Suno to Spotify workflow

From "I like this Suno song" to a release on Spotify, step by step. First use: `tracks/the-day-that-never-comes-bebop.md`. Companion files: `prompts/suno-prompt-template.md` (how to write prompts), `docs/release-checklist.md` (tick-box list per release), `docs/for-profit-vs-nonprofit.md` (rights and money).

**Hard stop:** no agent uploads to any distributor, signs up to one, or spends money without Brando's explicit yes. Every step that needs Brando is marked **BRANDO MUST DO**.

Status of the commands below: written Oct 27, 2026. The ffmpeg and ImageMagick commands are standard usage; the ffmpeg ones were not run on the agent machine because ffmpeg is not installed there (the ImageMagick command was run and gave a 3000 x 3000 file). Run them once on a real file and fix this page if anything differs.

## Step 1. Create (Suno)

1. Write the style field and the lyrics (structure) field from `prompts/suno-prompt-template.md`.
2. Generate 2 to 3 takes. Keep all of them.
3. Log each take in `tracks/<slug>.md` (copy `tracks/TEMPLATE.md`).

## Step 2. Pick

1. Listen to every take in full. Judge melody, structure, ending, artifacts (glitches, swallowed notes, a cut-off ending).
2. Mark the keeper in the Takes table (`Keep? Yes`). Brando makes the final pick; an agent may shortlist.
3. For a keeper, copy from the Suno song page into the track file: title, full styles, lyrics, model version, created date, Suno link (use "Show full styles" on the page, the short view cuts the tags).
4. Decide the type now: **original** or **cover** (someone else's composition, even with a new arrangement). It decides Step 7.

## Step 3. Download as WAV (BRANDO MUST DO if the account needs it)

1. Signed in at suno.com, open the song, More options, Download, choose WAV (Suno's menu names change; MP3 is the other choice).
2. Save as `exports/<slug>/<slug>_v1_raw.wav`. The `exports/` folder is git-ignored; see AGENTS.md.
3. Not verified: whether WAV download needs a paid Suno plan. If the WAV choice is missing or locked, say so in the track file. Do not convert an MP3 to WAV and call it lossless; a WAV made from an MP3 is still MP3 quality, so note that in the track file if it happens.

## Step 4. Master to -14 LUFS, 44.1 kHz, 16-bit

Target: integrated loudness about -14 LUFS, true peak at most -1 dBTP, 44.1 kHz, 16-bit stereo WAV.

Two-pass ffmpeg loudness normalization (the first pass measures, the second applies):

```bash
SLUG=the-day-that-never-comes-bebop
cd exports/$SLUG

# Pass 1: measure. Read input_i, input_tp, input_lra, input_thresh, target_offset from the JSON at the end.
ffmpeg -hide_banner -i ${SLUG}_v1_raw.wav \
  -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null -

# Pass 2: apply with the measured values, resample to 44.1 kHz, dither down to 16-bit.
ffmpeg -hide_banner -i ${SLUG}_v1_raw.wav \
  -af "loudnorm=I=-14:TP=-1:LRA=11:measured_I=<input_i>:measured_TP=<input_tp>:measured_LRA=<input_lra>:measured_thresh=<input_thresh>:offset=<target_offset>:linear=true,aresample=44100:dither_method=triangular" \
  -ar 44100 -sample_fmt s16 -c:a pcm_s16le ${SLUG}_v1_master.wav

# Check: should print integrated loudness near -14 and true peak at or below -1.
ffmpeg -hide_banner -i ${SLUG}_v1_master.wav -af ebur128=peak=true -f null - 2>&1 | tail -12
ffprobe -hide_banner ${SLUG}_v1_master.wav 2>&1 | grep Audio
```

Write the measured LUFS, true peak and the date in the Mastering section of the track file. If `linear=true` falls back to dynamic mode, ffmpeg prints a warning; accept the result if the check shows about -14 LUFS and no clipping.

Listen to the master once on headphones and once on speakers. Old versions stay (`_v1_raw`, `_v1_master`); a remaster is `_v2_master`, never an overwrite.

## Step 5. Cover art, 3000 x 3000

1. Preferred: art that is clearly Brando's to use (his own image, or an image he generated and may use commercially under the tool's terms). Suno's own cover image is small, so it must be enlarged, and the rights of the image follow Suno's terms too.
2. Square crop and upscale to 3000 x 3000 JPG (RGB, no text blur, no store logos, no URLs or prices):

```bash
convert cover_in.png -filter Lanczos -resize 3000x3000^ -gravity center -extent 3000x3000 -quality 95 cover_3000.jpg
identify cover_3000.jpg   # must print 3000x3000
```

3. A simple enlarge of a 1024 px image looks soft; Brando may prefer a sharper original. Save as `exports/<slug>/cover_3000.jpg` and record the source in the track file.
4. A cover image under about 2 MB may be committed beside the track notes.

## Step 6. Metadata

Fill in the track file before opening the distributor: title, artist name (Brando decides; the one he wants on Spotify), genre, language (instrumental), explicit flag, release date at least a week ahead, composer and songwriter credits.

## Step 7. Rights check (must pass before any upload)

1. **Original song:** confirm that Suno's terms for the plan in use allow distribution. Songs made on a free Suno plan may be limited to non-commercial use; check the plan on the creation date (Brando's Suno billing history) and write the answer in the track file.
2. **Cover song** (the first candidate, Metallica's "The Day That Never Comes"):
   - Use the exact original title; drop Suno's "MP3" suffix.
   - Credit the original songwriters in the composition (C) line; performers only in the P line.
   - Licensing options, in the order Brando decides: (a) RouteNote to Spotify (and the stores RouteNote lists as not needing a license) with no license, excluding the USA, Canada, Mexico, India and Pakistan for other stores; (b) buy a mechanical license (about $12 per song through Affordable Song Licensing, per RouteNote's pages) and upload the PDF for full reach; (c) DistroKid later, which sells the license itself. Details and sources: `docs/for-profit-vs-nonprofit.md`, section 4.
   - A lawyer is the right check before relying on any of this for money.
3. Samples or loops: none expected from Suno output; note it.
4. AI disclosure: answer the distributor's AI-generated content question truthfully.

## Step 8. Upload through RouteNote free tier (BRANDO MUST DO: yes, login, ID checks)

Do not start until Brando says "upload" for this exact song.

1. Brando signs in (or creates his RouteNote account) himself or stores the login for the agent.
2. New release, upload `<slug>_v1_master.wav` and `cover_3000.jpg`.
3. Enter the metadata from Step 6, choose Spotify and the other stores, set territories per Step 7, attach the license PDF if he bought one.
4. Choose the free tier (RouteNote keeps a share of earnings). Any paid option needs Brando's yes first.
5. Submit, save the confirmation email, set Status to `submitted` and write the distributor and date in the track file.

## Step 9. After approval

1. When the release is live, copy the Spotify link into the track file and set Status to `live`.
2. **BRANDO MUST DO:** claim the artist profile in Spotify for Artists (artists.spotify.com): photo, bio, links.
3. Check that title, artwork and credits on Spotify match what was submitted.
4. Commit the updated track file straight to `main`.

## Agent hand-off rules

- Commit to `main` only, `git pull --rebase` first, no branches, nothing deleted.
- Never commit audio masters or other large files; they live in `exports/` on the machine that made them, and the track file records where.
- Report real results only: file names, measured LUFS, commit links. Say plainly what was not done.
