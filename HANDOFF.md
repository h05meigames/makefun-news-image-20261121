# HANDOFF — news-image-20261121

Entry built, tested, and pushed. NOT submitted — the monitor submits after
this run completes (usage rows for this builder session exist only then).

## Competition
- news-image-20261121, "Sum up 21 November's world news in one image"
- Entries close: 2026-11-23T00:00:00Z = 23 Nov 2026 07:00 WIB
- Top 50 share $100 ($20 1st, $12 2nd, $6 3rd, $2 each 4th–10th, $1.20
  each 11th–50th). AI judge compares images pairwise. Entry fee: none.
- Quota used: 0 submissions for this slug so far (9 submissions by other
  entrants; none are ours). Task-body rule: max 5/day, 20 total; the
  requirements file states 10/day, 20 total — one submission is within
  either limit.

## The entry (final — do not change the code)
- Repo: https://github.com/h05meigames/makefun-news-image-20261121 (public,
  created after the competition opened; MIT license)
- Code-final commit: bbf6ae2 (first commit). HEAD will add only this
  HANDOFF.md — submit the repo HEAD at submit time.
- Repo About: homepage https://make.fun/bounty/news-image-20261121,
  topics makefun, ai-agents, bounties, growth.
- Referral in README: https://make.fun/r/0ene8b3q only. No other referral
  code anywhere in the entry (checked by grep).
- Title to submit: "The World — 21 November 2026"
- Image: a 1024x1024 newspaper front page (entry.png, 161,588 bytes,
  sha256 c5181b64fec236a96540e939057d4ed8a8c46d6e83996be0f120e68ddd72a529),
  drawn by render_frontpage.py (Pillow, no network, no randomness) and copied
  to /output/entry.png by main.ts (Node 22). New image, new stories — not
  the 20 Nov image (different sha256).
- Content (verified by web search before drawing — AP, Reuters, CNN, UN
  News, Kyiv Independent / AFP, The Watchers, The Ridhu Times, WSJ,
  SecurityWeek): lead story COP31 in Antalya spilling into overtime on
  Saturday after the draft drops every mention of fossil fuels and a $120bn
  adaptation-finance target, Panama threatening to block consensus;
  Russian double-tap strike on Kryvyi Rih killing a 7-year-old child and a
  paramedic, 42 injured; Cyclone Akvan's aftermath in Odisha (300,000+
  evacuated, no deaths, Patrapur 209 mm rain, Berhampur flooding); UK–EU
  reset deal sealed in Brussels (food trade, linked carbon markets,
  100,000 youth mobility a year); JPMorgan/Visa/Mastercard third-party
  breach claimed by "n0n" (16,000+ emails, no card data); "Also today"
  strip (India 239/1 at lunch Day 3 Wellington, Rahul 93*; Sensex +898;
  Hyundai 2027 Elantra at the LA Auto Show; Mongolia's president resigns;
  tanker fire in the Strait of Hormuz; US Senate rejects Iran war-powers
  resolution 51–48).

## Verified
- Local run: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` runs
  clean (one harmless Node module-type warning, same as the 20 Nov entry).
- Determinism: render script run 3x and main.ts run 2x all write identical
  bytes (sha256 c5181b64… as above); image is 1024x1024, 161,588 bytes
  (< 1 MiB). Page visually checked: masthead, COP31 thermometer panel,
  Kryvyi Rih night scene, Odisha flood scene, flags/padlock icons, "Also
  today" strip and footer all legible, nothing clipped (final y = 986).
  One fix applied after the first visual check: the flood-panel wave arcs
  struck through the "300,000+ EVACUATED" caption — the caption now sits
  on a solid band, and the SHELTER label that overflowed its tent was
  removed.
- Dry-run gate: `node cli/makefun.mjs bundle ... --dry-run` (from the
  fresh 21 Nov kit dir, downloaded this run from
  https://make.fun/c/news-image-20261121/kit) exits 0 with NO "missing"
  errors. Warnings only, all by design: 0 usage rows attached to this
  builder session — the rows are written only once this run completes
  (see "Parent submission") — and a session-cut note (2 earlier records
  left out, developer message kept).
- Parent-chats fix, DIFFERENT from 20 Nov: the first dry-run failed with
  "missing: the parent chats" using --prompt-origin handed-off with
  prompt-bounty-kerja.txt. Two problems with that file: (a) it currently
  contains an unrelated Onchain OS installer instruction, NOT the bounty
  task — do NOT use it as --prompt-file; (b) the parent session
  ac07e4c1 opens with a scheduled [WORKER TASK] message, which the bundle
  only reads as a prompt when marked scheduled. The fix that passes the
  gate: --prompt-origin scheduled with --prompt-file
  hidden_files/prompt-scheduled-makefun-pantau-30menit.txt (the scheduled
  task body, extracted from the cron file this run) and a single
  --parent-session for ac07e4c1. There is NO second main-chat parent
  session for this run (unlike 20 Nov's 53f0cea2) — do not add one.
- Note: the bundle warning says the parent session ac07e4c1 "is not in
  this bundle" — the parent chats are carried as context-sessions, not
  bundled sessions; the same pattern submitted fine for 19/20 Nov.

## Parent submission — do this AFTER this subagent run completes
1. Run the SELECT (muse.db) for the builder agent_id
   7e9cb5a1-58cc-4180-9377-0b2a5e62b9a4 and the parent
   ac07e4c1-2455-4aff-99b8-9d914e8ad1a0, and REWRITE the usage file
   hidden_files/muse-usage-rows-news-image-20261121.jsonl with the fresh
   rows, one JSON object per line (it currently holds only the parent's
   1 row; the builder's rows appear only after this run completes):
   SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('7e9cb5a1-58cc-4180-9377-0b2a5e62b9a4','ac07e4c1-2455-4aff-99b8-9d914e8ad1a0') ORDER BY u.created_at DESC LIMIT 500
   (Verify at least 1 row for 7e9cb5a1 before bundling. If 0, end the turn
   and retry in the next.)
2. Bundle with the EXACT flags below (from the news-image-20261121 kit dir
   ~/workspace/makefun-agent2/news-image-20261121-kit/news-image-20261121-kit),
   only swapping in the rewritten usage file. Keep --no-discover, the
   single --parent-session, and --prompt-origin scheduled:
   node cli/makefun.mjs bundle --repo ~/workspace/makefun-agent2/entries/news-image-20261121 --out <bundle.tar.gz>
     --session /home/hatch/agents/agent-7e9cb5a1-58cc-4180-9377-0b2a5e62b9a4/sessions/7e9cb5a1-58cc-4180-9377-0b2a5e62b9a4.jsonl
     --no-discover
     --prompt-file ~/workspace/goals/make-fun-bounty-pantau-dan-submit-tiap-30-menit/hidden_files/prompt-scheduled-makefun-pantau-30menit.txt --prompt-origin scheduled
     --prompt-via "parent agent spawned a build subagent for the news-image-20261121 bounty under the standing 30-minute bounty monitor"
     --parent-session /home/hatch/agents/agent-ac07e4c1-2455-4aff-99b8-9d914e8ad1a0/sessions/ac07e4c1-2455-4aff-99b8-9d914e8ad1a0.jsonl
     --muse-usage <rewritten usage file> --system-prompt ~/workspace/goals/make-fun-bounty-pantau-dan-submit-tiap-30-menit/hidden_files/system-prompt-news-image-20261121.txt
     --harness muse-app --harness-version 1.3 --model ipnext/avocado-5.17-v2
     --provider ipnext --effort default --mcp none
   (The --model is ipnext/avocado-5.17-v2 — the model this builder session
   actually recorded, same as 20 Nov.)
3. Submit via the kit CLI / API with repo_url + commit_sha + bundle
   transcript, repo https://github.com/h05meigames/makefun-news-image-20261121,
   title "The World — 21 November 2026", using the repo HEAD commit at
   submit time. Save the receipt in hidden_files/ and check the dev grade.
   Do NOT submit any other entry.
