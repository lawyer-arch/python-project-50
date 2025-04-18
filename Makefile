.PHONY: lint

install:
	uv pip install .[dev]

lint:
	uv run ruff check .

format:
	uv run ruff check --fix .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

check: lint test
