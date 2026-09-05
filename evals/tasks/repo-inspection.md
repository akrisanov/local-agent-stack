# Repository Inspection

## Goal

Evaluate whether a coding-agent harness can inspect the repository, understand its architecture, and produce a useful answer without modifying files.

## Prompt

Inspect this repository without modifying anything.

Explain:

1. The current architecture.
2. The responsibilities of the inference-host and agent-client roles.
3. How a request from this machine reaches the model.
4. The three most important improvements you would make next.

Do not modify any files.

## Success criteria

The agent should:

- inspect the repository using tools rather than guessing;
- correctly identify the inference-host and agent-client roles;
- correctly explain the client → transport → inference runtime → model path;
- distinguish coding-agent harnesses from the inference runtime;
- propose improvements grounded in the repository;
- produce a final answer;
- make no filesystem modifications.

## Signals to record

- harness;
- harness version;
- model;
- endpoint;
- wall-clock time;
- whether tool use worked;
- whether a final answer was produced;
- whether the repository was modified;
- approximate context/token usage, when available;
- notable correctness issues;
- overall verdict.
