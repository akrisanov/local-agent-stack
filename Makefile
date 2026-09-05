SHELL := /bin/bash

ROLE ?=

.PHONY: bootstrap doctor runtime models \
	codex-install codex-local \
	pi-install pi-local \
	goose-install goose-local \
	tunnel-start tunnel-stop tunnel-restart tunnel-status \
	eval

bootstrap:
	@if [ -z "$(ROLE)" ]; then \
		echo "Usage: make bootstrap ROLE=inference-host|agent-client"; \
		exit 1; \
	fi
	@./scripts/bootstrap "$(ROLE)"

doctor:
	@./scripts/doctor

runtime:
	@./scripts/install-runtime

models:
	@./scripts/models

codex-install:
	@./scripts/install-codex

codex-local:
	@./scripts/codex-local

pi-install:
	@./scripts/install-pi

pi-local:
	@./scripts/pi-local

goose-install:
	@./scripts/install-goose

goose-local:
	@./scripts/goose-local

tunnel-start:
	@./scripts/tunnel start

tunnel-stop:
	@./scripts/tunnel stop

tunnel-restart:
	@./scripts/tunnel restart

tunnel-status:
	@./scripts/tunnel status

eval:
	@if [ -z "$(HARNESS)" ] || [ -z "$(TASK)" ]; then \
		echo "Usage: make eval HARNESS=codex|pi|goose TASK=<task>"; \
		exit 1; \
	fi
	@./scripts/eval "$(HARNESS)" "$(TASK)"
