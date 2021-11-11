all:
	$(error please pick a target)

publish:
	rm -rf dist
	python -m build
	python -m twine upload dist/*

test:
	python -m flake8 .
	python -m pytest -v -rf
