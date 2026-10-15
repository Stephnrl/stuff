Corrections to the proposed split

Lite shouldn’t do linting or formatting. ruff, prettier, shellcheck, hadolint, terraform fmt/validate, tflint and kubeconform are faster, cost zero tokens, and are never wrong about syntax. Run them in hooks or CI. Lite is better used for small judgment tasks that tools can’t do:

Triaging and summarizing long logs or CI output before it reaches Smart’s context
Classifying or routing incoming tasks
Extracting structured data, such as turning kubectl describe output into JSON
Writing commit messages, PR descriptions, and changelog entries
Broad file and code search where only the conclusion matters

Max shouldn’t be the “tester.” Tests are run by tools. Max is valuable for designing the test strategy and for diagnosing failures that Smart couldn’t explain.

A split that works well
Role	Model	When
Plan, architecture, risk review	Max	Once at the start, and once on the final diff for risky changes
Implementation, iteration, fixing	Smart	The bulk of the work
Summarize, classify, draft text	Lite	High volume, low stakes
Lint, format, validate, test	Tooling	Always

Escalate to Max when:

Smart fails the same task twice
The change touches state that’s hard to undo, such as Terraform applies that destroy resources, DB migrations, IAM/RBAC, or networking
The work involves concurrency, security boundaries, or distributed-systems behavior

On hard problems, Max is often cheaper end to end. One correct pass costs less than three Smart retries, each re-reading the same context.

Where the token savings actually come from

Model choice matters less than context hygiene:

Max writes the plan to a file (PLAN.md) with steps and acceptance criteria. Smart workers read the file instead of re-deriving context. Each subagent starts cold, so a handoff file is the cheapest form of memory.
Pass pointers, not content. Give file paths and line ranges rather than pasting whole files or logs.
Subagents return conclusions, not dumps. “The failing test is X because Y” instead of 400 lines of output.
Keep a stable prompt prefix (system prompt, repo conventions, tool definitions) so prompt caching hits. Put the variable task at the end.
Skip orchestration for small tasks. A one-file fix should just go to Smart. Planner/worker/reviewer overhead only pays off on multi-step work.
How to start a prompt
GOAL: Add HPA to the payments service, scaling on CPU and queue depth.

CONTEXT: k8s/payments/, charts/payments/values.yaml. KEDA is installed.

CONSTRAINTS: No changes to prod values. Keep min replicas >= 2.
             Don't touch the ingress.

DONE WHEN: helm template renders, kubeconform passes,
           the staging values diff contains only the HPA/ScaledObject.

OUTPUT: The diff plus a 3-line summary of the risks.

The “done when” line is the most important part. It gives the agent an objective stopping condition, which prevents both premature “done” and runaway iteration, the two biggest sources of wasted tokens.

The flow in short: Max plans and defines “done,” Smart builds against it, tooling validates continuously, Lite handles the high-volume text work, and Max reviews only the risky diffs.
