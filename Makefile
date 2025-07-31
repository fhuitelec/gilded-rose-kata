PYTEST := uv run pytest
PYLINT := uv run pylint
PYRIGHT := uv run pyright
RUFF := uv run ruff
RADON := uv run radon
CLI := uv run src/gilded_rose/main.py
LINT_DIRECTORIES := src/gilded_rose tests

.PHONY: install
install:
	$(CLI)

.PHONY: run
run:
	$(CLI)

.PHONY: test
test:
	$(PYTEST) -v --cov-report term --cov=src/gilded_rose

.PHONY: lint
lint:
	$(PYLINT)  $(LINT_DIRECTORIES)
	$(PYRIGHT) $(LINT_DIRECTORIES)
	$(RUFF) format       $(LINT_DIRECTORIES)
	$(RUFF) check  --fix $(LINT_DIRECTORIES)

.PHONY: analyze
analyze:
	$(RADON) cc src/
	@echo
	@echo "To know more about cyclomatic complexity:"
	@echo "  - https://radon.readthedocs.io/en/latest/intro.html#cyclomatic-complexity"
	@echo "  - https://radon.readthedocs.io/en/latest/commandline.html#the-cc-command"
