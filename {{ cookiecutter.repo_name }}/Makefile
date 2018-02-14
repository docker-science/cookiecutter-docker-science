.PHONY: clean clean-model clean-pyc docs help init init-data init-docker start-container
.DEFAULT_GOAL := help

# SCRIPTS

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
        match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
        if match:
                target, help = match.groups()
                print("%-20s %s" % (target, help))
endef

define START_DOCKER_CONTAINER
if [ `$(DOCKER) inspect -f {% raw -%}{{.State.Running}}{%- endraw %} $(CONTAINER_NAME)` = "false" ] ; then
        $(DOCKER) start $(CONTAINER_NAME)
fi
endef

# VARIABLES


{% if cookiecutter.use_nvidia_docker == 'yes' -%}
export DOCKER=nvidia-docker
{% else %}
export DOCKER=docker
{%- endif %}
export PRINT_HELP_PYSCRIPT
export START_DOCKER_CONTAINER
export PYTHONPATH=$PYTHONPATH:$(PWD)
export IMAGE_NAME= {{ cookiecutter.repo_name }}
export CONTAINER_NAME= {{ cookiecutter.repo_name }}
export DATA={{ cookiecutter.data_source }}
export JUPYTER_HOST_PORT={{ cookiecutter.jupyter_host_port }}
export JUPYTER_CONTAINER_PORT=8888
export JUPYTER_CONFIG_PATH=config/jupyter_config.py

# TARGETS

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

init: init-docker init-data ## initialize repository for traning

init-data: ## download data
	-aws s3 sync $(DATA) ./data/

init-docker: ## initialize docker image
	$(DOCKER) build -t $(CONTAINER_NAME) -f ./docker/Dockerfile .

create-container: ## create docker container
	docker run -it -v $(PWD):/work -p $(JUPYTER_HOST_PORT):$(JUPYTER_CONTAINER_PORT) --name $(CONTAINER_NAME) $(CONTAINER_NAME)

start-container: ## start docker instance
	@echo "$$START_DOCKER_CONTAINER" | $(SHELL)
	@echo "Launched $(CONTAINER_NAME)..."
	$(DOCKER) attach $(CONTAINER_NAME)

jupyter: ## start Jupyter Notebook server
	jupyter-notebook --ip=0.0.0.0 --port=${JUPYTER_CONTAINER_PORT} --config=$(JUPYTER_CONFIG_PATH)

lint: ## check style with flake8
	flake8 {{ cookiecutter.repo_name }}

profile: ## show profile of the project
	@echo "CONTAINER_NAME: $(CONTAINER_NAME)"
	@echo "IMAGE_NAME: $(IMAGE_NAME)"
	@echo "JUPYTER_PORT: `$(DOCKER) port $(CONTAINER_NAME)`"
	@echo "DATA: $(DATA)"

clean: clean-model clean-pyc clean-docker ## remove all artifacts

clean-model: ## remove model artifacts
	rm -fr model/*

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

distclean: clean clean-data clean-docker ## remove all the reproducible resources including Docker images

clean-data:
	rm -fr data/*

clean-docker:
	-$(DOCKER) rm $(CONTAINER_NAME)
	-$(DOCKER) image rm $(CONTAINER_NAME)
