Dockerfiles for the automated building of container images on Docker Hub.

### frontend-build

A simple debian-based container for building and testing FE applications with
grunt and/or gulp and phantomjs. Please note this container operates as root
and as such currently requires your build script to fix permissions after
build.
