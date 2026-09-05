SHELL := /bin/bash

ROLE ?=

.PHONY: bootstrap doctor

bootstrap:
	@if [ -z "$(ROLE)" ]; then \
		echo "Usage: make bootstrap ROLE=inference-host|agent-client"; \
		exit 1; \
	fi
	@./scripts/bootstrap "$(ROLE)"

doctor:
	@./scripts/doctor
