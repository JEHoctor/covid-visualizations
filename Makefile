.PHONY: init lint format


init:
	python -m venv venv
	(source venv/bin/activate; pip install -e .)

lint:
	flake8 covid

format:
	@echo not implemented
