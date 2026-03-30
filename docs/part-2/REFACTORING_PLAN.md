# Part 2 Refactoring Plan

## Why this refactoring is needed

A close reading of Part 2 reveals structural overlap between Lessons 1 and 2, content gaps (no lesson on creating OER from scratch, no guidance on accessibility), and repetitive further-reading citations. Some lessons also try to cover too many concerns at once — for example, Lesson 3 covers licenses, Creative Commons elements, license compatibility, choosing a license, AND attribution.

The goal: each lesson gets a clear, focused purpose; overlap is eliminated; and identified gaps are filled.

---

## Problems

### 1. Lessons 1 and 2 overlap significantly

Both lessons cover the "reuse, adapt, create" decision framework:

- Lesson 1 outcome: "Decide when to reuse, adapt, or create resources"
- Lesson 2 outcome: "Make explicit decisions to reuse, adapt, or create resources"

Both reference Activity 14 section 2 (Design Decisions) and Activity 8. Lesson 1's "hidden assumptions" concept and Lesson 2's "contextual assumptions" concept cover the same ground under different labels.

A reader finishing Lesson 1 and starting Lesson 2 encounters the same decisions, concerns, and activities — Lesson 2 feels repetitive rather than progressive.

### 2. Some lessons bundle too many concerns

Lesson 3 covers licenses, Creative Commons elements, license compatibility, choosing a license for your own materials, AND attribution. These are related but serve different moments in the workflow — understanding licenses (when evaluating), attributing (when adapting), and choosing a license (when sharing). Bundling them forces readers to learn everything before they need it.

### 3. No lesson on creating OER from scratch

The "reuse, adapt, create" framework is central to Part 2, but only reuse and adaptation get dedicated lessons. Readers who need to create original materials — especially those working in niche domains, underrepresented languages, or emerging fields — get no guidance on:

- How to structure materials for openness from the start
- How to write instructions and activities that are context-portable
- How to build in adaptability by design (modular structure, replaceable examples, explicit assumptions)
- How "creating for openness" differs from just "creating materials"

Activity 14 section 2 asks readers to document what they will "create from scratch" but no lesson supports that decision.

### 4. No guidance on accessibility

There is no mention of making materials usable across devices, bandwidth levels, disabilities, or varying digital literacy. For a workbook about creating open and reusable educational resources, this is a notable omission — especially given the target audience of practitioners in resource-constrained settings.

### 5. Further reading is repetitive

Wiley (2014) appears in 5 of 6 lessons. UNESCO (2019) appears in all 6. The lesson skill spec says "2–4 references at the end, directly tied to the lesson. No generic sources." Each lesson should have references specific to its content.

---

## What does NOT need to change

- **Lessons 5 and 6 (publishing vs. sustaining) are genuinely distinct** — they should not be combined.
- **The overall Part 2 narrative arc is sound** — the progression from "design for openness" through "find, evaluate, license, adapt, share, sustain" is logical and well-scaffolded.
- **Activity 14 as a through-line** works well — each lesson focuses on specific sections, building up a complete OER workflow.

---

## Proposed new structure: 7 lessons + closing

### New Lesson 1: Designing for Openness

**Source:** Current Lesson 1, tightened with overlap removed

**Covers:** Openness as a design choice, the reuse/adapt/create framework (introduced, not practiced in detail), what makes materials reusable, hidden assumptions.

**Changes:**

- Remove the detailed reuse/adapt/create decision walkthrough (current Step 2) — this duplicates Lesson 2
- Remove Activity 14 section 2 reference — better placed in Lesson 2 where readers actively make those decisions
- Remove Activity 8 revisit — better placed after adaptation (Lesson 4) or creation (Lesson 5)
- Keep core framing, Steps 1/3/4/5, and Activity 14 section 0 (Context)

**Activities:** Activity 14 (section 0)

---

### New Lesson 2: Finding and Evaluating OER

**Source:** Current Lesson 2, absorbing reuse/adapt/create detail from current Lesson 1

**Covers:** Where to find OER, evaluating OER (six lenses — alignment, clarity, context fit, adaptability, accessibility, licensing), contextual assumptions, making practical reuse/adapt/create decisions.

**Changes:**

- Absorb the reuse/adapt/create decision-making detail from current Lesson 1
- Add accessibility as a sixth evaluation lens: "Can your learners actually access and use this material?"
- Simplify the licensing evaluation to a quick filter (detailed licensing is in Lesson 3)

**Activities:** Activity 14 (sections 1, 2), Activity 8

---

### New Lesson 3: Understanding Open Licenses

**Source:** Current Lesson 3, narrowed

**Covers:** What licenses are, open licenses vs. default copyright, Creative Commons elements (BY, SA, NC, ND) and common combinations, identifying licenses, license compatibility basics.

**Changes:**

- Remove "Choose a license for your materials" (current Step 4) — moves to Lesson 6 (Sharing) where the action happens
- Remove attribution section (current Step 5) — moves to Lesson 4 (Adaptation) where readers are working with others' materials
- Simplify license compatibility section

**Activities:** Activity 14 (sections 1, 2)

---

### New Lesson 4: Adapting, Remixing, and Localising OER

**Source:** Current Lesson 4, with attribution absorbed from current Lesson 3

**Covers:** Adaptation as expected practice, levels of adaptation (surface/structural/contextual), localisation, accessibility as adaptation, design trade-offs, attribution, documenting changes.

**Changes:**

- Absorb attribution from current Lesson 3 — this is where readers actually need to attribute
- Add accessibility as a dimension of adaptation (alt text, simplified language, alternative formats, offline usability)
- Consolidate Steps 1+2 (identify assumptions + identify what doesn't fit) into one step
- Consolidate Steps 5+6 (document + check coherence) into one step

**Activities:** Activity 14 (section 3), Activity 8

---

### New Lesson 5: Creating OER from Scratch (NEW)

**Source:** New content

**Covers:**

- When creation is the right choice (nothing suitable exists, niche domain, underrepresented language)
- Designing for openness from the start — how creating-for-reuse differs from creating-for-yourself
- Structuring materials for adaptability: modular design, replaceable examples, explicit assumptions
- Writing for audiences you cannot see
- Accessibility by design
- Connecting back to Part 1: learning outcomes, learner analysis, and activity design provide the foundation

**Why this lesson is needed:** The workbook's own audience — researchers and practitioners in resource-constrained environments — is precisely the group most likely to need to create OER from scratch. The current structure acknowledges "create" as an option but never teaches it.

**Why it goes here:** Creation sits alongside adaptation as a path to having materials ready to share. Both paths converge at Lesson 6 (Sharing).

**Activities:** Activity 14 (sections 2, 3), Activity 8

---

### New Lesson 6: Sharing and Publishing OER

**Source:** Current Lesson 5, with license-choice absorbed from current Lesson 3

**Covers:** When materials are ready to share, choosing a license for your materials, documentation, accessible formats and platforms, platform choice, discoverability.

**Changes:**

- Absorb license-choice from current Lesson 3 — readers choose their license when preparing to share, not when learning what licenses mean
- Add accessibility guidance for publishing (formats and platforms that support access)
- Combine "improve clarity" with "check readiness" — these are the same activity

**Activities:** Activity 14 (section 4), Activity 9

---

### New Lesson 7: Sustaining and Improving OER

**Source:** Current Lesson 6, tightened

**Covers:** OER lifecycle, sustainability as realistic maintenance, collecting meaningful feedback, making targeted improvements, versioning and transparency, when to retire materials.

**Changes:**

- Consolidate Steps 1+3 (identify use patterns + decide maintenance level)
- Consolidate Steps 4+5 (make improvements + track changes)

**Activities:** Activity 14 (section 5)

---

### Part 2 Closing (NEW)

**Source:** New content, modelled on `docs/part-1/closing.md`

A short closing page that helps readers review their complete OER workflow, check coherence across decisions, and identify next steps. Not a numbered lesson.

**Activities:** Activity 14 (full review)

---

## Summary of changes

| Current | Action | New |
|---|---|---|
| L1: Designing for Openness | Remove overlap with L2 | New L1 |
| L2: Finding and Evaluating OER | Absorb reuse/adapt/create detail from L1, add accessibility lens | New L2 |
| L3: What Makes Resources Open? | Narrow: understanding licenses only; attribution → L4, license choice → L6 | New L3 |
| L4: Adapting and Localising | Absorb attribution from L3, add accessibility, consolidate steps | New L4 |
| *(gap)* | New lesson on creating OER from scratch | New L5 |
| L5: Sharing and Publishing | Absorb license choice from L3, add accessibility | New L6 |
| L6: Sustaining and Improving | Consolidate steps | New L7 |
| *(none)* | New closing page | closing.md |

**Net result:** 6 lessons become 7 more focused lessons plus a closing page.

---

## Accessibility integration plan

Accessibility is woven throughout rather than isolated in a standalone lesson:

| Lesson | Accessibility content | How it fits |
|---|---|---|
| L2 (Find/Evaluate) | Sixth evaluation lens: format, bandwidth, devices, assistive tech, language | Natural extension of existing 5-lens framework |
| L4 (Adapt) | Adaptation dimension: alt text, simplified language, alternative formats, offline usability | Fits within "levels of adaptation" |
| L5 (Create) | Design-from-start principle: building in accessibility from the beginning | Core to "how creating for openness differs" |
| L6 (Share/Publish) | Platform and format choices: HTML over PDF, structured headings, accessible documents | Natural extension of platform choice guidance |

---

## Activity 14 changes needed

- Section 1: Expand accessibility prompt to include bandwidth, device, and assistive technology considerations
- Section 2/3: Add creation-focused prompt: "What did you create from scratch? Why was creation the right choice?"
- Update `used_in` frontmatter to match new lesson numbers and titles

---

## Further reading deduplication

Each lesson should have 2–4 references specific to its content. Proposed assignments:

- Wiley (2014) — Lessons 1, 2, 3 only
- UNESCO (2019) — Lessons 1, 6 only
- Hodgkinson-Williams & Trotter (2018) — Lessons 2, 4 only
- Creative Commons (n.d.) — Lesson 3 only
- Hilton (2016) — Lesson 2 only
- Atenas & Havemann (2014) — Lesson 6 only
- Wiley & Hilton (2018) — Lesson 7 only
- Atenas, Havemann & Timmermann (2020) — Lesson 7 only
- New references needed for Lesson 5 (creating OER) and for accessibility content

---

## Other files to update

- `docs/part-2/index.md` — update lesson list to 7 entries plus closing
- `mkdocs.yml` — update Part 2 nav section
- `docs/activities/activity_14_oer.md` — expand prompts, update frontmatter
- All Part 2 lesson cross-references — update to new numbering

---

## Implementation instructions

Work through the lessons in order. For each lesson file:

1. **Use the `/lesson` skill** — this ensures the lesson conforms to the expected structure, voice, and formatting
2. **Use the `/voice-and-tone` skill** — apply the workbook's writing style to all content
3. After all lessons are complete, update `index.md`, `mkdocs.yml`, and Activity 14

### Step-by-step

1. Rewrite `lesson-1.md` using `/lesson` — tighten, remove overlap with L2
2. Rewrite `lesson-2.md` using `/lesson` — absorb detail from old L1, add accessibility lens
3. Rewrite `lesson-3.md` using `/lesson` — narrow to understanding licenses only
4. Rewrite `lesson-4.md` using `/lesson` — absorb attribution, add accessibility, tighten
5. Create new `lesson-5.md` using `/lesson` — Creating OER from Scratch
6. Rename current `lesson-5.md` to `lesson-6.md`, then rewrite using `/lesson` — absorb license choice, add accessibility
7. Rename current `lesson-6.md` to `lesson-7.md`, then rewrite using `/lesson` — tighten
8. Create `closing.md`
9. Update `docs/activities/activity_14_oer.md`
10. Update `docs/part-2/index.md`
11. Update `mkdocs.yml`
12. Verify all cross-references
