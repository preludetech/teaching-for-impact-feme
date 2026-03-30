We are planning a 4-hour hands-on, collaborative workshop based on **part {{part: 1 or 2}}** of the Teaching for Impact workbook.

## Where to find the content

- **Lessons:** `docs/part-{{part: 1 or 2}}/lesson-*.md` — read all of them
- **Activities:** `docs/activities/activity_*.md` — read the ones referenced by the lessons above
- **Learning outcomes:** in the `learning_outcomes` frontmatter of each lesson file

## Your task

Read all the lessons and activities for part {{part: 1 or 2}}. Then design a **session plan** — not just a list of exercises, but a full workshop arc with an opening, exercises, transitions, breaks, and a closing.

### Step 1: Evaluate each activity

For every activity in this part, assess:

1. **Feasibility** — Can it work live in a room of ~20 researchers/academics who are not trained in pedagogy? Will it feel engaging or contrived?
2. **Prior knowledge needed** — What do learners need to know before attempting it?
3. **Time cost** — How many minutes will it realistically take (including setup, the activity itself, and debrief)?
4. **Outcome alignment** — Which learning outcomes from the lesson frontmatter does it address? Can we meet outcomes at a lighter depth (e.g. "discuss" instead of "apply")?
5. **Overlaps** — Do multiple activities hit the same outcomes? Flag these as alternatives so the user can choose.

### Step 2: Recommend a session plan with alternatives

Present **all viable exercises** (not just your top picks). Group them into:

- **Recommended:** Your suggested lineup that fits ~3 hours of content. Aim for **4–6 exercises**.
- **Alternatives:** Exercises that could swap in for a recommended one. For each alternative, state which recommended exercise it could replace and the tradeoff (e.g. "Exercise B is more hands-on but takes 10 min longer than Exercise A; both cover Outcome X").
- **Cut:** Exercises that don't work for a live workshop at all, with a one-line reason.

The user will make the final selection. Your job is to make the tradeoffs clear so they can decide confidently.

### Step 3: Design the session flow

Arrange the **recommended** exercises into a session timeline (the user may swap in alternatives before running the build-slides command). The timeline should include:

- **Opening (10–15 min):** A warm-up that connects participants' existing expertise to the workshop topic. Not a lecture — something interactive.
- **Exercises with context:** Each exercise needs ~5 min of framing/instruction before it and brief debrief time after.
- **A break:** Place it roughly at the midpoint. Specify when and how long (15–20 min).
- **Energy pacing:** Alternate between high-energy activities (group discussion, movement) and lower-energy ones (individual reflection, pair work). Don't front-load all the high-energy work.
- **Closing (10–15 min):** A reflection activity where participants identify what they'll do differently or what they want to explore further. This is critical for the "build curiosity" goal.

### Step 3: Tag for time pressure

Mark each exercise as **core** (must happen) or **stretch** (can be cleanly dropped if running behind). At least 2 exercises should be stretch.

## Workshop constraints

- **Remote, minimal tools.** The workshop runs on a video call with breakout rooms — no shared canvas, whiteboard, or collaborative doc. Design exercises that work with conversation and screen-sharing only.
- **Team-based participants.** Learners join as teams, each developing their own training on a different topic. This is a strength — they have a real project to apply ideas to immediately.
- **Grouping flexibility.** Some exercises benefit from **cross-team mixing** (fresh perspectives, seeing how others approach the same problem). Others work best when teams **stay together** (applying ideas to their own training). For each exercise, specify the recommended grouping and why.

## Design principles

- **Go broad, build curiosity.** The goal is familiarity, not mastery — we want participants to keep learning on their own afterwards.
- **Keep it active.** Prefer pair/group discussion, short hands-on tasks, and think-pair-share over passive instruction. All activities must work in breakout rooms with conversation only — no tools beyond what participants can say or screen-share.
- **Be ruthless with time.** 4 hours including breaks means ~3 hours of real content. Every exercise must earn its slot.
- **Budget for instruction and Q&A.** Exercises don't exist in a vacuum — learners need context before each activity and time to ask questions. Factor in ~5 minutes of framing/instruction before each exercise and leave buffer for organic discussion.

## Output

Save the session plan to `presentations/part-{{part: 1 or 2}}-session-exercises.md`.

At the top, include a summary:
- Total session time for the recommended lineup (should add up to ~4 hours including breaks)
- Number of exercises: recommended (core vs stretch) and how many alternatives are available
- An **outcome coverage map** — list each learning outcome and which exercises (recommended + alternatives) address it, so the user can see at a glance what's covered and where they have choices
- Any outcomes that are NOT covered by any viable exercise, with a note on why that's acceptable

Then a **timeline** showing the full session flow with times:

```
## Timeline

| Time        | Duration | What                          | Type       |
|-------------|----------|-------------------------------|------------|
| 0:00–0:15   | 15 min   | Welcome + warm-up             | Opening    |
| 0:15–0:20   | 5 min    | Context for Exercise 1        | Framing    |
| 0:20–0:40   | 20 min   | Exercise 1: [Name]            | Core       |
| ...         | ...      | ...                           | ...        |
| 3:45–4:00   | 15 min   | Closing reflection            | Closing    |
```

Then **three sections** with exercise details:

### Recommended exercises

```
### Exercise N: [Name] — [core/stretch]

**Original activity:** [reference to the workbook activity, e.g. Activity 3: Learner Map]
**Grouping:** [Own team / Cross-team mix / Individual → share] — [one-line reason for this grouping]
**Adapted instructions:** [what learners will actually do in the workshop — must work in breakout rooms with conversation only]
**Time:** [minutes, broken down: setup / activity / debrief]
**Reason for inclusion:** [why this exercise earns its slot]
**Outcomes addressed:** [specific outcomes from the lesson frontmatter]
**If cut:** [what happens to outcome coverage — only needed for stretch exercises]
```

### Alternative exercises

For each alternative, use:

```
### Alternative: [Name]

**Original activity:** [reference]
**Could replace:** Exercise N ([Name])
**Grouping:** [Own team / Cross-team mix / Individual → share] — [one-line reason]
**Tradeoff:** [what you gain vs. what you lose by swapping — be specific about outcomes, time, energy level, engagement style]
**Adapted instructions:** [what learners would do — must work in breakout rooms with conversation only]
**Time:** [minutes]
**Outcomes addressed:** [specific outcomes]
```

### Cut exercises

A table of exercises that don't work for this format:

```
| Activity | Reason for cutting |
|----------|--------------------|
| ...      | ...                |
```

**Stop here and wait for the user to review and edit the file before continuing.**
