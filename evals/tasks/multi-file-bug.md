# Multi-file Bug

## Goal

Evaluate whether the coding-agent harness can investigate a failing test
across multiple modules, trace the observed failure to its actual source,
implement the minimal correct fix, and verify it with tests.

## Workspace

`evals/fixtures/config-service`

## Prompt

Inspect the code in the current workspace and fix the failing tests.

Requirements:

1. Identify the root cause before changing anything.
2. Trace the failure through the relevant modules rather than only fixing
   the code closest to the failing assertion.
3. Make the smallest correct code change.
4. Do not modify the tests.
5. Run the tests after the change.
6. Report what you changed and whether the tests pass.

Do not make unrelated changes.

## Success criteria

The agent should:

- inspect the failing test and relevant implementation files;
- trace the behavior from `app.py` through `config.py` and `client.py`;
- identify that `bool()` does not parse string boolean values and that
  `bool("false")` evaluates to `True`;
- fix boolean parsing in `config.py`;
- correctly handle at least the `"true"` and `"false"` values exercised
  by the test suite;
- leave the tests unchanged;
- run the tests after editing;
- get the full test suite passing;
- avoid unrelated changes;
- produce a final answer describing the root cause, change, and verification.

## Signals to record

- harness;
- harness version;
- model;
- wall-clock time;
- whether tools worked;
- whether the failing test was inspected;
- whether the execution path was traced across modules;
- whether the root cause was identified before editing;
- files inspected;
- files changed;
- size of the diff;
- whether tests were modified;
- whether tests were run after editing;
- final test result;
- whether unrelated changes were made;
- final-answer completion;
- notable incorrect claims.
