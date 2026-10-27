# Codex prompt: set up Brando's Spotify artist presence

Suggested model and effort: GPT-5.6 Sol (Codex CLI), high reasoning effort. This is docs-only work and needs no tools beyond git and gh.

Paste the text below into Codex, run from a clone of `brando90/ultimate-music`.

---

In the repo brando90/ultimate-music, set up my artist presence for Spotify.

1. Read agents/AGENTS.md and docs/release-checklist.md.
2. Create docs/artist-profile.md with: artist name (ask me if not set), a 150-word bio, genres (orchestral metal, cinematic), a 3000x3000 px avatar and header brief, and links to my website.
3. Create docs/spotify-setup.md with the exact steps: pick a distributor (RouteNote free tier first, DistroKid later), upload the first release, claim the profile in Spotify for Artists once the release is live, and add the artist photo and bio.
4. For each step that needs my login, payment or ID check, write a clear 'BRANDO MUST DO' line and stop there. Never enter my passwords.
5. Commit on a branch named spotify-setup and open a PR. Do not merge.

---

Notes for whoever runs it:

- Read docs/for-profit-vs-nonprofit.md too: it holds the distributor fees, the cover-song license rules for the Metallica arrangement, and Suno's commercial-use terms, which the setup steps must respect.
- Origin: the prompt text was sent to Brando on WhatsApp on Oct 27, 2026 at 09:35, after he asked for a Codex prompt to create his Spotify.
