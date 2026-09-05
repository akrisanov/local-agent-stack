SHELL := /bin/bash

ROLE ?=

.PHONY: bootstrap doctor runtime models

bootstrap:
	@if [ -z "$(ROLE)" ]; then \
		echo "Usage: make bootstrap ROLE=inference-host|agent-client"; \
		exit 1; \
	fi
	@./scripts/bootstrap "$(ROLE)"

runtime:
	@./scripts/install-runtime

models:
	@./scripts/models

doctor:
	@./scripts/doctor
