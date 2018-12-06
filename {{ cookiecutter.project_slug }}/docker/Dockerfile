{% if cookiecutter.choice_docker == 'nvidia' -%}
FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04
RUN apt-get update && apt-get install -y \
  git \
  python3.5 \
  python3-pip \
  python3-dev
RUN pip3 install --upgrade pip

{% elif cookiecutter.choice_docker == 'anaconda3' -%}
FROM continuumio/anaconda3
{% elif cookiecutter.choice_docker == 'miniconda3' -%}
FROM continuumio/miniconda3
{%- endif %}

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m
USER docker

WORKDIR /work
ENV JUPYTER_ENABLE_LAB=yes
ENTRYPOINT ["/bin/bash"]
