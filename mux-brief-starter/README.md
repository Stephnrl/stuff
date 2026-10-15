# mux-brief starter

Original, lightweight prompt-briefing skill for terminal agents. It can run as a standalone Agent Skill, a Claude Code plugin, or as a plugin in a local/private Claude Code marketplace. **It generates instructions, not live cloud commands or changes.**

## Why this approach

- Prioritizes scoped coding agents and cloud tasks instead of maintaining dozens of provider-specific model profiles.
- The primary `SKILL.md` is deliberately compact; `references/` load only for relevant domains.
- Distinguishes observing, proposing, and applying; cloud work defaults to read-only analysis and approval gates.
- Includes a deterministic offline JSON-to-prompt renderer that requires no dependency or model API key.
- Treats token savings as a hypothesis to benchmark, not a guarantee.

## Layout

```text
mux-brief-starter/
  .claude-plugin/marketplace.json      # Local marketplace catalog
  plugins/mux-brief/
    .claude-plugin/plugin.json         # Claude Code plugin metadata
    skills/mux-brief/
      SKILL.md                         # Short instruction layer
      references/                     # Domain-specific, on demand
      assets/brief.example.json        # Machine-readable example
      scripts/brief.py                 # Optional offline renderer
  scripts/validate.py
  tests/test_brief.py
  .github/workflows/validate.yml
  BENCHMARK.md
  PROVENANCE.md
  LICENSE
```

## Try with Claude Code, no installation

From the directory that contains this README:

```bash
claude plugin validate ./plugins/mux-brief
claude --plugin-dir ./plugins/mux-brief
```

Inside Claude Code:

```text
/mux-brief:mux-brief Write a read-only AKS troubleshooting brief for a Copilot CLI agent.
```

## Try via the local marketplace

```bash
claude plugin validate .
claude plugin marketplace add .
claude plugin install mux-brief@mux-marketplace-starter
```

Inside Claude Code, invoke `/mux-brief:mux-brief`.

To use this in your existing private marketplace, copy the `plugins/mux-brief/` directory into it and add an equivalent `plugins` entry to the marketplace's `.claude-plugin/marketplace.json`. Don't overwrite an existing catalog.

## Use as a standalone Agent Skill

Copy `plugins/mux-brief/skills/mux-brief` into your agent's supported skills directory. For Claude Code, for example:

```bash
mkdir -p ~/.claude/skills
cp -R plugins/mux-brief/skills/mux-brief ~/.claude/skills/
```

Check the destination first if you already have a skill named `mux-brief`.

## Offline CLI renderer

```bash
python plugins/mux-brief/skills/mux-brief/scripts/brief.py \
  --input plugins/mux-brief/skills/mux-brief/assets/brief.example.json \
  --stats
```

The renderer emits a fixed task brief from JSON; it does not call an LLM, validate technical claims, tokenize with a model tokenizer, or execute commands. The secret scanner is a heuristic, not a DLP tool.

## Tests

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

For a fully authoritative Claude Code check run `claude plugin validate` locally, since this starter's Python checks are intentionally minimal.

## Adaptation roadmap

1. Extend the three domain references for your environments (GitLab CI, AKS/EKS, AWS/Azure Gov, internal Jira/Data Center).
2. Add a small set of standard test tasks and evaluate it against unguided prompts. See BENCHMARK.md.
3. Add optional approved command wrappers, but keep command execution separate from this prompt-authoring skill.
4. Add organization policy rules without including secrets or sensitive infrastructure identifiers in public distributions.
5. Pin releases in the private marketplace after passing your own enterprise review.

## License and attribution

The files in this starter are newly authored and covered by our own MIT license in `LICENSE`. See `PROVENANCE.md` before reusing upstream material. Change the copyright holder to the correct person/team before distribution.
