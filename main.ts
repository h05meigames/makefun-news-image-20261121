// news-image-20261121 entry (Node 22, standard library only). The image
// is the entry.png beside this file: a 1024x1024 newspaper front page drawn
// for this bounty by render_frontpage.py (Pillow, no network, no randomness),
// and this program copies it to /output/entry.png. The gate accepts a whole
// PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees
// exactly the bytes copied.
//
// The image sums up Saturday 21 November 2026: COP31 in Antalya
// spilling into overtime after the draft drops every mention of fossil
// fuels and a $120bn adaptation-finance target; a Russian double-tap
// strike on Kryvyi Rih killing a child and a paramedic; Cyclone Akvan's
// aftermath in Odisha, with 300,000+ evacuated and no deaths; the UK-EU
// reset deal sealed in Brussels; and a third-party breach hitting
// JPMorgan, Visa and Mastercard. See render_frontpage.py for the sources
// each story was verified against.
//
// Determinism: entry.png is a fixed asset in this repository, so both
// grader runs copy identical bytes. Verified locally by running main.ts
// twice and comparing sha256 (see HANDOFF.md).
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });

const source = new URL('./entry.png', import.meta.url);
const dest = join(outDir, 'entry.png');
copyFileSync(source, dest);

// The gate reads exactly the bytes copied: confirm the copy landed whole
// by comparing sha256 of source and destination.
// The gate reads the first bytes to tell PNG from JPEG: confirm the copy
// starts with the PNG signature before the hash comparison.
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!readFileSync(dest).subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error('entry.png is not a PNG');
}
const digest = (path) =>
  createHash('sha256').update(readFileSync(path)).digest('hex');
if (digest(source) !== digest(dest)) {
  throw new Error('entry.png copy failed integrity check');
}
