.PHONY: virtual install flake8 run

virtual: .venv/bin/pip # Creates an isolated python 3 environment

.venv/bin/pip:
	python3 -m venv .venv

install: virtual
	.venv/bin/pip install -r requirements.txt
	.venv/bin/python3 manage.py migrate
	.venv/bin/python3 manage.py collectstatic --noinput
	.venv/bin/python3 manage.py create_admin
	
update-requirements: install
	.venv/bin/pip freeze > requirements.txt

flake8:  # Lints code using flake8
	.venv/bin/flake8 api/*.py
	.venv/bin/flake8 vehicles/*.py

test:
	.venv/bin/python3 manage.py test

run:
	.venv/bin/python3 manage.py runserver
	