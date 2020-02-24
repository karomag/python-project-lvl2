install:
	poetry install

lint:
	poetry run flake8 gendiff

tests:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

build: tests
	poetry build

publish: build
	poetry publish -r testpypi

.PHONY: tests
