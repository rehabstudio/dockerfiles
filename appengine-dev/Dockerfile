FROM debian:wheezy
MAINTAINER Paddy Carey <patrick@rehabstudio.com>

# update apt cache, upgrade the system and install the system utils we need
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        apt-transport-https \
        build-essential \
        python-imaging \
        python-numpy \
        python-dev \
        python-pip \
        sudo

# lxml requirements
RUN apt-get install -y libxslt1-dev

# install all the packages we need from pypi
ADD ops/assets/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# add remote shell script to allow python shell access to running instance
ADD ops/scripts/remote_shell.py /usr/local/bin/remote_shell.py
RUN chmod a+x /usr/local/bin/remote_shell.py

# add custom motd to remind users of how persistance works
ADD ops/assets/motd /etc/motd

# Download and install the Appengine Python SDK
ADD ops/scripts/gaesdk_download.py /tmp/gaesdk_download.py
RUN python /tmp/gaesdk_download.py 1.9.26
ENV PATH /opt/google_appengine:$PATH

# Remove tmp files
RUN rm -r /tmp/*

# Add volumes for pesistence between runs
VOLUME ['/.ipython', '/home/aeuser']

# create a non-root user we can use to run the application inside the container
RUN groupadd -r aeuser -g 1000 && \
    useradd -u 1000 -rg aeuser -md /home/aeuser -s /bin/bash aeuser

# ensure aeuser owns volumes
RUN mkdir /.ipython
RUN chown -R aeuser:aeuser /.ipython
RUN chown -R aeuser:aeuser /home/aeuser

# add .bashrc for aeuser
ADD ops/assets/bashrc /home/aeuser/.bashrc

# add sudo config to enable root access for aeuser
ADD ops/assets/sudoers /etc/sudoers.d/aeuser

# switch to the new user account so that all commands run as `aeuser`
ENV HOME /home/aeuser
USER aeuser

# default run command
CMD bash

# expose ports (application server & admin server)
EXPOSE 8000 8080
