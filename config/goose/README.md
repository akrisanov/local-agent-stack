# Goose

Goose is configured through environment variables rather than a generated configuration file.

`scripts/goose-local` derives the Goose configuration from the common local-agent-stack environment:

- `LOCAL_AGENT_MODEL` → `GOOSE_MODEL`
- `LOCAL_AGENT_BASE_URL` → `OLLAMA_HOST`
- provider → `GOOSE_PROVIDER=ollama`

This intentionally avoids modifying the user's global Goose configuration.
