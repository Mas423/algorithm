FROM ubuntu:20.04

# インタラクティブモードを回避
ARG DEBIAN_FRONTEND=noninteractive
# __pycahe__を作成しない
ENV PYTHONDONTWRITEBYTECODE=1 \
  PATH="/usr/local/bin:$PATH"
# タイムゾーンを日本に設定
ENV TZ=Asia/Tokyo

RUN /bin/echo -e "\n\
    Acquire::http::Timeout \"300\";\n\
    Acquire::ftp::Timeout \"300\";" >> /etc/apt/apt.conf.d/99timeout

RUN apt-get update && apt-get install -y --no-install-recommends \
    zsh \
    time \
    tzdata \
    tree \
    curl \
    vim \
    expect \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# zshをデフォルトに設定
# SHELL ["/bin/zsh", "-c"]
RUN chsh -s $(which zsh)

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.8 \
    python3-pip \
    pypy3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash && \
    apt-get install -y nodejs && \
    npm install -g atcoder-cli

# atcoder-cliの設定
RUN acc config-dir && \
    acc config default-template python && \
    acc config default-test-dirname-format test

# configを設定
COPY ./docker/template.json /root/.config/atcoder-cli-nodejs/python/
COPY ./docker/main.py /root/.config/atcoder-cli-nodejs/python/

# zsh設定をコピー
COPY ./docker/.zshrc /root

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 30 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 30 && \
    update-alternatives --install /usr/bin/pypy pypy /usr/bin/pypy3 30

# pythonのライブラリはpoetryで管理する
RUN pip3 install poetry

WORKDIR /workspace
COPY ./workspace/pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install

RUN rm -f pyproject.toml

WORKDIR /workspace/src