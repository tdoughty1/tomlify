test:
    uv run pytest -vv

lint:
    uv run ruff check src tests

typecheck:
    uv run mypy src --disallow-untyped-calls --disallow-untyped-defs
