Introduction
------------

Many researchers and engineers do their machine learning or data mining experiments in **Docker** container.
For such data science tasks, researchers apply various tools and system libraries which are constantly updated, installing and
updating them cause problems. In addition, to reproduce the experiments in Docker containers are handy
since the needed tools are already installed in the containers. This aspect of Docker is important for reproducibility of experiments
and keeping the projects in continuous integration systems.

Unfortunately running experiments in Docker containers is also troublesome. Adding a new library into ``requirements.txt``
or Dockerfile does not installed as if local machine. We need to create Docker image and container each time.
We also need to forward ports to see Jupyter Notebook UI launch in Docker container in our local PC.
``cookiecutter-docker-science`` provides targets used to make working with Docker simple.

This project is a template for machine learning projects developed with Docker environments.
In machine learning tasks, projects glow uniquely to fit target tasks, but in the initial state,
most directory structure and targets in `Makefile` are common.
``cookiecutter-docker-science`` generate initial directories which fits simple machine learning tasks.

Requirements
------------

* Python 2.7 or Python 3.5
* Cookiecutter 1.6 or later

Quick start
-----------

To generate your project from docker template, please run the following 2 commands.

1. Downaload cookiecutter template repositiory (`cookiecutter-docker-science-alpha`)

``git clone git@ghe.ckpd.co:research/cookiecutter-docker-science-alpha.git``

2. Generate project directory from template

To generate project from the template, please run the following command.

``cookiecutter ../cookiecutter-docker-science-alpha``

Then the cookiecutter command ask for several questions on generated project as follows.

::

    cookiecutter ~/cookiecutter-docker-science-alpha
    project_name [project_name]: my-data-science-project
    repo_name [my-data-science-project]:
    jupyter_host_port [8888]: 9999
    description [Please Input a short description]: This project keep the experimental results on automatic image detection tasks.
    data_source [Please Input data source in S3]: s3://cookiecutter.ap-northeast-1/data/image

Then you get the generated project directory, ``my-data-science-project``.

