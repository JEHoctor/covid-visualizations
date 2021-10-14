.PHONY: init lint format


init:
	python -m venv venv
	(source venv/bin/activate; pip install -e .)

lint:
	flake8 covid

test: lint
	pytest -vv tests/covid

format:
	black covid
