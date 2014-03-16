.PHONY: docs

init:
	pip install -r requirements.txt

clean:
	find . -name *.pyc -delete

test:
	coverage run tests.py

coverage:
	coverage html

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

verify:
	pyflakes checkers
	pep8 checkers
