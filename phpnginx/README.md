phpnginx example
================

A simple ubuntu-based container for building and testing PHP applications. Uses the public pemcconnell/phpnginx image as found on the Docker Hub.

A brief breakdown of the software and modules is as follows:

- php5-fpm
- php5-mysql php-apc php5-imagick php5-mcrypt php5-curl php5-cli php5-gd php5-pgsql php-pear
- curl
- composer
- nginx
- supervisor
- git

## Requirements
- [Docker >= 0.10.0](https://www.docker.io/)


## Linux users

Linux users can simply run the following command to get up and running. Note: you may want to update the Makefile so that it tags your container appropriately (currently `pemcconnell/phpnginx-test`):

- `make run`

Now you can run `docker ps` and view the url to view for port 80 of the container. Visit this in your browser and voila.
