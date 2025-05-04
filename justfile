test:
    uv run pytest -vv

lint:
    uv run ruff check --select ALL --fix --ignore D100,D101,D102,D103,D104,D105,D107,D400,FIX002,TD002,TD003,PT011

type:
    uv run mypy --strict src tests

todo:
    git grep "# TODO:" -- '*.py'
    git grep "noqa" -- '*.py' | grep -v N802 | grep -v S101 
    git grep "# type" -- '*.py'
