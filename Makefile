.PHONY: all help venv run

# make all - Default Target. Does nothing.
all:
	@echo "Python helper commands."
	@echo "For more information try 'make help'."

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: venv = activate virtual environment
.PHONY: venv
venv:
	source $(CURDIR)/.venv/bin/activate

# target: init = load initial data to database
run:
	python src/domain_manager/main.py

lint:
	pre-commit autoupdate
	pre-commit run --all-files
