# Design review: Prompt Master inspiration -> mux-brief

## Verified upstream shape

At the time of inspection (14 October 2026), `nidhinjs/prompt-master` is a Claude skill whose root contains `LICENSE`, `README.md`, `SKILL.md`, and `references/` with `templates.md` and `patterns.md`. Its LICENSE is MIT, copyright 2026 Nidhin Joseph Nelson.

The README describes tool/model targeting for many AI services, nine dimensions of prompt intent, optional clarifying questions, 13 template categories, pattern-based prompt repair, session-context carry-forward, and attempts to minimize unnecessary output. Its skill provides a large number of tool-specific text instructions, including model/version suggestions that may change over time.

## What the new design preserves as *ideas*, not copied text

- Intentional instructions are more useful than vague requests.
- Different downstream tasks need different brief formats.
- A generated prompt should be aware of scope, verification, and missing context.
- Additional detailed guidance should be available when needed, rather than loaded unconditionally.

These are general design concepts. The implementation, labels, instructions, examples, and tests in this starter were newly written.

## Primary design changes

| Dimension | Prompt Master approach (per inspected repo) | mux-brief starter |
| --- | --- | --- |
| Use case | Wide assortment of AI model/tool profiles | Terminal coding agents and engineering/cloud work first |
| Core metaphor | Prompt engineering templates and diagnostic patterns | Small, reviewable instruction contracts |
| Model versions | Large embedded provider/model profile library | Portable targets; verify capabilities when relevant |
| Memory | Include salient prior-session context | Include only user-supplied or verified project state |
| Automation | Prompt drafting in skill | Prompt drafting plus opt-in, offline JSON formatter |
| Infrastructure writes | Agentic guardrails | Distinct observe/propose/apply intent, explicit approval gates |
| Token cost | Trim verbose instructions | Minimize always-loaded content and measure full workflow outcomes |
| Packaging | Single Claude skill repository | Standards-format skill + distributable marketplace plugin |
| Evaluation | Prompt quality logic | Unit tests, structural checks, written A/B benchmark plan |

## Security posture

This is a *drafting* skill: no Azure/AWS permissions, ServiceNow/Atlassian tokens, MCP connections, GitHub credentials, or script execution authority are given to downstream agents by this package. The optional Python formatter only loads JSON and renders text. Its secret detection is intentionally limited and must not be represented as a security boundary.

## Licensing choice

`mux-brief` has its own MIT LICENSE because it consists of newly authored content. Its provenance file credits the source of the idea without claiming to incorporate the upstream work. If upstream wording/templates/code are later copied, include the source copyright and MIT permission text in distributed copies or substantial portions, and document the reused material. Cosmetic changes are not a route around attribution obligations.

This is a practical engineering overview, not legal advice.

## Next increments

- Define supported 'read-only' CLI envelopes by tool without assuming all vendors expose the same flags.
- Add acceptance examples for Jira Data Center and governance-sensitive AWS GovCloud/Azure Government operations.
- Add policy-driven environment aliases stored outside the skill and free of secrets.
- Run benchmark scenarios across Claude Code, Copilot CLI, and Codex with reported provider usage numbers.
- Add an optional validated JSON schema output and publishing pipeline for your private marketplace.
