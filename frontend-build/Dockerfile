FROM debian:wheezy
MAINTAINER Ryan Grieve <ryan@rehabstudio.com>

# install apt dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        apt-transport-https \
        build-essential \
        curl \
        git \
        inotify-tools \
        libfontconfig1 \
        libfreetype6 \
        ruby \
        sudo && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install Node stable
RUN curl -sL https://deb.nodesource.com/setup | bash - && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# npm-ception: install latest from npm
RUN npm install -g npm
# install global task runners and phantomjs
RUN npm install -g grunt-cli gulp phantomjs webpack

# install gulp sass requirements
RUN gem install sass

RUN mkdir /src
RUN mkdir /src/node_modules

ADD assets/package.json /src/
RUN cd /src; npm install

VOLUME ['/src/node_modules']
WORKDIR /src
