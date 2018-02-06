Introduction
------------

.. note:: please see `the slides <https://speakerdeck.com/takahiko03/cookiecutter-for-ml-experiments-with-docker>`_ before you get started.

.. raw:: html

    <script async class="speakerdeck-embed" data-id="eb687f10632f49ec87b3b677dd197905" data-ratio="1.77777777777778" src="//speakerdeck.com/assets/embed.js"></script>

Many researchers and engineers do their machine learning or data mining experiments.
For such data engineering tasks, researchers apply various tools and system libraries which are constantly
updated, installing and updating them cause problems in local environments. Even when we work in hosting
environments such as EC2, we are not free from this problem. Some experiments succeeded in one
instance but failed in another one, since library versions of each EC2 instances could be different.

By contrast, we can creates the same container in which needed tools with the same version are already installed in one command without
changing system libraries in host machines. This aspect of Docker is important for reproducibility of experiments,
and keep the projects in continuous integration systems.

Unfortunately running experiments in Docker containers is troublesome. Adding a new library into ``requirements.txt``
or ``Dockerfile`` does not installed as if local machine. We need to create Docker image and container each time.
We also need to forward ports to see server responses such as Jupyter Notebook UI launch in Docker container in our local PC.
``cookiecutter-docker-science`` provides utilities to make working in Docker container simple.

This project is a tiny template for machine learning projects developed in Docker environments.
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

To generate project from the template, please run the following command on the parent directory of the repository.

``cookiecutter ./cookiecutter-docker-science-alpha``

Then the cookiecutter command ask for several questions on generated project as follows.

::

    $cookiecutter ~/cookiecutter-docker-science-alpha
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

    ├── Makefile                          <- Makefile contains many targets such as create docker container or
    │                                        get input files.
    ├── config                            <- This directory contains configuration files used in scripts
    │   │                                    or Jupyter Notebook.
    │   └── jupyter_config.py
    ├── data                              <- data directory contains the input resources.
    ├── docker                            <- docker directory contains Dockerfile.
    │   └── Dockerfile                    <- Dockerfile have the container settings. Users modify Dockerfile
    │                                        if additional library is needed for experiments.
    ├── model                             <- model directory store the model files created in the experiments.
    ├── my-data-science-project           <- cookie-cutter-docker-science creates the directory whose name is same
    │   │                                    as project name. In this directory users puts python files used in scripts
    │   │                                    or Jupyter Notebook.
    │   └── __init__.py
    ├── notebook                          <- This directory sotres the ipynb files saved in Jupyter Notebook.
    ├── requirements.txt                  <- Libraries needed to run exeperiments. The library listed in this file
    │                                        are installed in the Docker container.
    └── scripts                           <- Users add the script files to generate model files or run evaluation.


Makefile targets
----------------

cookiecutter-docker-science provides many Makefile targets to supports experiments in a Docker container. Users can run the target with `make [TARGET]` command.

init
~~~~~

After cootiecutter-docker-science generate the directories and files, users first run this command. `init` setups resources for experiments.
Specifically `init` run `init-docker` and `init-data` command.

- init-docker

  `init-docker` command first creates Docker the images based on `docker/Dockerfile`.

- init-data

  `init-data` downloads input files stored in S3. If you do not store the input files in S3, please modify the target to download the data source.

create-container
~~~~~~~~~~~~~~~~~

`create-container` command creates Docker container based on the created image and login the Docker container.

start-container
~~~~~~~~~~~~~~~~

Users can start and login the Docker container with `start container` created by the `create-container`.

jupyter
~~~~~~~

`jupyter` target launch Jupyter Notebook server.

profile
~~~~~~~

`profile` target shows the misc information of the project such as port number or container name.


clean
~~~~~

`clean` target removes the artifacts such as models and *.pyc files.

- clean-model

  `clean-model` command removes model files in `model` directory.

- clean-pyc

  `clean-pyc` command removes model files of *.pyc, *.pyo and __pycache__.

distclean
~~~~~~~~~

`distclean` target removes large filesize objects such as datasets and docker images.

- clean-data

  `clean-data` command removes all datasets in `data` directory.

- clean-docker

  `clean-docker` command removes the Docker images and container generated with `make init-docker` and `make create-container`.
  When we update Python libraries in `requirements.txt` or system tools in `Dockerfile`, we need to clean Docker the image and container with this target and create the updated image and container with `make init-docker` and `make create-container`.

Working in Docker container
----------------------------

Files and directories
~~~~~~~~~~~~~~~~~~~~~

When you log in a Docker container by ``make create-container`` or ``make start-container`` command, the log in directory is ``/work``.
The directory contains the project top directories in host computer such as ``data`` or ``model``. Actually the Docker container mounts
the project directory in ``/work`` and therefore when you edit the files in the Docker container, the changes are
reflected in the files in host environments.

Jupyter Notebook
~~~~~~~~~~~~~~~~~

We can run Jupyter Notebook in the Docker container. The Jupyter Notebook uses the default port ``8888`` in **Docker container (NOT HOST)** and
the port is forwarded to the one you specify with ``JUPYTER_HOST_PORT``  in the cootiecutter command. You can see the Jupyter Notebook UI accessing
"http://localhost:JUPYTER_HOST_PORT". When you save notebooks the files are saved in the ``notebook`` directory.

Tips
-----


Port number for Jupyter Notebook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the generation of project with cookiecutter, the default port of Jupyter Notebook in host is ``8888``. The number is common and could
have a collision to another server processes.

In such cases, you can make the Docker container changing the port number in ``make create-container`` command.
For example the following command creates Docker container forwarding Jupyter default port ``8888`` to ``9900`` in host.

::

    make create-container JUPYTER_HOST_PORT=9900

Then you launch Jupyter Notebook in the Docker container, you can see the Jupyter Notebook in http://localhost:9900
