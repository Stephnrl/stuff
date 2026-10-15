# Coding-agent briefing

Use when the receiving system can inspect or modify a repository.

## Decide the editing envelope

Translate requests into precise *allowed* scope. Keep these distinct:

- Entry point: known relevant files, functions, issue references, or an explicit discovery task.
- Modification boundary: which files can change. If unknown, permit investigation before editing, not hypothetical path invention.
- Compatibility: versioned runtime or API guarantees only when the user provided them.
- Verification: tests or checks the agent can actually run; when unavailable, ask for a description of how to verify.
- Review gate: new dependency, migration, public API behavior, irreversible edits or expanded scope.

## Suggested concise shape

```text
Outcome: [behavior after the change]
Repository context: [known state only]
Work boundary: [target paths or read-only discovery]
Keep stable: [behaviors/interfaces that must not move]
Proof: [test cases, command outputs, changed-file summary]
Approval gate: [material scope expansion or destructive operation]
```

For issue investigation, replace `Work boundary` with `Questions to establish` and request supporting file paths, logs, and reproduction evidence before fixes.

Never invent a test invocation, claim repository access, or assert that an agent executed a command because it appeared in the brief.
