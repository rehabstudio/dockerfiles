A simple debian-based container for building and testing Polymer applications
with vulanize, crisper, polybuild and gulp. Please note this container operates
as root and as such currently requires your build script to fix permissions
after build.

Usage:

- Mount the root of your FE application (where your `package.json` lives) as
  volume `/src` when running the container
- Run the container with `npm install`, `bower install` and your build commands

e.g. `docker run -ti --rm -v /path/to/your/app:/src rehabstudio/frontend-build npm install && bower install && gulp build`

N.B. It will be much easier to group your build actions, along with permission
fixes, in a Makefile as opposed to running multiple chained commands like the
example above.
