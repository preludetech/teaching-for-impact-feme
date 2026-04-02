The user has finalised the workshop exercise plan in `presentations/part-{{part: 1 or 2}}-session-exercises.md`. Now build the presentation slides.

## Your task

1. Read `presentations/part-{{part: 1 or 2}}-session-exercises.md` for the session plan
2. Read the relevant lesson files in `docs/part-{{part: 1 or 2}}/lesson-*.md` to source context/theory for slides
3. Read `presentations/base.html` for the HTML template structure
4. Generate the slides in `presentations/part-{{part: 1 or 2}}.html`, **replacing all existing slide content** inside `{% block slides %}`

Use the voice-and-tone skill when writing slide text.

## Slide structure

The file extends `base.html` using Jinja blocks. Only write content inside `{% block title %}` and `{% block slides %}`. Use nested `<section>` tags: outer `<section>` = lesson/topic group, inner `<section>` = individual slide.

## Required slides (in order)

1. **Title slide** — workshop title and subtitle
2. **Agenda slide** — overview of the session with timings so participants can see the shape of the day
3. **Housekeeping slide** — break time, wifi, etc. (use `<aside class="notes">` to remind the facilitator to fill in venue-specific details)
4. **Warm-up slide(s)** — instructions for the opening activity from the session plan
5. **For each concept in order:**
   - **Context slide(s)** — just enough theory for learners to do the activity. Pull key concepts from the lesson files. Keep these minimal: a key idea, a diagram prompt, or a short quote. Do not reproduce full lesson content.
   - **Transition** — if moving to a new topic group, add one slide that connects the previous topic to the next (e.g. "We've identified who our learners are — now let's look at how they actually learn")
   - **Exercise slide(s)** — clear heading (e.g. "Exercise 3: Learner Personas"), instructions (what to do, how long, group size), and any prompts or discussion questions. An exercise may span multiple slides if it has distinct phases (e.g. one slide for the breakout task, another for the debrief). **Each phase's slide must be fully self-contained** — participants need all the information for that phase visible on the current slide without flipping back. Never split a single phase's instructions across multiple slides; tighten the wording instead.
6. **Break slide** — "Break — back at [time]" (use speaker notes to remind facilitator to state the actual time)
7. **Closing slide(s)** — reflection activity from the session plan, key takeaways, pointer to the full workbook for continued learning
8. **Thank-you slide** — with link back to the workbook

## Slide design rules

1. **Use the existing CSS classes** (`.highlight-box`, `.accent`) — do not add new styles
2. **One idea per slide.** If a bullet list has more than 6 items, split it across slides. 
3. **Keep text short.** Slides are prompts, not scripts. If you're writing a paragraph, rewrite it as 2–3 bullet points
4. **Default to Reveal.js fragments on bullet lists** — progressive reveal keeps learners focused on the speaker. Only show all bullets at once when learners need to reference the full list simultaneously (e.g. exercise instructions, resource links)

## Facilitator notes

Include `<aside class="notes">...</aside>` on every exercise slide and context slide. Notes should cover:

- **Timing cues** — every slide or short group of slides should state how long it should take (e.g. "~3 min", "~5 min"). For exercise slides, include the total exercise time and a suggestion if running long (e.g. "This exercise should take 15 min. If running long, cut debrief to 3 min.")
- **Setup instructions** — "Ask participants to form groups of 3–4"
- **Debrief prompts** — "Ask 2–3 groups to share. Listen for..."
- **Expected responses** — what "success" looks like so the facilitator knows the exercise landed
- **Cut strategy** — for stretch exercises, note "This can be skipped if behind schedule. If cutting, briefly mention [key point] verbally instead."

## Images

Lesson files may contain images (e.g. `![alt text](../images/foo.png)`). When you encounter an image that illustrates a concept being presented:

- Include it on the relevant context slide using an `<img>` tag with an appropriate `alt` attribute
- Use the path as-is from the lesson file — the presentation's `<base>` or relative path will resolve it. The presentations are served from the `presentations/` directory, so adjust the relative path accordingly (e.g. `../docs/part-1/images/foo.png` or similar)
- Don't force every image onto slides — only use images that genuinely aid understanding at presentation pace
- If an image is too detailed for a slide (e.g. a dense table or lengthy diagram), mention it in speaker notes instead and point learners to the workbook

## Mermaid diagrams

Lesson files may contain Mermaid code blocks (` ```mermaid `). When you encounter a diagram that illustrates a concept being presented:

- Include it on the relevant context slide using a `<div class="mermaid">` wrapper with the raw Mermaid syntax inside (no code fences)
- Apply the same judgment as images — only include diagrams that genuinely aid understanding at presentation pace
- If a diagram is too complex for a slide, mention it in speaker notes and point learners to the workbook

Example:

```html
<div class="mermaid">
flowchart LR
  A[Inputs] --> B[Activities] --> C[Outputs] --> D[Outcomes] --> E[Impact]
</div>
```

## Constraints

- Aim for roughly **40–60 slides total** (about 1 slide per 3–4 minutes of content)
- Do not invent content — all theory must come from the lesson files
- Mark stretch exercises clearly in speaker notes so the facilitator can skip them smoothly
