# Typography Mastery — Knowledge Base
## Elite Graphic Design Agent | Reference Document v1.0

---

## 1. THE TYPOGRAPHIC SCALE

### Modular Scale System
Base unit: **8px**. All type sizes must be drawn from a modular scale.
Choose ONE ratio per project and apply it consistently.

| Ratio Name         | Ratio  | Best For                        |
|--------------------|--------|---------------------------------|
| Major Second        | 1.125  | Dense UI, data-heavy interfaces |
| Minor Third         | 1.200  | Mobile UI, compact layouts      |
| Major Third         | 1.250  | General UI, SaaS products       |
| Perfect Fourth      | 1.333  | Editorial, marketing sites      |
| Augmented Fourth    | 1.414  | Editorial, magazine layouts     |
| Golden Ratio        | 1.618  | Display, high-impact branding   |

### Standard Scale (Major Third — 1.250)
```
8px   → 0.5rem   — Caption micro
10px  → 0.625rem — Legal / footnote
12px  → 0.75rem  — Caption / label
14px  → 0.875rem — Secondary body
16px  → 1rem     — Primary body (BASE)
20px  → 1.25rem  — Lead paragraph
24px  → 1.5rem   — H4 / card title
32px  → 2rem     — H3 / section header
40px  → 2.5rem   — H2 / page header
48px  → 3rem     — H1 / hero heading
64px  → 4rem     — Display / large hero
80px  → 5rem     — Oversized display
96px  → 6rem     — Maximum display scale
```

RULE: Never use a size not on the scale. One-off sizes break visual rhythm.

---

## 2. LEADING (LINE HEIGHT)

| Context               | Ratio  | Example (16px base)  |
|-----------------------|--------|----------------------|
| Display / Headlines   | 1.1×   | 48px type → 53px lh  |
| Subheadings           | 1.2×   | 32px type → 38px lh  |
| Lead paragraph        | 1.4×   | 20px type → 28px lh  |
| Body text             | 1.5×   | 16px type → 24px lh  |
| Captions              | 1.4×   | 12px type → 17px lh  |
| Code / Monospace      | 1.6×   | 14px type → 22px lh  |

RULE: Leading values must be multiples of the 8px base grid where possible.
RULE: Tighter leading on large type; looser leading on small type.

---

## 3. MEASURE (LINE LENGTH)

- **Minimum:** 45 characters per line
- **Optimal:** 66 characters per line
- **Maximum:** 75 characters per line

Lines below 45 characters: excessive hyphenation, choppy reading rhythm.
Lines above 75 characters: eye loses its place returning to the next line.

**CSS Implementation:**
```css
body {
  max-width: 66ch;   /* optimal measure */
  /* or */
  max-width: 75ch;   /* maximum measure */
}
```

---

## 4. TRACKING (LETTER-SPACING)

| Context                        | Value         |
|--------------------------------|---------------|
| Uppercase labels / ALL CAPS    | +50 to +100   |
| Uppercase headings             | +20 to +40    |
| Display headlines (≥64px)      | −20 to −40    |
| Body text                      | 0 (default)   |
| Tight display / brand lockup   | −40 to −80    |

RULE: NEVER track body text negatively. Never track uppercase text negatively.
RULE: Optical kerning overrides metrics kerning for type ≥32px.

---

## 5. TYPEFACE PSYCHOLOGY MATRIX

| Category         | Examples                        | Psychological Signal              | Industry Fit                          |
|------------------|---------------------------------|-----------------------------------|---------------------------------------|
| Old Style Serif  | Garamond, Caslon, Palatino      | Heritage, craft, literary trust   | Publishing, law, academia             |
| Transitional Serif | Times New Roman, Baskerville  | Authority, neutrality, precision  | Finance, journalism, government       |
| Modern Serif     | Didot, Bodoni                   | Luxury, fashion, high contrast    | Fashion, cosmetics, editorial         |
| Slab Serif       | Rockwell, Clarendon, Archer     | Confidence, stability, strength   | Industrial, automotive, sports        |
| Geometric Sans   | Futura, Avenir, Montserrat      | Precision, modernity, efficiency  | Technology, architecture, luxury      |
| Humanist Sans    | Gill Sans, Frutiger, Myriad     | Warmth, approachability, clarity  | Healthcare, education, NGO            |
| Neo-Grotesque    | Helvetica, Univers, Neue Haas   | Neutrality, objectivity, system   | Corporate, signage, wayfinding        |
| Display / Script | Playfair Display, Lobster       | Personality, expression, voice    | Accent ONLY — never body text         |
| Monospace        | Courier, JetBrains Mono         | Technical, code, precision        | Developer tools, data, tech editorial |

---

## 6. TYPEFACE PAIRING LOGIC

**The Two-Family Rule:** Maximum 2 typefaces per design system.
The third "typeface" is always a **weight variant** of an existing family.

**Pairing Strategies:**
1. **Serif + Geometric Sans:** Classic authority × modern clarity
   — Example: Freight Text Pro + Futura PT
2. **Old Style Serif + Humanist Sans:** Warmth + humanity
   — Example: Garamond + Gill Sans
3. **Modern Serif + Neo-Grotesque:** Contrast + tension
   — Example: Didot + Helvetica Neue
4. **Slab Serif + Geometric Sans:** Strength + precision
   — Example: Rockwell + Avenir

**Anti-Patterns (NEVER DO):**
- Two serifs from the same classification
- Two geometric sans-serifs
- Script + Script
- More than 2 families in a system

---

## 7. WEIGHT HIERARCHY

Use weight to create hierarchy before size changes.

| Role              | Weight  | Font-Weight Value |
|-------------------|---------|-------------------|
| Display headline  | Black   | 900               |
| Hero headline     | Bold    | 700               |
| Section heading   | SemiBold| 600               |
| Subheading        | Medium  | 500               |
| Body text         | Regular | 400               |
| Caption / meta    | Light   | 300               |

RULE: Never use Light (300) for body text below 18px — legibility failure.
RULE: Never use Black (900) for body text — readability failure.

---

## 8. VARIABLE FONTS

Variable font axes to control programmatically:

| Axis Tag | Name         | Range     | Application                         |
|----------|--------------|-----------|-------------------------------------|
| `wght`   | Weight       | 100–900   | Dynamic weight scaling              |
| `wdth`   | Width        | 50–200    | Condensed to extended variants      |
| `opsz`   | Optical Size | 8–144     | Auto-optimize for display vs. text  |
| `ital`   | Italic       | 0–1       | Interpolated italic angle           |
| `slnt`   | Slant        | −90 to 90 | Oblique angle control               |

**CSS Implementation:**
```css
h1 {
  font-variation-settings: 'wght' 700, 'opsz' 48;
}
body {
  font-variation-settings: 'wght' 400, 'opsz' 16;
}
```

---

## 9. TYPOGRAPHIC COLOR THEORY

"Typographic color" = the visual density and tone of a text block.
Controlled entirely through: weight, size, tracking, and leading.
NEVER requires literal color changes.

**Darkening the page:** Increase weight, decrease tracking, decrease leading.
**Lightening the page:** Decrease weight, increase tracking, increase leading.

A well-set body text passage should produce a visually consistent grey tone
with no dark clusters or sparse white holes.

---

## 10. RESPONSIVE TYPOGRAPHY

**Fluid Type (CSS clamp):**
```css
/* Scales from 16px at 320px viewport to 20px at 1440px */
font-size: clamp(1rem, 0.875rem + 0.625vw, 1.25rem);

/* Hero display: 40px → 80px */
font-size: clamp(2.5rem, 1.5rem + 3.33vw, 5rem);
```

**Breakpoint Scale Adjustments:**
- Mobile (375px): Base 15px, scale ratio 1.2
- Tablet (768px): Base 16px, scale ratio 1.25
- Desktop (1440px): Base 17px, scale ratio 1.333

---

## 11. PRINT TYPOGRAPHY STANDARDS

- Minimum body text size for print: **9pt** (approximately 12px)
- Optical resolution for print type: **300 DPI minimum**
- Font embedding: ALWAYS embed fonts in PDF/X-1a output
- Avoid hairline strokes below **0.25pt** — disappear on press
- Black body text: **K100 only** (no rich black — registration issues)
- Reverse text (white on dark): Increase weight one step and size +1pt

---

## 12. TYPOGRAPHIC CHECKLIST

Before delivering any design:

- [ ] Scale drawn from single modular ratio
- [ ] Minimum 3 distinct hierarchy levels visible
- [ ] Body text measure within 45–75 characters
- [ ] Leading meets ratio requirements for each level
- [ ] Maximum 2 typeface families in system
- [ ] Tracking applied correctly per context
- [ ] Optical kerning active on display type ≥32px
- [ ] No orphans or widows in body text
- [ ] No hyphenation in headlines
- [ ] ALL CAPS tracked +50 minimum
- [ ] Accessible contrast at all type sizes (WCAG 2.1)

---

*typography_mastery.md | Elite Graphic Design Agent Knowledge Base*
*Last Updated: 2026 | Version 1.0*
