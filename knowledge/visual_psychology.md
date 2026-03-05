# Visual Psychology — Knowledge Base
## Elite Graphic Design Agent | Reference Document v1.0

---

## 1. GESTALT PSYCHOLOGY — COMPLETE PRINCIPLE SUITE

Gestalt theory: the human brain organizes visual information into unified
wholes rather than collections of separate parts. The designer who masters
Gestalt controls perception at the pre-conscious level.

---

### Principle 1: PROXIMITY
**Definition:** Elements placed close together are perceived as a group,
regardless of shape, color, or size differences.

**Mechanism:** Spatial closeness overrides visual difference for grouping.

**Application:**
- Group related navigation items without explicit dividers
- Cluster form fields with their labels (8px max gap)
- Separate unrelated content blocks with 32px+ spacing
- Card components group their child elements via tight internal padding

**Misuse Warning:** Elements accidentally placed close together will be
perceived as related even when they are not. Audit every layout for
unintentional proximity groupings.

---

### Principle 2: SIMILARITY
**Definition:** Elements that share visual properties (shape, color, size,
texture) are perceived as belonging to the same group.

**Mechanism:** Visual matching creates categorical association without labels.

**Application:**
- Use consistent color to signal all interactive elements (links, buttons)
- Use consistent icon style to signal the same functional category
- Apply consistent type treatment to all headings at the same hierarchy level
- Use matching card dimensions for grid items of the same content type

**Advanced Use:** Intentional similarity violation = emphasis.
If every bullet is black and one is red, the red one reads as a warning.

---

### Principle 3: CONTINUITY
**Definition:** The eye naturally follows paths, curves, and lines.
Elements arranged in a smooth path are perceived as more related than
elements on a broken or jagged path.

**Mechanism:** The brain prefers smooth visual trajectories.

**Application:**
- Align elements along invisible horizontal/vertical axes
- Use diagonal composition to direct eye from headline to CTA
- In photography, use leading lines (roads, fences, corridors) to direct gaze
- In UI: progress stepper components leverage continuity
- Carousel/slider patterns rely on implied continuation

---

### Principle 4: CLOSURE
**Definition:** The brain fills in missing parts of an incomplete shape
to perceive it as a complete, whole object.

**Mechanism:** Cognitive completion of open forms.

**Application:**
- Logo design: open letterforms or icons that suggest completion (FedEx arrow)
- Negative space logos (WWF panda, NBC peacock)
- Typographic ligatures suggest unified forms
- Grid layouts with partial cards suggest "more content" beyond the edge
- Loading indicators can use partial circles to indicate incompleteness

**Key Insight:** Closure requires active cognitive engagement.
That engagement creates ownership and memorability.

---

### Principle 5: FIGURE/GROUND
**Definition:** Visual perception always separates elements into "figure"
(the subject of attention) and "ground" (the background/context).

**Mechanism:** Contrast, enclosure, and convexity determine which is figure.

**Rules:**
- Smaller area = figure; larger area = ground
- Convex shapes = figure; concave shapes = ground
- Warmer colors advance (become figure); cooler colors recede (become ground)
- Surrounded elements = figure; surrounding elements = ground

**Application:**
- Ensure the primary UI element reads as figure against its background
- Modal overlays use dark ground to make modal content the clear figure
- Negative space logos deliberately make the ground ambiguous (FedEx, Rubin's vase)
- Button design: the button surface must read as figure against the page

**Failure Mode:** Poor figure/ground = ambiguous interfaces where users
cannot identify what is clickable vs. what is background.

---

### Principle 6: COMMON FATE
**Definition:** Elements moving in the same direction at the same speed
are perceived as a unified group.

**Mechanism:** Synchronized motion creates grouping stronger than static proximity.

**Application:**
- Accordion components: expanding items share movement direction
- Scroll-triggered animations: items that scroll-reveal together are grouped
- Parallax layers: elements on the same parallax level are related
- Hover states: sibling cards that lift together communicate categorical equality
- Page transitions: elements that exit together are perceived as one unit

**Critical for Animation:** This is the most powerful grouping principle in
motion design. Use it deliberately to reinforce information architecture.

---

### Principle 7: SYMMETRY AND ORDER (Prägnanz)
**Definition:** The brain interprets ambiguous or complex images in the
simplest, most regular form possible.

**Mechanism:** Cognitive economy — the brain minimizes processing load.

**Application:**
- Icon design: reduce forms to their simplest recognizable essence
- Logo simplification: the fewer anchor points, the more memorable the mark
- Grid layouts: symmetrical layouts convey stability and reliability
- Ambiguous shapes: the simplest interpretation will always dominate

---

### Principle 8: UNIFORM CONNECTEDNESS
**Definition:** Elements visually connected by lines, borders, or shared
containers are perceived as the most strongly related, stronger than proximity
or similarity alone.

**Application:**
- Lines between related data points in a relationship diagram
- Shared card containers group diverse content types
- Underlines and borders to explicitly link label to value
- Table rows are related by the shared horizontal band

---

## 2. ATTENTION SCIENCE AND EYE-TRACKING

### Pre-Attentive Attributes
Pre-attentive processing occurs BEFORE conscious attention — within 200ms.
These attributes are detected in parallel across the entire visual field.

**Pre-attentive attributes (use for hierarchy and emphasis):**

| Attribute     | Example Use                              |
|---------------|------------------------------------------|
| Color (hue)   | Highlight one data point in a chart      |
| Color (value) | Show dark = important, light = secondary |
| Size          | Larger = more important                  |
| Orientation   | Tilted element stands out in a grid      |
| Shape         | Different icon shape = different category|
| Motion        | Moving element captures attention first  |
| Enclosure     | Bordered element reads as selected/active|
| Spatial position | Top-left reads first (Western culture)|

### Eye-Tracking Behavioral Data

**F-Pattern fixation distribution (editorial/content):**
- First horizontal scan: covers full width (100% of elements)
- Second horizontal scan: shorter (60–70% of width)
- Vertical scan: left edge only (10–15% of width)
- Implication: top-left content receives maximum attention

**Z-Pattern fixation distribution (marketing/landing):**
- Primary fixation at top-left (logo, brand)
- Strong saccade to top-right (navigation, social proof)
- Diagonal path through middle
- Final fixation at bottom-right or bottom-center (CTA)

**Above-the-Fold Primacy:**
First 100px of vertical scroll height receives disproportionate attention.
Place: Primary value proposition, trust signals, CTA hint.
NEVER place: Generic stock photography with no information value.

---

## 3. COGNITIVE LOAD THEORY

Cognitive load = the mental effort required to process visual information.
Designers must minimize extraneous cognitive load and maximize germane load.

**Three types of cognitive load:**

| Type         | Definition                              | Design Action                        |
|--------------|-----------------------------------------|--------------------------------------|
| Intrinsic    | Complexity inherent to the content      | Cannot be eliminated — structure it  |
| Extraneous   | Complexity added by poor design         | ELIMINATE — this is design failure   |
| Germane      | Mental effort that builds understanding | MAXIMIZE — this is design success    |

**Extraneous cognitive load killers:**
- Inconsistent visual language (different button styles on same page)
- Redundant information (same content stated twice in different formats)
- Excessive decoration (elements with no information function)
- Ambiguous hierarchy (two elements with equal visual weight competing)
- Unnecessary animation (motion that delivers no information)

---

## 4. HICK'S LAW

**Formula:** RT = b × log₂(n + 1)
Where RT = reaction time, b = empirical constant, n = number of choices.

**Practical Rule:** Decision time increases logarithmically with the number
of choices available.

**Design Implications:**

| Context                | Maximum Choices | Ideal |
|------------------------|-----------------|-------|
| Primary navigation     | 7               | 5     |
| Dropdown menu          | 10              | 7     |
| CTA on a page          | 1               | 1     |
| Onboarding steps shown | 5               | 3     |
| Filter options visible | 8               | 5     |

RULE: One page, one primary CTA. Every additional CTA reduces conversion.
RULE: Progressive disclosure — show only what is necessary for the current
decision. Reveal complexity only when the user requests it.

---

## 5. MILLER'S LAW

**Rule:** Human working memory holds 7 ± 2 chunks of information.
(More recent research by Cowan (2001) suggests the true limit is 4 ± 1.)

**Design Implications:**
- Maximum 7 primary navigation items
- Maximum 7 items in any list before grouping/pagination
- Maximum 4–5 data columns visible in a table without horizontal scroll
- Maximum 5 steps in a visible progress indicator
- Maximum 3–4 pricing tiers before cognitive paralysis

**Chunking Strategy:**
Group information into meaningful units to reduce apparent item count.
9 separate items → 3 groups of 3 items → Perceived as 3 units.

---

## 6. THE SERIAL POSITION EFFECT

**Primacy Effect:** Items at the beginning of a list are most remembered.
**Recency Effect:** Items at the end of a list are second-most remembered.
**Middle items:** Least remembered.

**Application:**
- Place the most important navigation item first or last — never in the middle
- In a feature list, lead with and close with the strongest benefit
- In pricing tables, the plan you want users to select should not be the
  middle option — anchor it with positioning language and visual weight
- CTA copy: most important word first and last

---

## 7. VISUAL ANCHORING AND THE ANCHORING EFFECT

The first visual or numerical value presented becomes the cognitive anchor
against which all subsequent values are judged.

**Application:**
- Pricing: Show the highest price tier first. All others feel affordable.
- Before/after comparisons: The "before" state anchors the viewer's perception
  of the improvement magnitude.
- Typography scale: Display the largest size first in a size-variant showcase.
- Progress indicators: Starting with completion feels faster than starting at 0.

---

## 8. THE VON RESTORFF EFFECT (ISOLATION EFFECT)

**Definition:** An item that differs from its surroundings is more likely
to be remembered.

**Application:**
- Highlight the recommended pricing plan with color, badge, or scale
- Use a single accent color in an otherwise monochromatic layout for the CTA
- Differentiate the primary CTA button from secondary actions by size AND color
- In a data table, use row banding to make anomalous data visible

RULE: The Von Restorff effect requires conformity first.
If EVERYTHING is different, NOTHING stands out.

---

## 9. THE DOHERTY THRESHOLD

**Rule:** System response time under 400ms maintains user flow state.
Above 400ms, the user is aware of waiting and flow is broken.

**Design Implications:**
- Skeleton screens and progressive loading maintain perceived performance
- Optimistic UI (assume success, show result before server confirmation)
  keeps the user in flow
- Micro-animation during load (100–300ms) gives cognitive feedback
- Page transitions under 300ms feel instantaneous

---

## 10. EMOTIONAL RESPONSE AND VISUAL TRUST

### Trust Signals in Visual Design

| Visual Element        | Trust Signal                                   |
|-----------------------|------------------------------------------------|
| High whitespace       | Confidence, premium, not desperate for sales   |
| Consistent type system| Professionalism, attention to detail           |
| Real photography      | Authenticity (stock photography = minus trust) |
| Precise grid alignment| Competence, engineering quality               |
| Generous touch targets| Consideration for user, mobile respect         |
| Fast load performance | Technical reliability                           |
| Accessible design     | Inclusive, ethical, thoughtful brand           |

### The Aesthetic-Usability Effect
Users perceive aesthetically pleasing designs as more usable — even when
they are objectively not. Beautiful design creates positive affect that
extends to perceived functionality.

**Implication:** Aesthetic excellence is NOT vanity — it directly improves
perceived product quality, trust, and conversion.

---

## 11. BIOPHILIC DESIGN PRINCIPLES

Human visual systems evolved in natural environments. Biological preferences:

| Natural Pattern       | Design Application                              |
|-----------------------|-------------------------------------------------|
| Organic curves        | Rounded corners, fluid shapes, wave dividers    |
| Fractal complexity    | Layered textures at multiple scales             |
| Natural color palettes| Earth tones, sky blues, green spectrums         |
| Golden ratio forms    | Proportions found throughout nature             |
| Light and shadow depth| Elevation shadows, light-source consistency     |

Applications in 2026 design: organic blob shapes, natural texture overlays,
earthy color systems, "imperfect" hand-drawn illustration styles.

---

## 12. VISUAL PSYCHOLOGY QC CHECKLIST

Before delivering any design:

- [ ] Primary focal point established via pre-attentive attribute
- [ ] Gestalt principles identified and intentionally applied
- [ ] Cognitive load minimized — zero extraneous elements
- [ ] Reading pattern (Z or F) appropriate and enforced
- [ ] Hick's Law respected — maximum choices per decision point verified
- [ ] Miller's Law respected — information chunked to ≤7 units per level
- [ ] Von Restorff isolation used for primary CTA or key element
- [ ] Serial position effect applied to list/nav ordering
- [ ] Figure/ground relationship unambiguous throughout
- [ ] White space used to create proximity groupings intentionally
- [ ] All motion follows Common Fate for grouped elements

---

*visual_psychology.md | Elite Graphic Design Agent Knowledge Base*
*Last Updated: 2026 | Version 1.0*
