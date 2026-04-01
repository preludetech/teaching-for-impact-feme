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
5. **For each exercise in order:**
   - **Context slide(s)** — just enough theory for learners to do the activity. Pull key concepts from the lesson files. Keep these minimal: a key idea, a diagram prompt, or a short quote. Do not reproduce full lesson content.
   - **Transition** — if moving to a new topic group, add one slide that connects the previous topic to the next (e.g. "We've identified who our learners are — now let's look at how they actually learn")
   - **Exercise slide(s)** — clear heading (e.g. "Exercise 3: Learner Personas"), brief instructions (what to do, how long, group size), and any prompts or discussion questions
6. **Break slide** — "Break — back at [time]" (use speaker notes to remind facilitator to state the actual time)
7. **Closing slide(s)** — reflection activity from the session plan, key takeaways, pointer to the full workbook for continued learning
8. **Thank-you slide** — with link back to the workbook

## Slide design rules

1. **Use the existing CSS classes** (`.highlight-box`, `.accent`, `.subtitle`) — do not add new styles
2. **One idea per slide.** If a bullet list has more than 6 items, split it across slides
3. **Keep text short.** Slides are prompts, not scripts. If you're writing a paragraph, rewrite it as 2–3 bullet points
4. **Use Reveal.js fragments sparingly** — only for bullet lists where sequential reveal genuinely helps (e.g. discussion prompts). Do not fragment every list

## Facilitator notes

Include `<aside class="notes">...</aside>` on every exercise slide and context slide. Notes should cover:

- **Timing cues** — "This exercise should take 15 min. If running long, cut debrief to 3 min."
- **Setup instructions** — "Ask participants to form groups of 3–4"
- **Debrief prompts** — "Ask 2–3 groups to share. Listen for..."
- **Expected responses** — what "success" looks like so the facilitator knows the exercise landed
- **Cut strategy** — for stretch exercises, note "This can be skipped if behind schedule. If cutting, briefly mention [key point] verbally instead."

## Constraints

- Aim for roughly **40–60 slides total** (about 1 slide per 3–4 minutes of content)
- Do not invent content — all theory must come from the lesson files
- Mark stretch exercises clearly in speaker notes so the facilitator can skip them smoothly
