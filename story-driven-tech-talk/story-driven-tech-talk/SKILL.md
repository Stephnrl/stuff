---
name: story-driven-tech-talk
description: Turn a technical tool or workflow into a story-driven talk: hook-first deck, per-slide talk track, word-for-word practice script and a 5-minute cut. Use for tech talks, demos and leadership presentations.
---

# Story-driven technical talk

Builds a presentation that hooks the audience with a real story before explaining anything technical, then gives the presenter everything they need to deliver it: the deck, speaker notes, Notepad-style notes, a full practice script, and a short cut.

Use it when someone wants to present a tool, workflow or technical idea (to a team, leadership, or as a recorded episode) and wants people to care, not just understand.

## What to produce

1. **The deck.** Use the Slides artifact type when it's available, otherwise a .pptx. About 12 slides.
2. **Speaker notes** on every slide, written as talking points (format below).
3. **Notepad notes:** a plain-text file, one short numbered block per slide, to keep beside the screen.
4. **A word-for-word practice script:** 13 to 15 minutes, for rehearsing out loud.
5. **On request:** a 5-minute cut, a demo plan, and recording adjustments.

Send the text files as files. Don't paste long scripts into the reply.

## Step 1: Gather the story first

The story is the content, so get it before building anything. Ask for:

- **One real ticket or task** that shows the problem. The best ones have small technical work but slow approvals or handoffs between teams.
- **The before numbers:** how long it took end to end, and how many rounds of review.
- **The after numbers:** the same measures with the new approach.
- **A second proof point**, ideally a different kind of win (for example, faster testing rather than faster approval).
- **Credibility:** what the presenter does day to day, told as part of the story, not as a resume.
- **A personal moment:** something they wish they'd known, or a mistake they made.
- **The audience,** whether it's live or recorded, whether it's part of a series, and the exact name of the tool.

Rules for numbers:
- Never invent a statistic. Use a bracketed placeholder like `[__ days]` and list every placeholder in the reply.
- Compare like with like. If "before" is end to end including waiting, "after" must be too, or label each one honestly (for example, "~1 day of work").
- If a real ticket isn't available, a hypothetical is fine, as long as the presenter says so out loud.

## Step 2: The story arc

Story first, then hook, then an overview (not an agenda), then the technical content. Use this 12-slide arc and adapt the names:

1. **Cover = the hook.** The title is the outcome ("One request. Zero revisions."). A panel shows before vs. after numbers, with the before crossed out.
2. **The ticket.** The everyday task and the painful usual loop, as 3 or 4 steps. End on a teaser: "This time it was approved on the first try." The overview line goes in this slide's notes.
3. **The real problem.** One clear statement ("The work isn't slow. The handoffs are."), the before numbers shown big, and one credibility line.
4. **The journey.** Two things that didn't work (one of them a mistake the presenter owns), then the thing that worked.
5. **Concept primer.** One slide only. Save the deep how-to for a later episode and say so.
6. **The key idea, problem first.** Open with what goes wrong without it, then give one memorable line to repeat.
7. **The mechanism.** How the pieces fit together, with an analogy ("the job description plus the toolbox for one hire").
8. **The team or roster.** What exists today, and what each one is for.
9. **Replay the same ticket** with the new approach. Show the before numbers crossed out above the after numbers. This is the climax.
10. **Second proof point**, with the same before/after treatment.
11. **Trust and guardrails.** Short. Point at two items and let people read the rest.
12. **What changes.** Four outcomes, then the hand-off line to the demo, plus a footer teasing the next episode.

The framing matters:
- Repeat the key numbers on the problem slide and the replay slide. Repetition is what makes them stick.
- When agents or tools stand in for other teams, frame them as "the first pass before the real review," never as replacing those teams. Show that people still approve.
- Save the skill-building, how-to or deep technical slides for Episode 2. Episode 1 is the why.

## Step 3: Design in the Slate & Amber style

Use the Slate & Amber style unless the user asks for another. The template's 12 slides follow the same order as the arc in Step 2, so slide N of the arc uses template slide N (1 Cover, 2 Steps, 3 Big numbers, 4 Journey, 5 Code panel, 6 Dark comparison, 7 Config panel, 8 Card grid, 9 Replay, 10 Second proof, 11 Icon grid, 12 Closer).

**Where to find it:**
- **In Claude, with the Slides artifact type:** build the deck from the Slides type and use the "Slate & Amber" design system (list the Design System artifacts to find it). Copy each slide's layout from the "Slate & Amber: Talk Template" deck (list the Slides artifacts, or ask for its link), replacing the bracketed text.
- **As files (Claude Code, mux.snc, or when a .pptx is asked for):** start from `assets/Slate-and-Amber-Template.pptx` in this skill's folder. It has 5 layouts (SA Cover, SA Dark, SA Dark Edge, SA Light, SA Light Alt) and 12 example slides with usage notes. Copy the example slide for each arc slide, replace the bracketed text, and delete the examples you don't use. Colors, type and spacing are in `assets/tokens.json`; the full style guide is `references/slate-and-amber.md`.
- **Neither available:** follow the rules below with these values: slate `#0F1A24`, paper `#F4F2EC` and `#E9E5DA`, amber `#9A5B0E` on light and `#E8A33D` on dark, blue `#2A64A8` on light and `#7FB2EA` on dark; IBM Plex Sans for text, JetBrains Mono for labels and code.

The PowerPoint file needs IBM Plex Sans and JetBrains Mono installed (free from Google Fonts), or PowerPoint substitutes other fonts. Mention this when you hand over a .pptx.

**The rules behind the style:**
- **Palette:** one dark tone, one light tone, a second light tone for variety, and 1 or 2 accents. No pure white or black.
- **Dark slides** for the cover, the key-idea slide, the replay (climax) and the closer. Don't run more than about 5 light slides in a row. If the user deletes slides, check the balance again.
- **One idea per slide.** Prefer card rows, big numbers (about 120px) and short statements over bullet lists.
- **"Before" values:** muted and crossed out. **"After" values:** in the accent color.
- **Headings** sit in the same place on every slide, and the eyebrow label goes above them in a monospace face.
- **Re-read the deck before editing,** because the user may have changed slides. Look for stray elements left by accidental clicks.

## Step 4: Speaker notes format

Write talking points, not a script:

```
SAY: the opening line for this slide
STORY / EXAMPLE / POINT: the one thing to point at or tell
BRIDGE: one sentence that leads into the next slide
```

Mark exactly three lines to memorize: the opening, the key line, and the hand-off to the demo. Mark fill-ins as `[ ]`.

## Step 5: Practice materials

- **Notepad notes:** plain text in numbered blocks. Mark lines to memorize with `*`, fill-ins with `[ ]`, and bridges with `>`. End with a clear cue such as `>>> SWITCH TO THE TERMINAL <<<`.
- **Full script:** word for word, with `(pause)` and `(point at ...)` cues. Advise reading it out loud 2 or 3 times, then switching to the Notepad notes and saying it in their own words. Suggest recording one run and listening back.
- **Pacing:** about 1 to 2 minutes per slide. Concept slides take longer; slides with a strong visual go fast.

## Step 6: Variants

**Recorded rather than live:**
- Add a 15-second intro on the cover: name, role, "Episode N of a series," this episode is the why, the next one is the how.
- Replace "live" with "let me show you."
- End with "Drop your questions in [channel]" instead of "Questions?"
- The demo can take several takes, and the waits can be edited out.

**5-minute cut:**
- Same slides, about 500 spoken words, with a time target for each slide.
- Keep the hook, every number, the key line and the "doesn't replace teams" framing.
- Cut the bridges and the demo, and point to the full episode at the end.
- Count the spoken words to check the length.

**Screen sharing in Teams:** recommend PowerPoint Live (attendees see only the slides; the presenter keeps their notes) or sharing a single window. Warn that sharing a whole ultrawide screen shows everything and shrinks the text for viewers.

## Demo plan

Replay the opening story with a sanitized sample (made-up app, bucket and account names; nothing real on screen). For example, hand an overly broad policy to the specialist and let viewers watch it narrow the permissions and write the justification. Optionally, hand the result to a second specialist to show the handoff between teams. Before demoing, enlarge the terminal font and keep the window roughly 16:9.

## Worked example

An IAM role request that usually took 2 to 3 weeks and 3 rounds with security was done in about 1 day of work, with 0 revisions, using a security-engineer agent persona. The second proof point: testing Bottlerocket with FIPS on EKS went from weeks to about 2 days. The key line was "Skills say how. A persona says who." Episode 2 was set up as building your own skills.
