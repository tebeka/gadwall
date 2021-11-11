all:
	$(error please pick a target)

publish:
	rm -rf dist
	python -m build
	python -m twine upload dist/*
