install:
	poetry install

make-requirements:
	poetry export -f requirements.txt --output requirements.txt

make-migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

setup:
	make install
	make migrate

start:
	poetry run python manage.py runserver

check:
	poetry check

lint:
	poetry run flake8 . --exclude=*/migrations/*

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test .
	poetry run coverage html
	poetry run coverage report

heroku-migrate:
	heroku run python manage.py migrate

deploy:
	git push heroku main
