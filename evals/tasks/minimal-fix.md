# Minimal Fix

## Goal

Evaluate whether the coding-agent harness can diagnose a small failing
codebase, implement the minimal correct fix, and verify it with tests.

## Workspace

`evals/fixtures/cache-service`

## Prompt

Inspect the code in the current workspace and fix the failing tests.

Requirements:

1. Identify the root cause before changing anything.
2. Make the smallest correct code change.
3. Do not modify the tests.
4. Run the tests after the change.
5. Report what you changed and whether the tests pass.

Do not make unrelated changes.

## Success criteria

The agent should:

- inspect the implementation and tests;
- identify the inverted TTL expiration condition;
- modify only the TTL comparison in `cache.py`;
- leave `test_cache.py` unchanged;
- run the tests after editing;
- get both tests passing;
- produce a final answer describing the change and verification.

## Signals to record

- harness;
- harness version;
- model;
- wall-clock time;
- whether tools worked;
- whether the root cause was identified before editing;
- files changed;
- size of the diff;
- whether tests were modified;
- whether tests were run after editing;
- final test result;
- whether unrelated changes were made;
- final-answer completion;
- notable incorrect claims.
