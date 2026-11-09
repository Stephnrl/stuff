# Slate & Amber

A presentation style for story-driven technical talks: deep slate and warm paper, with amber for the moments that matter. It was first used in “A Team of Agents: Episode 1” and works for any talk that leads with a real story and real numbers.

## Voice

The slides tell a story before they explain anything.

- **Titles state the point**, not the topic: “The work isn’t slow. The handoffs are.”, not “Process overview”.
- **Numbers are real** or left in brackets (`[__ weeks]`) until they are. A before and an after measure the same thing.
- **One idea per slide.** Cards, big numbers and short statements, not bullet lists.
- **Plain words.** Short sentences, no exclamation marks, no emoji. Technical names go in mono.
- **Typographic punctuation**: ’ and “ ” in everything people read; straight quotes only in code.

## Visual foundations

**Canvas.** 1920×1080, with `slide-margin` (128px) on every side, so content sits in 1664×824. A slide with a footer pins it `footer-offset` (64px) from the bottom and grows its bottom padding to 160px.

**Two themes, one per slide.** Every slide is either light (`surface` is paper) or dark (`surface` is slate). Light slides carry the story; dark slides mark four moments:

1. the cover,
2. the turning point (the key idea),
3. the climax (the before/after replay),
4. the closer.

Don’t run more than about five light slides in a row. Use `surface-alt` (a second paper tone) for primers, proof points and guardrails, so a light run still has rhythm.

**Color.**
- `ink` for headings, `ink-muted` for body text.
- `accent` (amber) for eyebrows, big numbers, after values, arrows and the one highlighted card’s 2px border.
- `info` (blue) for step numbers, item names, icons and code keys.
- `inverse` for the single dark card on a light slide: the thing that worked, or what’s next.
- Code panels are always dark (`code-bg`), with `code-key`, `code-text` and `code-comment`.
- The cover, climax and closer carry a 24px `amber-500` stripe on the left edge (`edge-stripe`).

**Type.** IBM Plex Sans for everything people read, JetBrains Mono for anything technical: eyebrows, step numbers, item names and code. Five sizes do all the work: 120 (display and big numbers), 72 (slide titles), 44 (statements), 32 (card titles), 28 (body), plus 24 for labels. Nothing smaller than 24px. Every slide title sits at the top margin, under an uppercase mono eyebrow in `accent` with 4px letter-spacing, so headings never move between slides.

**Before and after.** The before value is `ink-struck` with a line through it, smaller or above; the after value is `accent` at 120px. Always label both in words (“Before”, “With my agents”). Color and strikethrough never carry the meaning alone.

**Cards.** `card` fill, 1px `line` border (`line-strong` on `surface-alt`), `radius-card` (16px) corners and `space-lg` (32px) padding. One card per row may be the hero, with a 2px `accent` border. Cards in a row are equal width with `space-lg` gaps; grids use `space-md`.

**Arrows.** Solid block arrows in `accent` between steps, about 2:1.

## Iconography

Line icons in `info` at 40px, one per guardrail or feature card, never decorative. They always sit above a title that says the same thing in words.

## Layouts

The template deck “Slate & Amber: Talk Template” has all twelve layouts with placeholder text and notes on when to use each:

| Layout | Theme | Use it for |
| --- | --- | --- |
| Cover with before/after hook | dark | Opening: the outcome as the title, the numbers as the hook |
| Process in steps | light | The usual painful loop, with the worst step outlined |
| Big numbers and causes | light | The problem in numbers, plus your credibility line |
| Three attempts | light | The journey, owning a mistake; what worked on an inverse card |
| Code panel and points | light, alt | A one-slide concept primer |
| Dark comparison | dark | The turning point and the memorable line |
| Config panel and legend | light | How the pieces fit together |
| Card grid | light | A roster, with one hero card and a “what’s next” card |
| Replay with before/after | dark | The climax: the same story with the new approach |
| Before → after and checklist | light, alt | A second proof point |
| Icon grid | light, alt | Trust and guardrails |
| Closer | dark | Four outcomes and the hand-off |

## Don’ts

- No gradients, drop shadows, photos of people or stock imagery.
- No left-border accent cards; the highlight is a full 2px border.
- No pure white or black; use the paper and slate tones.
- No more than one hero card or one big-number pair per slide.
