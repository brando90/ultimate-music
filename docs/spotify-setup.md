# Spotify first release: preparation and execution log

**Doc link:** <https://github.com/brando90/ultimate-music/blob/main/docs/spotify-setup.md>

**TLDR:** The local release candidate passed checksum, audio-format and artwork-dimension checks. Account setup and distribution await Brando’s artist-name confirmation, Suno plan details, full listening check and action approval; nothing has been uploaded or purchased by this session.

## Assignment and current state

- Source: `prompts/codex-spotify.md` at incoming commit `ea60b73`; scheduled checks every 15 minutes until noon on 10-27-2026, America/Los_Angeles.
- Public release title and draft biography: [artist profile](artist-profile.md). Track title: The Day That Never Comes.
- Local preparation completed 10-27-2026 10:06 PDT. No account or checkout screens visited, no account created, no distributor draft created, no upload, payment or submission.
- Browser tools are available; account state has not been inspected. Existing accounts must not be presumed absent.

## Verified assets

Folder: `experiments/2026-10-27_first-release/`.

| Check | Observed result |
|---|---|
| Audio file | `the-day-that-never-comes-bebop-44k-16bit.wav` |
| SHA-256 (Secure Hash Algorithm, 256-bit) | `a62cdf9b01bbda212341d869ff8ee26c211a6a8f4cfa4eb4220a74b2cb3e3f8a`; matches README |
| Encoding | 44,100 samples/second, 16-bit, stereo |
| Duration | 181.92 seconds |
| Sample peak | -2.494 decibels relative to full scale; zero clipped samples |
| Integrated loudness / true peak | Prior README reports -14.0 loudness units relative to full scale / -2.5 decibels relative to full scale; not remeasured here because ffmpeg is unavailable on the current command path or standard install paths |
| Artwork | `cover_3000.jpg`, 3000 × 3000 pixels; visually inspected, soft upscale |
| Listening | Full listening and approval of start/end remain pending |

## Corrections and unresolved differences

1. [Metallica’s official catalog](https://www.metallica.com/songs/the-day-that-never-comes.html) lists James Hetfield, Lars Ulrich, Kirk Hammett and Robert Trujillo. The incoming prompt omitted the last two; profile, track notes and execution prompt now include all four.
2. The incoming profile called this a non-commercial release. That describes an intention, not proof of distribution rights. The draft now calls it a personal music project and leaves distribution rights unresolved.
3. [RouteNote’s cover guidance](https://support.routenote.com/kb-article/how-do-i-get-the-rights-to-distribute-a-cover/) permits Spotify and its listed streaming services without a mechanical license. The incoming prompt inconsistently applies exclusions to Spotify itself versus other stores. Verify the live store/territory controls before selecting territories; do not copy the conflicting instruction blindly.
4. [Suno’s rights pages](https://help.suno.com/en/categories/550145) distinguish free-plan use, paid-plan distribution and download rights. Confirm both generation and download details for this take before deciding the route. No rights conclusion is inferred from “for fun.”

## Remaining execution sequence

1. Confirm public artist name (proposed: Brando Miranda), Suno plan and generation/download dates, and Brando’s full listen.
2. Account step: after approval, inspect existing Spotify access and RouteNote account state, reuse appropriate existing accounts or create the approved free accounts. Record actual screens and outcomes; handle any real sign-in challenge through the authorized workflow.
3. Optional license step: only if selected and explicitly authorized, inspect Affordable Song Licensing’s live terms and total. Existing cap: one-time total at most $15, no recurring purchase. No payment authorized in this session.
4. Draft step: confirm title from the profile, all four songwriters, Suno disclosure, artwork rights, supported store/territory combination, and a release date at least seven days ahead. Upload requires Brando’s explicit authorization under AGENTS.md, including upload to a draft.
5. Submission step: present the completed release for review, act on clear authorization for submission, then verify the actual receipt and update track status.
6. After the release is live: record the Spotify link, claim the artist profile using the correct account, and apply the approved biography and images.

## Gate log

| Time (America/Los_Angeles) | Event | Evidence |
|---|---|---|
| 10-27-2026 10:06 PDT | Preparation completed | Local checksum, Python audio inspection, image dimensions and official sources above |
| 10-27-2026 10:06 PDT | Account / license / upload approvals | Not supplied in this chat; no gated actions performed |

Future runs: check for new instructions or user answers, retain this log, and do not repeat completed preparation. The source prompt’s gate labels identify actions; a clear user approval of the concrete pending action is sufficient under the applicable shared account workflow.
