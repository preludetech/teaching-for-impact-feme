# Workbook Style + Design Specification (v2)  
Teaching for Impact: Designing Effective & Open Training

---

# 1. Purpose of this Specification

This document defines the structural, stylistic, and pedagogical rules for all sections in the workbook.

It ensures:
- consistency across sections  
- alignment with how the lessons are actually structured and used  
- usability in real-world, resource-constrained contexts  
- compatibility with Material for MkDocs  

This version reflects **observed implementation patterns in lessons**, not only intended design.

---

# 2. Core Design Principles

## 2.1 Design for action, not reading
Content must:
- support decisions  
- lead to outputs  
- enable immediate application  

Avoid:
- passive explanation without use  

---

## 2.2 Context-first design
All sections must connect to:
- learner realities  
- constraints  
- real-world application  

---

## 2.3 Learning through doing
Learning is driven by:
- activities  
- practice  
- feedback  
- iteration  

Content supports these — it does not lead.

---

## 2.4 Progressive layering
Each section:
- introduces a concept once  
- deepens it later  
- avoids repetition  

---

## 2.5 Reuse and adaptability
Content must:
- be understandable without facilitation  
- be reusable across contexts  
- model good OER practices  

---

# 3. Standard Section Structure (MANDATORY)

Each section MUST follow this structure:

---

## [Section Title]

### Learning Outcomes + Guiding Questions

- Use a **2-column markdown table**
- Left = Learning Outcomes (HTML unordered list)
- Right = Guiding Questions (HTML unordered list)

---

## Why this matters

Must include:
- reference to previous section  
- clear problem framing  
- explanation of why this section matters in practice  

Must include:

!!! quote "This section helps you move from..."
    *“Before”*  
    to:  
    *“After”*

---

## Core concepts

- 3–5 concepts maximum  

Each concept:

!!! abstract "Concept name"
    Clear, concise definition

Followed by:
- short explanation  
- why it matters  

Concepts must:
- introduce terminology once  
- be reused later without redefining  

---

## Practical guidance

Must be structured as **step-based guidance**:

### Step 1 — ...
### Step 2 — ...
### Step 3 — ...

Each step:
- action-oriented  
- concise  
- directly usable  

---

### Decision point (EMBEDDED, NOT A SEPARATE SECTION)

Decision points must:

- appear within Practical guidance  
- be formatted as:

> How much / what / which choice should you make?

Followed by:
- 2–3 realistic options  

Must:
- influence downstream design decisions  
- not be abstract or rhetorical  

---

## Example (REQUIRED)

Must follow exact structure:

- **Context:**  
- **Decision:**  
- **Action:**  
- **Outcome:**  

Requirements:
- realistic scenario  
- shows decision-making  
- shows consequences  

---

## In practice

This section is **expanded and iterative (CRITICAL UPDATE)**

Must:

- include at least ONE template  
- may include MULTIPLE templates  
- may include revisiting previous templates  

---

### Format

👉 Use [Template X: Name](link)

Include:

- **what to do:** clear action  
- **expected output:** concrete deliverable  
- **approximate time:** realistic estimate  

---

### Optional second block

👉 Revisit [Template Y: Name](link)

Include:
- refinement, iteration, or improvement task  

---

### Suggested process (OPTIONAL but encouraged)

Used when:
- deeper thinking is required  
- multiple steps are involved  

Structure:

**Step 1 — ...**  
**Step 2 — ...**  
**Step 3 — ...**

---

## Key takeaways

Strict rules:

- Maximum 2 takeaways  
- Use !!! tip  

Example:

!!! tip "Key takeaway"
    Insight

---

## Before you move on

CRITICAL FUNCTION:

This is NOT a summary.

It must:
- validate outputs  
- confirm readiness to proceed  

Format:

You should now have:

- concrete output  
- concrete output  
- concrete output  

---

## Further reading (optional)

Must:
- appear at end  
- follow strict format  

See Section 13.

---

# 4. Formatting Rules (Material for MkDocs)

## 4.1 Admonitions

Allowed:
- !!! tip  
- !!! abstract  
- !!! quote  

Avoid:
- warning (only if absolutely necessary)

---

## 4.2 Admonition limits

Per section:

- max 4 total  
- max 2 tips  
- max 2 abstracts  
- max 1 quote  

---

## 4.3 Tables

- Use simple markdown tables  
- No nested formatting  
- HTML lists allowed inside cells  

---

## 4.4 Lists

- short  
- parallel  
- scannable  

---

## 4.5 Headings

Use consistent hierarchy:

- ## main sections  
- ### steps  

---

# 5. Language and Tone

## 5.1 Tone

- clear  
- direct  
- professional  
- practical  

---

## 5.2 Sentence structure

- short to medium  
- avoid complexity  

---

## 5.3 Terminology

- define once  
- reuse consistently  

---

## 5.4 Clarity rule

If it requires explanation during facilitation → rewrite it.

---

# 6. Pedagogical Requirements (UPDATED)

## 6.1 One example (mandatory)

Must:
- include decision + consequence  

---

## 6.2 Decision-making is embedded

Decision points:
- occur in Practical guidance  
- are not standalone sections  

---

## 6.3 Strong section linking

Each section must:

At start:
> In the previous section, you...

Implicitly or explicitly.

---

## 6.4 Template integration

Each section must:

- include at least one template  
- define output  
- define action  

---

## 6.5 Iteration across sections (NEW RULE)

Templates must:

- be revisited across lessons  
- support refinement, not one-off completion  

---

## 6.6 Output-driven closure

Each section must end with:

You should now have:

- outputs (not ideas)  

---

# 7. Use of Examples

## Requirements

Each example must:

- reflect real-world constraints  
- show a decision  
- show an outcome  

---

## Running case

A consistent scenario should:

- evolve across sections  
- show cumulative design  

---

# 8. Activity and Template Integration (UPDATED)

## 8.1 Templates are iterative

Templates are not one-time tasks.

They must:

- evolve across sections  
- support refinement  

---

## 8.2 Multi-template use allowed

“In practice” can include:

- primary task  
- refinement task  

---

## 8.3 Alignment rule

Templates must:

- directly support section outcomes  
- not introduce unrelated work  

---

# 9. Managing Cognitive Load

## 9.1 Chunking

- small sections  
- clear headings  

---

## 9.2 Avoid overload

Do not:

- introduce too many concepts  
- mix abstraction + application without structure  

---

## 9.3 Layering

Order:

1. concept  
2. guidance  
3. example  
4. practice  

---

# 10. OER Integration Rules

## 10.1 Build progressively

Do not:
- repeat OER concepts unnecessarily  

---

## 10.2 Focus on decisions

Include:
- reuse vs adapt vs create  

---

## 10.3 Practical implications

Must include:
- real constraints  
- usability considerations  

---

# 11. Flow Between Sections (UPDATED)

## Start of section

Must:
- reference previous section  
- position current section  

---

## End of section

“Before you move on” must:
- confirm outputs  
- prepare for next step implicitly  

---

# 12. Quality Control Checklist

## Content
- [ ] leads to action  
- [ ] supports outcomes  
- [ ] includes example  

## Structure
- [ ] follows section structure  
- [ ] includes all required sections  

## Formatting
- [ ] adheres to MkDocs rules  
- [ ] clean markdown  

## Pedagogy
- [ ] includes practice  
- [ ] produces outputs  
- [ ] supports iteration  

## Clarity
- [ ] no ambiguity  
- [ ] no facilitation dependency  

---

# 13. Further Reading (STRICT FORMAT)

Each reference must follow:

- Author (Year) — *Title*  
  → Supports: concept  
  → Why it matters: 1 sentence  
  → Source: URL  

Rules:
- 2–4 references  
- directly tied to section  
- no generic sources  

---

# 14. Key Changes from v1

This version corrects:

- ❌ overly rigid structure → ✅ flexible but consistent implementation  
- ❌ missing iteration → ✅ explicit iterative template design  
- ❌ isolated decision points → ✅ embedded decision-making  
- ❌ minimal In practice → ✅ expanded, multi-step, iterative  
- ❌ summary endings → ✅ output validation endings  
- ❌ theoretical bias → ✅ action-first structure  

---

# 15. Versioning

- Version: v2  
- Status: Updated based on implemented lessons  
- Alignment: Lessons 2, 3, 4, 7  

---

# End of Specification