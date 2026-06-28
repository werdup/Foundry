.PHONY: test lint

test:
	python -m pytest

lint:
	python -m compileall foundry

format:
	@echo "Formatting will be added later."