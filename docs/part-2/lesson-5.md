---
learning_outcomes:
  - Identify when creating OER from scratch is the right choice
  - Design materials that are structured for openness and adaptability from the start
  - Write instructions and activities that work for audiences you cannot see
  - Build accessibility into materials by design rather than as an afterthought
guiding_questions:
  - When is creation the right choice over reuse or adaptation?
  - How does creating for reuse differ from creating for yourself?
  - What makes materials easy for others to adapt?
  - How do you write for learners you will never meet?
---

{% include "lesson_header.md" %}

Sometimes the right resource does not exist. You have searched, evaluated, and checked licenses — and nothing fits. Perhaps you work in a niche domain where open training materials are scarce. Perhaps you need materials in a language that is underrepresented in OER repositories. Perhaps your training approach is novel enough that existing resources would need more reworking than building fresh.

In these situations, creation is not a fallback — it is the right choice. But creating materials that will be open, reusable, and adaptable requires thinking differently from creating materials just for your next workshop.

## Why this matters

Most training materials are created for a single delivery: this workshop, this group, this week. That is a natural starting point, but it means the materials often depend on your presence, your context, and your tacit knowledge to work. They are functional notes, not standalone resources.

Creating for openness means designing materials that can work beyond your immediate delivery — materials that a colleague in a different country could pick up, understand, adapt, and use effectively. This is a higher bar than "good enough for me," but it does not mean perfection. It means being deliberate about structure, clarity, and the assumptions you build in.

This matters especially for the audience of this workbook. If you are a researcher or practitioner in a field where OER is scarce — particularly in the Global South, in indigenous knowledge systems, in emerging technical domains, or in languages other than English — you are not just creating materials for yourself. You are potentially filling a gap that affects everyone who comes after you. The choices you make about structure and openness determine whether your work can serve as a foundation others build on or remains locked to your specific use.

## When to create from scratch

Creation makes sense when:

- **Nothing suitable exists** — you have searched and evaluated, and no existing resource covers what you need
- **The gap is too large to bridge through adaptation** — an existing resource would need to be so heavily modified that starting fresh is more efficient
- **Your context is underrepresented** — the training you need reflects a setting, language, discipline, or learner population that is not well-served by existing OER
- **Your approach is novel** — you are teaching something new, or teaching something familiar in a way that does not have established open materials

The decision to create should come *after* evaluating what exists (Lesson 2), not before. Even when you create from scratch, existing resources can inform your approach — you might borrow a structure from one, a question format from another, and an assessment approach from a third, without reusing any content directly.

## Designing for openness from the start

The difference between "creating materials" and "creating open materials" comes down to a set of design choices you make from the beginning, not features you add at the end.

### Make your structure modular

A monolithic resource — a single 50-page document or a tightly sequenced set of activities that only work together — is hard for others to adapt. They may need only one section, or they may need to rearrange the sequence for their context.

Design in modules: self-contained sections that make sense individually as well as in sequence. Each module should have its own clear purpose, stated outcomes, and necessary context. A facilitator should be able to use Module 3 without having delivered Modules 1 and 2 — or at least understand what prerequisite knowledge they need to provide.

This does not mean every module must be completely independent. It means the dependencies are *stated*, not *hidden*. A note at the top — "This activity assumes learners have completed a basic analysis of their dataset, or have equivalent experience" — lets someone adapt around the dependency rather than being surprised by it.

!!! example "Modular vs. monolithic"
    A 4-hour workshop on data management could be structured as a single flow that only works in sequence, or as four 1-hour modules: (1) Planning data collection, (2) Organising files and naming conventions, (3) Data cleaning basics, (4) Documentation and metadata. Each module has stated outcomes and prerequisites. A facilitator who only has 2 hours could use modules 2 and 3. Someone with learners who already manage their files well could skip module 2. The same content, structured for flexibility.

### Use replaceable examples

Examples are one of the hardest elements to transfer across contexts. A case study about water quality monitoring in rural Kenya is powerful for learners in East Africa — and potentially irrelevant to learners working on urban public health in Brazil.

When you create examples, build in replaceability:

- **State the purpose of the example** explicitly. If a case study is meant to illustrate how conflicting stakeholder interests complicate data collection, say so. This helps someone replacing your example choose one that serves the same purpose.
- **Provide the example alongside a prompt** for adaptation. A note like *"This example uses water quality data from Kenya. If your learners work in a different domain, substitute a dataset and scenario from their context that involves conflicting priorities"* makes adaptation straightforward.
- **Separate examples from the teaching structure.** If possible, keep examples in distinct sections or files rather than weaving them so deeply into the explanation that replacing them requires rewriting the teaching content.

### Make assumptions explicit

Every resource carries assumptions. When you create from scratch, you have the opportunity to make them visible from the start — rather than leaving them for someone else to discover.

It's useful to state:

- **What learners need to know** — prior knowledge, skills, or concepts
- **What learners need to have** — tools, software, connectivity, physical materials
- **What context is assumed** — institutional setting, cultural context, language level, time available

These are not limitations to apologise for. They are design parameters that help others judge fit and plan adaptations. The more explicit your assumptions, the easier it is for someone in a different context to adapt your materials rather than starting over.

### Write for people you will never meet

When you create materials for your own delivery, you write shorthand — you know what you mean, and you can fill in gaps during facilitation. When you create for openness, the materials must speak for themselves.

This means writing instructions that are complete enough to follow without you in the room. Not just "discuss in pairs" but "in pairs, take 5 minutes each to describe your data collection process to your partner. The listener should identify one assumption the speaker is making about their data. Switch roles and repeat." The instruction should tell the reader what to do, how to do it, how long it takes, and what the expected output is.

It also means avoiding insider references. Terms, acronyms, and cultural references that are obvious to you may be opaque to someone in a different field or region. Define terms when you first use them. Spell out acronyms. When you use a culturally specific example, provide enough context that someone unfamiliar with that setting can still understand the point.

!!! question "The stranger test"
    Read through your materials and imagine a competent colleague in a different country, working in a related but not identical field, who has never met you. Can they understand what to do? Can they see why each activity matters? Can they adapt the materials for their context without guessing at your intentions?

## Building in accessibility from the start

Creating from scratch is an opportunity to build accessibility in from the beginning — not as a retrofit, but as a design principle.

**Structure your documents with headings.** Use proper heading hierarchy (H1, H2, H3) rather than bold text styled to look like headings. This supports screen readers and makes documents navigable on all devices.

**Describe your images.** Every image, diagram, and chart should have alt text that conveys the information the image communicates — not just "diagram of data flow" but "diagram showing data flowing from three collection points through a central cleaning process to two output databases." If an image is purely decorative, it does not need alt text.

**Design for variable bandwidth.** If your materials will be used in low-bandwidth settings, avoid embedding large media files. Offer text alternatives to video content. Keep file sizes manageable. Consider whether your materials can be used offline.

**Write clearly.** Simple, direct language is the most universally accessible design choice. Short sentences, active voice, common vocabulary, and defined technical terms make materials usable for learners working in a second language, learners with cognitive disabilities, and — frankly — everyone.

**Offer multiple formats when possible.** If you create a set of slides, also provide a text version. If you produce a complex table, offer a simplified version alongside it. Multiple entry points mean more learners can engage with your content.

## Connecting back to Part 1

The work you did in Part 1 is the foundation for everything you create here. Your learning outcomes define what the materials need to achieve. Your learner analysis tells you who you are designing for and what constraints they face. Your activity designs provide the structure that your new materials bring to life.

If you are creating from scratch, revisit your Part 1 outputs:

- Do your **learning outcomes** still hold? If you have refined them through the process of evaluating and adapting resources, update them now.
- Does your **learner analysis** account for the broader audience your materials might reach? The "learner" is no longer just your immediate participants — it includes facilitators and learners in other contexts.
- Do your **activity designs** translate into written form? An activity that works when you facilitate it may need significant restructuring to work on paper or screen.

## In practice

👉 Use [Activity 14: OER Workflow](../activities/activity_14_oer.md) — document what you are creating and why

Return to Sections 2 and 3. In Section 2, document what you are creating from scratch and why creation was the right choice (rather than reuse or adaptation). In Section 3, if your new materials draw on or are inspired by existing resources, document that relationship.

- **what to do:** Document your creation decisions — what you are building, why existing resources were not suitable, and how your design supports reuse by others
- **focus sections:** 2 (Design Decisions — creation rationale), 3 (Adaptation and Localisation Log — if building on existing approaches)
- **expected output:** Clear documentation of what you are creating and the design choices that support openness and adaptability
- **approximate time:** 20–30 minutes

---

👉 Come back to [Activity 8: Learning Activity Design](../activities/activity_8_activity_design.md)

- **what to do:** Take one activity you are creating from scratch and write it as a standalone resource — complete instructions, stated assumptions, replaceable examples, and clear expected outputs. Test it against the "stranger test": could a colleague in a different context understand and use it?
- **expected output:** One complete, standalone activity designed for openness and reuse
- **approximate time:** 15–20 minutes

## Before you move on

You should now have:

- at least one resource or activity created from scratch with openness in mind
- modular structure with stated dependencies between sections
- explicit assumptions documented for each piece of content
- instructions complete enough to follow without facilitation
- accessibility built in (headings, alt text, clear language, manageable file sizes)

In the next lesson, you will prepare all your materials — adapted and created — for sharing and publication.

## Further reading (optional)

- Bali, M., Cronin, C., & Jhangiani, R. S. (2020) — *Framing open educational practices from a social justice perspective*
  → Supports: understanding why creation is necessary in underrepresented contexts
  → Why it matters: argues that OER creation — not just adoption — is essential for equitable representation in educational materials
  → Source: https://doi.org/10.1007/s11423-020-09752-2

- UNESCO (2019) — *Recommendation on Open Educational Resources*
  → Supports: principles for creating accessible, inclusive open materials
  → Why it matters: defines international standards for OER creation that prioritise access, equity, and quality
  → Source: https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer

- Ossiansson, E. (2018) — *OER awareness and use: The affinity between higher education and K-12*
  → Supports: OER creation practices and design for reuse
  → Why it matters: provides evidence on how OER creators can design materials that are actually adopted and adapted by others
  → Source: https://doi.org/10.19173/irrodl.v19i2.3431
