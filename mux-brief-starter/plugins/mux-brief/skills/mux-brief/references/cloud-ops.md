# Cloud / CLI briefing

Use for preparing prompts targeted at `aws`, `az`, `kubectl`, `helm`, `terraform`, or similar command-line tasks.

## Operating posture

Choose one explicitly:

- `observe`: inspect state, explain findings, propose changes; no writes.
- `propose`: create a plan or diff and hold for review.
- `apply`: only when the user specifically requests actionable write instructions; still include review gates for destructive/high-impact steps.

For scoped infrastructure, specify the provider, tenant/account/subscription, environment, cluster, namespace, and resource when they are *known*. Omit unknown identifiers or replace them with brackets to be filled by the operator.

Require the downstream operator/agent to state the current identity and target context before any write where cross-environment confusion is possible. A prompt never grants extra RBAC permissions.

Default to least-privilege and dry-run/plan or read-only inspection when supported by the specific tool. Do not imply every tool supports an identical dry-run option.

## Example operation brief

```text
Outcome: Determine why a workload is failing to become Ready.
Known context: Azure Kubernetes Service; exact cluster and namespace not provided.
Allowed: Read-only inspection of selected cluster, events, pod state, and logs.
Forbidden: Deployments, restarts, secret reads, role grants, or environment switching without confirmation.
Evidence: Observations, commands proposed or actually run, likely cause, and next diagnostic step.
Approval gate: Stop before any mutating remediation.
```

Do not reproduce credentials, kubeconfig entries, cloud tokens, or secret values.
