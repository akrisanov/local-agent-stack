# Feature Implementation

## Goal

Evaluate whether the coding-agent harness can understand an existing codebase,
implement a small feature from written requirements, preserve existing
behavior, add appropriate tests, and verify the result.

## Workspace

`evals/fixtures/rate-limiter`

## Prompt

The current rate limiter applies one request limit globally.

Change it so that request limits are tracked independently for each client.

Requirements:

1. `RateLimiter.allow()` must accept a client identifier.
2. Each client must have its own request count.
3. Reaching the limit for one client must not affect another client.
4. `RateLimitMiddleware.handle()` must accept a client identifier and apply
   the limit to that client.
5. Preserve the existing limit semantics: the first `max_requests` requests
   for a client are allowed, and subsequent requests are rejected.
6. Update or add tests for the new behavior.
7. Run the complete test suite after making the changes.
8. Keep the implementation small and avoid unrelated refactoring.

Report what you changed and whether the tests pass.

## Success criteria

The agent should:

- inspect the existing implementation and tests before editing;
- understand that the current limiter maintains a single global counter;
- change request accounting to be per client;
- update `RateLimiter.allow()` to accept a client identifier;
- update `RateLimitMiddleware.handle()` accordingly;
- preserve the existing limit boundary behavior;
- demonstrate through tests that two clients have independent limits;
- update existing tests where required by the API change;
- avoid unrelated changes;
- run the complete test suite after editing;
- finish with all tests passing;
- produce a final answer describing the implementation and verification.

## Signals to record

- harness;
- harness version;
- model;
- wall-clock time;
- files inspected;
- files changed;
- tests added or changed;
- size of the diff;
- whether the existing behavior was preserved;
- whether client isolation was tested;
- whether tests were run before editing;
- whether tests were run after editing;
- final test result;
- editing or tool errors;
- recovery steps;
- unrelated changes;
- final-answer completion;
- notable incorrect claims.
