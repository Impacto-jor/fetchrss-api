style:
	black .

upload:
	rm -rf dist/
	python setup.py sdist
	twine upload dist/*

.PHONY: upload
