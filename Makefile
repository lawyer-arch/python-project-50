.PHONY: lint test format test-coverage check install

install:
	uv pip install .[dev]

lint:
	ruff check .

format:
	ruff check --fix .

test:
	pytest

test-coverage:
	pytest --cov=gendiff --cov-report=xml

check: lint test
