# Qwen3.6 35B MLX

`qwen3.6:35b-mlx` · Ollama / MLX · local inference over SSH

## At a glance

**Goose is the best fit so far.** It passed every task, finished the recorded runs much faster than Codex,
and needed no recovery on the multi-file task. Pi also passed everything, though a few runs included navigation
or editing mistakes that it had to recover from. Codex generally reasoned and edited correctly,
but this setup was slow, reported unusually high token usage, and twice failed to produce the expected final response.

| Harness           | Inspection | Diagnosis | Minimal fix | Multi-file bug | Recorded time* | Current read                         |
| ----------------- | ---------: | --------: | ----------: | -------------: | -------------: | ------------------------------------ |
| **Goose**         |       Pass |      Pass |        Pass |           Pass |    **58–111s** | Best fit so far                      |
| **Pi 0.85.1**     |       Pass |      Pass |        Pass |           Pass |              — | Solid, with some recovery needed     |
| **Codex 0.153.4** |    Partial |      Pass |     Partial |           Pass |   **276–304s** | Works, but inefficient in this setup |

\* Timing was not captured for every run, so these numbers are useful observations rather than a controlled performance benchmark.

## Goose

Goose had the cleanest results across the current suite.

- Repository inspection: **111s**, ~**14k / 128k** context.
- Bug diagnosis: **60s**, ~**7k / 128k** context.
- Minimal fix: **71s**, ~**8k / 128k** context.
- Multi-file bug: **58s**, ~**8k / 128k** context, **6 tests passed**.
- No editing or recovery problems on the multi-file task.

There were a couple of tool-advertisement errors in earlier runs, but Goose recovered and completed the tasks normally.

## Pi

Pi passed all four evaluations and handled recovery reasonably well when things went wrong.

On the multi-file task, its first edit left `config.py` with invalid Python. Pi noticed the pytest collection failure,
reread the file, repaired the edit, and finished with **6 tests passed**. Earlier runs also included a few minor navigation mistakes.

One useful finding came from the first version of the minimal-fix fixture: Pi chose `>` instead of `>=`,
and the original tests did not catch the boundary case. Adding an exact-TTL test exposed the problem;
Pi then produced the correct fix. That was as much a test-suite issue as an agent issue, and the fixture was kept stricter afterward.

## Codex

Codex was capable of doing the coding work, but the integration with this local model was noticeably less efficient.

- Repository inspection: **304s**, Partial because no final response was produced.
- Bug diagnosis: **299s**, ~**370k** reported tokens, Pass.
- Minimal fix: **276s**, ~**651k** reported tokens, Partial because no final response was produced.
- Multi-file bug: **303s**, **6 tests passed**, Pass.

The diagnosis and code changes were generally correct. The main concerns were the roughly five-minute runtime
even on small fixtures, very high reported token counts, and inconsistent completion of the final agent response.

Codex also repeatedly reported that metadata for `qwen3.6:35b-mlx` was unavailable and that fallback metadata was being used.
The results do not show that this warning caused the behavior, but it is worth keeping in mind when interpreting the Codex numbers.

## What has been tested

The suite currently covers four different kinds of work:

1. understanding an unfamiliar repository;
2. diagnosing a bug without modifying code;
3. making a small, targeted fix;
4. tracing and fixing a bug across several modules.

All three harnesses solved the multi-file task and ended with **6 passing tests**.

## Takeaway

For this particular `qwen3.6:35b-mlx` setup, I would use **Goose as the default harness today**.
Pi is a reasonable alternative and has shown that it can recover from its own mistakes.
Codex works at the reasoning and editing level, but the current local-model pairing is too slow and inconsistent to be the default.
