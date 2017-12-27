# {{ cookiecutter.repo_name }}

{{ cookiecutter.description }}

## Setup development environment

We setup the development environment in a Docker container with the following command.

- `make init`

This command gets the resources for training and testing, and then prepares the Docker image for the experiments.
After creating the Docker image, you run the following command.

- `make create-container`

The above command create Docker container from the Docker image we create with `make init` and then login the Docker container.
Now we made the development envrionment. For create and evaluate the model, you run the following command.

## Usage

This section shows the detailed usages.

### Login Docker container

Only the first time you need to create a Docker container, from the image created in `make init` command.
`make create-instance` creates and launch the {{ cookiecutter.repo_name }} container.
After creating the container, you just need run `make start-container`.

### Logout from Docker container

When you logout from shell in Docker container, please run `exit` in the console.

### Development

We continue the development of this repository. When we need to add libraries in Dockerfile or requirements.txt
which are added to working envrionment in the Docker container, we need to drop the current Docker container and
image and then create them again with the latest setting. To remove the Docker the container and image, run `make clean-docker`
and then `make init-docker` command to create the Docker container with the latest setting.
