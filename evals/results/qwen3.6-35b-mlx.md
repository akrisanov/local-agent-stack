# Qwen3.6 35B MLX

`qwen3.6:35b-mlx` · Ollama / MLX · local inference over SSH

## At a glance

**Goose is the best fit so far.** It passed every task and has the best recorded latency.
Pi also passed the full suite and handled its recovery cases well.
Codex generally reasoned and edited correctly, but this setup was much slower, reported unusually high token usage,
and twice failed to produce the expected final response.

| Harness           | Inspection | Diagnosis | Minimal fix | Multi-file bug | Feature | Recorded time* | Current read                         |
| ----------------- | ---------: | --------: | ----------: | -------------: | ------: | -------------: | ------------------------------------ |
| **Goose**         |       Pass |      Pass |        Pass |           Pass |    Pass |    **58–111s** | Best fit so far                      |
| **Pi 0.85.1**     |       Pass |      Pass |        Pass |           Pass |    Pass |              — | Solid, with good recovery            |
| **Codex 0.153.4** |    Partial |      Pass |     Partial |           Pass |    Pass |   **276–304s** | Works, but inefficient in this setup |

\* Timing was not captured for every run, so these numbers are useful observations rather than a controlled performance benchmark.

## Goose

Goose has the cleanest results across the current suite.

- Repository inspection: **111s**, ~**14k / 128k** context.
- Bug diagnosis: **60s**, ~**7k / 128k** context.
- Minimal fix: **71s**, ~**8k / 128k** context.
- Multi-file bug: **58s**, ~**8k / 128k** context, **6 tests passed**.
- Feature implementation: **90s**, ~**12k / 128k** context, **6 tests passed**.

The feature task required one recovery: the first test edit introduced an indentation error.
Goose caught the pytest collection failure, fixed the test file, and completed the task successfully.
Earlier runs also included a couple of tool-advertisement errors that did not prevent completion.

## Pi

Pi passed all five evaluations and has shown good recovery when its first attempt was not clean.

On the multi-file task, its first edit left `config.py` with invalid Python. Pi noticed the pytest collection
failure, reread the file, repaired the edit, and finished with **6 tests passed**.

The feature implementation was cleaner: Pi implemented per-client request accounting, updated the middleware API,
added client-isolation coverage, and finished with **6 tests passed**. Its middleware isolation test used separate
limiter instances, so that particular test did not prove isolation within a shared limiter; the limiter-level
test did cover that behavior correctly.

An earlier version of the minimal-fix fixture also exposed a useful boundary case. Pi chose `>` instead of `>=`,
and the original tests did not catch it. After an exact-TTL test was added, Pi produced the correct fix.
That finding led to a stricter fixture rather than being treated only as an agent failure.

## Codex

Codex can do the coding work, but the integration with this local model remains noticeably less efficient.

- Repository inspection: **304s**, Partial because no final response was produced.
- Bug diagnosis: **299s**, ~**370k** reported tokens, Pass.
- Minimal fix: **276s**, ~**651k** reported tokens, Partial because no final response was produced.
- Multi-file bug: **303s**, **6 tests passed**, Pass.
- Feature implementation: **303s**, **7 tests passed**, Pass.

The feature run was clean: Codex implemented per-client accounting, updated both APIs, added explicit isolation tests,
ran the suite successfully, and produced a final response without needing recovery.

The main concerns remain the roughly five-minute runtime even on small fixtures, very high reported token counts in
the recorded runs, and inconsistent completion of the final agent response.

Codex also repeatedly reported that metadata for `qwen3.6:35b-mlx` was unavailable and that fallback metadata
was being used. The results do not show that this warning caused the behavior,
but it is worth keeping in mind when interpreting the Codex numbers.

## What has been tested

The suite currently covers five kinds of work:

1. understanding an unfamiliar repository;
2. diagnosing a bug without modifying code;
3. making a small, targeted fix;
4. tracing and fixing a bug across several modules;
5. implementing a feature from written requirements and adding tests.

All three harnesses passed the feature implementation task.

## Takeaway

For this particular `qwen3.6:35b-mlx` setup, I would use **Goose as the default harness today**.
It has passed every evaluation and has the strongest recorded latency so far. Pi is a credible alternative and
has recovered well from its mistakes. Codex works at the reasoning and editing level, and its latest runs
have completed cleanly, but the current local-model pairing is still too slow and inefficient to be the default.
