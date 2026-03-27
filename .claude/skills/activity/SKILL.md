---
description: Use this skill when creating or editing activity files. Activity files are named `activity_{n}_{name}.md`
---

Use the voice-and-tone skill when writing activity content.

# Principles

- **Artefacts, not thoughts.** Every activity must produce a concrete, reusable output — a table, a map, a plan, a set of decisions. If the reader finishes with only reflections and no artefact, the activity has failed.
- **Context-grounded.** Activities exist in real-world settings with constraints. Push the reader to confront their actual context, not an idealised one.
- **Connected, not standalone.** Activities form a design system. Each one should use outputs from earlier activities and produce outputs that feed later ones. The reader should feel cumulative progress, not isolated exercises.
- **Actionable prompts.** Every prompt should drive toward a specific output. If it can be answered with "yes" or "no", it needs a follow-up that produces something concrete.
- **Structure serves the activity.** Organise each activity however best serves its purpose. Some need tables, some need step-by-step progressions, some need checklists. Do not force a uniform structure across activities that do fundamentally different things.

# Audience

Activities are for educated professionals who are designing training but are not trained in pedagogy. They are capable readers but may be encountering instructional design concepts for the first time.

Do NOT oversimplify or assume low literacy. DO provide enough scaffolding that someone can complete the activity without a facilitator.

# Activity Anatomy

## Required elements

Every activity must begin with frontmatter and the header include. Beyond that, include whatever sections the activity needs — no more, no fewer.

### 1. Frontmatter

```yaml
---
used_in:
  - "Part X — [Lesson N: Title](../part-x/lesson-n.md#in-practice)"
what_to_do: "Clear action statement"
expected_output: "What the reader will have when done"
approximate_time: "15–30 minutes"
---
```

### 2. Header include

```
{% include "activity_header.md" %}
```

This provides the standard introduction, download button, and metadata display. 

### 3. Instructions

A short orientation: what this activity does and why. 1–3 sentences. Do not re-explain the lesson concepts — the reader just came from the lesson.

### 4. Core task

This is the main work of the activity. Structure it however serves the content best:

- A list of questions to answer
- A structured table to fill in
- A step-by-step diagnostic (diagnose → improve)
- A mapping exercise
- A set of structured prompts with labelled fields
- A comparison (intended vs actual, before vs after)

The core task must produce a **concrete artefact** — something the reader can review, revise, and reference later.

## Sections to include when they serve the activity

These are not mandatory. Include them when they add value; omit them when they would be forced or redundant. Each one has a specific purpose — if you include it, make sure it does its job.

### You will use

References specific outputs from earlier activities that the reader needs as inputs. Include this when the activity genuinely builds on prior work.

Rules:
- Only reference activities that come BEFORE this one in the sequence
- Name the specific output, not just the activity (e.g., "1 learner constraint from [Activity 3: Learner Reality Mapping](../activities/activity_3_learner_reality.md)" not "from Activity 3")
- At least one step in the core task must require the reader to actually use that output — don't list dependencies then ignore them

Activity 1 has no prior activities. That's fine — omit this section.

### Dual-path structure (existing vs new training)

When useful, offer two paths:

**"If you already have a training"** — diagnose what exists, then improve it. This is the stronger path because the reader has material to work with.

**"If you are creating a new training"** — provide at least 2–3 concrete, scaffolded prompts. These readers have less experience to draw on and need MORE guidance, not less. Never reduce this to "do the same as above" or a single sentence.

Not every activity needs this split. Some work the same way regardless. Use judgement.

### Translation to your learners

Pushes the reader to adapt their work to their learners' real context. Include when there's a genuine gap between "what I designed" and "what my learners actually need."

This section asks: *How does this apply to your learners' context? What needs to change?*

### Context check

Forces confrontation with constraints — time, resources, infrastructure, culture, power. Include when the activity's output could be unrealistic without a reality check.

This section asks: *What constraints affect feasibility? What is outside your control?*

### Reflection

A closing prompt that asks the reader to step back and synthesise. 1–2 questions maximum. This should be the last substantive section the reader engages with — place it before any forward-looking reference sections.

This section asks: *What shifted in your thinking? What will you change?*

**Critical rule:** Reflection must NOT restate Translation or Context Check questions. If you could move the question to one of those sections and it would still make sense, rewrite it. Reflection is about metacognition — what changed, what surprised you, what you'll do differently.

### Reuse in later sections

Points forward to activities that will use this activity's output. Include when the dependency is real and the reader benefits from knowing what's coming. This is a reference section, not active work — it always comes after Reflection.

Rules:
- Only reference activities that come AFTER this one
- Use correct activity numbers, titles, and file paths
- Never leave as `[TODO]` — either fill it in or omit the section

### Iteration

Signals that this is a living document. Include when the activity will genuinely be revisited — i.e., when a later lesson or activity will prompt the reader to return and update.

When included, go beyond the generic `v0/v1/v2` boilerplate. Name the specific trigger: "After completing Activity 9, return here and check whether your feedback plan still aligns with this activity."

# Activity Reference

The latest list of activities can be found in ./docs/activities. Treat the actual files and names as the source of truth

**Cross-reference accuracy is a common source of errors.** When editing an activity, verify that every reference uses the correct number, name, and file path from this table. Past errors include referring to "Activity 2" when meaning Activity 3 (Learner Reality), and mislabelling activities (e.g., calling Activity 8 "Evaluation Plan" when it is "Learning Activity Design").

# Formatting

- `##` for primary body sections, `###` for subsections 
- Avoid tables — they render poorly in the docx export. Prefer lists with labelled fields or structured prompts instead. Only use a table when the content genuinely requires a grid (e.g., a multi-column comparison that would be unreadable as a list)
- Use labelled fields (e.g., `- Title:`, `- Key outcomes:`) for fill-in-the-blank outputs
- Use `---` horizontal rules to separate major sections visually
- Straight quotes in all MkDocs/Jinja syntax

# Quality Checklist

Before finishing an activity, verify:

- [ ] Produces a concrete, reusable artefact — not just reflections
- [ ] Can be completed without a facilitator
- [ ] Every prompt drives toward a specific output (no yes/no dead ends)
- [ ] All cross-references use correct activity numbers, titles, and file paths (check the reference table)
- [ ] "You will use" only references earlier activities; "Reuse in later sections" only references later ones
- [ ] No `[TODO]` placeholders remain
- [ ] No section appears more than once
- [ ] No two sections ask the same question in different words
- [ ] If dual-path is used, the "new training" path has real scaffolding (2–3 prompts minimum)
- [ ] Structure serves THIS activity — not copied from a template
- [ ] Headings use `##` for primary body sections, `###` for subsections
