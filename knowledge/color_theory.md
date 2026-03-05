# Color Theory — Knowledge Base
## Elite Graphic Design Agent | Reference Document v1.0

---

## 1. THE COLOR MODEL TRIAD

### HSV (Hue, Saturation, Value) — Primary Working Model
- **Hue (H):** 0°–360° — The color identity on the spectrum
- **Saturation (S):** 0–100% — Color intensity (0% = grey, 100% = full color)
- **Value (V):** 0–100% — Brightness (0% = black, 100% = maximum brightness)

### HSL (Hue, Saturation, Lightness) — For CSS/UI Implementation
```css
/* HSL in CSS */
color: hsl(210, 80%, 55%);
background: hsl(210, 80%, 97%);
```

### CMYK — Print Production ONLY
Never design in CMYK; convert at final export stage.
Profile: ISO Coated v2 300% (ECI) — Europe
Profile: SWOP v2 — United States

RULE: Every color decision must be stated as HSV + HEX. Color names alone
are never a sufficient specification.

---

## 2. THE 6-LEVEL SATORI PROGRESSION

For every primary brand color, generate all 6 levels.
This creates a complete, internally consistent tonal system.

Formula applied to any base color (H°, 100%, 55%):

| Level | Name               | S Value | V Value | Use Case                              |
|-------|--------------------|---------|---------|---------------------------------------|
| L1    | Tint / Background  | 10%     | 97%     | Page backgrounds, card surfaces       |
| L2    | Soft Accent        | 25%     | 92%     | Hover states, secondary surfaces      |
| L3    | Mid Accent         | 55%     | 78%     | Supporting accents, dividers          |
| L4    | Primary Brand      | 100%    | 55%     | PRIMARY — buttons, links, brand       |
| L5    | Pressed / Active   | 100%    | 38%     | Pressed button, active nav state      |
| L6    | Dark Anchor        | 100%    | 18%     | Dark mode base, deep shadows          |

**Example — Brand Blue (H:215°):**
```
L1: HSV(215°, 10%, 97%)  → #F0F5FC  — Background tint
L2: HSV(215°, 25%, 92%)  → #D5E3F5  — Hover surface
L3: HSV(215°, 55%, 78%)  → #5A9AC7  — Supporting accent
L4: HSV(215°, 100%, 55%) → #006AB8  — PRIMARY brand blue
L5: HSV(215°, 100%, 38%) → #004A82  — Active/pressed state
L6: HSV(215°, 100%, 18%) → #00233D  — Dark mode anchor
```

---

## 3. THE 60-30-10 PALETTE RULE

| Role         | Proportion | Application                               |
|--------------|------------|-------------------------------------------|
| Dominant     | 60%        | Neutral backgrounds, surfaces, white space|
| Secondary    | 30%        | Content areas, body, supporting UI panels |
| Accent       | 10%        | CTAs, highlights, active states ONLY      |

RULE: NEVER invert this ratio.
RULE: The accent color (10%) carries the brand's most recognizable hue.
RULE: The dominant color (60%) is almost always near-neutral.

---

## 4. WCAG 2.1 CONTRAST STANDARDS

### Compliance Levels

| Standard | Contrast Ratio | Text Application                          |
|----------|---------------|-------------------------------------------|
| AA       | 4.5:1         | Normal text (< 18pt regular / <14pt bold) |
| AA Large | 3:1           | Large text (≥18pt regular / ≥14pt bold)   |
| AA UI    | 3:1           | UI components, graphical objects, icons   |
| AAA      | 7:1           | Enhanced — target for body text           |
| AAA Large| 4.5:1         | Enhanced for large text                   |

### Common Safe Combinations

| Background | Text Color  | Ratio  | Status        |
|------------|-------------|--------|---------------|
| #FFFFFF    | #000000     | 21:1   | ✅ AAA        |
| #FFFFFF    | #767676     | 4.54:1 | ✅ AA         |
| #FFFFFF    | #949494     | 2.85:1 | ❌ FAIL       |
| #F8F9FA    | #212529     | 16.1:1 | ✅ AAA        |
| #0066CC    | #FFFFFF     | 5.74:1 | ✅ AA         |
| #FFD700    | #000000     | 9.98:1 | ✅ AAA        |
| #FF0000    | #FFFFFF     | 3.99:1 | ❌ AA FAIL    |

### Contrast Verification Tools
- **WebAIM Contrast Checker:** https://webaim.org/resources/contrastchecker/
- **Colour Contrast Analyser (desktop app):** TPGi
- **Figma Plugin:** Stark or A11y - Color Contrast Checker

RULE: Run contrast check on EVERY text/background pair before delivery.
RULE: If a color fails AA, it does not ship. Resolve before client review.

---

## 5. SIMULTANEOUS CONTRAST AND VIBRATION

**Simultaneous Contrast:** A color appears different depending on the colors
surrounding it. The same grey looks darker on white and lighter on black.

**Chromatic Vibration:** Occurs when two complementary colors of equal or
near-equal saturation share a border. The edge appears to shimmer or pulse.
This is perceptually disturbing and must be managed.

**Resolution Protocol:**
1. Desaturate one color by minimum 20%
2. Shift value of one color by minimum 15%
3. Introduce a neutral (black, white, grey) border between them
4. Reduce the size of one color area significantly

**High-Risk Pairs (ALWAYS check):**
- Red + Green (equal saturation)
- Blue + Orange (equal saturation)
- Purple + Yellow (equal saturation)

---

## 6. DARK MODE VALUE-SHIFT PROTOCOL

NEVER simply invert the light mode palette.

| Light Mode Role   | Dark Mode Equivalent      | Reason                              |
|-------------------|---------------------------|-------------------------------------|
| #FFFFFF background| #121212 (not pure black)  | Pure black increases halation       |
| #000000 text      | #E8E8E8 (not pure white)  | Pure white on black causes fatigue  |
| Brand Primary L4  | Brand Primary L3 or L2    | L4 becomes too dark on dark surface |
| Surface L1        | L6 value                  | Swap light and dark extremes        |
| Error #EF4444     | #FF6B6B (lightened +20%V) | Maintain 3:1 on dark background     |

**Elevation in Dark Mode (Material Design pattern):**
```
Base surface:    #121212
1dp elevation:   #1E1E1E  (+0.05 white overlay)
2dp elevation:   #232323
4dp elevation:   #272727
8dp elevation:   #2C2C2C
16dp elevation:  #2E2E2E
24dp elevation:  #303030
```

---

## 7. COLOR PSYCHOLOGY MAP

| Color Family    | Hue Range     | Psychological Signal              | Primary Industries                       |
|-----------------|---------------|-----------------------------------|------------------------------------------|
| Red             | 0°–15°        | Urgency, passion, energy, danger  | Food & beverage, retail, alerts, health  |
| Orange          | 15°–45°       | Enthusiasm, warmth, creativity    | Consumer, food, entertainment            |
| Yellow          | 45°–65°       | Optimism, clarity, attention      | Warning, children, energy (use sparingly)|
| Yellow-Green    | 65°–100°      | Fresh, natural, youthful          | Organic, youth, sustainability           |
| Green           | 100°–150°     | Growth, health, sustainability    | Finance, wellness, environment           |
| Teal / Cyan     | 150°–200°     | Calm, clarity, balance            | Healthcare, technology, finance          |
| Blue            | 200°–240°     | Trust, reliability, competence    | Finance, technology, corporate           |
| Indigo          | 240°–260°     | Depth, authority, integrity       | Legal, government, premium tech          |
| Purple          | 260°–300°     | Creativity, wisdom, luxury        | Beauty, creative, education, spirituality|
| Magenta / Pink  | 300°–340°     | Femininity, playfulness, romance  | Beauty, fashion, entertainment           |
| Brown / Earth   | 15°–40° low S | Reliability, natural, stability   | Food, outdoor, heritage craft            |
| Black           | — (0% S, 0% V)| Luxury, authority, elegance       | Fashion, premium, automotive             |
| White           | — (0% S, 100%)| Cleanliness, simplicity, space    | Healthcare, tech, premium minimal        |
| Grey (neutral)  | 0°, 0–20% S   | Neutrality, professionalism       | Technology, corporate, industrial        |

---

## 8. FUNCTIONAL COLOR SYSTEM

Define these MANDATORY functional colors for every UI design system:

| Function   | Light Mode Hex | Dark Mode Hex  | Usage                         |
|------------|----------------|----------------|-------------------------------|
| Success    | #22C55E        | #4ADE80        | Confirmations, completed tasks|
| Warning    | #F59E0B        | #FCD34D        | Non-critical alerts           |
| Error      | #EF4444        | #FF6B6B        | Failures, destructive actions |
| Info       | #3B82F6        | #60A5FA        | Informational messages        |

Verify ALL functional colors meet 3:1 contrast on their container backgrounds.

---

## 9. PALETTE CONSTRUCTION METHODS

### Analogous (Harmonious, Low Tension)
Colors within 30° of each other on the wheel.
Use: lifestyle brands, wellness, approachable products.
Risk: Can feel monotonous — vary saturation and value aggressively.

### Complementary (High Contrast, High Energy)
Colors 180° apart.
Use: CTAs, emphasis, sports, urgency.
Risk: Chromatic vibration — desaturate one side.

### Split-Complementary (Harmonious + Tension)
One base color + two colors adjacent to its complement.
Use: Most versatile. Balanced energy without full complement clash.

### Triadic (Vibrant, Complex)
Three colors equally spaced (120° apart).
Use: Children's, entertainment, expressive brands.
Risk: Difficult to balance — use 60-30-10 rule strictly.

### Tetradic / Square (Rich, Complex)
Four colors at 90° intervals.
Use: Only for very experienced systems. Hard to control.

### Monochromatic (Minimal, Premium)
Single hue, multiple saturation and value levels.
Use: Luxury, minimalist, premium tech. Pair with strong typography.

---

## 10. COLOR TEMPERATURE AND SPATIAL DEPTH

**Warm colors (Red, Orange, Yellow):** Advance — appear closer to the viewer.
**Cool colors (Blue, Green, Purple):** Recede — appear further from the viewer.

Apply to create depth without 3D techniques:
- CTA button: Warm accent on cool background = maximum visual advancement
- Background: Cool, desaturated hues create visual depth behind content
- Typography on warm background: Use dark cool color for maximum contrast

---

## 11. PRINT COLOR CONVERSION

| RGB Hex | CMYK Equivalent           | Pantone Reference (if needed)  |
|---------|---------------------------|--------------------------------|
| #000000 | C0 M0 Y0 K100             | Process Black                  |
| Rich Black fills | C60 M40 Y40 K100  | —                              |
| #FFFFFF | C0 M0 Y0 K0               | —                              |
| #FF0000 | C0 M99 Y100 K0            | 485 C                          |
| #0000FF | C100 M100 Y0 K0           | 2728 C                         |
| #FFFF00 | C0 M0 Y100 K0             | 102 C                          |

RULE: Rich black (C60 M40 Y40 K100) for large fills ONLY.
RULE: K100 only for body text and fine lines to avoid registration issues.

---

## 12. COLOR QC CHECKLIST

Before delivering any design:

- [ ] Every color specified as HSV + HEX (not name-only)
- [ ] All text/background pairs verified against WCAG 2.1 AA
- [ ] 60-30-10 ratio applied and verifiable
- [ ] 6-level Satori progression documented for brand colors
- [ ] Functional colors (success/warning/error/info) defined
- [ ] Dark mode palette remapped (not inverted)
- [ ] Chromatic vibration checked at all complementary borders
- [ ] Print files converted to CMYK with correct profile
- [ ] Color psychology alignment verified against brand positioning

---

*color_theory.md | Elite Graphic Design Agent Knowledge Base*
*Last Updated: 2026 | Version 1.0*
