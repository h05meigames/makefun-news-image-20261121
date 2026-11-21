#!/usr/bin/env python3
"""Draw the news-image-20261121 front page: one 1024x1024 newspaper page
summing up Saturday 21 November 2026. Pillow only, no network, no
randomness: running this script twice writes byte-identical PNGs.

Stories, verified by web search on 21 Nov 2026 (AP via WCIA/Reflector,
Reuters, CNN, UN News, Kyiv Independent / AFP via Roya News, The Watchers,
The Ridhu Times, Reuters UK, Reuters/WSJ/SecurityWeek):
- LEAD, 21 Nov: COP31 in Antalya spills into overtime on Saturday after
  negotiators pull an all-nighter; the draft cover decision has stripped
  out every mention of fossil fuels and dropped a $120bn adaptation-finance
  target, Panama threatens to block consensus, and campaigners warn of the
  "worst COP ever". The talks acknowledge the world will overshoot 1.5C.
- KRYVYI RIH: a Russian double-tap ballistic missile strike on the city
  centre kills a 7-year-old child and a paramedic and injures 42 people,
  four of them children; rescuers are hit by the second strike.
- ODISHA: Cyclone Akvan's aftermath — more than 300,000 people evacuated
  (3.72 lakh), no deaths reported, the storm weakens to a deep depression;
  Patrapur records 209 mm of rain and Berhampur streets flood.
- BRUSSELS: the UK and EU seal a reset deal — food trade without
  certificates, linked carbon markets, and a youth mobility scheme for
  100,000 young people a year; London puts the food deal at +GBP 5.1bn a
  year and the carbon link at +GBP 3.8bn.
- CYBER: JPMorgan Chase, Visa and Mastercard disclose third-party vendor
  breaches claimed by extortion group "n0n"; more than 16,000 customer
  email addresses are posted, but no card numbers or payment networks are
  affected.
- ALSO TODAY: India reach 239/1 at lunch on Day 3 in Wellington (KL Rahul
  93*) after Nicholls' 175* carried New Zealand to 368; Sensex rallies
  nearly 898 points; Hyundai unveils the 2027 Elantra at the Los Angeles
  Auto Show; Mongolia's president resigns, triggering a snap election;
  a tanker catches fire in the Strait of Hormuz; the EU adopts EUR 1bn in
  military aid for Ukraine; the US Senate rejects an Iran war-powers
  resolution 51-48.
"""
import math

from PIL import Image, ImageDraw, ImageFont

CANVAS_W, CANVAS_H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
CRIMSON = (163, 24, 44)
NAVY = (24, 68, 112)
SEA = (52, 110, 158)
LAND = (216, 195, 140)
MUTED = (88, 88, 88)
FAINT = (232, 226, 207)
TEAL = (18, 110, 96)

FONT_DIR = "/usr/share/fonts/truetype/liberation/"


def load(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


def serif_b(size):
    return load("LiberationSerif-Bold.ttf", size)


def serif(size):
    return load("LiberationSerif-Regular.ttf", size)


def serif_i(size):
    return load("LiberationSerif-Italic.ttf", size)


def sans_b(size):
    return load("LiberationSans-Bold.ttf", size)


def sans(size):
    return load("LiberationSans-Regular.ttf", size)


page = Image.new("RGB", (CANVAS_W, CANVAS_H), PAPER)
pen = ImageDraw.Draw(page)

LEFT = 36
RIGHT = CANVAS_W - LEFT
SPAN = RIGHT - LEFT


def split_lines(text, face, width):
    out, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if pen.textlength(trial, font=face) <= width:
            current = trial
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def block(text, face, x, y, width, gap, colour=INK):
    for line in split_lines(text, face, width):
        pen.text((x, y), line, font=face, fill=colour)
        y += gap
    return y


def hline(x0, y, x1, thick=2, colour=INK):
    pen.line([(x0, y), (x1, y)], fill=colour, width=thick)


# ---------------- masthead ----------------
pen.text((CANVAS_W // 2, 16), "THE WORLD", font=serif_b(82),
         fill=INK, anchor="ma")
pen.text((CANVAS_W // 2, 102), "The day's news in one page",
         font=serif_i(19), fill=MUTED, anchor="ma")
hline(LEFT, 132, RIGHT, 3)
hline(LEFT, 137, RIGHT, 1)
pen.text((LEFT, 144), "SATURDAY, 21 NOVEMBER 2026", font=sans_b(18),
         fill=CRIMSON)
pen.text((RIGHT, 144), "WORLD NEWS  •  ONE IMAGE", font=sans_b(18),
         fill=INK, anchor="ra")
hline(LEFT, 170, RIGHT, 1)

# ---------------- lead: COP31 overtime ----------------
y = 182
pen.text((LEFT, y), "ANTALYA  —  THE CLIMATE TALKS RUN OVER TIME",
         font=sans_b(19), fill=CRIMSON)
y = 206
y = block("COP31 spills into overtime as fossil fuels vanish from the deal",
          serif_b(40), LEFT, y, SPAN, 46)
y += 2
y = block("After an all-night session, the draft cover decision drops every "
          "mention of moving away from coal, oil and gas — and a $120bn "
          "adaptation-finance target with it.", serif_i(20), LEFT, y, SPAN,
          26, colour=(62, 62, 62))
y += 8


def cop_panel(x0, y0, w, h):
    """Antalya at dusk: a rising thermometer past 1.5C, and the two words
    the draft deleted, struck through."""
    pen.rectangle([x0, y0, x0 + w, y0 + h], fill=(22, 30, 48))
    # Thermometer on the left: tube, bulb, mercury past the 1.5C mark.
    tx, ty = x0 + 52, y0 + 12
    pen.rounded_rectangle([tx, ty, tx + 26, ty + 82], radius=13,
                          fill=(255, 255, 255))
    pen.ellipse([tx - 8, ty + 72, tx + 34, ty + 114], fill=(255, 255, 255))
    pen.rounded_rectangle([tx + 6, ty + 22, tx + 20, ty + 82], radius=7,
                          fill=(220, 50, 40))
    pen.ellipse([tx - 2, ty + 78, tx + 28, ty + 108], fill=(220, 50, 40))
    # The 1.5C line, dashed, across the tube.
    for dx in range(0, 44, 8):
        pen.line([(tx + 30 + dx, ty + 30), (tx + 34 + dx, ty + 30)],
                 fill=(255, 214, 90), width=3)
    pen.text((tx + 82, ty + 18), "1.5°C", font=sans_b(24),
             fill=(255, 214, 90))
    pen.text((tx + 82, ty + 48), "OVERSHOOT", font=sans_b(24),
             fill=(255, 255, 255))
    pen.text((tx + 82, ty + 76), "ACKNOWLEDGED — NOT STOPPED",
             font=sans_b(13), fill=(180, 190, 205))
    # Right half: the deleted words, struck through in red.
    rx = x0 + 470
    pen.text((rx, y0 + 14), "THE DRAFT DELETES:", font=sans_b(14),
             fill=(180, 190, 205))
    pen.text((rx, y0 + 36), "FOSSIL FUELS", font=sans_b(34),
             fill=(255, 255, 255))
    pen.line([(rx - 4, y0 + 55), (rx + 268, y0 + 49)], fill=(220, 50, 40),
             width=6)
    pen.text((rx, y0 + 76), "$120bn ADAPTATION TARGET", font=sans_b(22),
             fill=(255, 255, 255))
    pen.line([(rx - 4, y0 + 91), (rx + 330, y0 + 87)], fill=(220, 50, 40),
             width=5)
    # Delegate silhouettes along the bottom edge.
    for i, hx in enumerate([x0 + 30, x0 + 90, x0 + 150, x0 + 880]):
        pen.ellipse([hx, y0 + h - 26, hx + 18, y0 + h - 8],
                    fill=(58, 66, 88))
        pen.rectangle([hx - 2, y0 + h - 10, hx + 20, y0 + h],
                      fill=(58, 66, 88))
    pen.text((x0 + w - 14, y0 + h - 24),
             "PANAMA THREATENS TO BLOCK  •  “WORST COP EVER” WARNING",
             font=sans_b(13), fill=(255, 255, 255), anchor="ra")


panel_x, panel_y, panel_w, panel_h = LEFT, y, SPAN, 128
cop_panel(panel_x, panel_y, panel_w, panel_h)
y = panel_y + panel_h + 8
y = block("Negotiators from nearly 200 countries worked through the night "
          "in Antalya; Turkey and Australia, the co-hosts, are criticised "
          "for the slimmed-down text, while the summit's main surviving "
          "pledge is electrification: 35% of energy by 2035.",
          serif(18), LEFT, y, SPAN, 24)
y += 4
hline(LEFT, y, RIGHT, 1)
y += 8

# ---------------- row two: two columns ----------------
HALF = 464
top2 = y


def strike_scene(x0, y0, w, h):
    """Kryvyi Rih at night: a damaged red-brick building, smoke, and
    flashing ambulance lights."""
    pen.rectangle([x0, y0, x0 + w, y0 + h], fill=(22, 30, 48))
    # Damaged building, centre-left, with a broken corner.
    bx, bw = x0 + 60, 150
    pen.polygon([(bx, y0 + h), (bx, y0 + 18), (bx + 60, y0 + 6),
                 (bx + bw, y0 + 14), (bx + bw, y0 + h)], fill=(122, 52, 44))
    for wy in range(y0 + 26, y0 + h - 8, 16):
        for wx in range(bx + 10, bx + bw - 14, 26):
            pen.rectangle([wx, wy, wx + 14, wy + 9], fill=(255, 214, 90))
    # Smoke curls above the broken roof.
    for (sx, sy, r) in [(bx + 90, y0 + 6, 10), (bx + 110, y0 + 2, 13),
                        (bx + 132, y0 + 8, 9)]:
        pen.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(120, 125, 140))
    # Ambulance: white box with a red cross, blue and red flashers.
    ax, ay = x0 + 270, y0 + h - 26
    pen.rectangle([ax, ay, ax + 84, ay + 20], fill=(235, 235, 235))
    pen.rectangle([ax + 34, ay + 4, ax + 50, ay + 16], fill=(200, 30, 30))
    pen.rectangle([ax + 40, ay - 2, ax + 44, ay + 22], fill=(200, 30, 30))
    pen.ellipse([ax - 14, ay - 8, ax - 2, ay + 4], fill=(60, 120, 255))
    pen.ellipse([ax + 88, ay - 8, ax + 100, ay + 4], fill=(255, 60, 60))
    # Falling debris dots.
    for (dx, dy) in [(bx + 170, y0 + 20), (bx + 190, y0 + 34),
                     (bx + 160, y0 + 46)]:
        pen.ellipse([dx - 2, dy - 2, dx + 2, dy + 2], fill=(255, 140, 0))


def flood_scene(x0, y0, w, h):
    """Odisha after Akvan: rain over flooded streets, houses at the
    waterline and a relief shelter."""
    pen.rectangle([x0, y0, x0 + w, y0 + h], fill=(70, 96, 110))
    # Rain streaks.
    for i in range(26):
        rx = x0 + 12 + (i * 37) % (w - 24)
        ry = y0 + 6 + (i * 13) % 34
        pen.line([(rx, ry), (rx - 4, ry + 12)], fill=(200, 215, 225),
                 width=2)
    # Houses on the far bank.
    for (hx, hw, hh) in [(x0 + 24, 70, 26), (x0 + 110, 84, 32),
                         (x0 + 210, 64, 24)]:
        pen.rectangle([hx, y0 + 44 - hh, hx + hw, y0 + 44], fill=(96, 66, 22))
        pen.polygon([(hx - 4, y0 + 44 - hh), (hx + hw // 2, y0 + 58 - hh),
                     (hx + hw + 4, y0 + 44 - hh)], fill=(163, 24, 44))
    # Flood water with wave lines.
    pen.rectangle([x0, y0 + 44, x0 + w, y0 + h], fill=(38, 84, 128))
    for wy in [y0 + 54, y0 + 64, y0 + 74]:
        for wx in range(x0 + 10, x0 + w - 10, 46):
            pen.arc([wx, wy, wx + 30, wy + 8], 200, 340,
                    fill=(180, 210, 230), width=2)
    # Relief shelter tent on the right, above the water.
    sx = x0 + w - 140
    pen.polygon([(sx, y0 + 44), (sx + 60, y0 + 6), (sx + 120, y0 + 44)],
                fill=(240, 235, 215))
    # Caption strip: solid band behind the text so the waves cannot
    # strike through it.
    pen.rectangle([x0 + 6, y0 + h - 24, x0 + 316, y0 + h - 2],
                  fill=(24, 60, 96))
    pen.text((x0 + 12, y0 + h - 22), "300,000+ EVACUATED  •  NO DEATHS",
             font=sans_b(14), fill=(255, 255, 255))


x = LEFT
pen.text((x, top2), "KRYVYI RIH  —  DOUBLE-TAP STRIKE", font=sans_b(15),
         fill=CRIMSON)
yy = block("Russian missiles kill a child and a paramedic; 42 injured",
           serif_b(28), x, top2 + 22, HALF, 32)
yy += 4
strike_scene(x, yy, HALF, 74)
yy += 74 + 6
end_left = block("A second missile hits as rescuers work the wreckage of "
                 "the first; four of the injured are children. The EU "
                 "adopts €1bn in military aid for Ukraine.",
                 serif(17), x, yy, HALF, 22)

x = RIGHT - HALF
pen.text((x, top2), "ODISHA  —  AFTER THE CYCLONE", font=sans_b(15),
         fill=CRIMSON)
yy = block("Akvan weakens, but the rain keeps coming; streets flood",
           serif_b(28), x, top2 + 22, HALF, 32)
yy += 4
flood_scene(x, yy, HALF, 74)
yy += 74 + 6
end_right = block("More than 300,000 people were moved to shelters before "
                  "landfall near Gopalpur; Patrapur records 209 mm of rain "
                  "and Berhampur pumps out flooded streets.",
                  serif(17), x, yy, HALF, 22)
y = max(end_left, end_right) + 6
hline(LEFT, y, RIGHT, 1)
y += 8

# ---------------- row three: two short items ----------------
def flags_icon(cx, cy):
    # Union Jack (simplified): blue field, white saltire, red cross.
    pen.rectangle([cx - 20, cy - 12, cx - 2, cy + 12], fill=(0, 36, 125))
    pen.line([(cx - 20, cy - 12), (cx - 2, cy + 12)], fill=(255, 255, 255),
             width=3)
    pen.line([(cx - 20, cy + 12), (cx - 2, cy - 12)], fill=(255, 255, 255),
             width=3)
    pen.line([(cx - 11, cy - 12), (cx - 11, cy + 12)], fill=(200, 16, 46),
             width=4)
    pen.line([(cx - 20, cy), (cx - 2, cy)], fill=(200, 16, 46), width=4)
    # EU flag: blue field, ring of gold stars.
    pen.rectangle([cx + 2, cy - 12, cx + 20, cy + 12], fill=(0, 51, 153))
    for k in range(8):
        ang = 2 * math.pi * k / 8
        sx = cx + 11 + 6.5 * math.cos(ang)
        sy = cy + 6.5 * math.sin(ang)
        pen.ellipse([sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5],
                    fill=(255, 209, 0))


def padlock(cx, cy):
    pen.arc([cx - 10, cy - 16, cx + 10, cy + 2], 180, 360,
            fill=(90, 90, 100), width=4)
    pen.rounded_rectangle([cx - 13, cy - 4, cx + 13, cy + 14], radius=3,
                          fill=(24, 68, 112))
    pen.ellipse([cx - 3, cy, cx + 3, cy + 6], fill=(255, 214, 90))


def short_item(x, kicker, head, body, draw_icon):
    pen.text((x + 44, y), kicker, font=sans_b(13), fill=CRIMSON)
    yy = block(head, sans_b(19), x + 44, y + 16, HALF - 44, 23)
    draw_icon(x + 20, y + 26)
    return block(body, serif(16), x + 44, yy + 2, HALF - 44, 21)


y2 = short_item(LEFT, "BRUSSELS", "UK–EU seal the reset deal",
                "Food trade without certificates, linked carbon markets and "
                "a youth mobility scheme for 100,000 a year; London values "
                "the package at up to £8.9bn a year.", flags_icon)
y3 = short_item(RIGHT - HALF, "NEW YORK", "Banks hit by vendor breach",
                "JPMorgan, Visa and Mastercard disclose third-party "
                "incidents claimed by the “n0n” group; 16,000+ customer "
                "emails are posted, but no card data is hit.", padlock)
y = max(y2, y3) + 6
hline(LEFT, y, RIGHT, 1)
y += 6

# ---------------- also today ----------------
pen.text((LEFT, y), "ALSO TODAY", font=sans_b(15), fill=CRIMSON)
y = block("India 239/1 at lunch on Day 3 in Wellington, Rahul 93* after "
          "Nicholls' 175* carried New Zealand to 368  ·  Sensex rallies "
          "nearly 898 points  ·  Hyundai unveils the 2027 Elantra at the "
          "Los Angeles Auto Show  ·  Mongolia's president resigns, a snap "
          "election follows  ·  A tanker catches fire in the Strait of "
          "Hormuz  ·  US Senate rejects an Iran war-powers resolution "
          "51–48",
          sans(15), LEFT + 118, y, RIGHT - LEFT - 118, 20, colour=(62, 62, 62))
y += 4
hline(LEFT, y, RIGHT, 1)
pen.text((CANVAS_W // 2, y + 5),
         "Compiled from the day's reporting  •  21 November 2026",
         font=sans(13), fill=MUTED, anchor="ma")

page.save("entry.png")
print("saved; final y =", y)
