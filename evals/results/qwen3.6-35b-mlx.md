# Qwen3.6 35B MLX

- Model: `qwen3.6:35b-mlx`
- Runtime: Ollama / MLX
- Transport: SSH tunnel to the inference host
- Client endpoint: <http://127.0.0.1:11434>
- Codex and Pi use the OpenAI-compatible endpoint: <http://127.0.0.1:11434/v1>
- Goose uses the native Ollama provider with: OLLAMA_HOST=<http://127.0.0.1:11434>

## Summary

| Harness       | Repository inspection | Bug diagnosis | Minimal fix | Overall             |
| ------------- | --------------------- | ------------- | ----------- | ------------------- |
| Codex 0.153.4 | Partial               | Pass          | Partial     | Problematic pairing |
| Pi 0.85.1     | Pass                  | Pass          | Pass        | Viable              |
| Goose         | Pass                  | Pass          | Pass        | Viable              |

Pass means that the harness completed the task, produced the expected result,
and produced a final answer.

Partial means that the underlying work was substantially correct but one or more
important success criteria were not satisfied.

## Repository inspection

### Codex

Result: `Partial`

The agent successfully:

- inspected the repository;
- used tools;
- reconstructed the architecture.

However, it returned to the interactive prompt without producing a visible final answer.

Observed wall time: `5m04s`

Codex reported:

```shell
Model metadata for `qwen3.6:35b-mlx` not found.
Defaulting to fallback metadata.
```

This warning is a possible contributor to the poor behavior, but
the evaluation does not establish causality.

### Pi

Result: `Pass`

The agent successfully:

- inspected the repository;
- used tools;
- reconstructed the inference-host and agent-client roles;
- produced a final answer;
- made no repository modifications.

The agent recovered from an initial path/navigation mistake without affecting the final result.

Wall-clock time was not recorded for the initial run.

### Goose

Result: `Pass`

The agent successfully:

- inspected the repository;
- used tools;
- reconstructed the architecture;
- produced a final answer;
- made no repository modifications.

Observed wall time: `1m51s`

Observed context usage: `~14k / 128k`

The answer contained a minor unsupported implementation detail about MLX/MPS,
but the architectural explanation was otherwise correct.

## Bug diagnosis

Task: [bug-diagnosis⁠](./tasks/bug-diagnosis.md)

The fixture contains an inverted cache TTL expiration condition.

The expected diagnosis is:

```python
if time.monotonic() - created_at >= self.ttl_seconds:
```

The task is read-only: the harness must diagnose the problem without modifying the workspace.

### Codex

Result: `Pass`

The agent:

- inspected the implementation and tests;
- ran all three tests;
- observed three failures;
- identified the inverted TTL condition;
- correctly handled the exact-TTL boundary;
- proposed the minimal < → >= fix;
- produced a final answer;
- made no intentional modifications.

Observed wall time: `4m59s`

Observed token usage:

```text
input:  368,177
output:   1,636
total:  369,813
```

Codex again reported that model metadata was unavailable and fallback metadata was being used.

### Pi

Result: `Pass`

The agent:

- inspected the implementation and tests;
- ran the tests;
- identified the inverted TTL condition;
- proposed the correct minimal fix;
- produced a final answer;
- did not intentionally modify the workspace.

The agent initially attempted to access files using incorrect absolute paths,
received ENOENT, and recovered by using the workspace-relative paths.

It also performed an unnecessary package.json probe despite the fixture being a Python project.

### Goose

Result: Pass

The agent:

- inspected the fixture;
- ran the tests;
- identified the inverted TTL condition;
- proposed the correct minimal fix;
- produced a final answer;
- did not modify the workspace.

Observed wall time: `1m00s`

Observed context usage: `~7k / 128k`

A tool-advertisement error occurred during the run, but the agent recovered and completed the task.

## Minimal fix

Task: [minimal-fix⁠](./tasks/minimal-fix.md)

The expected change is exactly:

```diff
-        if time.monotonic() - created_at < self.ttl_seconds:
+        if time.monotonic() - created_at >= self.ttl_seconds:
```

The tests must remain unchanged.

### Codex

Result: `Partial`

The agent correctly:

- identified the root cause before editing;
- ran the failing tests;
- changed only the TTL comparison;
- used the correct >= boundary;
- left the tests unchanged;
- ran the tests again.

However, after the post-edit test command Codex displayed:

```shell
(no output)
```

and returned to the interactive prompt without producing the required final
answer.

Manual verification after the session confirmed:

```shell
3 passed
```

The fixture comparison also confirmed that `test_cache.py` was unchanged.

Observed wall time: `4m36s`

Observed token usage:

```shell
input:  650,028
output:   1,387
total:  651,415
```

Codex again reported fallback model metadata.

The implementation itself was correct; the failure was in completing
the agent workflow and reporting the result.

### Pi

Result: `Pass`

The agent:

- identified the root cause before editing;
- ran the failing tests;
- changed only the TTL comparison;
- used >=;
- left the tests unchanged;
- reran the tests;
- obtained three passing tests;
- produced a final answer.

An earlier version of the fixture did not test the exact-TTL boundary.
On that version Pi implemented > rather than >=, while still passing both tests.

The fixture was subsequently strengthened with an exact-TTL test.
On the current fixture Pi selected the correct >= comparison and passed all three tests.

This earlier result is retained because it exposed a weakness in the evaluation fixture itself
rather than being silently discarded.

### Goose

Result: `Pass`

The agent:

- identified the root cause before editing;
- made the expected one-line change;
- left the tests unchanged;
- ran the tests after editing;
- obtained passing tests;
- produced a final answer;
- made no unrelated changes.

Observed wall time: `1m11s`

Observed context usage: `~8k / 128k`

A tool-advertisement error occurred during the run, but the agent recovered
and completed the workflow.

## Observations

### Codex

The model demonstrated adequate reasoning and coding ability through Codex:
repository inspection, test execution, diagnosis, and editing all worked.

The primary problems observed were:

- very high latency;
- extremely high reported input-token usage for the small controlled fixture;
- missing final answers in two of the three evaluations;
- repeated fallback-model-metadata warnings.

These results support describing this specific configuration as a problematic pairing.

They do not establish that Codex itself or Qwen3.6 itself is unsuitable.

### Pi

Pi completed all current evaluation tasks successfully.

It recovered from minor navigation/tool mistakes and produced normal final answers.

The first minimal-fix run also demonstrated why boundary cases need to be
encoded explicitly in evaluation fixtures rather than inferred from expected agent reasoning.

### Goose

Goose completed all current evaluation tasks successfully and showed
good wall-clock performance in the recorded runs.

The harness also recovered from tool-advertisement errors rather than terminating the agent loop.

The current evidence supports describing Goose as viable, but the suite is
still too small to make a broader quality claim.

## Current conclusion

For `qwen3.6:35b-mlx` on the current local inference stack:

1. Pi is a viable coding-agent harness.
2. Goose is a viable coding-agent harness and has shown good latency in the recorded tasks.
3. Codex can reason, inspect, execute tools, and edit correctly,
   but this particular local-model integration currently has
   substantial efficiency and agent-loop completion problems.

More complex evaluations are required before selecting a preferred harness.
