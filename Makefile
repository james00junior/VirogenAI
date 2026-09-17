.PHONY: install test lint format typecheck check api

install:
	python -m pip install -e '.[dev]'

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy apps ai analytics data simulation

check: lint typecheck test

api:
	uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8000
