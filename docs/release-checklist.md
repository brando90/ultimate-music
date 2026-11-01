# Release checklist

**Doc link:** <https://github.com/brando90/ultimate-music/blob/main/docs/release-checklist.md>

Copy this list into the song's notes file under `tracks/` and tick it off for each release.

## 1. Audio

- [ ] Final mix exported as a **WAV, 44.1 kHz, 16-bit**, stereo
- [ ] **Peaks under 0 dB** (true peak about -1 dB is safer), no clipping
- [ ] Loudness **about -14 LUFS** integrated (Spotify's reference level)
- [ ] No silence at the start, no cut-off tail, clean fade or ending
- [ ] Listened to the full file once on headphones and once on speakers

## 2. Artwork

- [ ] Cover art **3000 x 3000 px**, square, JPG or PNG
- [ ] No blurry text, no store logos, no URLs or prices on the image
- [ ] Artwork is original or licensed, and I can say where it came from

## 3. Metadata

- [ ] Song title, artist name, genre and language
- [ ] Songwriter and composer credits spelled correctly
- [ ] Explicit flag set correctly
- [ ] Release date chosen (at least a week ahead, so playlists and Spotify for Artists can pick it up)

## 4. Rights

- [ ] **Original song:** I own it (or it is clearly mine to release), and any AI tool terms allow distribution
- [ ] **Cover song:** arrangement and source rights checked; original songwriters credited; license requirements verified for the selected stores and territories. RouteNote permits eligible Spotify-only covers without a separately purchased mechanical license; do not apply other-store territory exclusions to Spotify. See [cover rights](spotify-cover-rights.md).
- [ ] Samples and loops cleared, if any
- [ ] Suno plan **and input permissions** established: Premier coverage for the first candidate is verified, but permission for Suno's use of the underlying composition remains unresolved. Paid-plan status alone does not clear third-party material. See [historical terms assessment](spotify-cover-rights.md).

## 5. Distributor steps

**First releases: RouteNote (free tier)**

- [ ] Sign in to RouteNote and start a new release
- [ ] Upload the WAV and the cover art
- [ ] Fill in the metadata and choose only the authorized stores (Spotify only for the first release)
- [ ] Pick the free tier (RouteNote keeps a share of earnings) and submit
- [ ] Wait for approval and the live date; save the confirmation email

**Later: DistroKid (paid)**

- [ ] Move over only when earnings or release count justify the yearly fee
- [ ] Release under the same artist name, and confirm the artist profile is linked, not duplicated

## 6. After release

- [ ] Find the song on Spotify and copy its link into the song's notes file
- [ ] **Claim the artist profile in Spotify for Artists** (artists.spotify.com): add photo, bio and links
- [ ] Check that the title, artwork and credits match what was submitted
- [ ] Log the release in `tracks/<song>.md` (status: live, date, distributor)
