# Inference host

The inference host runs the model runtime and exposes an API to agent clients.

## Responsibilities

- install and run the inference runtime
- download configured models
- expose an OpenAI-compatible API
- provide health information
- keep model storage local to the host

## Current implementation

The initial runtime is Ollama.

The default local API is `http://127.0.0.1:11434`.

The OpenAI-compatible endpoint is `http://127.0.0.1:11434/v1`.

## Security

The inference runtime should remain bound to loopback by default.

Remote access should be provided through a separate authenticated network layer such as:

- SSH over Tailscale
- Tailscale Serve

Do not expose an unauthenticated inference API directly to the public internet.
