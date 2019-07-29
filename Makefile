BAKE_OPTIONS=--no-input

help:
	@echo "bake 		generate project using defaults"
	@echo "watch 		generate project using defaults and watch for changes"
	@echo "replay 		replay last cookiecutter run and watch for changes"
	@echo "test			run bake tests on this cookiecutter template"
	@echo "watch_test	run bake tests on this cookiecutter template and watch for changes"

bake:
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

watch: bake
	watchmedo shell-command -p '*.*' -c 'make bake -e BAKE_OPTIONS=$(BAKE_OPTIONS)' -W -R -D \{{cookiecutter.project_slug}}/

test:
	py.test

watch_test:
	watchmedo shell-command -p '*.*' -c 'py.test' -W -R

replay: BAKE_OPTIONS=--replay
replay: watch
	;
