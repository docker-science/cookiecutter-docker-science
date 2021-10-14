{%- if cookiecutter.use_nvidia_docker == 'yes' -%}
FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04
{%- else -%}
FROM ubuntu:18.04
{%- endif %}

RUN apt-get update && apt-get install -y \
  git \
  python3.8 \
  python3-pip \
  python3.8-dev \
  python3-opencv

RUN pip3 install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ARG UID
RUN useradd docker -l -u $UID -s /bin/bash -m
USER docker

ENV PATH=$PATH:/home/docker/.local/bin
