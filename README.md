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

Desired models are declared in `models/models.yaml`.

Model installation and locking will be added separately.

## Agent harnesses

The first harnesses planned for this project are:

- Codex CLI
- Pi
- Goose

Qwen Code and OpenCode may be added later for comparison.

---

© 2026, Andrey Krisanov
