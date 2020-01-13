install:
	poetry install

lint:
	poetry run flake8 gendiff

tests:
	poetry run pytest --cov gendiff/

build: lint
	poetry build

publish: build
	poetry publish -r testpypi