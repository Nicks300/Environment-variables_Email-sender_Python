FROM python:3.11.9-slim

RUN apt-get update && apt-get install -y \
    git \
    jq \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /test

COPY . /test
RUN pip install -r /test/tests/requirements.txt

WORKDIR /test

SHELL ["/bin/bash", "-c"]
