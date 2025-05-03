test:
    uv run pytest -vv

lint:
    uv run ruff check .

typecheck:
    uv run mypy --strict src tests
