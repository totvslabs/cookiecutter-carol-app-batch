PYLINT = flake8
PYLINTFLAGS = -rn
PYTHONFILES := $(wildcard *.py)

IMAGE = {{cookiecutter.carol_app_docker_image}}
APP = {{cookiecutter.carol_app_tenant}}
OPERATOR ?= api.operator.carol.ai
ENVIRONMENT ?= labs-ai-apps-production

OPERATORTOKEN ?=
USER ?=
ID ?=
GHTOKEN ?=


ifeq ($(OS),Windows_NT)
	OPEN := start
else
	UNAME := $(shell uname -s)
	ifeq ($(UNAME),Linux)
		OPEN := xdg-open
	endif
	ifeq ($(UNAME),Darwin)
		OPEN := open
	endif
endif

.PHONY: help

.check-env:
	@test $${OPERATORTOKEN?Please set environment variable OPERATORTOKEN}
	@test $${USER?Please set environment variable USER}
	@test $${ID?Please set environment variable ID}
	@test $${GHTOKEN?Please set environment variable GHTOKEN}

help: ## Show this help message
	@echo "{{cookiecutter.project_slug}} Makefile help.\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init: ## Install all package dependencies
	pip install -r requirements.txt

test: ## Runs all project test suite, recording all test converage data
	pytest --cov={{cookiecutter.project_slug}} tests/

coverage: ## Create XML and HTML Test coverare report.
	coverage xml -o coverage-reports/coverage.xml
	coverage3 html

htmlcov: coverage ## Opens the current test coverage report on the default browser
	$(OPEN) htmlcov/index.html

clean: ## Cleans all temporary and preprocessed files
	rm -rf dist
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	rm -rf htmlcov/*

dev: ## Install all development packages dependencies
	pip install -r requirements-dev.txt

docs: ## Compile all package documentation in HTML format
	$(MAKE) -C docs html

{%- if cookiecutter.sonarqube %}
code_scan: ## Execute a Code Qualiry scan and send the data to SonarQube server
	@echo "~~~ Code Quality Scan"
	sonar-scanner -Dsonar.projectKey={{cookiecutter.project_slug}} -Dsonar.sources=. -Dsonar.host.url=${SONAR_URL} -Dsonar.login=${SONAR_TOKEN} -Dsonar.branch.name=${BUILDKITE_BRANCH} -Dsonar.python.coverage.reportPaths="coverage-reports/coverage.xml"
{%- endif %}

lint: ## Lint all code for best practicies
	flake8 ./{{cookiecutter.project_slug}} ./tests

run: ## Runs the Batch process locally
	python3 -m luigi --module {{cookiecutter.project_slug}}/{{cookiecutter.algorithm_name}}.py main.runMe --local-scheduler

build_ci: ## Build CI Docker Image
	docker build -f docker/ci_image/Dockerfile -t ci_image .

venv: ## Create the virtualenv for this Carol App
	python3 -m venv .venv
	source .venv/bin/activate && pip install --upgrade pip

all_tests: tests coverage code_scan ## Runs all test related tasks

docker_image: ## Build the Carol App docker image
	docker build -t ${IMAGE} .

dist: clean ## Create the dist file to deploy on Carol
	@mkdir dist
	@mkdir dist/ai-script
	@cp {{cookiecutter.project_slug}}/manifest.json dist/ai-script
	@cd dist && zip -r {{cookiecutter.project_slug}}.zip ai-script/*

spec: .check-env ## Create the Build Spect for this Carol App
	@APP=$(USER) IMAGE=$(IMAGE) ENVIRONMENT=$(ENVIRONMENT) envsubst < spec.json > spec.json_tmp

build: spec ## Send all specs to Carol Operator to build the image
	@curl -sXPOST -H "x-auth-token:$(OPERATORTOKEN)" \
		"https://$(OPERATOR)/api/builds" -d@./spec.json_tmp

get: .check-env ## Get the docker image status from Carol Operator
	@curl -sXGET -H "x-auth-token:$(OPERATORTOKEN)" \
		"https://$(OPERATOR)/api/builds/build/$(APP)/$(ID)"

delete: .check-env ## Delete a Docker Image built by Carol Operator
	@curl -sXDELETE -H "x-auth-token:$(OPERATORTOKEN)" \
		"https://$(OPERATOR)/api/builds/build/$(APP)/$(ID)"
