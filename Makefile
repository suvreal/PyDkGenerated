.PHONY: install install-dev lint type-check test coverage all

install:
	pip install .

install-dev:
	pip install .[dev]

install-dev-poetry:
	poetry install

lint:
	poetry run ruff check

format:
	ruff format

format-check:
	ruff check

lint-fix:
	poetry run ruff check --fix

type-check:
	poetry run mypy --explicit-package-bases pydk_wrapper

test:
	python -m pytest --cov=pydk_wrapper tests/

all: install-dev lint type-check test

help:
	@echo "Available commands:"
	@echo "  make install         Install package"
	@echo "  make install-dev     Install dev dependencies (pytest, ruff, mypy)"
	@echo "  make lint            Run ruff lint checks"
	@echo "  make format          Format code using ruff"
	@echo "  make type-check      Run mypy static type checks"
	@echo "  make test            Run all tests"
	@echo "  make coverage        Run tests with coverage report"
	@echo "  make all             Run all checks and tests"
	@echo "  make help            Show this help message"
