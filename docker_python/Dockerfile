FROM python:3.10.3-buster

ARG DEBIAN_FRONTEND=noninteractive
# __pycahe__を作成しない
ENV PYTHONDONTWRITEBYTECODE=1 \
  PATH="/usr/local/bin:$PATH"

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash && \
    apt-get install -y nodejs

RUN pip3 install poetry

WORKDIR /workspace

COPY ./workspace/pyproject.toml ./
COPY  ./workspace/Makefile ./

RUN poetry config virtualenvs.create false
RUN poetry install

RUN rm -f pyproject.toml

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash && \
    apt-get install -y nodejs

