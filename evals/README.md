# Evaluations

This directory contains reproducible tasks for comparing coding-agent
harnesses against the same local inference stack.

The goal is not to benchmark model quality in isolation.

Each evaluation keeps the following variables fixed whenever possible:

- repository;
- prompt;
- model;
- inference runtime;
- transport;
- machine.

The harness is the primary variable being changed.

## Running an evaluation

For example:

```bash
make eval HARNESS=pi TASK=repo-inspection
```

Supported harnesses:

- codex
- pi
- goose

The eval runner prints the task prompt and launches the selected harness.

Run the prompt unchanged.

After the agent finishes, verify `git status --short`.

Then record the result in evals/results/.

## Interpretation

These evaluations are intended to expose differences in:

- tool-call reliability;
- agent-loop behavior;
- latency;
- context handling;
- final-answer reliability;
- unnecessary tool usage;
- unintended modifications;
- compatibility between a harness and a particular local model.

A successful inference request does not imply that a harness/model pairing is
a successful coding-agent configuration.
