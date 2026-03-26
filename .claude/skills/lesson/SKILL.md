---
description: Use this skill when creating or editing lesson files. Lesson files are named `lesson-{n}.md`
---

Use the voice-and-tone skill when writing learning content.

# Principles

- **Design for action.** Every section must lead to a decision, an output, or immediate application. No passive explanation without use.
- **Context-first.** Connect all content to learner realities, constraints, and real-world application.
- **Progressive layering.** Introduce a concept once, deepen it later, avoid repetition.
- **Standalone.** Content must be understandable without facilitation and reusable across contexts.
- **Make it engaging.** Include explanations where useful. Vary structure and rhetorical approach across lessons so no two feel identical.
- **Check your facts.** Do not assume existing content is correct. When in doubt, use a research sub-agent to verify. Store research output as markdown files in the `research/` directory.

# Writing Style

The voice-and-tone skill governs all prose. One rule deserves extra emphasis here because lessons have historically over-relied on lists:

**Default to prose. Use bullets only for genuinely parallel items.** A bullet list is right for a set of tools, a list of options, or enumerable requirements. It is wrong for ideas that build on each other, have causal relationships, or need explanation. If a bullet needs a sub-explanation, that is a paragraph.

# Lesson Anatomy

## Required elements

These must appear in every lesson. Their order is fixed as listed below, but the **body** section has full structural flexibility.

### 1. Frontmatter

```yaml
---
learning_outcomes:
  - outcome 1
  - outcome 2
guiding_questions:
  - question 1
  - question 2
---
```

### 2. Opening (no heading)

Orient the reader: what this lesson does, and how it connects to what came before. Vary the device across lessons — a question, a direct statement, a short scenario, a `!!! quote` admonition. Do not use the same opening pattern in every lesson.

### 3. Why this matters

Frame the problem or need this lesson addresses. This can be a standalone `## Why this matters` section or woven into the opening if that reads more naturally.

### 4. Body

This is the main teaching content. Organise it however serves the material best. You might:

- Lead with a method, then explain the concept behind it
- Open with an example, then draw out principles
- Interleave concepts and practical guidance rather than separating them
- Use a single extended walkthrough instead of separate "concepts" and "steps" sections

By the end of the body, the reader must understand the key ideas AND have actionable methods they can apply. Beyond that, structure is yours to decide. Use `##` for major sections and `###` for subsections within them.

A standalone "Core concepts" section with `!!! abstract` admonitions is permitted but not required. Concepts can also be introduced inline within the body.

### 5. In practice

This section sends the reader away to do an activity, then brings them back. Frame it as an action to take, not a template to fill in. The reader should feel like they're applying what they just learned, not completing a form.

```
👉 [Activity X: Name](../activities/activity_x.md) — one-line description of what they'll do and why
```

When an activity builds on earlier work, include metadata:

```
👉 Come back to [Activity Y: Name](../activities/activity_y.md)

**what to do:** clear action

```

At least one activity per lesson. Multiple activities and returning to earlier ones is encouraged. Activities should support refinement across lessons, not one-off completion.

### 6. Before you move on

This is output validation, not a summary. Format:

```
You should now have:

- concrete output
- concrete output
- concrete output
```

## Optional elements

- **Key takeaways** — max 2, using `!!! tip "Key takeaway"`. Include when the lesson's core insight benefits from being stated memorably. Omit when the takeaway is self-evident.
- **Further reading** — 2–4 references at the end, directly tied to the lesson. No generic sources. Strict format:

```
- Author (Year) — *Title*
  → Supports: concept
  → Why it matters: 1 sentence
  → Source: URL
```

# Teaching Methods, Not Checklists

When the body explains how to do something, give the reader a **method** — a way of thinking or working they can follow. Do not just list considerations.

**Weak (tells what, not how):**

> Step 1 — Map your system. Identify: who is involved, what resources exist, what constraints matter.

**Strong (gives a method):**

> Start by placing your training at the centre of a simple diagram. Around it, add every person, organisation, or resource that affects whether it succeeds. Draw lines to show relationships. Look for clusters — where several actors depend on the same resource, or where one person sits between two groups. These are the pressure points your design needs to account for.

**Vary the format.** A process might need 2 steps or 7. It might not be steps at all — it could be a set of questions to work through, a comparison table, a decision tree, or a worked example the reader adapts. Choose whatever teaches most effectively.

**Decision points are optional.** Include one when a genuine fork exists with real downstream consequences. Do not fabricate a 3-tier choice (minimal / moderate / strong) where the answer is obvious. When you do include a decision point, show what changes based on the choice.

# Examples

Examples are teaching tools, not illustrations tacked on at the end. Place them wherever they do the most good — at the start of a section, in the middle of an explanation, or as a capstone.

**At least one substantial example per lesson.** "Substantial" means it teaches something the reader could not grasp from explanation alone. It must reflect real-world constraints, show a decision, and show its consequences.

**Vary the format across lessons:**

- A short narrative (2–3 paragraphs telling a real-world story)
- A before/after comparison
- A worked example showing a method applied step by step
- A decision walkthrough showing how someone reasoned through a choice
- A "what went wrong" case that teaches through failure
- A comparison table

**Running scenario.** Where it helps continuity, build on a consistent scenario across lessons so the reader sees cumulative design decisions. This is encouraged but not required.

# Cross-referencing Other Lessons

Reference other lessons organically in the body text when concepts genuinely connect. Both forward and backward references help the reader see the workbook as a coherent journey:

- "You'll apply this Theory of Change again when you design assessment in Lesson 8."
- "This builds on the learner analysis from Lesson 2 — if your map has changed, update it now."

Don't force references where they don't serve the reader.

# Formatting (Material for MkDocs)

**Straight quotes only in MkDocs syntax.** Admonition titles, Jinja `{% include %}` tags, and any other MkDocs/template syntax must use straight double quotes (`"`, U+0022), never directional/curly quotes (`"` `"`, U+201C/U+201D). Curly quotes silently break rendering. Curly quotes are fine in body prose — this rule applies only to syntax.

**Admonitions** — use these to break up the flow of content and draw attention to specific kinds of information. Each type has a distinct purpose:

- `!!! abstract "Title"` — **Key concept or definition.** Use when introducing a core idea that the reader needs to hold onto. Good for the one-sentence version of a concept before the fuller explanation.
- `!!! tip "Title"` — **Practical advice or takeaway.** Use for actionable guidance the reader can apply directly. Good for methods, rules of thumb, or "here's what this means for your design."
- `!!! quote "Title"` — **Perspective shift or reframing.** Use to highlight a change in thinking — a before/after mindset, or a provocation that challenges assumptions.
- `!!! question "Title"` — **Reflective prompt.** Use to pause the reader and ask them to think about their own context before continuing. Good at transition points between ideas.
- `!!! warning "Title"` — **Common pitfall or mistake.** Use to flag something that frequently goes wrong or a trap the reader might fall into. Effective because it speaks to real experience.
- `!!! example "Title"` — **Illustrative scenario.** Use for brief, inline examples that support a point without needing a full standalone example section.

Per section: max 4 admonitions total. Don't stack them back-to-back — they should be separated by prose. The point is to punctuate the content, not replace it.

**Tables** — simple markdown tables, no nested formatting. HTML lists inside cells are allowed.

**Lists** — short, parallel, scannable. Only for genuinely enumerable items.

**Headings** — `##` for major sections, `###` for subsections. Do not skip levels.

**Diagrams** — use Mermaid for flowcharts, process diagrams, and similar visuals. Wrap in a fenced code block with the `mermaid` language identifier. Keep diagrams simple and readable — they should clarify, not replace, the surrounding prose.

**Design comments** — use HTML comments (`<!-- ... -->`) to explain non-obvious design decisions to other instructional designers working on the project. These are invisible to readers but help collaborators understand *why* something was structured a particular way. Use sparingly — only when the reasoning wouldn't be obvious from the content itself.

# Quality Checklist

Before finishing a lesson, verify:

- [ ] Body teaches methods (how), not just considerations (what)
- [ ] Prose is used where ideas connect; bullets only for parallel items
- [ ] At least one example that teaches, not just illustrates
- [ ] Cross-references to other lessons are organic, not forced
- [ ] Structure serves THIS content — not copied from another lesson
- [ ] "In practice" links to at least one template with clear action
- [ ] "Before you move on" lists concrete outputs, not vague ideas
- [ ] Content leads to action and supports stated learning outcomes
- [ ] Clean markdown, correct MkDocs admonition syntax
- [ ] Facts and claims have been verified where uncertain
