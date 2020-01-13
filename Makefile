install:
	poetry install

lint:
	poetry run flake8 gendiff

tests:
	poetry run pytest --cov=gendiff gendiff/tests/ --cov-report xml

build: lint
	poetry build

publish: build
	poetry publish -r testpypi