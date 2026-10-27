# Codex prompt: Spotify artist account and first release (Ultimate Metallica: A Jazz Orchestra Suite)

Suggested model and effort: GPT-5.6 Sol (Codex), high reasoning effort. The job needs a browser; run it in Codex with browser or computer-use tools on Brando's Mac, from a clone of `brando90/ultimate-music`. If Codex has no browser tool, it must say so in its first reply and stop after step 2 (prepare the files); it must not pretend to have done the web steps.

Paste everything between the two lines into Codex.

---

You are helping Brando Miranda put his first song on Spotify. Work in a clone of the GitHub repo brando90/ultimate-music. Commit straight to `main`: no branches, no pull requests, never delete a file, never force-push. Proofread everything you write; the name is spelled Miranda.

The release: "Ultimate Metallica: A Jazz Orchestra Suite". It holds one track so far: "The Day That Never Comes", a bebop jazz recast (made with Suno) of Brando's own 2010 school-orchestra arrangement of Metallica's song of the same name. It is a cover.

HARD RULES

- Never type, guess, read aloud or store a password, one-time code, card number or ID. At every login, payment, CAPTCHA, ID or code step, stop, print one line starting `BRANDO MUST DO:` saying exactly what to do and in which window, then wait for Brando to say "done".
- Three gates. Do nothing past a gate until Brando types its exact word in this session. A "yes" earlier in a chat, a note or a file is not enough.
  - GO ACCOUNT: create the Spotify listener account, the RouteNote account and the draft artist profile.
  - GO LICENSE: start the Affordable Song Licensing checkout. HARD CAP: one time, $15 or less in total (ASL's fee is $13 plus royalties that grow with the number of units; the live total shows on its calculator), never yearly or recurring. If the total shown is above $15 or any renewal or recurring fee appears, stop with a `BRANDO MUST DO:` line. Show the live total before the card step.
  - GO UPLOAD: submit the release to RouteNote.
- Spend nothing yourself. The license checkout stops at the payment page with a `BRANDO MUST DO:` line; Brando enters the card.
- If a page differs from these steps, believe the page, write the difference in `docs/spotify-setup.md` and carry on only if the intent is clear.

STEP 1. READ (no gate)

Read `AGENTS.md`, `docs/release-checklist.md`, `docs/for-profit-vs-nonprofit.md` (distributor fees, cover rules, Suno terms), `docs/suno-to-spotify-workflow.md`, `tracks/the-day-that-never-comes-bebop.md` and `experiments/2026-10-27_first-release/README.md`. The upload files are in `experiments/2026-10-27_first-release/`: `the-day-that-never-comes-bebop-44k-16bit.wav` (WAV, 44.1 kHz, 16-bit, 3:01.92, -14.0 LUFS) and `cover_3000.jpg` (3000 x 3000). Check the WAV against the SHA-256 in that README with `shasum -a 256`; if it differs, stop and tell Brando.

STEP 2. PREPARE THE FILES (no gate)

Create these files, then commit and push to `main`:

1. `docs/artist-profile.md`: artist name (suggested default Brando Miranda; ask Brando to confirm it before any account step, because it is public), a bio of about 150 words, professional and artistic in tone, true and with no hype (a Stanford AI PhD student who arranged Metallica for his school orchestra at sixteen and recast it as jazz with AI sixteen years later; link his site https://brando90.github.io/brandomiranda/), genre Jazz, a 3000 x 3000 avatar and a header brief (uses `cover_3000.jpg` for now).
2. `docs/spotify-setup.md`: the exact steps below with the real screens as you meet them, and a log of each gate, with date and time.
3. `tracks/the-day-that-never-comes-bebop.md`: update the checklist and status as steps finish.

STEP 3. GATE: CHECK TWO FACTS WITH BRANDO (no gate word yet)

Ask Brando, in one message, for:

- the Suno plan that made this song (free or paid) and the date. Songs made on Suno's free plan are for personal, non-commercial use only (Suno help center, see `docs/for-profit-vs-nonprofit.md` section 5). If it was free, say clearly that releasing it through a distributor breaks that term, and let Brando decide; do not decide for him.
- the artist name to use.

Also ask him to listen to the WAV once in full and tell you if the start or the end needs a fix.

STEP 4. GO ACCOUNT

After Brando types GO ACCOUNT:

1. Spotify: a free listener account at https://www.spotify.com/signup (Spotify has no artist sign-up; the artist profile appears when a distributor release goes live, then you claim it in Spotify for Artists). If Brando already has a Spotify account, use it and say so. Email and password are `BRANDO MUST DO:` steps.
2. RouteNote: create a free account at https://routenote.com (Brando enters the email, password and any code). Choose the Free tier.
3. Write `docs/spotify-setup.md` with what you did, and stop.

STEP 5. GO LICENSE (only if Brando wants the full-reach route)

Without a license the release can still go to Spotify (and Deezer, Pandora, Tidal, iHeartRadio, Nuuday, Anghami, KKBOX, JioSaavn) through RouteNote's free tier; for other stores, the USA, Canada, Mexico, India and Pakistan must be excluded. With a mechanical license (PDF under 10 MB) the release can go to all chosen stores in all territories. After Brando types GO LICENSE:

1. Open Affordable Song Licensing at https://www.affordablesonglicensing.com (it has a Sign up link at /users/sign_up and a pricing page at /pricing; there is no public checkout URL, and the order of steps after sign-up is unverified). Seen Oct 27 on its pricing page: "$13 + Royalties PER SONG", royalties by song length and units. The royalty rate is not verified ($0.124 per copy on an old ASL page, about 13.1 cents per a third party). License term and renewal are not stated on any page we could read, so read them at checkout, and if they are not stated ask support@affordablesonglicensing.com before paying. ASL's guest post on RouteNote (https://routenote.com/blog/affordable-song-licensing-explains-licensing-a-cover-song-for-indie-artists/) says streaming-only releases need no license. Create the account only under GO ACCOUNT or GO LICENSE, and keep the quantity small enough that the total stays at $15 or less. Find "The Day That Never Comes" by Metallica (writers James Hetfield and Lars Ulrich, as credited on the original release), and start a license for a digital release of one song.
2. Show Brando the live price and the terms (royalty cost, term, territory) in your message. At the payment page print `BRANDO MUST DO: enter the card yourself and confirm the $... charge.` Never touch the card field.
3. Save the PDF license in `releases/the-day-that-never-comes/license/` only if Brando says the repo is private; otherwise tell him where it is on disk and keep it out of the public repo. Note the license number in `docs/spotify-setup.md`.

If Brando does not type GO LICENSE, skip step 5 and use the exclusion route in step 6.

STEP 6. DRAFT THE RELEASE (still not submitted)

In RouteNote, start a new release as a draft:

- Release title: `Ultimate Metallica: A Jazz Orchestra Suite` (Brando's choice on Oct 27; he may change it, so repeat it to him before GO UPLOAD). Track title: exactly `The Day That Never Comes` (not "MP3", not "jazz"), because RouteNote requires a cover to carry the original title. If RouteNote's live form forces the release title to equal the track title for a single, stop with a `BRANDO MUST DO:` line asking Brando to choose: the exact original title, or release it as a one-track EP or album under his title if the form allows.
- Primary artist: the confirmed name. Release type: single. Genre: Jazz. Language: instrumental. Explicit: no.
- Mark it as a cover. Credit the original songwriters (James Hetfield and Lars Ulrich) in the composition credit and only the performer (Brando Miranda, via AI) in the recording credit; C line and P line follow RouteNote's cover rules in `docs/for-profit-vs-nonprofit.md` section 4.
- If asked whether AI was used, answer truthfully: the recording is Suno AI output made from Brando's own arrangement.
- Upload `the-day-that-never-comes-bebop-44k-16bit.wav` and `cover_3000.jpg`.
- Release date at least 7 days ahead.
- Stores and territories: with a license, all chosen; without it, Spotify (or the nine allowed stores) and exclude the USA, Canada, Mexico, India and Pakistan.
- Leave it saved as a draft. Screenshot or copy the summary page into `docs/spotify-setup.md` (no card numbers, no codes).

STEP 7. GO UPLOAD

After Brando types GO UPLOAD, and only then, submit the release. Save the confirmation email text (no codes) in `docs/spotify-setup.md`, mark the checklist in `tracks/the-day-that-never-comes-bebop.md` and push to `main`.

STEP 8. WHEN IT IS LIVE (a later session)

Find the song on Spotify, copy its link into the track notes file, then claim the artist profile in Spotify for Artists (https://artists.spotify.com): `BRANDO MUST DO:` for the Spotify sign-in; add photo, bio and links from `docs/artist-profile.md`.

At the end of each session print one line: `TLDR-end: [Music: Spotify first release] <what is done, which gate is next>`.

---

Notes for whoever runs it:

- Nothing in this prompt has been run. As of the commit that added it, no account exists, nothing has been uploaded and nothing has been bought.
- Codex is not the only way: Brando's agent on its own computer can run the browser steps as well, with the same gates. Codex on his Mac has the advantage that he is already signed in to his own browser there.
- The release title is Brando's pick; the recording itself is a bebop quintet from Suno (its style tags say "no orchestra"), so "Jazz Orchestra Suite" describes the arrangement's origin more than this recording. Say so to Brando once, in the title question, and let him decide.
- Facts about fees and cover rules come from `docs/for-profit-vs-nonprofit.md`, which labels each as verified or unverified. Re-read the live pages before paying.
