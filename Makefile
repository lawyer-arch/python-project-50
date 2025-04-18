.PHONY: lint

lint:
	uv run ruff check .

format:
	uv run ruff check --fix .