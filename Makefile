install:
	poetry install

lint:
	poetry run flake8 gendiff

tests:
	pytest

build: lint
	poetry build

publish: build
	poetry publish -r testpypi