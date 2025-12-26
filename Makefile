.PHONY: test coverage lint clean all

all: lint test

test:
	python -m pytest tests/ -v

coverage:
	python -m pytest tests/ --cov=. --cov-report=html --cov-report=xml --cov-report=term
	@echo "Coverage report generated in htmlcov/"

lint:
	python -m ruff check .
	python -m ruff format --check .

lint-fix:
	python -m ruff check --fix .
	python -m ruff format .

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov coverage.xml .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
