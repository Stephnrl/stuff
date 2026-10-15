# Evaluation plan (not measured results)

Goal: determine whether this skill improves first-response usefulness without introducing excessive instruction overhead.

## Test set

- 10 repository changes: bounded bug fixes, tests, refactors, review tasks
- 10 cloud operations: AKS/EKS status inspections, CI failures, Terraform plan reviews
- 5 knowledge/document tasks: incident summaries, change requests, engineering briefs

For each task create a grounded scenario with expected output and prohibited actions. Keep task prompts, runtime settings, and supplied context identical between control and skill-assisted runs.

## Capture

- API-reported input/output tokens (when supported); otherwise label estimates clearly
- Completion correctness (pass/fail by test or review rubric)
- Unauthorized modification/command attempts (count)
- Human clarification turns and manual correction time
- Downstream tool calls and cost; track prompt-generation cost separately

Run at least three randomized repeats per task per condition where practical, and review failures qualitatively. Compare medians and task-success rates, not claims about saving "zero tokens". Do not store credentials, private customer data, or raw sensitive prompts in the benchmark data.

## Suggested success gates for first iteration

- No secret reproduction in tests or evaluations
- No unauthorized write instructions in read-only operation scenarios
- Equal or better completion quality than baseline in at least 80% of reviewed scenarios
- No more than 10% median end-to-end token increase unless quality improves materially

These are *targets*, not results. Use provider usage records for actual token counts.
