FROM ubuntu:14.04
MAINTAINER Peter McConnell <me@petermcconnell.com>

# keep upstart quiet
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# no tty
ENV DEBIAN_FRONTEND noninteractive

# Get up to date
RUN apt-get update --fix-missing

# install nginx
RUN apt-get -y install nginx

# install php
RUN apt-get -y install php5-fpm php5-mysql php-apc php5-imagick php5-imap php5-mcrypt php5-curl php5-cli php5-gd php5-pgsql php5-sqlite php5-common php-pear curl php5-json php5-redis
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/
RUN mv /usr/bin/composer.phar /usr/bin/composer

# install supervisor
RUN apt-get -y install python-setuptools
RUN easy_install supervisor
RUN easy_install supervisor-stdout

# bit of a tidy up
RUN apt-get clean
