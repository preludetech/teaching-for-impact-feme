---
learning_outcomes:
  - Explain how open licenses enable reuse, adaptation, and sharing
  - Distinguish between different Creative Commons license types and their practical implications
  - Identify the license on a resource and determine what it allows
  - Assess whether resources with different licenses can be combined
guiding_questions:
  - 'What does "open" actually allow you to do with a resource?'
  - How do different licenses affect what you can reuse and adapt?
  - What should you check before combining resources with different licenses?
  - What happens when a resource has no license at all?
---

{% include "lesson_header.md" %}

In the previous lesson, you evaluated resources for fit — alignment, clarity, context, adaptability, accessibility, and licensing. You may have noticed that licensing was the one lens where "it depends" was not a satisfying answer. Either you can modify a resource or you cannot. Either you can share your adapted version or you cannot.

This lesson gives you the understanding you need to answer those questions confidently. It is not about becoming a licensing expert. It is about knowing enough to make practical decisions when you encounter a resource you want to use.

## Why this matters

Access is not the same as permission. A resource being freely available online — downloadable, viewable, shareable by link — does not mean you are allowed to modify it, combine it with other materials, or redistribute your version. By default, copyright reserves all rights to the creator. Unless a license explicitly grants permission, you are limited to reading and personal use.

Open licenses exist to change that default. They are tools that creators use to say, in advance, "here is what you are allowed to do with my work." Understanding how they work lets you move from hoping a resource is usable to *knowing* what you can do with it.

This matters practically. If you plan to adapt a resource (as most people do), you need to know the license allows adaptation. If you plan to combine two resources into a single workshop, you need to know their licenses are compatible. And if you skip this step, you risk either violating someone's license terms or, more commonly, avoiding useful resources out of unnecessary caution.

## How open licenses work

A license is a permission statement attached to a piece of work. It tells anyone who encounters the work what they can and cannot do with it. Most creative work — documents, slides, videos, datasets — is automatically copyrighted the moment it is created. Without a license, the default is "all rights reserved."

Open licenses flip that default. Instead of reserving all rights, they grant specific permissions in advance. The most widely used system of open licenses is **Creative Commons (CC)**, which uses a small set of conditions that combine in predictable ways.

### The four conditions

Creative Commons licenses are built from four elements. Each adds a specific condition to the permission being granted:

**BY (Attribution)** — You must credit the original creator. This appears in every CC license. It ensures that people who share their work openly still receive recognition.

**SA (ShareAlike)** — If you adapt the work, you must release your adaptation under the same (or a compatible) license. This keeps adapted versions open on the same terms as the original.

**NC (NonCommercial)** — You may not use the work for commercial purposes. This is more restrictive than it sounds — "commercial" can include uses within for-profit organisations, even for internal training.

**ND (NoDerivatives)** — You may not modify the work. You can share it as-is, but you cannot create adaptations. For training materials that need localisation or context-specific changes, this is a significant limitation.

### Common license combinations

These four conditions combine into six standard licenses, ranging from most to least open:

**CC BY** — The most permissive. You can reuse, adapt, and share with attribution. This is the license most compatible with open educational practice.

**CC BY-SA** — Same as CC BY, but your adaptations must use the same license. Good for building open ecosystems where adaptations remain open.

**CC BY-NC** — Reuse and adaptation are allowed, but not for commercial purposes. This can create complications if your training is delivered by or within a for-profit organisation.

**CC BY-NC-SA** — Combines non-commercial and share-alike restrictions.

**CC BY-ND** — Reuse is allowed, but no modifications. You can share the original but cannot adapt it. This is problematic for most training contexts where adaptation is the whole point.

**CC BY-NC-ND** — The most restrictive CC license. No modifications, no commercial use. Essentially "free to read and share, nothing else."

![Creative Commons license permissions](../assets/images/lesson-visual-aids/creative-commons.jpg)

*Source: [Creative Commons Licenses](https://foter.com/blog/how-to-attribute-creative-commons-photos/#more-4) by Foter ([CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/))*

!!! tip "Key takeaway"
    For training materials, the most useful licenses are **CC BY** and **CC BY-SA** — they allow the adaptation and resharing that make OER practical. Licenses with ND restrictions prevent adaptation entirely, which limits their usefulness for training design.

## Identifying the license on a resource

Before you can decide what to do with a resource, you need to find its license. This is sometimes straightforward and sometimes frustratingly unclear.

Look in these places:

- **On the resource itself** — a license statement at the bottom of a document, on the first or last slide, or in a footer
- **On the hosting page** — repository metadata, a sidebar, or a "License" section on the download page
- **In a separate file** — on GitHub and similar platforms, look for a `LICENSE` or `LICENSE.md` file in the repository root
- **In the metadata** — Zenodo, OER Commons, and other repositories often include license information in the record metadata

If you cannot find a license statement after checking these places, treat the resource as fully copyrighted. You may still be able to reference it, link to it, or draw inspiration from its approach — but you cannot copy, adapt, or redistribute it.

!!! warning "Ambiguous is not open"
    Phrases like "free to use," "for educational purposes," or "feel free to share" are not licenses. Without a specific license (e.g., CC BY 4.0), you do not have clear legal permission to adapt or redistribute. When in doubt, contact the creator or choose a different resource.

## Checking license compatibility

Combining resources with different licenses is where things get tricky. When you pull together materials from multiple sources — a dataset from one, activities from another, explanatory text from a third — their licenses need to work together.

The core question is: **can the licenses coexist in a single combined work?**

Here are the most common issues:

**ND blocks combination.** If any component has an ND (NoDerivatives) license, you cannot include it in an adapted or combined work. You can only share it separately, unchanged.

**SA requires your output to match.** If you include SA (ShareAlike) material, your combined work must be released under the same (or a compatible) license. This is not necessarily a problem — but it means the SA license effectively sets the license for your final product.

**NC restricts downstream use.** If any component has an NC (NonCommercial) restriction, your combined work inherits that restriction. Anyone who reuses your materials is also bound by the non-commercial condition.

**Multiple SA licenses may conflict.** Two different SA licenses (e.g., CC BY-SA and CC BY-NC-SA) may not be compatible with each other, because each requires the output to carry its specific license.

When you encounter a conflict, you have practical options:

- **Replace the conflicting resource** with one that has a more permissive license
- **Keep resources separate** rather than combining them into a single work — you can link to an ND resource without incorporating it
- **Create your own version** inspired by the approach but not derived from the licensed content
- **Simplify your design** to avoid the combination that creates the conflict

!!! example "Compatibility in practice"
    You are combining a CC BY activity with a CC BY-SA reading. The CC BY material can go into a CC BY-SA combined work (BY is compatible "upward" with BY-SA). Your combined work must be released as CC BY-SA. This is a common and workable combination. But if you also want to add a CC BY-NC resource, you have a conflict: BY-SA and BY-NC-SA are generally not compatible. You would need to replace one resource or keep them as separate materials.

## In practice

👉 Come back to [Activity 14: OER Workflow](../activities/activity_14_oer.md) — check the licensing status of your selected resources

Return to the resources you evaluated in Lesson 2. For each one, identify the license and determine what it allows. Update your decisions in Section 2 if licensing changes what is realistic.

- **what to do:** Identify the license for each resource you selected. Note what is allowed (reuse, adapt, combine, share). Check whether your chosen resources can work together.
- **focus sections:** 1 (Find and Evaluate Resources — licensing fields), 2 (Design Decisions — update if needed)
- **expected output:** Each resource annotated with its license type and what it permits. Updated design decisions where licensing constraints change your plan.
- **approximate time:** 15–20 minutes

## Before you move on

You should now have:

- the license identified for each resource you are working with
- a clear understanding of what each license allows and restricts
- any compatibility issues between resources identified and resolved
- updated design decisions that account for licensing realities

In the next lesson, you will start adapting resources for your context — including how to properly attribute the work you build on.

## Further reading (optional)

- Creative Commons (n.d.) — *About The Licenses*
  → Supports: understanding license types and permissions
  → Why it matters: the authoritative source on how CC licenses work, with clear explanations of each element and combination
  → Source: https://creativecommons.org/licenses/

- Wiley, D. (2014) — *The Access Compromise and the 5th R*
  → Supports: the relationship between licensing and meaningful reuse
  → Why it matters: explains why permission to revise and remix (not just access) is essential for open education
  → Source: https://opencontent.org/blog/archives/3221
