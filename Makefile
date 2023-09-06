SHELL := /bin/bash

install_dependencies:
	python3.10 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
	source venv/bin/activate && pip install "apache-airflow[celery]==2.7.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.0/constraints-3.8.txt"
	source venv/bin/activate && pre-commit install --hook-type pre-push --hook-type post-checkout --hook-type pre-commit

run_precommit:
	pre-commit run --all-files

run_tests:
	py.test tests/


