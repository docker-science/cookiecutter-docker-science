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

Initial directories and Files
-------------------------------

The following is the initial directory structure generated in the previous section.

::

    ├── Makefile                          <- Makefile contains many targets such as create docker container or get input files.
    ├── config                            <- This directory contains configuration files used in scripts or Jupyter Notebook.
    │   └── jupyter_config.py
    ├── data                              <- data directory contains the input resources.
    ├── docker                            <- docker directory contains Dockerfile.
    │   └── Dockerfile                    <- Dockerfile have the container settings. Users modify Dockerfile if additional library is needed for experiments.
    ├── model                             <- model directory store the model files created in the experiments.
    ├── my-data-science-project           <- cookie-cutter-docker-science creates the directory whose name is same as project name. In this directory users puts python files used in scripts or Jupyter Notebook.
    │   └── __init__.py
    ├── notebook                          <- This directory sotres the ipynb files saved in Jupyter Notebook.
    ├── requirements.txt                  <- Libraries needed to run exeperiments. The library listed in this file are installed in the Docker container.
    └── scripts                           <- Users add the script files to generate model files or run evaluation.


Makefile targets
----------------

cookiecutter-docker-science provides many targets to supports experiments in Docker container. Users can run the target with `make [TARGET]` command.

init
~~~~~

After cootiecutter-docker-science generate the directories and files, users first run this command. `init` setups resources for experiments.
Specifically `init` run `init-docker` and `init-data` command.

init-docker
~~~~~~~~~~~

`init-docker` command first creates Docker the images based on `docker/Dockerfile`.

init-data
~~~~~~~~~~

`init-data` downloads input files stored in S3. If you do not store the input files in S3, please modify the target to download the data source.

create-container
~~~~~~~~~~~~~~~~~

`create-container` command creates Docker container based on the created image and login the Docker container.

start-container
~~~~~~~~~~~~~~~~

`start-container` launches the Docker container created by the `create-container` target.


jupyter
~~~~~~~

`jupyter` target launch Jupyter Notebook server.


clean-model
~~~~~~~~~~~~

`clean` target removes the artifacts such as model files in `model` directory.


clean-docker
~~~~~~~~~~~~~

`clean-docker` target removes the Docker images and container generated with `make init-docker` and `make create-container`.
When we update Python libraries in `requirements.txt` or system tools in `Dockerfile`,
we need to clean Docker the image and container with this target and create the updated image and container
with `make init-docker` and `make create-container`.
