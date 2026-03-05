# Layout and Composition — Knowledge Base
## Elite Graphic Design Agent | Reference Document v1.0

---

## 1. THE 8PX BASE GRID SYSTEM

The foundational spatial unit for all digital design is **8px**.

All spacing, sizing, and positioning values MUST be multiples of 8px.

### The Core Spacing Scale
```
4px   → 0.25rem  — Micro gap (icon internal padding)
8px   → 0.5rem   — XS  — Tight element grouping
16px  → 1rem     — SM  — Default component padding
24px  → 1.5rem   — MD  — Component separation
32px  → 2rem     — LG  — Section internal spacing
40px  → 2.5rem   — XL  — Component to section gap
48px  → 3rem     — 2XL — Section top/bottom padding
64px  → 4rem     — 3XL — Major section separation
80px  → 5rem     — 4XL — Hero padding
96px  → 6rem     — 5XL — Page-level macro spacing
128px → 8rem     — 6XL — Maximum macro white space unit
```

RULE: 4px is permitted for micro-adjustments only (icon padding, fine-tuning).
RULE: No fractional pixel values. No 7px, 13px, 23px.
RULE: CSS rem values assume 1rem = 16px root font size.

---

## 2. THE 12-COLUMN WEB GRID

Standard responsive grid system.

### Desktop (1440px canvas)
```
Columns:      12
Column width: ~88px (varies with container)
Gutter:       24px
Margin:       80px (left + right)
Max content:  1280px
```

### Desktop Narrow (1280px canvas)
```
Columns:      12
Column width: ~78px
Gutter:       24px
Margin:       40px
```

### Tablet (768px canvas)
```
Columns:      8
Gutter:       16px
Margin:       40px
```

### Mobile (375px canvas)
```
Columns:      4
Gutter:       16px
Margin:       16px
```

### Column Span Usage Guide
| Content Type            | Column Span (12-col) |
|-------------------------|----------------------|
| Full-width hero         | 12 cols              |
| Primary content area    | 8 cols               |
| Sidebar                 | 4 cols               |
| Card (3-up grid)        | 4 cols               |
| Card (4-up grid)        | 3 cols               |
| Feature callout         | 6 cols               |
| CTA section             | 8 cols (centered)    |
| Narrow editorial text   | 6 cols (centered)    |

RULE: NEVER use fractional column spans.
RULE: NEVER let content bleed into the margin zone.

---

## 3. THE GOLDEN RATIO

**Ratio:** 1 : 1.618 (φ — Phi)

Applications:
- Canvas proportions (A4: 210 × 297mm ≈ 1:1.414; close to φ)
- Hero section height vs. remaining page content
- Logo proportions (wordmark width to height)
- UI panel relationships (sidebar : main content)
- Typography size relationships between heading levels

**Golden Rectangle Construction:**
A rectangle whose sides are in ratio 1:1.618.
Subdivide it: the remaining rectangle after removing the square is another
golden rectangle. Repeat to create a logarithmic spiral (golden spiral).

**Practical Application:**
```
If primary panel = 800px wide
Secondary panel = 800 / 1.618 = 494px wide
```

---

## 4. BASELINE GRID AND VERTICAL RHYTHM

The baseline grid ensures consistent vertical alignment of all text.
Every line of text should sit on a baseline grid increment.

**Standard baseline grid:** 8px
**Body text example:**
- Font size: 16px
- Line height: 24px (1.5× = 3 × 8px baseline units) ✅

**Heading example:**
- Font size: 32px
- Line height: 40px (5 × 8px baseline units) ✅

RULE: Leading must always be a multiple of the baseline grid unit.
RULE: Section padding must align text blocks to the baseline grid.

---

## 5. COMPOSITIONAL LAWS

### The Rule of Thirds
Divide the canvas into 3 equal rows and 3 equal columns (9-part grid).
Primary focal points belong at the 4 intersection points.
Secondary focal points belong along the 4 lines.

Use for: Photography composition, hero layouts, print advertisements.

### The Golden Spiral
Place the primary focal point at the center of the golden spiral.
Visual weight flows along the spiral path toward the focal point.

Use for: Logo design, poster composition, editorial spreads.

### The Z-Pattern (Marketing Layouts)
Eye path on marketing pages with sparse copy:
```
1 (Top Left) ————→ 2 (Top Right)
                          ↓
3 (Bottom Left) ←——— (diagonal)
          ↓
4 (CTA — Bottom Center/Right)
```
Place: Brand/logo at position 1, trust signal at 2, supporting content at 3,
CTA at position 4.

### The F-Pattern (Editorial / Content Layouts)
Eye path on text-heavy, information-dense pages:
```
━━━━━━━━━━━━━━━━━━━━  (full first scan — headline)
━━━━━━━━━━━━━          (partial second scan)
━                      (vertical scan down left edge)
━
━
```
Place: Highest-value content in the first two lines and left column.
Use for: News sites, dashboards, documentation, email.

---

## 6. WHITE SPACE DISCIPLINE

### Macro White Space
The large, deliberate emptiness that structures page regions.
Signals: confidence, premium positioning, editorial authority.

RULE: NEVER fill macro white space because it feels "empty."
That emptiness IS the design message.

Macro white space applications:
- Hero section above-the-fold breathing room
- Between major page sections (min 80px–128px)
- Around hero typography (let it breathe)
- Logo clear space zones

### Micro White Space
The small-scale spacing within and between components.
Controls readability, cognitive load, and perceived quality.

| Component            | Micro White Space Rule                    |
|----------------------|-------------------------------------------|
| Button padding       | 12px top/bottom, 24px left/right (minimum)|
| Card internal padding| 24px all sides (minimum)                  |
| Form field height    | 44px minimum (accessibility)             |
| Icon to label gap    | 8px                                       |
| List item gap        | 4px–8px                                   |
| Paragraph bottom margin | 16px–24px                             |

### The Emptiness = Premium Signal
Crowded layouts signal: low-cost, high-volume, commodity.
Open layouts signal: premium, confident, exclusive.

Budget allocation rule: Give 30% of your canvas to white space intentionally.

---

## 7. ASYMMETRIC TENSION

Intentional visual imbalance creates dynamic energy and visual interest.

**Principle:** One large dominant element (visual anchor) counterbalanced by
a cluster of smaller elements on the opposite side/quadrant.

**Visual weight factors (heavy → light):**
1. Saturated warm colors > desaturated cool colors
2. Large shapes > small shapes
3. Dark values > light values
4. Complex textures > flat fills
5. Irregular shapes > regular shapes
6. Isolated elements > grouped elements

**Implementing asymmetric tension:**
- Place the primary image/element in one third
- Place supporting content in the opposing two-thirds
- Never center the primary visual unless symmetry IS the message

---

## 8. GRID SYSTEMS FOR PRINT

### ISO Paper Proportions
```
A0:  841mm × 1189mm
A1:  594mm × 841mm
A2:  420mm × 594mm
A3:  297mm × 420mm
A4:  210mm × 297mm  ← Most common print format
A5:  148mm × 210mm
```

### Bleed and Safe Zone (Mandatory for Print)
```
Bleed:     3mm outside trim on ALL sides
Safe zone: 5mm inside trim on ALL sides
           (all critical content — text, logos — stays inside safe zone)
```

### Business Card Dimensions
```
Standard:  88mm × 54mm (EU) / 3.5" × 2" (US)
Bleed:     94mm × 60mm (with 3mm bleed)
Safe zone: 82mm × 48mm (with 3mm safe zone inside trim)
```

### The Van de Graaf Canon (Classical Book Layout)
A method for dividing a page into harmonious text area and margins:
```
Inner margin:   1/9 of page width
Top margin:     1/9 of page height
Text area:      the remaining 4/9 × 4/9 (of the page)
```
Produces a text block where height = page width. Classically harmonious.

---

## 9. LAYOUT HIERARCHY ENFORCEMENT

The layout must communicate hierarchy through structure alone.
Test: Remove all color. Remove all text. Can you still tell what the
most important element is? If no: the layout fails.

**5-Level Visual Hierarchy:**
```
Level 1: Primary focal point  — Largest, most contrast, isolated
Level 2: Secondary message   — Supporting headline, key visual
Level 3: Supporting content  — Body text, sub-sections
Level 4: Metadata            — Captions, labels, dates
Level 5: Navigational chrome — UI controls, footnotes
```

RULE: No two elements can occupy the same hierarchy level with equal
visual weight unless they are intentionally parallel items.

---

## 10. COMPONENT SPACING SYSTEM

### The "Space Between" Rule
Space between elements that are RELATED: use smaller increments (8px–16px).
Space between elements that are UNRELATED: use larger increments (32px–64px).
This is Gestalt Proximity in action.

### The Box Model Hierarchy
```
Atom padding:       8px–16px
Molecule padding:   16px–24px
Organism padding:   24px–40px
Section padding:    48px–80px
Page margin:        80px–128px
```

---

## 11. RESPONSIVE LAYOUT PATTERNS

| Pattern         | Behavior                                      | Best For                    |
|-----------------|-----------------------------------------------|-----------------------------|
| Column Drop     | Multi-column → stacked at breakpoint          | Most content layouts        |
| Layout Shifter  | Layout changes significantly at each bp       | Complex app interfaces      |
| Tiny Tweaks     | Minor adjustments to single-column layout     | Blog, editorial, articles   |
| Off Canvas      | Secondary content off-screen until triggered  | Navigation, filters         |
| Mostly Fluid    | Fluid grid with fixed margins at wide screens | E-commerce, marketing       |

### Mobile-First Approach (REQUIRED)
Design for 375px first. Add complexity at wider breakpoints.
```css
/* Mobile first */
.grid { display: grid; grid-template-columns: 1fr; gap: 16px; }

/* Tablet */
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); gap: 24px; }
}

/* Desktop */
@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); gap: 24px; }
}
```

---

## 12. LAYOUT QC CHECKLIST

Before delivering any layout:

- [ ] All spacing values are multiples of 8px
- [ ] Grid system documented (columns, gutters, margins)
- [ ] No fractional pixel values anywhere
- [ ] White space is intentional, not accidental
- [ ] Reading pattern (Z or F) appropriate for content type
- [ ] Visual hierarchy survives grayscale test
- [ ] Baseline grid alignment active on all text elements
- [ ] Responsive behavior defined for all breakpoints
- [ ] Touch targets ≥44×44px on all interactive elements
- [ ] Compositional law identified and applied (rule of thirds, golden ratio)
- [ ] Asymmetric tension active (or symmetry intentional and justified)

---

*layout_composition.md | Elite Graphic Design Agent Knowledge Base*
*Last Updated: 2026 | Version 1.0*
