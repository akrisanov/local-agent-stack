# local-agent-stack

A reproducible, local-first environment for running coding agents against a shared inference service.

The project separates two responsibilities:

- **inference host** — runs the model runtime and model weights
- **agent client** — runs coding-agent harnesses such as Codex, Pi, and Goose

A single machine may have both roles.

## Goals

- Reproducible setup on macOS and Linux.
- One shared local inference endpoint for multiple machines.
- Interchangeable coding-agent harnesses.
- Declarative model configuration.
- No secrets or personal infrastructure details in Git.
- A single health-check command.
- Reproducible evaluation of model/harness combinations.
- Ability to replace the inference host without rebuilding the client environment.

## Architecture

```text
             ┌── Codex
             ├── Pi
Agent client ┼── Goose
             └── other harnesses
                  │
                  ▼
          inference endpoint
                  │
                  ▼
             model runtime
                  │
                  ▼
                model
```

The initial reference environment is:

```text
Mac mini / Apple Silicon
        │
        └── Ollama
              │
              └── local coding model

MacBook / Linux laptop
        │
        └── coding-agent harness
              │
              └── remote inference endpoint
```

The architecture intentionally does not depend on the Mac mini.

A future backend may be:

```text
Linux
  └── NVIDIA GPU
       └── Ollama / vLLM / another OpenAI-compatible runtime
```

without changing the agent-client workflow.

## Roles

### inference-host

Responsible for:

- model downloads
- model runtime
- inference API
- runtime health checks

### agent-client

Responsible for:

- Codex
- Pi
- Goose
- agent configuration
- connection to an inference endpoint

## Quick start

Clone the repository:

```shell
git clone <https://github.com/akrisanov/local-agent-stack.git>
cd local-agent-stack
```

Configure a machine as an inference host:

```shell
make bootstrap ROLE=inference-host
make doctor
```

Configure a client:

```shell
make bootstrap ROLE=agent-client
make doctor
```

## Local configuration

Public defaults live in `.env.example`.

Machine-specific configuration lives outside the repository in `~/.config/local-agent-stack/env`.

The repository excludes secrets and personal infrastructure details, such as:

- API keys
- OAuth tokens
- Tailscale auth keys
- SSH credentials
- machine-specific private addresses
- work infrastructure endpoints

## Models

Desired models are declared in `models/models.yaml` and managed through the repository tooling.

The current reference model is `qwen3.6:35b-mlx`, served by Ollama on the inference host.

## Agent harnesses

The project currently supports:

- Codex CLI
- Pi
- Goose

Each harness has repository-managed installation and local-inference launch scripts:

```shell
make codex-install
make codex-local

make pi-install
make pi-local

make goose-install
make goose-local
```

Qwen Code and OpenCode may be added later for comparison.

## Evaluations

The repository includes a controlled evaluation suite for comparing model/harness combinations.

Run an evaluation with:

```shell
make eval HARNESS=pi TASK=bug-diagnosis
```

The current tasks are:

- `repo-inspection` — inspect the repository, reconstruct its architecture and request paths,
  and propose concrete improvements without modifying files
- `bug-diagnosis` — inspect a failing codebase, identify the root cause, and explain
  the minimal fix without modifying files
- `minimal-fix` — diagnose the failure, implement the smallest correct change, and verify it with tests
- `multi-file-bug` — trace a failure across multiple modules, identify the root cause,
  implement the smallest correct fix, and verify the full test suite
- `feature-implementation` — implement a small cross-file feature, update the relevant tests,
  and verify the complete test suite

Evaluation fixtures live in `evals/fixtures/`, task definitions in `evals/tasks/`,
generated runs in `evals/runs/`, manual reviews in `evals/reviews/`, and consolidated results in `evals/results/`.

Each evaluation produces objective run metadata locally, including wall time, test results, changed files, and diff size.
A separate committed review records the subjective verdict, recovery behavior, requirement coverage,
final-answer completion, and notes.

Create a review template after a run with:

```shell
make review HARNESS=goose TASK=minimal-fix
```

Preview the consolidated report for the current model with:

```shell
make report
```

The current baseline evaluates `qwen3.6:35b-mlx` with Codex, Pi, and Goose.
Goose has a complete structured baseline across all five tasks;
Pi and Codex are being migrated to the same evaluation pipeline
so harness comparisons use identical run metadata and review criteria.

---

© 2026, Andrey Krisanov
