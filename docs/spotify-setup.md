# Spotify first release: preparation and execution log

**Doc link:** <https://github.com/brando90/ultimate-music/blob/main/docs/spotify-setup.md>

**TLDR:** DistroKid submission of The Day That Never Comes by Ultimate Brando is verified on 11-01-2026. The refreshed dashboard now explicitly awaits the cover license before store delivery; the Spotify link lookup has no release yet. The six-hour follow-up is active for this existing release, and the submission email has a verified Sent receipt.

## Assignment and current state

- Source: `prompts/codex-spotify.md` at incoming commit `ea60b73`; scheduled checks every 15 minutes until noon on 10-27-2026, America/Los_Angeles.
- Public release title and draft biography: [artist profile](artist-profile.md). Track title: The Day That Never Comes.
- DistroKid submission verified 11-01-2026 17:58 PST after Brando completed the form. The release is processing; the amount charged and final store list are not independently verified.
- Latest check, 11-01-2026 17:58 PST: DistroKid success screen confirmed; Spotify link lookup reports no releases yet. The existing automation now monitors this DistroKid release every six hours; do not submit through RouteNote or create a duplicate.

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

**Current route, 11-01-2026:** The DistroKid release is submitted. Monitor its licensing, store delivery and direct Spotify listening link; no further submission is needed. The numbered preparation sequence below is historical and superseded by the latest submission section. Retain the [rights assessment](spotify-cover-rights.md); submission acceptance is not blanket legal clearance.

1. Public artist name and Suno plan at creation are confirmed. Use the already-held paid-period audio file and preserve its receipt/history evidence. Complete the content and rights checks needed for the actual distributor declarations; today's Free download screen alone does not invalidate earlier rights.
2. Account setup was authorized directly on 10-27-2026 and signup was reported complete on 10-28-2026. Reuse the existing Spotify listener account. Sign in to the existing RouteNote account, verify the dashboard and complete any matching email verification. Do not repeat signup just because the current browser is logged out.
3. Optional license step: only if selected and explicitly authorized, inspect Affordable Song Licensing’s live terms and total. Existing cap: one-time total at most $30, no recurring purchase. Brando approved the one-time payment on 10-28-2026, within the existing $30 total cap; checkout still stops for his card entry.
4. Draft step: confirm title from the profile, all four songwriters, Suno disclosure, artwork rights, supported store/territory combination, and a release date at least seven days ahead. Brando explicitly authorized publishing this song on 10-28-2026; this includes the upload and submission sequence, subject to verified eligibility and any action-time tool requirements.
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

## Evening follow-up (10-27-2026 19:01 PDT)

The user rescheduled the follow-up to 7 p.m. on 10-27-2026. The repository had no newer assignment. The previous RouteNote tab had closed; reopening the login page showed no signed-in session. A sender search for `from:routenote.com` in the matching music mailbox returned no messages. Account creation remains unverified.

Reopened the signup page and filled the previously prepared username and music email. Password, security answer, verification challenge, agreement and submission remain for the user. The browser tool requires user entry and submission of new credentials, so no account was created by the agent. The tab is retained for that handoff; screenshot: `exports/the-day-that-never-comes-bebop/routenote-registration-10-27-2026-evening.png` (local, ignored).

The one-time automation was deleted after this attempt. Resume on the user's completion message, verify the account and any email verification, then continue the remaining authorized steps. No music upload, release submission or purchase occurred.

## Publication approval and route decision (10-28-2026)

Brando directly approved moving forward and posting this Suno jazz song, accepted the one-time payment, and requested a Claude consultation. This authorizes the release workflow; it does not establish that signup, payment, upload or submission has happened. The existing one-time $30 total limit and user card-entry requirement remain in force.

**Selected route:** RouteNote Free, Spotify only, with truthful cover and artificial-intelligence disclosure. No license purchase is needed for this store selection according to RouteNote’s [store/territory instructions](https://support.routenote.com/kb-article/how-do-i-format-stores-and-territories-for-a-cover-release-without-a-mechanical-license/), checked today: Spotify is exempt from the five-country exclusion. Do not automatically exclude the United States from Spotify. RouteNote’s [artificial-intelligence policy](https://support.routenote.com/kb-article/can-i-upload-ai-releases/) accepts some generated content, subject to moderation; it excludes content-recognition services, Korean partner stores and Amazon. Those stores are outside this release’s scope.

**Credits correction:** RouteNote’s [cover metadata instructions](https://support.routenote.com/kb-article/can-i-upload-cover-songs-with-routenote/) distinguish the composition copyright line from publishing credits: use Metallica in the cover’s C line per that guidance, all four verified writers in publishing details, and the approved performing artist in the recording P line. The earlier instruction equating the C line with songwriter names is superseded.

**Source evidence:** Local history of `brando90/brandomiranda` places the exact original audio blob in commit `deae315` at 05-07-2026 13:06:53 PDT. Its SHA-256 is `a05f2cb091f6069b29fb37aa0c0a36237bc212dd059e1faec985d30eb9b66ee6`, matching the candidate README. This establishes possession by that timestamp during Premier coverage; it does not independently prove the precise download channel. Suno’s [current terms](https://suno.com/terms), effective 09-03-2026, require permitted downloads and rights in submitted material. The older creation predates those terms; preserve the original evidence rather than assuming how later terms apply. The [public creation account](https://brando90.github.io/brandomiranda/2026/05/07/metallica-goes-jazz.html) describes using Brando’s own school arrangement. Exact uploaded source and eligibility still need verification before any rights attestation.

The prepared RouteNote signup was reopened with username and music email. New password/security answer entry and final credential submission remain a mandatory user handoff under the browser tool policy. This is an access dependency, not a request to reapprove publication.

**Claude consultation completed:** [Metallica cover release decision](https://claude.ai/chat/f172978c-7b27-49be-a98f-3dd9e111191a), using the signed-in Claude web interface showing Opus 5.5 / Extra. Claude independently recommended RouteNote Free, Spotify only, worldwide, no license purchase, truthful cover/AI disclosure, and verification of the source audio and permitted download before release. Its broad legal interpretations and third-party claims are advisory, not verified clearance; the route above rests on independently checked RouteNote pages. Its older $12 licensing quote is not used to authorize any purchase.

**Name decision:** Use Brando Miranda, matching this chat’s direct user approval. Coworker commit `5eb98a7` reported Brando Miranda Garay; retain that provenance here rather than treating an assistant’s report as a new direct instruction. The draft public profile and execution prompt now use Brando Miranda. No public distributor metadata has been entered.

**Next action:** After Brando completes signup, verify the account, inspect the exact Suno source/download provenance and finish the listening check, then prepare the approved Spotify-only release. Use the original track title; retain the chosen release title where the live form permits it. If submission includes new legal attestations, present the completed screen for the tool-required action-time confirmation. No upload, payment or submission has occurred.

## Signup reported complete; account verification pending (10-28-2026 09:35 PDT)

Brando reported completing RouteNote signup and requested verification and continuation. The retained registration tab still displayed the registration form; a separate visit to the official login page displayed a logged-out sign-in form. This does not disprove account creation. Searches in the matching music Gmail account for `from:routenote.com` and `in:anywhere routenote` found no RouteNote confirmation or verification message (the broader search returned one unrelated message).

The password-manager icon led to a real 1Password unlock prompt for the matching music account. A vault unlock or direct RouteNote sign-in is required before authenticated verification can continue. The existing-account login tab is retained with the prepared username; no password was read or saved. Brando was asked to unlock 1Password or sign in, and to identify a different signup account if applicable. No duplicate signup, password reset, upload, purchase or release submission was attempted. Resume at the account dashboard, complete any matching email-verification challenge, then continue the already authorized Spotify-only release. Screenshot: `exports/the-day-that-never-comes-bebop/routenote-login-10-28-2026.png` (local, ignored).

## Status and cost confirmation (10-29-2026 10:58 PDT)

Brando reiterated the goal of uploading the song to Spotify, ideally with only a one-time rights payment. The current Chrome tab still shows RouteNote's sign-in form, an empty password field and an unchecked verification challenge. The native 1Password app is locked. Signup remains reported complete but not independently verified; no release has been uploaded or submitted. The login tab is retained for direct sign-in, followed by dashboard verification. Screenshot: `exports/the-day-that-never-comes-bebop/routenote-login-10-29-2026.png` (local, ignored).

Rechecked RouteNote's official [pricing](https://support.routenote.com/kb-article/how-much-does-routenote-cost/) and [cover store/territory guidance](https://support.routenote.com/kb-article/how-do-i-format-stores-and-territories-for-a-cover-release-without-a-mechanical-license/). RouteNote Free has no upfront or annual fee; the artist receives 85% of net revenue. Spotify is exempt from the mechanical-license country exclusions, so the selected Spotify-only route needs no separate mechanical-license purchase under that policy. Premium introduces an annual renewal and is outside the selected route. This store policy does not establish the eligibility of the particular Suno source material; retain the source check before making a rights attestation.

## Dashboard report and source trace (10-29-2026 12:00 PDT)

Brando reported being signed in and explicitly instructed uploading this jazz Metallica cover to Spotify on the free plan, with any necessary one-time licensing payment. Publication authorization is clear. The connected Chrome Brando profile nevertheless showed the existing login form and a fresh login form; RouteNote's homepage navigation also offered Login. Available browser inventories, Chrome windows and Firefox showed no RouteNote dashboard. Asked which browser/device holds the reported dashboard, rather than repeating signup. Account access is still unverified, and no distributor draft, upload, submission or payment occurred.

Suno session recovery succeeded. The exact jazz take links a parent song, `47a53f0a-a374-4232-95c2-2e18017b84dd`, under the same `brandojazz` account, created 05-07-2026 at 12:21 p.m. The parent download dialog stated that it was unlocked and could be downloaded again. Downloaded its audio through Suno's official interface and compared it with the documented local Sibelius playback. The full recording strongly matches after decoding and alignment: stereo Pearson correlation 0.995258 across 344.955625 seconds, versus 0.000942 for a deliberately shifted control. Left and right correlations are 0.995193 and 0.995311. Twelve consecutive windows span 0.994362–0.998415. These are descriptive comparisons of the entire supplied recording, not population estimates; confidence intervals and significance tests are inapplicable. [Full measurements, hashes, method and limitations](../experiments/2026-10-27_first-release/provenance-comparison-10-29-2026.json).

This evidence strongly supports the source being a re-encoded copy of Brando's documented Sibelius playback. It does not independently clear the underlying composition, sample library or historical Suno submission permissions. RouteNote's [cover definition](https://support.routenote.com/kb-article/what-is-a-cover-song/) includes changes of style, instrumentation and arrangement; its [generated-content policy](https://support.routenote.com/kb-article/can-i-upload-ai-releases/) still requires appropriate rights and moderation. Do not describe a mechanical-license purchase as blanket clearance of those separate issues.

The jazz take's current download dialog shows Free, 7 downloads and Unlock & Download; no new download or unlock of the jazz take was performed. Preserve the original paid-period file and receipt evidence. The current dialog does not establish the historical approved download channel or retroactively resolve the terms that governed creation. Candidate audio hash, encoding, duration and cover dimensions were rechecked and remain unchanged. Source comparison files and screenshots remain local under `exports/the-day-that-never-comes-bebop/`.

## Completion email request (10-29-2026)

Brando explicitly requested email notification to his inboxes when the release is done and wants the Spotify listening link. Codex owns delivery: one verified submission notice, clearly distinguished from publication, followed by a live notice containing the verified Spotify track and artist links. Delivery is pending; no completion email has been sent because no distributor submission or live release has been verified.

Created the active in-chat follow-up `ultimate-music-spotify-release-notifications`, every six hours. It resumes unfinished authorized work when account access permits, remains quiet while the blocker is unchanged, checks actual submission/live evidence, verifies and deduplicates email receipts, and removes itself after the live email succeeds. Recipient routing and message identifiers stay in private local records. The available Gmail connector was verified; browser access remains the immediate dependency. Keep this Mac on and the desktop app running for the local follow-up.

## Retained Suno rights and dashboard targeting (10-29-2026)

Suno's [08-10-2026 transition announcement](https://suno.com/blog/suno-updates-tos) explicitly preserves commercial use for songs downloaded on paid plans, while applying the new download limits to future downloads of older songs. Its [guidance dated 12-17-2025](https://help.suno.com/en/articles/2425729) says rights to songs made while subscribed survive cancellation. The current Free / Unlock & Download screen therefore does not establish loss of previously granted rights or a need to buy another subscription. Use the already-held candidate, backed by Premier coverage and same-day original-file possession. Exact historical download mechanics remain unaudited; do not turn the present download-access screen into a new payment requirement.

Brando again reported the dashboard open in Chrome's Brando profile. Checked both available tabs and user-owned tabs, inspected the native Chrome tab list, and refreshed the retained RouteNote page: only Sign in was exposed. 1Password remained locked and no task-specific credentials file was found. The browser security policy rejected opening Chrome's internal password-manager page; no workaround was attempted. Requested the exact dashboard tab via @Chrome or its URL to resolve the mismatch. Retained the normal RouteNote login page with the known username; screenshot `exports/the-day-that-never-comes-bebop/routenote-login-10-29-2026-1224.png` is local and ignored. No upload, submission or payment occurred; the existing email follow-up remains active.

## Vault unlocked; existing password unavailable (10-29-2026 13:09 PDT)

After Brando reported unlocking 1Password, the native app was verified unlocked. Searches for `routenote` and `route` returned no matching item; the RouteNote password-field menu independently displayed **No items to show**. A visit to RouteNote's authenticated Trends destination redirected to Sign in. These checks establish the available session and saved-login state, not whether signup succeeded elsewhere.

In the matching music mailbox, `from:routenote.com` returned no messages; `in:anywhere routenote` returned one unrelated conversation and no signup or verification message. A secondary connected-mail search also found none. No private message contents or credentials were saved. The initially failing verification challenge recovered after reloading the login page.

The existing-account login is retained in Chrome with the prepared username and an empty password field. Brando must supply the existing password and complete sign-in; another vault unlock will not resolve the missing login item. Screenshot: `exports/the-day-that-never-comes-bebop/routenote-login-unlocked-10-29-2026.png` (local, ignored). Resume directly at dashboard verification, then upload the prepared assets under the already approved free Spotify-only route. No duplicate signup, password reset, purchase, upload or submission occurred. The existing email follow-up remains responsible for verified submission and live-link notices.

## Reported sign-in and coworker continuation (10-29-2026 13:22 PDT)

Brando reported sign-in complete and again requested upload and a live-link email. The connected Chrome Brando profile still exposes Login; a fresh request to the authenticated Trends page redirects to Login. Native Chrome and Firefox checks found no dashboard. Requested the exact authenticated dashboard URL or tab attachment to resolve the session discrepancy. Audio checksum, 44,100-sample-per-second/16-bit stereo format, 181.92-second duration and 3000 × 3000 artwork dimensions remain unchanged; the six-hour email follow-up is active.

Saved the previously requested [Scalable Coworker continuation prompt](../prompts/cowork-routenote-release.md) with the exact assets, approved metadata, account evidence, payment limits and notification owner. The prompt has not been sent to another service, and no coworker execution or ownership transfer is claimed. No distributor upload, submission or live Spotify link has been verified.

## Incoming MP3 received and compared (10-29-2026)

Brando reported that Slack delivery to the coworker could take time and the MP3 would arrive soon. Incoming commit `bbb5583` then added `experiments/2026-10-27_first-release/The Day That Never Comes.mp3`. Synced the commit and preserved the existing prepared master. Actual inspection corrects the initial bitrate note: the supplied file is stereo at 48,000 samples per second, with a reported duration of 181.968 seconds and estimated average bitrate of 188,562 bits per second, not 64,000.

The decoded incoming file strongly matches the prepared jazz recording across the full 181.92-second overlap: stereo Pearson correlation 0.997492, left 0.997485 and right 0.997501, with zero-sample offset. A deliberate 10-second shift gives 0.005599; seven consecutive comparison windows span 0.996856–0.998548. These are descriptive full-recording measurements, not population estimates; confidence intervals and significance tests are inapplicable. [Full measurements, hashes, method and limits](../experiments/2026-10-27_first-release/incoming-audio-comparison-10-29-2026.json).

The prepared WAV remains the upload source. This comparison establishes strong recording-identity evidence and does not independently establish distribution rights or claim that a full human listening check occurred. No upload, submission, payment or live-link email occurred during this file check. Codex continues to own the release and the existing notification follow-up.

## Sign-in submitted; password explicitly missing (10-29-2026 14:34 PDT)

Brando instructed Codex to click Sign in on the prepared RouteNote tab. The verification checkbox was visibly completed. Codex clicked Sign in once, and RouteNote displayed the validation alert **Password field is required**. This confirms the concrete missing input; it is not evidence of an incorrect password or a completed login. The warning was dismissed, the existing form was retained, and Brando was asked to enter his existing password directly there.

Resume after password entry or a verified dashboard session, checking whether the verification challenge has expired. No matching saved login was found in the unlocked vault. The audio, artwork, upload approval and email follow-up remain ready; no distributor upload or submission has occurred. Local screenshot: `exports/the-day-that-never-comes-bebop/routenote-password-required-10-29-2026.png` (ignored).

## Recovery does not recognize the known emails (10-29-2026 14:51 PDT)

Brando reported that he could not find the RouteNote password in 1Password. Opened RouteNote's official Forgotten password form and submitted the intended music email, then three other already-known addresses belonging to Brando. Each lookup displayed **This Email address has not been recognised**. This suggests the original signup may not have completed, but does not exclude an account under another email. No security answer was guessed, reset link issued or credential changed.

Prepared the previously authorized free signup with the original username and music email. New password, confirmation, security question/answer, verification, terms and submission remain untouched. The current browser tool requires the user to enter and submit new authentication credentials, so Brando was asked to complete those steps himself or identify a different registered email. The signup tab is retained and visible in native Chrome; the extra recovery tab opened by the site was closed. Screenshot: `exports/the-day-that-never-comes-bebop/routenote-signup-recovery-10-29-2026.png` (local, ignored). No account creation, upload, purchase or distributor submission has been verified. Codex retains the music release and notification work.

## Expanded 1Password search (10-29-2026 15:18 PDT)

Brando said the password should be in 1Password. The unlocked native app and Chrome extension yielded no RouteNote match in the available account/vault search. The extension displayed **No results found in "All Vaults"**. Its Password Generator History contained no RouteNote-associated entry; the Archive search had zero matches, and the visible Recently Deleted list had no RouteNote entry. These checks do not establish that no item exists under a different name, in another account, or on another device. No credential value was saved to the repository.

A fresh submission of the intended music email through RouteNote's official recovery form again returned **This Email address has not been recognised**. No reset link, account creation or dashboard access was verified. Asked Brando for the saved item title and vault name, without sending the password in chat. The prepared signup remains retained with empty password and security-answer fields; the browser tool requires user entry and submission of new credentials if signup is needed. The signup verification challenge was completed after Brando explicitly approved it, but it may expire before submission. Terms remain unchecked. Screenshot: `exports/the-day-that-never-comes-bebop/routenote-email-recheck-10-29-2026.png` (local, ignored).

The upload assets and authorization remain ready. No distributor upload, submission, purchase or completion email occurred. Codex still owns the release and existing email follow-up.

## Login verified; final-file hold (11-01-2026)

RouteNote authenticated account and welcome page were verified. Codex inspected the release creation form and catalog but did not create a release, upload audio or submit. Brando explicitly stopped uploading pending his final WAV. The existing notification automation is PAUSED. Do not use earlier masters without renewed approval. See [Spotify costs and rights](spotify-cover-rights.md) for the verified policy explanation and Google Doc companion.

## Hand-entered arrangement and historical Suno terms (11-01-2026)

Brando requested a substantive assessment, retaining responsibility for his decision. The [rights assessment](spotify-cover-rights.md) now distinguishes independent recording rights, the underlying composition, cover-arrangement scope, Suno input permission and Spotify distribution licensing. An archived official Suno page captured 08-31-2026 identifies revision 03-26-2026; its input-rights conditions and conditional paid-output grant materially limit the earlier paid-plan conclusion. Applicability on the May creation date is a documented inference, not an exact-day archive verification.

The free Spotify-only route remains supported for eligible covers. Full clearance of this specific production is not established by the evidence. Updated the existing Google Doc and current track/checklist state. No release, rights-holder contact, payment or milestone email was initiated. Uploading remains on Brando's final-file hold.

## DistroKid requested; account setup handoff (11-01-2026 16:02 PST)

Brando asked to upload through DistroKid and supplied a workflow requiring exact original title, cover licensing, original writer credits, truthful artificial-intelligence disclosure and explicit approval before every charge. He also asked whether RouteNote is preferable. RouteNote Free remains the better fit for avoiding annual fees; DistroKid is a viable paid alternative. No recurring purchase is authorized merely by initiating this workflow.

The existing DistroKid session is signed in. The My Music dashboard displayed **No releases... yet**. Selecting Upload music showed a required phone-number step. Opening Add contact information led to **Set a password for your DistroKid account**. No password was entered or changed. The computer-use tool requires Brando to enter, confirm and submit new credentials himself; the retained browser tab is ready for that handoff, followed by the required contact number. An existing personal-profile tab with Brando's edits was preserved.

Prepared choices, not yet entered into an upload form:

| Field | Value / state |
|---|---|
| Release and track title | The Day That Never Comes |
| Main artist | Brando Miranda, human artist |
| Type / genre / language | Single; Jazz; English title; instrumental |
| Cover | Another artist wrote it; original artist Metallica |
| Songwriters | James Hetfield, Lars Ulrich, Kirk Hammett, Robert Trujillo |
| Composition notice | © 2008 Creeping Death Music (Global Music Rights), verified in Metallica's official song catalog; do not invent ownership shares |
| Recording | Existing 181.92-second, 44.1 kHz, 16-bit stereo jazz WAV; checksum reverified |
| Generated-content credits | Disclose generated instrumental audio; preserve original human composition credits; use the actual form's applicable audio choices |
| Artwork | Existing cover_3000.jpg, 3000 × 3000; no title text conflicts; previously noted upscale softness remains |
| Stores | Spotify only, retaining the narrower established scope |
| Plan and cover fee | Musician plan requested; published estimate $24.99/year plus $12/cover/year; account-specific checkout total and current paid-plan status not yet verified |
| Payment | Stop before any charge; present exact total and renewal terms; Brando enters his own card |

Sources: [Metallica's credits](https://www.metallica.com/songs/the-day-that-never-comes.html), [DistroKid track fields](https://support.distrokid.com/hc/en-us/articles/39974262480019-Entering-Track-Information-on-the-Upload-Form), [generated-content credits](https://support.distrokid.com/hc/en-us/articles/50784709021971-How-to-Fill-Out-AI-Credits).

No audio upload, release draft, cover-license purchase, subscription purchase or submission is verified. A screenshot of the empty password-creation form is stored locally under ignored exports; credential-bearing URLs are not saved here. Resume after the user completes account setup, inspect current plan status, and advance to a concrete checkout or release-review screen. The existing notification automation remains paused to avoid the older RouteNote instructions running concurrently.

## Release form prepared; exact charge decision (11-01-2026 17:30 PST)

Brando explicitly requested **Ultimate Brando** as the release artist and maximum included distribution. The signed-in DistroKid upload form is accessible. The supplied `Downloads/The Day That Never Comes (Jazz Cover).wav` matches the repository master byte for byte; both have SHA-256 `a62cdf9b01bbda212341d869ff8ee26c211a6a8f4cfa4eb4220a74b2cb3e3f8a`. The filename is visibly attached to the form. The chosen jazz-club saxophone portrait is displayed as the release artwork. This verifies preparation, not completed distributor submission or delivery.

| Field | Verified form state |
|---|---|
| Title / artist | The Day That Never Comes / Ultimate Brando |
| Recording | Instrumental; Jazz; all audio performed by artificial intelligence; human artist or group |
| Cover credits | Metallica; James Hetfield, Lars Ulrich, Kirk Hammett, Robert Trujillo |
| New artist pages | No existing Spotify, Apple Music or YouTube Music artist selected; no listener-profile identifier used |
| Social mapping | https://www.instagram.com/ultimatebrandojazz/ and https://www.facebook.com/61596193078228; the latter was opened and verified as Ultimate Brando before entry |
| Stores selected | Spotify; Instagram & Facebook; TikTok & other ByteDance stores; YouTube Music; Amazon; Pandora; Deezer; Tidal; iHeartRadio; Qobuz; Saavn; Boomplay; Anghami; NetEase; Tencent; MassiveMusic; Claro Música; Joox; Kuack Media; Adaptr; Flo; MediaNet |
| Cover license | $9 now, billed annually under the displayed promotion; standard $12/year shown; later renewal price not independently established |
| User-selected optional extras | Leave a Legacy, $29 once; loudness normalization, $2.99 once; other extras unchecked |
| Current displayed total | $40.99; removing both optional extras gives $9 |
| Submission state | Continue not clicked by Codex after these corrections; no receipt, charge or live link verified |

Apple Music and iTunes were temporarily deselected because the form's original Brando Miranda/Saxophone credit conflicts with the wholly generated recording. The required performer field needs an accurate accepted credit; no invented performer or instrument was entered. DistroKid's [generated-content instructions](https://support.distrokid.com/hc/en-us/articles/50784709021971-How-to-Fill-Out-AI-Credits) support the all-audio/human-artist disclosure but do not resolve that separate field. [Apple's specification](https://help.apple.com/itc/musicspec/en.lproj/static.html#recommended-contributor-roles) calls for the actual performed role or instrument. These stores can be revisited after clarification.

[Snapchat](https://support.distrokid.com/hc/en-us/articles/360063786913-Submitting-Your-Music-to-Snapchat) and [Roblox](https://support.distrokid.com/hc/en-us/articles/32623398062739-Delivering-Your-Music-to-Roblox) require ownership of the underlying composition, so neither was selected for this Metallica cover. Included-store selection does not guarantee store acceptance; the [documented rights questions](spotify-cover-rights.md) remain separate.

The user-selected distribution agreement and rights checkboxes were already checked when inspected. Codex preserved those choices without representing that the prior rights assessment had established full clearance. A single charge-choice question was presented: approve $9 with annual cover-license renewal and remove extras, approve $40.99 with annual renewal and retain extras, or hold. This is required because the previous payment authorization excluded recurring charges and capped one-time spending at $30. No new card information was entered or stored.

Local proof: `exports/artist-profile/distrokid-review-11-01-2026.png`. Resume the retained existing release form, apply the user's charge choice, verify the total, submit once, and save the actual distributor confirmation before sending the authorized submission email. Do not describe the recording as live until a direct listening link is verified.

## DistroKid submission verified (11-01-2026 17:58 PST)

Brando completed submission and pasted the success screen. Codex independently read the authenticated page confirming **The Day That Never Comes — Ultimate Brando**, one song, processing for streaming platforms. Release identifier: `05E43806-5482-42DC-AE5A916C71A0C713`. Actual charges and final selected stores were not independently verified after submission; the earlier form total is not a payment receipt.

The [HyperFollow page](https://distrokid.com/hyperfollow/ultimatebrando/the-day-that-never-comes) is promotional, not a direct Spotify listening link. The authenticated [Spotify identifier lookup](https://distrokid.com/uri/spotify/) reports no releases found and says delivery may not have occurred yet. Spotify publication is therefore unverified, with no direct listening link available from that lookup.

The confirmation screen advises at least five business days for Spotify. [DistroKid's cover guidance](https://support.distrokid.com/hc/en-us/articles/360013648953-Uploading-Cover-Songs-to-DistroKid) separately allows up to 14 business days to secure the cover license before delivery. Roughly one to four weeks is a planning estimate, not a promised release date.

The existing `ultimate-music-spotify-release-notifications` automation was updated and verified ACTIVE at its existing six-hour cadence. It now monitors this submitted DistroKid release, verifies the correct artist and live playback before emailing the direct Spotify link, and prepares promotion drafts for Brando to post. It stops after the live notification and drafts are delivered. The submission milestone email was sent with a Gmail Sent receipt after checking Sent for duplicates; receipt details remain private under ignored exports. No live-link email has been sent.

Local evidence: `exports/artist-profile/distrokid-submission-confirmed-11-01-2026.png`, `exports/artist-profile/spotify-link-pending-11-01-2026.png`, and private `exports/artist-profile/submission-email-receipt-11-01-2026.json`.

### Promotion drafts for verified publication

These drafts are not sent. Use them only after verifying Spotify publication and replacing `[SPOTIFY_LINK]` with the direct listening link; Brando will post them.

**Bachata group:** Hey dance fam! 🎷 My first release as Ultimate Brando is on Spotify! It’s a jazz cover of Metallica’s “The Day That Never Comes,” based on an arrangement I wrote in high school in 2010 and brought to life with Suno. A little jazz between bachatas 😄 Would love for you to hear it! [SPOTIFY_LINK]

**Deck / Hala’s Deck group:** Hey everyone! I finally released some music 🎷 “The Day That Never Comes” is on Spotify under Ultimate Brando—a jazz take on Metallica, made with Suno from an arrangement I wrote back in high school in 2010. Pretty wild hearing that old score come alive. Give it a listen! [SPOTIFY_LINK]

## Distributor transfer check (11-02-2026 00:03 PST)

The authenticated release dashboard reports that the files were successfully processed and the single is being transferred to stores. All 22 submitted destinations are confirmed, including Spotify and Instagram/Facebook; this does not establish live availability in either service. Universal Product Code (UPC): `700149599211`. The dashboard displays upload date 11-02-2026; the original submission was observed on 11-01-2026 in Pacific time.

The dashboard lists the cover-song license, Leave a Legacy and loudness normalization as attached extras. Separate license approval and the actual charge remain unverified. Spotify identifier lookup still reports no releases found; the public HyperFollow page offers Spotify Pre-Save only. The connected mailbox has the already-sent submission notification and no new matching distributor status email. No live-link email or promotional post was sent.

Synced coworker [launch drafts](promotion/launch-drafts.md) and [promotion log](promotion/promotion-log.md) from incoming commit `2357b7c`; the log records no published posts. Use those records to coordinate the live campaign. Existing monitoring continues at its six-hour cadence.

## Cover-license queue confirmed (11-02-2026 08:50 PST)

After refreshing the authenticated release dashboard, the current message explicitly says DistroKid is securing the cover-song license before sending the single to stores. This more specific state supersedes the earlier generic transfer banner. The 22 destination badges still say submitted, but they do not establish completed store delivery or license approval.

The Spotify identifier lookup still has no release, and HyperFollow still offers Spotify Pre-Save without a direct listening link. No new matching distributor email was found in the connected mailbox; the existing submission-email receipt remains the only milestone notification. There is no rejection or requested user action. Continue the existing watch without a duplicate submission, email or promotion.
