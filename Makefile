# 'make' will list all documented targets, see https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "\033[33mAvailable targets, for more information, see \033[36mREADME.md\033[0m"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

 ifeq (, $(shell which poetry))
 $(error "No 'poetry' in $$PATH, follow install instructions at https://python-poetry.org")
 endif

install-deps:  ## install project dependencies
	poetry install

dev-server:  ## run development server for backend
	poetry run uvicorn ujira.server:app --reload

jira-shell:  ## run ipython shell for experimenting with 'jira' package
	bash scripts/jirashell.sh
