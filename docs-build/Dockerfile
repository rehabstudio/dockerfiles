FROM debian
MAINTAINER Ryan Grieve <me@ryangrieve.com>

# no tty
ENV DEBIAN_FRONTEND noninteractive

# update apt cache, upgrade the system and install the system utils we need
RUN apt-get update --fix-missing && apt-get upgrade -y
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    inotify-tools \
    python \
    python-pip \
    graphviz \
    build-essential \
    openjdk-7-jre

# install sphinx
RUN pip install \
    sphinx \
    sphinx-rtd-theme \
    sphinxcontrib-httpdomain

# install plantuml
RUN wget http://garr.dl.sourceforge.net/project/plantuml/plantuml.jar \
    -O /opt/plantuml.jar

ENV PLANTUML_JAR /opt/plantuml.jar

CMD bash
