# Suno beautify experiment: Metallica for orchestra (2026-10-27)

## Goal

Take Brando's 2010 school-orchestra arrangement of Metallica's *The Day That Never Comes* (`tracks/metallica-orchestra/`) and beautify it with Suno, so it sounds like a professional San Francisco-style orchestra instead of a Sibelius mock-up. If one take is good enough, make it the **first for-fun upload** to Spotify through the RouteNote free tier. Money, maybe later.

## Inputs

- Audio input for Suno: `tracks/metallica-orchestra/the-day-that-never-comes-sibelius-playback.mp3` (Sibelius playback of the score).
- Reference: the 31-page score PDF in the same folder.
- A MIDI would be a better input but does not exist yet (see the notes file there).
- Existing jazz prompts from the May 2026 blog post: `source-jazz-prompts-from-website.md` (not used here; this experiment goes orchestral, not jazz).

## Method

1. Upload the MP3 playback to Suno as the audio input, in the mode that keeps the song's structure (Suno's cover or upload mode; the menu names change, so check the current screen).
2. Paste one prompt from `prompts.md` into the style field, with the universal add-on at the end.
3. Generate 2 to 3 takes per prompt, log each one in the table at the bottom of `prompts.md`.
4. Listen to each take against the score: melody and structure should still be recognizable as the arrangement.
5. Pick one take. Download as WAV, master, then run the checklist in `prompts.md`.
6. Release through RouteNote as a **cover** (below).

## Rights and release (cover-song facts)

A Metallica arrangement is a cover, not an original. Facts checked Oct 27, 2026 on the distributors' own pages:

**RouteNote (free tier)**
- To reach all stores and territories you need a mechanical license. It must include a license number, valid date, valid source and valid information on the covered song. RouteNote recommends Affordable Song Licensing at $12 per song plus royalties, covering US digital and physical sales. (https://support.routenote.com/kb-article/what-license-do-i-need-for-a-cover/)
- Without a license: covers can go to Spotify, Deezer, Pandora, iHeartRadio, Saavn, Nuuday, Anghami, Tidal and KKBox. If a release goes only to those nine stores, the territories do not matter. A license is needed only for Canada, the United States, Mexico, India and Pakistan; to skip it, leave those five territories out, or send only to the nine stores there. (https://support.routenote.com/kb-article/which-stores-and-territories-can-i-send-a-cover-track-to/)
- Melon, Bugs!, Flo, Vibe and Genie take covers only with written permission from the original artist.
- A cover must be a new recording, clearly a cover and not a soundalike; mark the release as a cover in the album details.

**DistroKid (paid, later)**
- $12 per year per cover song; every plan includes cover licensing. At upload choose Songwriter > "another artist wrote it". DistroKid gets a compulsory mechanical license and deducts 12.7 cents per song sold in the US for the songwriter (via the Harry Fox Agency). You must use DistroKid's license even if you hold your own. (https://distrokid.com/product/cover-song-licensing)
- DistroKid's support pages say licensing can take up to 14 business days and that covers are not for sale in India, Pakistan, Mexico or Canada (streaming allowed). Source: DistroKid support (support.distrokid.com), found through search, not opened on this run.

**Practical reading for the first upload (a labeled best guess, not legal advice):** RouteNote to Spotify only, with the five license-needed territories excluded, needs no license on RouteNote's rules. Selling or streaming in the US needs the $12 per song license. The song's publishers and Metallica's side are separate from the distributor's rules.

**Suno terms:** songs made on a free Suno plan may not be allowed for commercial release; check Suno's current terms and Brando's plan before uploading. Also check whether Suno accepts an upload of a copyrighted song as input.

## Open question for Brando (copyright exposure)

This public repo now contains the arrangement files: the score PDF, both `.sib` files and the MP3 playback of an arrangement of a copyrighted Metallica song. The same files are already public on Brando's website and in his public `brandomiranda` repo, so this adds no new exposure beyond them, but it is a second public copy. Options: make `ultimate-music` private, or keep the arrangement files out of the public repo. Nothing has been deleted; Brando decides.
