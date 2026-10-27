# Spotify first release: preparation and execution log

**Doc link:** <https://github.com/brando90/ultimate-music/blob/main/docs/spotify-setup.md>

**TLDR:** The local release candidate passed checksum, audio-format and artwork-dimension checks. Brando Miranda Garay is the confirmed artist name (Brando, 10-27-2026, after the earlier note below), an existing Spotify listener account was found, and Premier coverage at Suno creation was verified. RouteNote signup awaits user-entered credentials and submission; listening and distribution checks remain pending.

## Assignment and current state

- Source: `prompts/codex-spotify.md` at incoming commit `ea60b73`; scheduled checks every 15 minutes until noon on 10-27-2026, America/Los_Angeles.
- Public release title and draft biography: [artist profile](artist-profile.md). Track title: The Day That Never Comes.
- Local preparation completed 10-27-2026 10:06 PDT. No account or checkout screens visited, no account created, no distributor draft created, no upload, payment or submission.
- Browser account inspection completed; see the dated account findings below.

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

1. Public artist name and Suno plan at creation are confirmed. Complete the download-date evidence and Brando’s full listen.
2. Account setup was authorized directly on 10-27-2026. Reuse the existing Spotify listener account. RouteNote registration is prepared in Chrome; the user must enter the new password/security answer and complete submission. Verify the result and any email verification afterward.
3. Optional license step: only if selected and explicitly authorized, inspect Affordable Song Licensing’s live terms and total. Existing cap: one-time total at most $30, no recurring purchase. No payment authorized in this session.
4. Draft step: confirm title from the profile, all four songwriters, Suno disclosure, artwork rights, supported store/territory combination, and a release date at least seven days ahead. Upload requires Brando’s explicit authorization under AGENTS.md, including upload to a draft.
5. Submission step: present the completed release for review, act on clear authorization for submission, then verify the actual receipt and update track status.
6. After the release is live: record the Spotify link, claim the artist profile using the correct account, and apply the approved biography and images.

## Gate log

| Time (America/Los_Angeles) | Event | Evidence |
|---|---|---|
| 10-27-2026 10:06 PDT | Preparation completed | Local checksum, Python audio inspection, image dimensions and official sources above |
| 10-27-2026 10:06 PDT | Account / license / upload approvals | Not supplied in this chat; no gated actions performed |

Future runs: check for new instructions or user answers, retain this log, and do not repeat completed preparation. The source prompt’s gate labels identify actions; a clear user approval of the concrete pending action is sufficient under the applicable shared account workflow.

## Account findings (10-27-2026 10:10 PDT)

- **User decision:** Use Brando Miranda publicly (later superseded: Brando's final answer at 10:09 to the artist-name question is `Brando Miranda Garay`, spelled exactly); proceed with free account setup and inspect the historical Suno plan. This is explicit account authorization; no special gate word is needed. It does not authorize a distributor upload, submission or purchase.
- **Spotify:** The native Mac app is signed in as Brando Miranda Garay and shows Premium. No new listener account is needed; no subscription was changed. The browser account page required sign-in, so browser authentication for a later artist claim remains unverified.
- **Suno identity:** Signed-in profile is `brandojazz`, handle `@ultimate_brando9`, and owns the exact candidate song `f991d6df-ade7-4c1a-9561-2dedaa4179c7`. Settings show Free today; the song page displays creation on 05-07-2026 at 12:26 p.m.
- **Historical plan:** A Suno receipt in the matching music mailbox states **Suno Premier**, covering **05-07-2026–06-07-2026**, paid on 05-07-2026. Gmail shows receipt arrival at 12:17 p.m., before the song’s displayed 12:26 p.m. timestamp. Coverage on the creation date is established by the receipt; the two displayed times provide supporting sequence evidence, with no separate timezone audit. Receipt identifiers, payment details and the email body are deliberately excluded from this public repository.
- **Download:** Historical download date was not established. No song download, new generation or paid subscription was initiated during this inspection.
- **RouteNote:** Logged-out state observed. No RouteNote message appeared in a combined Suno/RouteNote sender search of the music mailbox; this does not prove an account never existed. Registration has username `BrandoMiranda` and the matching music email filled in. Password, security answer, challenge, agreement and final submission remain untouched. No account creation success has been observed.
- **Concrete handoff:** The browser tool requires the user to enter new authentication credentials. The prepared RouteNote Chrome tab is retained for the user to enter the password and security answer, complete verification, review terms and submit the free signup. Resume by inspecting that tab and verifying the success state before marking the account created.
- **Evidence storage:** Registration screenshot is local and ignored under `exports/the-day-that-never-comes-bebop/routenote-registration-10-27-2026.png`; no private receipt screenshot saved.

Gate event: 10-27-2026 10:10 PDT — artist name confirmed and free account setup authorized by Brando’s direct chat message. Signup prepared; user credential handoff pending.
