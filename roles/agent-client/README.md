# Agent client

An agent client runs coding-agent harnesses and connects them to an inference service.

## Responsibilities

- install agent harnesses
- configure the inference endpoint
- manage harness-specific configuration
- keep credentials outside the repository

## Initial harnesses

The first supported harnesses will be:

- Codex CLI
- Pi
- Goose

The architecture must allow each harness to use either:

- a local inference service
- a remote private inference service
- a cloud model provider

## Inference endpoint

Agent configuration should depend on a logical endpoint rather than on the physical inference host.

Example:

```text
LOCAL_AGENT_BASE_URL=http://127.0.0.1:11434/v1
```

A remote client may use another endpoint without changing the rest of the stack.
