# Bug Diagnosis

## Goal

Evaluate whether the coding-agent harness can investigate a small failing
codebase, identify the root cause, and explain the minimal fix without
modifying any files.

## Workspace

`evals/fixtures/cache-service`

## Prompt

Inspect the code in the current workspace and diagnose why the tests fail.

Do not modify any files.

Explain:

1. Which behavior is incorrect.
2. The root cause.
3. The minimal code change that would fix it.
4. Why that change is correct for both tests.

Run the tests if useful.

Do not implement the fix.

## Success criteria

The agent should:

- inspect the implementation and tests;
- identify the inverted TTL expiration condition;
- explain that entries younger than the TTL must remain valid;
- explain that entries at or beyond the TTL must expire;
- propose changing the comparison without making filesystem modifications;
- produce a final answer.

## Signals to record

- harness;
- harness version;
- model;
- wall-clock time;
- whether tools worked;
- whether tests were run;
- whether the root cause was identified;
- whether the proposed fix was minimal;
- whether any files were modified;
- final-answer completion;
- notable incorrect claims.
