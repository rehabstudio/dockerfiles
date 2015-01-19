Dockerfiles for the automated building of container images on Docker Hub.

### frontend-build

A simple debian-based container for building and testing FE applications with
grunt and/or gulp and phantomjs. Please note this container operates as root
and as such currently requires your build script to fix permissions after
build.

### phpnginx

Super simple PHP5-FPM/NGINX container for quickly getting a PHP environment up
and running. An example of how this image can be used can be found here:
https://github.com/pemcconnell/phpnginx-example
